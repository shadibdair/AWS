from boto3 import client
import hashlib
import filecmp


hasher = hashlib.sha256()

conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
for key in conn.list_objects(Bucket='mainbucketwithouthash')['Contents']:
    #print(key['Key'])
    file = key['Key']
    # Hash
    f = open(file, "rb")
    text = f.read()
    hasher.update(text)
    print(hasher.hexdigest(),"\n")

      
# result = filecmp.cmp(file, filee)
# print(result)

    
