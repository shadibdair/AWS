

import boto3

#s3 = boto3.client("s3")
s3 = boto3.client('s3')
response = s3.upload_file(Filename='/home/parallels/Desktop/Course-DevOps-Tsofen/AWS/AWS/project-Delivery-System/file-python.txt', Bucket='secretbucket-tsofen', Key='s3_output_key')


print(response)



 