#!/bin/bash
mapred streaming -input intro-to-hadoop/movielens/ratings.csv -output intro-to-hadoop/StatisticCal -file ./proj4/StatisticMapper.py -mapper StatisticMapper.py -file ./proj4/StatisticReducer.py -reducer StatisticReducer.py -file ./movielens/movies.csv


hdfs dfs -get intro-to-hadoop/StatisticCal .

