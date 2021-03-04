import mysql.connector
import gzip
import glob
import numpy as np
from tqdm import tqdm
import os

mydb = mysql.connector.connect(
  host=os.environ['HOST'],
  user=os.environ['USER'],
  password=os.environ['PASSWORD'],
  database=os.environ['DATABASE']
)

mycursor = mydb.cursor()
tsvs = glob.glob('imdb_dataset/*.tsv.gz')

batch_size = 1000000

def extract_tsv(tsv):
	f = gzip.open(tsv, 'rb')
	lines = f.readlines()
	f.close()
	return lines

def get_sql_command(name):
	if name == 'title.ratings.tsv.gz':
		sql = "INSERT INTO title_ratings (tconst, averageRating, numVotes) VALUES (%s, %s, %s)"
		column_len = 3
	elif name == 'name.basics.tsv.gz':
		sql = "INSERT INTO name_basics(nconst, primaryName, birthYear, deathYear, primaryProfession, knownForTitles) \
				VALUES ( %s, %s, %s, %s, %s, %s );"
		column_len = 6
	elif name == 'title.akas.tsv.gz':
		sql = "INSERT INTO title_akas(titleId, ordering, title, region, language, types, attributes, isOriginalTitle) \
				VALUES ( %s, %s, %s, %s, %s, %s, %s, %s);"
		column_len = 8
	elif name == 'title.basics.tsv.gz':
		sql = "INSERT INTO title_basics(tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres) \
				VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s);"
		column_len = 9
	elif name == 'title.crew.tsv.gz':
		sql = "INSERT INTO title_crew(tconst, directors, writers) \
				VALUES ( %s, %s, %s);"
		column_len = 3
	elif name == 'title.episode.tsv.gz':
		sql = "INSERT INTO title_episode(tconst, parentTconst, seasonNumber, episodeNumber) \
				VALUES ( %s, %s, %s, %s);"
		column_len = 4
	elif name == 'title.principals.tsv.gz':
		sql = "INSERT INTO title_principals(tconst, ordering, nconst, category, job, characters) \
				VALUES ( %s, %s, %s, %s, %s, %s);"
		column_len = 6
	return sql, column_len

def main():

	for tsv in tqdm(tsvs):
		name = tsv.split('/')[-1]
		lines = extract_tsv(tsv)
		sql, column_len = get_sql_command(name)
		lines_need = lines[1:]
		splitted_line = int(np.ceil(len(lines_need)/batch_size))
		for i in range(splitted_line):
			values = []
			for line in lines_need[i*batch_size:(i+1)*batch_size]:
				line = line.decode('utf-8')
				parts = line.strip().split('\t')
				parts = [None if i=='\\N' else i for i in parts]
				values.append(tuple([parts[i] for i in range(column_len)]))
			mycursor.executemany(sql, values)

	mydb.commit()

if __name__ == '__main__':
	main()