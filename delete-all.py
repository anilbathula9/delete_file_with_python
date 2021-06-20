import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('my-tf-s3backend-state-9')
bucket.objects.all().delete()