#!/usr/bin/python
import boto3
messg="myMessage"
client = boto3.client('sns')
topicArn='arn:aws:sns:us-west-2:797393685292:SNSTopic'
response = client.publish(TopicArn=topicArn,Message=messg)
print response