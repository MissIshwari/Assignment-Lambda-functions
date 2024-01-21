import boto3

try:
    #Creating boto3 client
    client=boto3.client('s3')

    #Listing all the buckets
    response=client.list_buckets()

    #Storing s3 bucket metdata
    buckets=response['Buckets']
    print(response['Buckets'])

    unencrypted_bucket=[]

    #Looping over each bucket object and checking whether it is SSE encrypted
    for bucket in buckets:
        name=bucket['Name']
        response=client.get_bucket_encryption(Bucket=name)

        #Storing bucket if it is unencrypted
        if response['ServerSideEncryptionConfiguration']['Rules'][0]['BucketKeyEnabled']==True:
            unencrypted_bucket.append(name)

    #printing nuckets if unencrypted
    print(unencrypted_bucket)


except Exception as e:
    print(e)