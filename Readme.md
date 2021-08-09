#### This utility loads all files in a directory recursivley to S3 bcket
#### You can also use this utility to list all files in a bucket, delete, or downlaod a file from a bucket

##### Requirments see config.ini file under config/config.ini

#####[DEFAULT]
- BucketName = test 
- Region = us-east-1
- Location = ./files
- aws_access_key_id = xxxxxxxxx
- aws_secret_access_key = xxxxxxxxxxx
- FileToDownLoad = test.txt

##### Note: access and secret key should have requried permissions to read and write to S3 bucket e.g see below
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::bucketname"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::bucketname/*"
        }
    ]
}
```
##### How to Load the file to S3 bucket
python loadfiles_s3.py

##### List all the files in S3 bucket
python listfiles_s3.py

##### Download file to local dir from S3 bucket
python download_s3.py

##### Delete a file from s3 bukcet
python delete_s3.py

##### if you don't want to install python just run the following executable to list, load and download files, 
##### note config.ini file has to be under config folder in the root directory
listfiles_s3.exe

loadfiles_s3.exe

download_s3.exe

delete_s3.exe
