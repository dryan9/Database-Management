

import pymysql
import configparser

config = configparser.ConfigParser()
config.read_file(open('credentials.py'))
dbhost = config['csc']['dbhost']
dbuser = config['csc']['dbuser']
dbpw = config['csc']['dbpw']

dbschema = 'movielens'

dbconn = pymysql.connect(host=dbhost,
                         user=dbuser,
                         passwd=dbpw,
                         db=dbschema,
                         use_unicode=True,
                         charset='utf8mb4',
                         autocommit=True)
cursor = dbconn.cursor()

selectGenre = "SELECT g.genre, COUNT(mg.genre_id) \
FROM `genres` g \
LEFT OUTER JOIN `movie_genres` mg \
ON mg.genre_id = g.genre_id \
GROUP By 1"


cursor.execute(selectGenre)

result = cursor.fetchall()

for row in result:
    print("Genre", row[0], "Count", row[1])

dbconn.close()
