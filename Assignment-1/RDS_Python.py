author = 'Anindita'

import mysql.connector
import boto3

conn = mysql.connector.connect(host='serverless-2.ccmdqmbvy12j.us-east-1.rds.amazonaws.com'
                               , user='admin',
                               password='serverlessadmin',
                               db='login_database')

cursor = conn.cursor()
# Inserting Value into database

id=input("Please enter the user id: ")
password=input("Please enter the password: ")

# sending file to S3 bucket
#
# s3=boto3.client('s3')
# s3.upload_file("Lookup5410.txt", "anindita-bucket","Lookup5410.txt")
#
# s=boto3.resource('s3')
# #fetching file from s3 bucket
# s.Bucket('anindita-bucket').download_file("Lookup5410.txt",'Lookup.txt')


#
LookUp={}
encryptedpass=''
with open('Lookup.txt','r') as read:
    lookup=read.readline().split()
    for i in read.readlines():
        LookUp[i.split()[0]]=i.split()[1]
    for letter in password:
        encryptedpass=encryptedpass+''+LookUp[letter]
print(encryptedpass)


insert_data=("INSERT into login (userId,password) values(%s,%s)")
cursor.execute(insert_data,(id,encryptedpass))


# Fetching value from database
fetch_id=int(input("id?"))
fetch_value = ("Select * from login where userId={0}".format(fetch_id))
cursor.execute(fetch_value)
results = cursor.fetchone()
decryptedpass=''

word = list(results[1])
it = iter(word)
print(word)
for i in it:
    match=i+''+ next(it)

    for key,value in LookUp.items():
        if value==match:
            decryptedpass=decryptedpass+''+ key
            break
print(decryptedpass)


conn.commit()
conn.close()
