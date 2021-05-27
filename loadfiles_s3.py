import configparser
import os
import sys

import boto3


def upload_dir(path, bucket_name, region, access_key, secret_key):
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    s3 = session.resource("s3", region_name=region)
    for root, dirs, files in os.walk(path):
        for file in files:
            data = open(os.path.join(root, file), 'rb')
            s3.Bucket(bucket_name).put_object(Key=file, Body=data)
            print("File:" + file + " has been copied to " + bucket_name + " bucket")


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('./config/config.ini')
    print("Loading files from dir: " + str(config['DEFAULT']['Location']))
    try:
        upload_dir(config['DEFAULT']['Location'], config['DEFAULT']['BucketName'], config['DEFAULT']['Region'],
                   config['DEFAULT']['aws_access_key_id'],
                   config['DEFAULT']['aws_secret_access_key'])
    except:
        print("An exception occurs: " + str(sys.exc_info()[0]))
