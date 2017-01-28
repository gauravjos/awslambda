#!/usr/bin/python
from __future__ import print_function
import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket('majha-bucket')

for obj in bucket.objects.all():
    print(obj.key)
