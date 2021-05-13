#!/bin/bash

hdfs dfs -get intro-to-hadoop/movielens/movies.csv movielens/


mapred streaming -input intro-to-hadoop/movielens/ratings.csv -output intro-to-hadoop/meanCal -file ./proj4/MeanMapper.py -mapper MeanMapper.py -file ./proj4/MeanReducer.py -reducer MeanReducer.py -file ./movielens/movies.csv


hdfs dfs -get intro-to-hadoop/meanCal .

