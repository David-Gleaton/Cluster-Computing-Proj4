 #!/bin/bash

mkdir movielens
hdfs dfs -get intro-to-hadoop/movielens/movies.csv movielens/

mapred streaming -input intro-to-hadoop/movielens/ratings.csv -output intro-to-hadoop/userCal -file ./proj4/UserMapper.py -mapper UserMapper.py -file ./proj4/UserReducer.py -reducer UserReducer.py -file ./movielens/movies.csv


hdfs dfs -get intro-to-hadoop/userCal .


