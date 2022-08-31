import boto3


def attachRoleUser():
    client = boto3.client('iam')
    response = client.attach_user_policy(
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess',
    UserName='Halland',
    )

    print(response)
