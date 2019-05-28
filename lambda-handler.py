import json
import os
import uuid
import boto3


def main(event, context):
    random_value = str(uuid.uuid4().hex)
    table_name = os.environ.get('TABLE_NAME')
    print(f'Random value is {random_value}')

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    table = dynamodb.Table(table_name)
    response = table.put_item(
        Item={
            'ID': random_value
        }
    )

    print("PutItem succeeded:")
    print(json.dumps(response, indent=2))
