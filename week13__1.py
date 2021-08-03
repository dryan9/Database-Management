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


filename = 'peopleData.csv'
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

insertQuery = 'INSERT INTO peopleData (first_name, last_name, company_name, adress, city, \
 county, state, zip, phone1, phone2, email, web) \
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
               
for item in myRows:
    zero = item[0]
    one = item[1]
    two = item[2]
    three = item[3]
    four = item[4]
    five = item[5]
    six = item[6]
    seven = item[7]
    eight = item[8]
    nine = item[9]
    ten = item[10]
    eleven = item[11]
    cursor.execute(insertQuery, (zero, one, two, three, four, five, six, seven,eight,\
                                 nine, ten, eleven))
print("_______________")
dbconn.close()
