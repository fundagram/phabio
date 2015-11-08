#!/usr/bin/python
import boto3
import sys

if __name__ == "__main__":
    accessKey = sys.argv[1]
    secretKey = sys.argv[2]    
    client = boto3.client('elasticbeanstalk')

