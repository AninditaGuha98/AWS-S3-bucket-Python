author="Anindita"

import boto3
import boto
#Linking with the client type
s3=boto3.client('s3')

#Uploading file to s3 bucket, format: Filepath, bucket-name, filename
# s3.upload_file("anindita.txt", "anindita-bucket","anindita.txt")

#Created second bucket
# s3.create_bucket(Bucket='anindita-second-bucket')

#part B
client=boto3.client('s3')
# response = client.create_access_point(
#     AccountId='998882546124',
#     Name='PartB',
#     Bucket='anindita-second-bucket',
#     PublicAccessBlockConfiguration={
#         'BlockPublicAcls': True,
#         'IgnorePublicAcls': False,
#         'BlockPublicPolicy': False,
#         'RestrictPublicBuckets': False
#     }
# )
response=client.put_bucket_acl(Bucket='anindita-second-bucket')
print(response)
