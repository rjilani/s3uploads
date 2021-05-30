import configparser
import os
import sys

import boto3

path = "./download_dir"
def download_dir(file, bucket_name, region, access_key, secret_key):
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    s3_client = session.client("s3", region_name=region)
    create_dir()
    with open(os.path.join(path, file), 'wb') as f:
        s3_client.download_fileobj(bucket_name, file, f)
        print('File: ' + file + ' downloaded')

def create_dir():
    if not os.path.exists(path):
        os.makedirs(path)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('./config/config.ini')
    print("Downloading file from bucket: " + str(config['DEFAULT']['BucketName']))
    try:
        download_dir(config['DEFAULT']['FileToDownLoad'], config['DEFAULT']['BucketName'], config['DEFAULT']['Region'],
                   config['DEFAULT']['aws_access_key_id'],
                   config['DEFAULT']['aws_secret_access_key'])
    except Exception as e:
        print("An exception occurs: " + str(sys.exc_info()[0]))
        print(e)
