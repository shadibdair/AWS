import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3', region_name='us-east-1')

def upload_my_file(bucket, file_to_upload, file_name):

    key = file_name
    response = s3_client.upload_file(file_to_upload, bucket, key)


#Upload file
upload_my_file("secretbucket-tsofen", "/project-Delivery-System/file-python.txt", "file-python.txt")

# home/parallels/Desktop/Course-DevOps-Tsofen/AWS/AWS