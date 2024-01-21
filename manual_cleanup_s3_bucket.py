import boto3

lambda_client=boto3.client('lambda')
response=lambda_client.invoke(FunctionName='ishwari-s3-cleanup',InvocationType='RequestResponse')
print(response)