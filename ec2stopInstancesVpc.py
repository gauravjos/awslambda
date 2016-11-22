#!/usr/bin/python

import boto3

client = boto3.client('ec2')
vfilters = [{  
'Name': 'tag:Name',
'Values': ['My VPC']
}]

instanceIds=[]
VPCresponse = client.describe_vpcs(Filters=vfilters)
vpcId = VPCresponse['Vpcs'][0]['VpcId']
ifilters= [{  
'Name': 'vpc-id',
'Values': [vpcId]
}]
Instresponse = client.describe_instances(Filters=ifilters)
for out in Instresponse['Reservations']:
	for insts in out['Instances']:
		instanceIds.append(insts['InstanceId'])

if(len(instanceIds)>0):
 	output=client.stop_instances(InstanceIds=instanceIds)
else:
  	print "None of the Instances Stopped"


