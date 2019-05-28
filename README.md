
# Lambda Writing to DynamoDb AWS CDK Demo

This is a very simple example of using AWS CDK to define in Python 
([Python >= 3.7.1](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)) a Lambda function which writes 
to a DynamoDb table every 1 minute (by way of a CloudWatch scheduled Rule).

## Installing the CDK CLI

```bash
npm install -g aws-cdk

cdk --version
```
You will also need your AWS CLI configured (`~/.aws/config`) 
See [docs](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) for details.

## Deploying this App Stack

Create your python virtual env
```bash
python -m venv .env
source ./.env/bin/activate
pip install -r requirements.txt

```
Optionally you can view the resulting CloudFormation template with `cdk synth`.
When you are ready to deploy;
```bash
cdk deploy
``` 

If you then log into the console you will see a CloudFormation template comprising the build of your Lambda function, DynamoDb table
and associated resources.

Note this app writes to a dynamodb table every minute so you will want to turn it off after you are done examining it.

```bash
cdk destroy
```