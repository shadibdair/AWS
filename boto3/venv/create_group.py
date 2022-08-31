import boto3

def cr_group(groupname):
    #creating group with client
    iam = boto3.client('iam')
    create_group_response = iam.create_group(GroupName = groupname)
    print(create_group_response)