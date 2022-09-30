from boto3 import client
import hashlib

hasher = hashlib.sha256()

conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
for key in conn.list_objects(Bucket='mainbucketwithouthash')['Contents']:
    #print(key['Key'])
    file = key['Key']
    # Hash
    f = open(file, "rb")
    text = f.read()
    #print(text)
    hasher.update(text)
    print(hasher.digest(),"\n")
    



# Output:
# text1.txt
# text2.txt
# text3.txt
# text4.txt
# text5.txt
# text6.txt