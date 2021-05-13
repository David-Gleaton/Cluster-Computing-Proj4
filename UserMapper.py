#!/software/spackages/linux-centos8-x86_64/gcc-8.3.1/anaconda3-2019.10-v5cuhr6keyz5ryxcwvv2jkzfj2gwrj4a/bin/python

import sys
import csv
import json

movieFile = "./movies.csv"

movieList = {}
userList = {}
#Average/Mean calculation given in codes

with open(movieFile, mode = 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        movieList[row[0]] = {}
        movieList[row[0]]["title"] = row[1]
        movieList[row[0]]["genre"] = row[2]

for oneMovie in sys.stdin:
    oneMovie = oneMovie.strip()
    ratingInfo = oneMovie.split(",")
    try:
        genres = movieList[ratingInfo[1]]["genre"]
        rating = float(ratingInfo[2])
        user = str(ratingInfo[0])

        for genre in genres.split("|"):
            if user in userList:
                if genre in userList[user]:
                    userList[user][genre] += 1
                else:
                    userList[user][genre] = 1
                userList[user]["total_count"] += 1
            else:
                userList[user] = {}
                userList[user]["total_count"] = 1
                userList[user][genre] = 1


    except ValueError:
        continue
        
for user in userList:
    print ("%s\t%s" % (user, json.dumps(userList[user])))
