import pymysql
import configparser
import random

# Get credentials to connect to database
config = configparser.ConfigParser()
config.read_file(open('credentials.py'))
dbhost = config['csc']['dbhost']
dbuser = config['csc']['dbuser']
dbpw = config['csc']['dbpw']

dbschema = 'dryan16'

# Open database connection
dbconn = pymysql.connect(host=dbhost,
                         user=dbuser,
                         passwd=dbpw,
                         db=dbschema,
                         use_unicode=True,
                         charset='utf8mb4',
                         autocommit=True)
cursor = dbconn.cursor()

user = input("enter your username:")

queryName = 'SELECT userId, PIN \
            FROM `userDatabase`\
             where userName = %s'

cursor.execute(queryName, (user))

result = cursor.fetchone()

print()
print("The current Pin for that username is:", result[1])

userP = input("Enter your new desired Pin:")

qUpdate = "UPDATE `userDatabase` SET PIN = %s \
            WHERE PIN = %s"

cursor.execute(qUpdate,(userP, result[1]))
print("Thank you, your information has been updated")
