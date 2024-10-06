import boto3
from dotenv import load_dotenv
import os
import re

load_dotenv()

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
AWS_BUCKET_PREFIX = os.getenv('AWS_BUCKET_PREFIX')

print(ACCESS_KEY)

s3 = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

def list_files(bucket_name, prefix):
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    return [item['Key'] for item in response.get('Contents', [])]

print(list_files(AWS_BUCKET_NAME, AWS_BUCKET_PREFIX))