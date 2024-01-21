import boto3
import datetime

try:
    client=boto3.client('s3')

    #Fetching current date and time 
    now=datetime.datetime.now()

    #Formatting above date and time
    formatted_date=datetime.datetime(now.year,now.month,now.day,now.hour,now.minute,now.second)

    #Listing all objects of a specific bucket
    response=client.list_objects_v2(Bucket='ishwari-s3')

    #Storing key all objects date in dictionary format in a variable.
    objects=response['Contents']

    #Looping over each object in the bucket
    for obj in objects:

        #Finding difference between datetime objects
        difference=(formatted_date-obj['LastModified'].replace(tzinfo=None)).days

        #Deleting the object if it is older than 30 days
        if(difference>0):

            response=client.delete_object(Bucket='ishwari-s3',Key=obj['Key'])

#Exception handling
except Exception as e:
    print(e)