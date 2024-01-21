import boto3

try:

    ec2 = boto3.client('ec2')

    #arrays to hold ids of instances to stop and start
    stop_instances=[]
    start_instances=[]



    #fetching all the tags of EC2 instances
    response = ec2.describe_tags()

    for i in response['Tags']:
        #checking whether the tag is Key with Action and it value is Auto-Start-Ishwari
        if i['Key']=='Action' and i['Value']=='Auto-Start-Ishwari':
                start_instances.append(i['ResourceId'])

            
        #checking whether the tag is Key with Action and it value is Auto-Stop-Ishwari
        elif i['Key']=='Action' and i['Value']=='Auto-Stop-Ishwari':
                stop_instances.append(i['ResourceId'])

    print('Instances to start '+str(start_instances))
    print('\nInstances to stop '+str(stop_instances))

    #starting instances
    response=ec2.start_instances(InstanceIds=start_instances)
    
    print("\nStart Instances state")
    for i in range(len(response['StartingInstances'])):
        print(response['StartingInstances'][i]['InstanceId'],response['StartingInstances'][i]['CurrentState']['Name'])
    
    #stopping instances
    response=ec2.stop_instances(InstanceIds=stop_instances)

    print("\nStop Instances state")
    for i in range(len(response['StoppingInstances'])):
        print(response['StoppingInstances'][i]['InstanceId'],response['StoppingInstances'][i]['CurrentState']['Name'])
    

except Exception as e:
    #Printing whatever exption has occurred instead of unexpectable termination
    print(e)