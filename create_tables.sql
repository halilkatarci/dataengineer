
/* CREATE TABLE */
CREATE TABLE title_ratings(
tconst VARCHAR(1000),
averageRating DOUBLE,
numVotes DOUBLE
);

/* CREATE TABLE */
CREATE TABLE name_basics(
nconst VARCHAR(1000),
primaryName VARCHAR(1000),
birthYear DOUBLE,
deathYear DOUBLE,
primaryProfession VARCHAR(1000),
knownForTitles VARCHAR(1000)
);

/* CREATE TABLE */
CREATE TABLE title_akas(
titleId VARCHAR(1000),
ordering DOUBLE,
title VARCHAR(1000),
region VARCHAR(1000),
language VARCHAR(1000),
types VARCHAR(1000),
attributes VARCHAR(1000),
isOriginalTitle DOUBLE
);

/* CREATE TABLE */
CREATE TABLE title_basics(
tconst VARCHAR(1000),
titleType VARCHAR(1000),
primaryTitle VARCHAR(1000),
originalTitle VARCHAR(1000),
isAdult DOUBLE,
startYear DOUBLE,
endYear VARCHAR(1000),
runtimeMinutes DOUBLE,
genres VARCHAR(1000)
);

/* CREATE TABLE */
CREATE TABLE title_crew(
tconst VARCHAR(1000),
directors VARCHAR(5000),
writers MEDIUMTEXT
);

/* CREATE TABLE */
CREATE TABLE title_episode(
tconst VARCHAR(1000),
parentTconst VARCHAR(1000),
seasonNumber DOUBLE,
episodeNumber DOUBLE
);

/* CREATE TABLE */
CREATE TABLE title_principals(
tconst VARCHAR(1000),
ordering DOUBLE,
nconst VARCHAR(1000),
category VARCHAR(1000),
job VARCHAR(1000),
characters VARCHAR(1000)
);
