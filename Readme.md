# This utility loads all files in a directory recursivley to S3 bcket
# You can also use this utility to list of all laoded files in a bucket

## Requirments see config.ini file under config/config.ini

##[DEFAULT]
- BucketName = atspdf 
- Region = us-east-1
- Location = ./files
- aws_access_key_id = xxxxxxxxx
- aws_secret_access_key = xxxxxxxxxxx

## Note: access and secret key should have requried permissions to read and write to S3 bucket e.g see below
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListObjectsInBucket",
            "Effect": "Allow",
            "Action": ["s3:ListBucket"],
            "Resource": ["arn:aws:s3:::bucket-name"]
        },
        {
            "Sid": "AllObjectActions",
            "Effect": "Allow",
            "Action": "s3:*Object",
            "Resource": ["arn:aws:s3:::bucket-name/*"]
        }
    ]
}
```
## How to Load the file
python loadfiles_s3.py

### if you don't want to install python just run the following executable, note config file has to be in the root folder
loadfiles_s3.exe

## List all the files loaded to bucket
python listfiles_s3.py

### if you don't want to install python just run the following executable, note config file has to be in the root folder
listfiles_s3.exe
