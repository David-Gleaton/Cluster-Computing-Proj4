 #!/bin/bash
hdfs dfs -get intro-to-hadoop/movielens/movies.csv movielens/


mapred streaming -input intro-to-hadoop/movielens/ratings.csv -output intro-to-hadoop/stdCal -file ./proj4/StdMapper.py -mapper StdMapper.py -file ./proj4/StdReducer.py -reducer StdReducer.py -file ./movielens/movies.csv


hdfs dfs -get intro-to-hadoop/stdCal .


