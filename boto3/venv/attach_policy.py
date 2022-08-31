import boto3
from create_policy import createPolicy as get_arn

def attachRoleUser():
    client = boto3.client('iam')
    response = client.attach_user_policy(
    PolicyArn = get_arn.arn,
    UserName = 'Dan',
    )

    #print(response)
    print("Done \t", response.PolicyArn, response.UserName)

#attachRoleUser()