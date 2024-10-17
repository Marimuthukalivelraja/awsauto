import boto3
import boto3.session
awsManagementConsole = boto3.session.Session(profile_name='default')
#iamConsole = awsManagementConsole.resource('iam')
#for eachUser in iamConsole.users.all():
#    print(eachUser.name)

#create a seperate console for iam
iamConsole = awsManagementConsole.client(service_name='iam')
user =iamConsole.list_users()
print(user['Users'])    

#create a seperate console for ec2
ec2Console = awsManagementConsole.client(service_name='ec2', region_name='us-east-1')

response=ec2Console.run_instances(
    ImageId ='ami-0fff1b9a61dec8a5f',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1
)
result= ec2Console.describe_instances() 

instance_names = []

for reservation in result['Reservations']:
    for instance in reservation['Instances']:
        name = None
        if 'Tags' in instance:
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    name = tag['Value']
                    break  
        instance_names.append(name)


print("EC2 Instance Names:")
for name in instance_names:
    print(name)

