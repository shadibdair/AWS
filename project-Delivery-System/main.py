import boto3
from http import client
from botocore.exceptions import ClientError

def upload_my_file(bucket, file_to_upload, file_name):
    s3_client = boto3.client('s3', region_name='us-east-1')
    key = file_name
    # Output the response of this request.
    response = s3_client.upload_file(file_to_upload, bucket, key)

def create_bucket_(bucket_name):
    s3 = boto3.client("s3")
    #response = s3.create_bucket(bucket_name='new-bucket-usingBoto3')
    response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
        'LocationConstraint': 'us-east-1'
    },)
    # Output the response of this request.
    print(response)


#Create Bucket
create_bucket_("new-bucket-usingBoto3")
#Upload File
upload_my_file("secretbucket-tsofen", "/project-Delivery-System/logs", "logs")


