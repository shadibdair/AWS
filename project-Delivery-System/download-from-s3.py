from http import client
import resource
import boto3


resource = boto3.resource('s3')
my_bucket = resource.Bucket('secretbucket-tsofen')

# Print the files that exist in the Bucket that I've chosen
print("- The files that exist in the Bucket that I've chosen :")
for s3_file in my_bucket.objects.all():
    print(s3_file.key) # prints the contents of bucket

# For Downloads files
response = my_bucket.download_file('uploadTest.txt', '/home/parallels/Desktop/Course-DevOps-Tsofen/AWS/AWS/project-Delivery-System/uploadTest.txt')

if response == None:
    print("\nSuccess !")
else:
    print("There's an error !")





