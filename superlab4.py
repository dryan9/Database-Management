import pymysql
import configparser
import hashlib


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

query = 'SELECT word FROM `bbWordList`'
updateQ = 'UPDATE `bbWordList` SET hashOfWord = %s where word = %s'

cursor.execute(query)

someword = cursor.fetchall()

for row in someword:
    #print(row[0])
    hash = hashlib.md5(row[0].encode()).hexdigest()
    print(hash)
    cursor.execute(updateQ, (hash, row[0]))
