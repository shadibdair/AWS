import boto3
from create_policy import createPolicy as get_arn

def attachRoleUser():
    client = boto3.client('iam')
    response = client.attach_user_policy(
    #PolicyArn = get_arn.arn,
    PolicyArn = 'arn:aws:iam::731589008417:policy/boto3-policy-new',
    UserName = 'User-1',
    )

    #print(response)
    #print("Done \t", response.PolicyArn, response.UserName)
    print("Success")

attachRoleUser()