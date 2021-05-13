#!/software/spackages/linux-centos8-x86_64/gcc-8.3.1/anaconda3-2019.10-v5cuhr6keyz5ryxcwvv2jkzfj2gwrj4a/bin/python

import sys
import csv
import json
import math

current_genre = None
current_rating_sum = 0
current_rating_count = 0
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
StdFinal = {}
MeanFinal = {}
MedianFinal = {}

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
            current_rating_sum += ratingInfo["Sum"]
        except ValueError:
            continue  

    else:
        if current_genre:
            #Get the Mean
            Mean = float(current_rating_sum/current_rating_count)
            #Subtract the mean from each entry.
            arrayofsub = []
            i = 0.0
            while(i < 5.5):
                #Here we subtract the mean, square, and multiply by the freq of ratings
                #Explained with parathesis (Multiply by freq of ratings(Square(Subtract the mean)))
                arrayofsub.append(((float(i - Mean)) ** 2 )*totalratings[str(i)])
                i += 0.5
            sumofsquarediff = 0
            for i in range(0, len(arrayofsub)):
                sumofsquarediff += arrayofsub[i]
            variance = float(sumofsquarediff/current_rating_count)
            Std = variance ** (1/2)
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

            #Sum the Squared differences, we get the # of entries by totalratings
            StdFinal[current_genre] = Std
            MeanFinal[current_genre] = Mean
            MedianFinal[current_genre] = Median
#            print ("%s\t%s" % (current_genre, Std))    
        current_genre = genre
        try:
            current_rating_sum = ratingInfo["Sum"]
            current_rating_count = ratingInfo["total_count"]
        except ValueError:
            continue

print("Output for Mean")
for item in MeanFinal:
    print("%s\t%s" % (item, MeanFinal[item]))
print("Output for Median")
for item in MedianFinal:
    print("%s\t%s" % (item, MedianFinal[item]))
print("Output for Std")
for item in StdFinal:
    print("%s\t%s" % (item, StdFinal[item]))
