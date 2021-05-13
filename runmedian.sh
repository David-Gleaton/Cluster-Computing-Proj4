 #!/bin/bash
hdfs dfs -get intro-to-hadoop/movielens/movies.csv movielens/


mapred streaming -input intro-to-hadoop/movielens/ratings.csv -output intro-to-hadoop/medianCal -file ./proj4/MedianMapper.py -mapper MedianMapper.py -file ./proj4/MedianReducer.py -reducer MedianReducer.py -file ./movielens/movies.csv


hdfs dfs -get intro-to-hadoop/medianCal .


