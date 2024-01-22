# Assignment-Lambda-functions

Assignment 1
In IAM dashboard, click on the Roles heading under IAM resources.
It displays all the Global roles, click on the button of Create Role.
It lands on a screen mentioning to select Trusted Entity Type, selected AWS Service whoch allows any AWS service such as Lambda, EC2 to perform actions in the account.
Selected Lambda as Use case to manage AWS Services on behalf of my account.
Attached AmazonEC2FullAccess policy to Lambda role.
Provided a name as Ishwari-lambda-ec2-full-access and additional description to the role and saved the role.
From the Lambda dashboard clicked on create function button.
Provided function name in text box as start-or-stop-instance-ishwari.
Runtime as python 3.12
Architecture as x86_64
In the permissions selected existing role as the one created earlier with full access to EC2 instances.
Created 2 EC2 instances namely stop_instance1, start_instance1 from AWS dashboard console.
Started Instance which needs to be stopped.
Wrote code in lambda function to start and stop instance in boto3
Invoked above lambda function from local python script.



Assignment 2
Created a s3 bucket named s3-ishwari for cleanup.
Uploaded file to it.
Under IAM Roles created a new role named Ishwari-s3-full-access and selected AWSS3FullAccess policy for it.
Created lambda function and a python script to trigger it.


 
Assignment4 - Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3

In IAM dashboard clicked Roles, it shows a list of roles which are already created in the account, clicked on Create Role button.
In next page selected AWS service as Trusted Entity type, service as S3.
Selected AmazonS3ReadOnlyAccess policy.
Provided role name as just_read_s3.
Under lambda function dashboard, clicked on Functions button in the next page of Create function, selected the default Author from scratch.
Used AmazonS3ReadOnlyAccess-botot3 
Created a lambda function to print all s3 buckets which are unencrypted


 
Assignment 18 - Restore EC2 Instance from Snapshot

Created a Lambda function to get create a snapshot from an existing EC2 instance and created a new instance from it.




 


