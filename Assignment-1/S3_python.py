author="Anindita"

import boto3
s3=boto3.client('s3') #Linking with the client type
def CreateBucket():
    s3.upload_file("anindita.txt", "anindita-bucket","anindita.txt")    #Uploading file to s3 bucket, format: Filename/path in local, bucket-name, filename in bucket
    s3.create_bucket(Bucket='anindita-third-bucket')   #Creating second bucket
    ChangePublicPersmission()


def ChangePublicPersmission():
    #Changing public access permissions
    client=boto3.client('s3')
    response = client.put_public_access_block(
    Bucket='anindita-second-bucket',
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        }
    )
    ChangeACLPermissions()

def ChangeACLPermissions():
    #Disabling ACL write permission
    s3.put_bucket_acl(
        AccessControlPolicy={
            'Grants': [
                {
                    'Grantee': {
                        'DisplayName': 'awslabsc0w516804t1575138305',
                        'ID': 'a8e938119a91aa2be92ca36e610229629bc0b265b354c5f068d5e21beb3b9439',
                        'Type': 'CanonicalUser',
                    },
                    'Permission': 'READ_ACP'
                },
            ],
            'Owner': {
                'DisplayName': 'awslabsc0w516804t1575138305',
                'ID': 'a8e938119a91aa2be92ca36e610229629bc0b265b354c5f068d5e21beb3b9439'
            }
        },
        Bucket='anindita-second-bucket'
    )
    MoveFile()

def MoveFile():
    #Move File from 1st bucket to 2nd bucket
    s3_resource=boto3.resource('s3')
    s3_resource.Object('anindita-second-bucket','anindita.txt').copy_from(CopySource='anindita-bucket'+'/'+'anindita.txt')
    s3_resource.Object('anindita-bucket','anindita.txt').delete()

CreateBucket()
