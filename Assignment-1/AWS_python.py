author="Anindita"

import boto3
s3=boto3.client('s3')   #Linking with the client type
# s3.upload_file("anindita.txt", "anindita-bucket","anindita.txt")    #Uploading file to s3 bucket, format: Filepath, bucket-name, filename
# s3.create_bucket(Bucket='anindita-third-bucket')   #Creating second bucket


# #Changing public access permissions
# client=boto3.client('s3')
# response = client.put_public_access_block(
# Bucket='anindita-second-bucket',
#     PublicAccessBlockConfiguration={
#         'BlockPublicAcls': True,
#         'IgnorePublicAcls': True,
#         'BlockPublicPolicy': True,
#         'RestrictPublicBuckets': True
#     }
# )

#Disabling ACL write permission
# response=s3.get_bucket_acl(Bucket='anindita-second-bucket')
# s3.put_bucket_acl(
#     AccessControlPolicy={
#         'Grants': [
#             {
#                 'Grantee': {
#                     'DisplayName': 'awslabsc0w516804t1575138305',
#                     'ID': 'a8e938119a91aa2be92ca36e610229629bc0b265b354c5f068d5e21beb3b9439',
#                     'Type': 'CanonicalUser',
#                 },
#                 'Permission': 'READ_ACP'
#             },
#         ],
#         'Owner': {
#             'DisplayName': 'awslabsc0w516804t1575138305',
#             'ID': 'a8e938119a91aa2be92ca36e610229629bc0b265b354c5f068d5e21beb3b9439'
#         }
#     },
#     Bucket='anindita-second-bucket'
# )

#Move File from 1st bucket to 2nd bucket

#dmfskdfmksdf
