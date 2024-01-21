import boto3

try:

    #EC2 client
    ec2=boto3.client('ec2')
    

    #Creating snapshot from EC2 instance
    response=ec2.create_snapshots(Description='Travel memory backend snapshot',
    InstanceSpecification={
        'InstanceId':'i-08c57a3f97fd6133e'
    })

    #Getting snapshot Id and storing variable 
    snapshotId=response['Snapshots'][0]['SnapshotId']

    #Created instance from snapshot.
    instance=ec2.run_instances(BlockDeviceMappings=[{
        'DeviceName':'/dev/sda1',
        'Ebs':{
            'SnapshotId':snapshotId
        }    
    }],ImageId='ami-0c7217cdde317cfec',MaxCount=1,MinCount=1)

    print(instance)


except Exception as e:
    print(e)