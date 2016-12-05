#!/usr/bin/python

import boto3

#ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
filters = [{  
'Name': 'tag:Name',
'Values': ['*']
}]
instanceIds=[]
response = client.describe_instances(Filters=filters)


#print  response['Reservations']

for out in response['Reservations']:
	for insts in out['Instances']:
		instanceIds.append(insts['InstanceId'])

if(len(instanceIds)>0):
	output=client.start_instances(InstanceIds=instanceIds)

print output['StartingInstances']