import csv
import pymysql
import configparser


config = configparser.ConfigParser()
config.read_file(open('credentials.py'))
dbhost = config['csc']['dbhost']
dbuser = config['csc']['dbuser']
dbpw = config['csc']['dbpw']

dbschema = 'dryan16'

dbconn = pymysql.connect(host=dbhost,
                         user=dbuser,
                         passwd=dbpw,
                         db=dbschema,
                         use_unicode=True,
                         charset='utf8mb4',
                         autocommit=True)
cursor = dbconn.cursor()




query = 'SELECT u.userName, l.hashOfWord \
FROM `bbWordList`l \
INNER Join `bbUserDatabase` u ON u.hashedPassword = l.hashOfWord'

cursor.execute(query)
items = cursor.fetchall()

for row in items:
    name = row[0]
    hash = row[1]
    print('the password for ', name, ' is ', hash)
dbconn.close
