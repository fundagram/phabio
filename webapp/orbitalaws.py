import boto3
import botocore.session

session = botocore.session.get_session()
session.profile = 'default'
boto3.setup_default_session(region_name='us-east-1', botocore_session=session )


def installLocalCreds():
    return ''

def listS3():
    s3 = boto3.resource('s3')
    buckets = []
    for bucket in s3.buckets.all():
        print(bucket.name)
        bucket.append[bucket.name]
    return buckets


def launchEC2Image():
    try:
        ec2 = boto3.resource('ec2')
        # load a default ami
        securityGroupdIds = ["sg-0bde6c6d"]
        print securityGroupdIds[0]
        result = ec2.create_instances(ImageId='ami-30b6c65a', MinCount=1, MaxCount=1, KeyName="nintendo", SecurityGroupIds=securityGroupdIds)
        return result
    except:
        return 'failed to launch'

if __name__ == "__main__":
  #listS3()
  launchEC2Image()