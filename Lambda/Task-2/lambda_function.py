import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object, Key and eventName from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    eventname = event['Records'][0]['eventName']
    sns_message = str("This Email Represent a File Status has been Changed in One of Your Bucket \n\n BUCKET NAME: "+ bucket +"\n\n FILE 
NAME: " + key + "\n\n OPERATION: " + eventname + "\n\n")
    try:
        print(eventname)
        if eventname == "ObjectRemoved:Delete":
            print("File is being Deleted")
            sns_message += str("File Deleted")
        else:
            response = s3.get_object(Bucket=bucket, Key=key)
            sns_message += str("FILE CONTENT TYPE: " + str(response['ContentType']) + "\n\nFILE CONTENT: " + 
str(response['Body'].read()))
            print("CONTENT TYPE: " + response['ContentType'])
        print(str(sns_message))
        subject= "S3 Bucket[" + bucket + "] Event[" + eventname + "]"
        print(subject)
        sns_response = sns.publish(
        TargetArn='<REPLACE THIS WITH YOUR SNS ARN>',
        Message= str(sns_message),
        Subject= str(subject)
        )
        #return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this 
function.'.format(key, bucket))
        raise e
