import configparser
import json
import sys

import boto3

path = "./download_dir"


def download_dir(file, bucket_name, region, access_key, secret_key):
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    s3_client = session.client("s3", region_name=region)

    response = s3_client.delete_object(
        Bucket=bucket_name,
        Key=file
    )

    print(json.dumps(response, indent=4, sort_keys=True))

    print('File: ' + file + ' deleted')


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('./config/config.ini')
    print("Deleting the file: " + str(config['DEFAULT']['FileToDelete']) + " from bucket: " + config['DEFAULT']['BucketName'])
    try:
        download_dir(config['DEFAULT']['FileToDelete'], config['DEFAULT']['BucketName'], config['DEFAULT']['Region'],
                     config['DEFAULT']['aws_access_key_id'],
                     config['DEFAULT']['aws_secret_access_key'])
    except Exception as e:
        print("An exception occurs: " + str(sys.exc_info()[0]))
        print(e)
