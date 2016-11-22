import boto3


s3 = boto3.resource('s3')
last_modified=0
bucket = s3.Bucket("majha-bucket")

# for obj in bucket.objects.all():
#     print "Deleting :",obj.key 
#     obj.delete()
for obj in bucket.objects.all():
	if (obj.last_modified.strftime("%s")>last_modified):
		last_modified=obj.last_modified.strftime("%s")
		obj_name=obj.key
	
for obj in bucket.objects.all():
	if(obj.key!=obj_name):
		obj.delete()


