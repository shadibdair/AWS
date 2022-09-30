# Imports
import json
import boto3

# Insert into table : people
def insert_into_people(client, first_name, phone_number):
    new_item={
        'name': {
            'S': first_name,
        },
        'phone': {
            'S': phone_number
        }
    }
    
    response = client.put_item(
        # The name of the table
        TableName='people',
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
def dynamodb_demo():
    creds = get_conf('cred.json')
    print(creds)
    client = boto3.client('dynamodb', aws_access_key_id=creds['access-key-id'],
                                      aws_secret_access_key=creds['secret-access-key'],
                                      region_name=creds['region'])
    insert_into_people(client, 'Shadi', "09-9827123")
    insert_into_people(client, 'Mark', "09-9112632")
    
# Calling the main function.
dynamodb_demo()