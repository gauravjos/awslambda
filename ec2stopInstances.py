#!/usr/bin/python

import boto3

#ec2 = boto3.resource('ec2')
regions = boto3.client('ec2').describe_regions()
for reg in regions['Regions']:
 	client = boto3.client('ec2',region_name=reg['RegionName'])
 	filters = [{  'Name': 'instance-state-name','Values': ['running']}]
 	instanceIds=[]
 	response = client.describe_instances(Filters=filters)
 	for out in response['Reservations']:
 		for insts in out['Instances']:
 			instanceIds.append(insts['InstanceId'])
 	if(len(instanceIds)>0):
 		output=client.stop_instances(InstanceIds=instanceIds)

# print output['StoppingInstances']
