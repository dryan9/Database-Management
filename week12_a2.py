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

userName = input("what is your desired username?")
email = userName + "@bigbank.com"

PINlength = 4
PINdigit = 0
PIN = ''
while PINdigit < PINlength:
    randomNum = random.randint(0, 9)
    PIN = PIN + str(randomNum)
    PINdigit += 1

print(PIN)

userNum = None

insertQuery = 'INSERT Into `userDatabase`(userID, userName, email , PIN)\
    VALUES(%s, %s, %s, %s)'

cursor.execute(insertQuery, (userNum, userName, email, PIN))

dbconn.close()

