

import boto3

#s3 = boto3.client("s3")
s3 = boto3.resource(service_name = 's3')
response = s3.meta.client.upload_file(Filename='/home/parallels/Desktop/Course-DevOps-Tsofen/AWS/AWS/project-Delivery-System/file-python.txt', Bucket='secretbucket-tsofen', Key='s3_output_key')
s3_client = boto3.client('s3', aws_access_key_id=self.accessid, aws_secret_access_key=self.accesskey)
s3_client.download_file(self.bucket, file_name, file_to_save)

print(response)



 