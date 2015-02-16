import random
import time
import sys

rankLine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
rankList = []

random.shuffle(rankLine)
#print rankLine
random.shuffle(rankLine)
#print rankLine

def randomize():
	for x in range(0, 20):
		newRank = rankLine[:]
		random.shuffle(newRank)
		rankList.append(newRank)

def create():
    print('Creating new text file') 

    name = 'list.txt'  # Name of text file coerced with +.txt

    try:
        file = open(name,'wb')   # Trying to create a new file or open one
        for x in range(0, 20):
			file.write('<'.join(map(str, rankList[x]))+"\n")

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python

randomize()
create()

	
