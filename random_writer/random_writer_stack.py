from aws_cdk import aws_events as events, aws_lambda as lambda_, cdk, aws_events_targets as targets
from aws_cdk.aws_dynamodb import Table, BillingMode, AttributeType


class RandomWriterStack(cdk.Stack):

    def __init__(self, app: cdk.App, id: str, **kwargs) -> None:
        super().__init__(app, id)

        table_name = 'RandomWriterTable'

        with open("lambda-handler.py", encoding="utf8") as fp:
            handler_code = fp.read()

        lambda_fn = lambda_.Function(
            self,
            "RandomWriter",
            code=lambda_.InlineCode(handler_code),
            handler="index.main",
            timeout=300,
            runtime=lambda_.Runtime.PYTHON37,
            environment={'TABLE_NAME': table_name},
        )
        # Add our 'Every Minute' scheduling rule for this Lambda (via a CloudWatch scheduled Role)
        rule = events.Rule(
            self,
            "Rule",
            schedule_expression="cron(* * * * ? *)"
        )
        rule.add_target(targets.LambdaFunction(lambda_fn))
        # Build our DynamoDb Table
        dynamodb = Table(
            self,
            table_name,
            table_name=table_name,
            partition_key={'name': 'ID', 'type': AttributeType.String},
            billing_mode=BillingMode.PayPerRequest)
        dynamodb.grant_full_access(lambda_fn)
