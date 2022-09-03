from http import client
import boto3

s3 = boto3.client("s3")
response = s3.create_bucket(Bucket="bucket-python-tsofen")

print(response)