import pymysql
import configparser
import json 

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

query = "SELECT rowId, musicinfo \
FROM `theGrowlers`"

cursor.execute(query)

insertQuery = "update theGrowlers \
set trackId = %s, \
 trackName = %s, \
 collectionName = %s, \
 artistName = %s, \
 trackPrice = %s, \
 previewUrl = %s, \
 trackTimeMillis = %s \
where rowId = %s"

rows = cursor.fetchall()

for row in rows:
    rowId = row[0]
    musicinfo = row[1]
    jsondata = json.loads(musicinfo)
    trackId = jsondata['trackId']
    collectionName = jsondata['collectionName']
    artistName = jsondata['artistName']
    trackPrice = jsondata['trackPrice']
    previewUrl = jsondata['previewUrl']
    trackTimeMillis = jsondata['trackTimeMillis']
    trackName = jsondata['trackName']
    cursor.execute(insertQuery,(trackId,trackName, collectionName,artistName, trackPrice, previewUrl, trackTimeMillis, rowId))

print("----")
dbconn.close()
