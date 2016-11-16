#!/usr/bin/python
from __future__ import print_function
import boto3

s3 = boto3.resource('s3')
print(*s3.buckets.all())
# for bucket in s3.buckets.all():
#     print(bucket.name)
