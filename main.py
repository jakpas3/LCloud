import boto3
from dotenv import load_dotenv
import os
import re
import argparse

load_dotenv()

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

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

def delete_files(bucket_name, prefix, pattern):
    files_to_delete = filter_files(bucket_name, prefix, pattern)
    for file_key in files_to_delete:
        s3.delete_object(Bucket=bucket_name, Key=file_key)


def create_parser():
    parser = argparse.ArgumentParser(description='AWS S3 Bucket Operations CLI')
    subparsers = parser.add_subparsers(dest='command')

    list_parser = subparsers.add_parser('list', help='List files in a bucket (schema: list your_bucket_name some_prefix/)')
    list_parser.add_argument('bucket', help='S3 bucket name')
    list_parser.add_argument('prefix', help='Prefix within the S3 bucket')

    upload_parser = subparsers.add_parser('upload', help='Upload a file to a bucket (schema: upload path/to/your/local/file.txt your_bucket_name some_prefix/)')
    upload_parser.add_argument('file_path', help='Local file path for upload ')
    upload_parser.add_argument('bucket', help='S3 bucket name')
    upload_parser.add_argument('prefix', help='Prefix within the S3 bucket')

    filter_parser = subparsers.add_parser('filter', help='Filter files in a bucket by regex (schema: filter your_bucket_name some_prefix/ ".*\.txt")')
    filter_parser.add_argument('bucket', help='S3 bucket name')
    filter_parser.add_argument('prefix', help='Prefix within the S3 bucket')
    filter_parser.add_argument('pattern', help='Regex pattern')

    delete_parser = subparsers.add_parser('delete', help='Delete files in a bucket by regex (schema: delete your_bucket_name some_prefix/ ".*\.json")')
    delete_parser.add_argument('bucket', help='S3 bucket name')
    delete_parser.add_argument('prefix', help='Prefix within the S3 bucket')
    delete_parser.add_argument('pattern', help='Regex pattern')

    return parser

def main():
    parser = create_parser()
    print("Type 'help' for command options or 'exit' to quit.")
    while True:
        args = input("Enter command: ").strip().split()
        if args[0].lower() == 'exit':
            print("Exiting...")
            break
        elif args[0].lower() == 'help':
            parser.print_help()
            continue

        try:
            args = parser.parse_args(args)
            if args.command == 'list':
                print(list_files(args.bucket, args.prefix))
            elif args.command == 'upload':
                upload_file(args.file_path, args.bucket, args.prefix)
            elif args.command == 'filter':
                print(filter_files(args.bucket, args.prefix, args.pattern))
            elif args.command == 'delete':
                delete_files(args.bucket, args.prefix, args.pattern)
        except SystemExit:
            continue

if __name__ == '__main__':
    main()