import boto3
from dotenv import load_dotenv
import os
import re

load_dotenv()

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
AWS_BUCKET_PREFIX = os.getenv('AWS_BUCKET_PREFIX')

s3 = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

def list_files(bucket_name, prefix):
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    return [item['Key'] for item in response.get('Contents', [])]

def upload_file(file_name, bucket_name, prefix, object_name):
    object_name = prefix + file_name
    response = s3.upload_file(file_name, bucket_name, object_name)

def filter_files(bucket_name, prefix, pattern):
    all_files = list_files(bucket_name, prefix)
    return [f for f in all_files if re.search(pattern, f)]

print(filter_files(AWS_BUCKET_NAME, AWS_BUCKET_PREFIX, '.*\.jpg'))
print(list_files(AWS_BUCKET_NAME, AWS_BUCKET_PREFIX))