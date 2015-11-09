import boto3
import botocore.session
import traceback

session = botocore.session.get_session()
#session.profile = 'default'
boto3.setup_default_session(region_name='us-east-1', botocore_session=session )


def installLocalCreds():
    return ''

def listS3():
    s3 = boto3.resource('s3')
    buckets = []
    for bucket in s3.buckets.all():
        print(bucket.name)
        buckets.append(bucket.name)
    return buckets


def launchEC2Image():
    try:
        ec2 = boto3.resource('ec2')
        # load a default ami
        securityGroupdIds = ["sg-0bde6c6d"]
        print securityGroupdIds[0]
        result = ec2.create_instances(ImageId='ami-d05e75b8', MinCount=1, MaxCount=1, KeyName="nintendo", SecurityGroupIds=securityGroupdIds, InstanceType="t2.micro")
        print "EC2 result:" + str(result)
        return result
    except:
        traceback.print_exc()
        return 'failed to launch'


def getAllNodes(typeFilter, stateFilter):
    try:
        ec2 = boto3.resource('ec2')
        eclient = ec2.meta.client

        
        result = eclient.describe_instances( Filters=[
                                                        {'Name': 'instance-type','Values': [typeFilter, ] },
                                                        {'Name': 'instance-state-name','Values': [stateFilter, ] },
                                                      ]
                                            )
        #result = eclient.describe_instances()
        #print "EC2 result:" + str(result)
        return result
    except:
        traceback.print_exc()
        return 'failed to retrieve instances'

if __name__ == "__main__":
  #listS3()
  launchEC2Image()