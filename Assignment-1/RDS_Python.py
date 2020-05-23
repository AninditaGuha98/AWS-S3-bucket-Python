author = 'Anindita'

import mysql.connector
import boto3

conn = mysql.connector.connect(host='serverless-2.ccmdqmbvy12j.us-east-1.rds.amazonaws.com'
                               , user='admin',
                               password='serverlessadmin',
                               db='login_database')

cursor = conn.cursor()
LookUp={}

# sending file to S3 bucket
def send_fetchS3():
    s3=boto3.client('s3')
    s3.upload_file("Lookup5410.txt", "anindita-bucket","Lookup5410.txt")
    s=boto3.resource('s3')
    #fetching file from s3 bucket
    s.Bucket('anindita-bucket').download_file("Lookup5410.txt",'Lookup.txt')
    readlookup()

#Reading the lookup text file
def readlookup():
    with open('Lookup.txt', 'r') as read:
        for i in read.readlines():
            LookUp[i.split()[0]] = i.split()[1]
    database_insert(cursor)


#Function for encrypting the password
def passwordEncryption(password):
    encryptedpass=''
    for letter in password:
        encryptedpass=encryptedpass+''+LookUp[letter]
    return encryptedpass


#Function for decrypting the password
def passwordDecryption(results):
    decryptedpass=''
    word = list(results[1])
    it = iter(word)
    for i in it:
        match=i+''+ next(it)
        for key,value in LookUp.items():
            if value==match:
                decryptedpass =decryptedpass+''+ key
                break
    return decryptedpass

# Inserting values into database
def database_insert(cursor):
    id=input("Please enter the user id: ")
    password=input("Please enter the password: ")
    encryptedpass=passwordEncryption(password)
    insert_data = ("INSERT into login (userId,password) values(%s,%s)")
    cursor.execute(insert_data, (id, encryptedpass))
    databaseRetrieve(cursor)


# Fetching value from database
def databaseRetrieve(cursor):
    fetch_id=int(input("Which id do you want to fetch?"))
    fetch_value = ("Select * from login where userId={0}".format(fetch_id))
    cursor.execute(fetch_value)
    results = cursor.fetchone()
    decryptedpass=passwordDecryption(results)
    print("Decrypted password: ",decryptedpass)

send_fetchS3()
conn.commit()
conn.close()
