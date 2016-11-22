import boto3

vpcId="vpc-f912109e"
asclient = boto3.client('autoscaling')

vfilters = [{  
'Name': 'vpc-id',
'Values': [vpcId]
}]

ASresponse = asclient.describe_auto_scaling_groups()
print ASresponse


