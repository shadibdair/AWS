import json
import boto3

def createPolicy():
    # Create IAM client
    iam = boto3.client('iam')

    # Create a policy
    my_managed_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "iam:Get*",
                    "iam:List*"
                ],
                "Resource": "*"
            }
        ]
    }
    response = iam.create_policy(
        PolicyName='boto3-policy-new',
        PolicyDocument=json.dumps(my_managed_policy)
    )

    print(response)

createPolicy()