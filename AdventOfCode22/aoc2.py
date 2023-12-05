#!/usr/bin/env python3

f = open("input2.txt", "r")
input = f.read()
#input = "A Y\nB X\nC Z"
input = input.replace("A", "R")
input = input.replace("B", "P")
input = input.replace("C", "S")
#input = input.replace("X", "R")
#input = input.replace("Y", "P")
#input = input.replace("Z", "S")
score = 0
rps = [1,2,3]
print("you","me","res")
def getScore(match):
	global score
	me = getVal(match[2:3])
	you = getVal(match[0:1])
	score += me
	if(me == you):
		score+=3
		print(match,"draw")
	elif(rps[me-2]==you):
		score+=6
		print(match,"won")
	else:
		print(match,"lost")
	
def getVal(choice):
	value = -1
	if (choice == "R"):
		return 1
	elif(choice == "P"):
		return 2
	elif(choice == "S"):
		return 3
	elif(choice == "X"):
		return 0
	elif(choice == "Y"):
		return 3
	elif(choice == "Z"):
		return 6

def getScore2(match):
	global score
	me = getVal(match[2:3])
	you = getVal(match[0:1])
	score+=me
	if(me==3):
		score+=you
		print("draw",score)
	elif(me==0):
		score+=rps[you-2]
		print("lost",score)
	else:
		score+=rps[you-3]
		print("won",score)

for i in inArr:
	getScore2(i)
print(score)