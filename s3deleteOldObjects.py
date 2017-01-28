import boto3


s3 = boto3.resource('s3')
last_modified=0
s3object = s3.Object("majha-bucket","myfolder2")
print s3object.
# for obj in bucket.objects.all():
#     print "Deleting :",obj.key 
# #     obj.delete()
# for obj in bucket.objects.all():
# 	if (obj.last_modified.strftime("%s")>last_modified):
# 		last_modified=obj.last_modified.strftime("%s")
# 		obj_name=obj.key
	
# for obj in bucket.objects.all():
# 	if(obj.key!=obj_name):
# 		print "Deleting: ",obj.key
# 		obj.delete()


