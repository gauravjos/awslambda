import boto3



s3 = boto3.resource('s3')

bucket = s3.Bucket('majha-bucket')

for obj in bucket.objects.all():
    obj.delete()