import boto3 

def cr_user(username):
    iam = boto3.client("iam")
    response = iam.create_user(UserName=username)
    print(response)
