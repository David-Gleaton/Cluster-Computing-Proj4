#!/software/spackages/linux-centos8-x86_64/gcc-8.3.1/anaconda3-2019.10-v5cuhr6keyz5ryxcwvv2jkzfj2gwrj4a/bin/python

import sys
import csv
import json

current_user = None
finallist = {
    "total_count": 0,
    "(no genres listed)": 0,
    "Action": 0,
    "Adventure": 0,
    "Animation": 0,
    "Children's": 0,
    "Comedy": 0,
    "Crime": 0,
    "Documentary": 0,
    "Drama": 0,
    "Fantasy": 0,
    "Film-Noir": 0,
    "Horror": 0,
    "Musical": 0,
    "Mystery": 0,
    "Romance": 0,
    "Sci-Fi": 0,
    "Thriller": 0,
    "War": 0,
    "Western": 0
}
ultimatelist = {
    "user": "",        
    "count":0,
    "genre": "",
    "genre_count": 0
}

for line in sys.stdin:
    line = line.strip()
    user, ratingString = line.split("\t", 1)
    ratingInfo = json.loads(ratingString)

    if current_user == user:
        try:
            for key in ratingInfo:
                finallist[key] += ratingInfo[key]

        except ValueError:
            continue  

    else:
        if current_user:
            if ultimatelist["count"] < finallist["total_count"]:
                ultimatelist["count"] = finallist["total_count"]
                ultimatelist["user"] = current_user
                temp = finallist["total_count"]
                finallist["total_count"] = -1
                genre = max(finallist, key=finallist.get)
                ultimatelist["genre"] = genre
                ultimatelist["genre_count"] = finallist[genre]
                finallist["total_count"] = temp
        current_user = user
        try:
             for key in ratingInfo:
                finallist[key] = ratingInfo[key]          
        except ValueError:
            continue
print("User Identification")
print ("%s-- Total Rating Counts: %s -- Most Rated Genre: %s - %s" % (ultimatelist["user"], ultimatelist["count"], ultimatelist["genre"], ultimatelist["genre_count"]))    
