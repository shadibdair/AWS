import json
import boto3

def createPolicy():
    download_permission = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "*"
        }
    ]
    }

    upload_permission = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "*"
        }
    ]
    }

    # Create IAM client
    iam = boto3.client('iam')

    # Create a policy
    my_managed_policy = upload_permission
    response = iam.create_policy(
        PolicyName='boto3-policy-new-upload',
        PolicyDocument=json.dumps(my_managed_policy)
    )

    print(response)

createPolicy()