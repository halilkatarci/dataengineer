# Answers

## a
`select seasonNumber, episodeNumber, averageRating from title_episode, title_ratings
where title_episode.tconst = title_ratings.tconst and title_episode.parentTconst = "tt0903747"
order by averageRating desc limit 0, 5;`

| seasonNumber | episodeNumber | averageRating |
|--------------|---------------|---------------
|            5 |            14 |            10 |
|            5 |            16 |           9.9 |
|            4 |            13 |           9.9 |
|            5 |            13 |           9.8 |
|            5 |             5 |           9.7 |


## b
`select seasonNumber, episodeNumber, averageRating from title_episode, title_ratings where title_episode.tconst = title_ratings.tconst and title_episode.parentTconst = "tt0903747" order by averageRating limit 0, 5;`

| seasonNumber | episodeNumber | averageRating |
|--------------|---------------|---------------|
|            3 |            10 |           7.8 |
|            4 |             3 |           8.1 |
|            1 |             4 |           8.3 |
|            3 |             4 |           8.3 |
|            2 |             4 |           8.3 |

## c
`select seasonNumber, episodeNumber, numVotes from title_episode, title_ratings where title_episode.tconst = title_ratings.tconst and title_episode.parentTconst = "tt0903747" order by numVotes DESC limit 0, 5;`

| seasonNumber | episodeNumber | numVotes |
|--------------|---------------|----------|
|            5 |            14 |   132802 |
|            5 |            16 |    90804 |
|            4 |            13 |    45404 |
|            5 |            15 |    34297 |
|            5 |            13 |    34076 |

## d
`select seasonNumber, episodeNumber, numVotes from title_episode, title_ratings where title_episode.tconst = title_ratings.tconst and title_episode.parentTconst = "tt0903747" order by numVotes limit 0, 5;`
| seasonNumber | episodeNumber | numVotes |
|--------------|---------------|----------|
|            5 |            14 |   132802 |
|            5 |            16 |    90804 |
|            4 |            13 |    45404 |
|            5 |            15 |    34297 |
|            5 |            13 |    34076 |
