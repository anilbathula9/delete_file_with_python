import boto3 
client = boto3.client('s3')
client.delete_object(Bucket='my-tf-s3backend-state-9', Key='AWSLogs/')