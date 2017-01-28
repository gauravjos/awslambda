#!/usr/bin/python
import boto3

client = boto3.client('sns')
response = client.create_topic(Name='SNS_Sample_topic')
print response['TopicArn']