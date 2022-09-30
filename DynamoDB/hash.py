from distutils import text_file
import hashlib
import hash

hasher = hashlib.sha256()

f = open('create_table_dynamodb.py', 'br')
text = f.read()

hasher.update(text)
hasher.digest()