import boto3
import gzip
import json
import time

# AWS clients
logs_client = boto3.client('logs')
s3_client = boto3.client('s3')

# Constants
S3_BUCKET_NAME = 'devtestes3cloud'
LOG_GROUP = 'LOG-FROM-EC2'
