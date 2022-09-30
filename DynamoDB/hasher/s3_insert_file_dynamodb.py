# Imports
import json
import boto3
from boto3 import client
import hashlib
import filecmp

# Insert into table : people
def insert_into_hashes_files(client_, hash_id):
    new_item={
        'hashId': {
            'B': hash_id,
        }
    }
    
    response = client_.put_item(
        # The name of the table
        TableName='hashes-files',
        Item = new_item,
        ReturnConsumedCapacity='TOTAL'
    )


# Function that read my cred
def get_conf(conf_file):
    try:
        with open(conf_file, 'r') as credfile:
            confdata = json.load(credfile)
            return confdata
    except OSError :
        return {'access_key_id': None, 'secret_access_key': None, 'region': None}   

# The main function that connect to my user on AWS console, and insert the query.
def dynamodb():
    creds = get_conf('cred.json')
    print(creds)
    client_ = boto3.client('dynamodb', aws_access_key_id=creds['access-key-id'],
                                      aws_secret_access_key=creds['secret-access-key'],
                                      region_name=creds['region'])
    hasher = hashlib.sha256()
    conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
    for key in conn.list_objects(Bucket='mainbucketwithouthash')['Contents']:
        #print(key['Key'])
        file = key['Key']
        # Hash
        f = open(file, "rb")
        text = f.read()
        hasher.update(text)
        hashed = hasher.hexdigest()
        insert_into_hashes_files(client_, hashed)




# Calling the main function.
dynamodb()