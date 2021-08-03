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


filename = 'peopleDOB.csv'
myRows = []
try:
    with open(filename, 'r') as myCSV:
        data = csv.reader(myCSV)
        next(myCSV)
        for row in data:
            myRows.append(row)
    myCSV.close()
except FileNotFoundError:
    print('no file!')

query = 'UPDATE peopleData set dob = %s\
    where primary_key = %s'

for item in myRows:
    dob = item[1]
    id = item[0]
    cursor.execute(query,(dob,id))
    
print("--------")