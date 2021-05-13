#!/software/spackages/linux-centos8-x86_64/gcc-8.3.1/anaconda3-2019.10-v5cuhr6keyz5ryxcwvv2jkzfj2gwrj4a/bin/python

import sys
import csv
import json

current_genre = None
current_rating_sum = 0
current_rating_count = 0
HeaderForMe = 0
totalratings = {
    "0.0":0,
    "0.5":0,
    "1.0":0,
    "1.5":0,
    "2.0":0,
    "2.5":0,
    "3.0":0,
    "3.5":0,
    "4.0":0,
    "4.5":0,
    "5.0":0
}
Median = 0


for line in sys.stdin:
    line = line.strip()
    genre, ratingString = line.split("\t", 1)
    ratingInfo = json.loads(ratingString)

    if current_genre == genre:
        try:
            i = 0.0
            while(i < 5.5):
                totalratings[str(i)] += ratingInfo[str(i)]
                i += 0.5
            current_rating_count += ratingInfo["total_count"]
        except ValueError:
            continue  

    else:
        if(HeaderForMe == 0):
            print("Genre Means")
            HeaderForMe += 1
        if current_genre:
#            print("%s" % (current_genre))
            #Calculating Median
            position = round(current_rating_count/2)
#            print("%s" % (position))
            #Subtracting out each rating total from position until a negative number is found
            subposition = position
            i = 0.0
            while(subposition > 0):
                subposition -= totalratings[str(i)]
                #In the unlikely occurance where subposition - a section is 0, then that last section is the median
                if(subposition == 0):
                    break
#                print("%s\t%s" % (subposition, i))
                i += 0.5
            #Odd Median here
            if(current_rating_count % 2 != 0):
                Median = i
            #Even Median here
            else:
                Median = float((i + (i+0.5))/2)
            print ("%s\t%s" % (current_genre, Median))    
        current_genre = genre
        try:
#            current_rating_sum = ratingInfo["total_rating"]
            current_rating_count = ratingInfo["total_count"]
        except ValueError:
            continue
