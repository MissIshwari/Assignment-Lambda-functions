import boto3

lambda_client=boto3.client('lambda')
response=lambda_client.invoke(FunctionName='start-or-stop-instance-ishwari',InvocationType='RequestResponse')
print(response['ResponseMetadata']['HTTPStatusCode'])