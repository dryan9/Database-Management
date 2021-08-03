import csv
import pymysql
import configparser
import random


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


filename = 'transactions.csv'
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

query = 'INSERT into aa_people(firstName, lastName, userName, email) \
    values(%s, %s,%s, %s)'
    
query2 = 'INSERT into aa_transaction(txn_id, amount, date) \
    values(%s, %s,%s)'
    
query3 = 'INSERT into aa_t_payee(txn_id) values(%s)'
    
query4= 'INSERT into aa_t_payer(txn_int) \
    values(%s)'
    
update = 'UPDATE `aa_t_payee` SET payeeId = %s where txn_id = %s'

update2 = 'UPDATE `aa_t_payer` SET payerID = %s where txn_int = %s'

    
for item in myRows:
    first = item[0]
    last = item[1]
    userName = item[2]
    email = item[3]
    txn_id = item[8]
    amount = item[9]
    date = item[10]
    six = item[6]
    #cursor.execute(query,(first,last,userName, email))
    #cursor.execute(query2,(txn_id,amount,date))
    #cursor.execute(query3,(txn_id))
    #cursor.execute(query4,(txn_id))
    cursor.execute(update,(item[6],txn_id))
    cursor.execute(update2,(item[2],txn_id))
print('done')