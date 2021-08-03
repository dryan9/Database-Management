import pymysql
import configparser

config = configparser.ConfigParser()
config.read_file(open('credentials.py'))
dbhost = config['csc']['dbhost']
dbuser = config['csc']['dbuser']
dbpw = config['csc']['dbpw']

dbschema = 'world'

dbconn = pymysql.connect(host=dbhost,
                         user=dbuser,
                         passwd=dbpw,
                         db=dbschema,
                         use_unicode=True,
                         charset='utf8mb4',
                         autocommit=True)
cursor = dbconn.cursor()

genreChoice = input('enter a movie genre:')

genreQuery = 'SELECT count(m.movie_id) \
                FROM movies m \
                INNER JOIN movie_genres mg ON m.movie_id = mg.movie_id \
                INNER JOIN genres g ON mg.genre_id = g.genre_id \
                WHERE g.genre = %s'
cursor.execute(genreQuery, (genreChoice))

result = cursor.fetchone()[0]
print('The number of movies in the', genreChoice, 'category is', result[0])

dbconn.close()
