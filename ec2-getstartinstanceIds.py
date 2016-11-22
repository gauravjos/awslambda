import boto3
import json
from datetime import datetime
client = boto3.client('ec2')
filters = [{  
'Name': 'instance-state-name',
'Values': ['stopped']
}]
response = client.describe_instances(Filters=filters)
for instance in response['Reservations']:
	for tag in instance['Instances']:
		print tag['Tags']

#CODE Is In Progress
