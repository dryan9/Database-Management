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
print("")
print('########################')
print('Great Movie Viewer Bot 9000')
print("##############################")
genreChoice = input('what genre are you interested in:')
print("")

genreQuery = 'SELECT m.title, Count(m.title) \
FROM `movies` m  \
INNER JOIN `ratings` r \
  ON m.movie_id = r.movie_id \
INNER JOIN `movie_genres` mg \
	 ON r.movie_id = mg.movie_id \
INNER JOIN 	`genres` g \
	ON mg.genre_id = g.genre_id \
where r.rating = 5 AND g.genre = %s \
Group by 1 \
ORDER by 2 DESC \
Limit 10'


cursor.execute(genreQuery, (genreChoice))
counter = 1
result = cursor.fetchall()
print("Top 10 highest ranked comedy movies:")
for i in result:
    print(counter,". ", i[0]," (",i[1], " '5' rating)", sep = '')
    counter +=1
print("")
print('Thank you for playing with Movie Viewer Bot 9000')
dbconn.close()
