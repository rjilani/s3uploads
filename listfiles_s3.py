import configparser
import sys

import boto3


def list_files_in_bucket(bucket_name, region, access_key, secret_key):
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    s3 = session.resource("s3", region_name=region)
    my_bucket = s3.Bucket(bucket_name)
    for file in my_bucket.objects.all():
        print(file.key)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('./config/config.ini')
    print("List of files in Bucket: " + config['DEFAULT']['BucketName'])
    try:
        list_files_in_bucket(config['DEFAULT']['BucketName'], config['DEFAULT']['Region'],
                             config['DEFAULT']['aws_access_key_id'],
                             config['DEFAULT']['aws_secret_access_key'])
    except Exception as e:
        print("An exception occurs: " + str(sys.exc_info()[0]))
        print(e)
