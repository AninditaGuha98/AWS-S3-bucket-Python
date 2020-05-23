author='Anindita'

import mysql.connector
import boto3
conn=mysql.connector.connect(host='serverless-2.ccmdqmbvy12j.us-east-1.rds.amazonaws.com'
                                 ,user='admin',
                                 password='serverlessadmin',
                                 db='login_database')

cursor=conn.cursor()
#Inserting Value into database

id=input("Please enter the user id: ")
password=input("Please enter the password: ")

#sending file to S3 bucket
#
# s3=boto3.client('s3')
# s3.upload_file("Lookup5410.txt", "anindita-bucket","Lookup5410.txt")
#
# s=boto3.resource('s3')
# #fetching file from s3 bucket
# s.Bucket('anindita-bucket').download_file("Lookup5410.txt",'Lookup.txt')

with open('Lookup.txt','r') as read:
    lookup=read.readlines()
    

    # for letter in password:
    #     for val in lookup:
    #         if val==letter
    #




# insert_data=("INSERT into login (userId,password) values(25,'XYZ')")
# cursor.execute(insert_data)
#
#
# #Fetching value from database
# fetch_value=("Select * from login")
# cursor.execute(fetch_value)
# print(cursor.fetchall())
#
# conn.commit()
# conn.close()

