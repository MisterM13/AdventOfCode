#!/usr/bin/env python3

import numpy as np
f = open("input14.txt", "r")
input = f.read()
input = "498,4 -> 498,6 -> 496,6\n503,4 -> 502,4 -> 502,9 -> 494,9"
ymax = 164
xmax = 1000
numField = np.zeros((xmax,ymax))
numField[500][0] = 1
input = input.split("\n")

def printField():
	strField = ""
	[xlen,ylen] = numField.shape
	for i in range(0,ymax):
		strField+="\n"
		for j in range(400,600):
			if(numField[j][i] == 1):
				strField+="+"
			elif(numField[j][i] == 2):
				strField+="#"
			elif(numField[j][i] == 3):
				strField+="o"
			elif(numField[j][i] == 4):
				strField+="x"
			else:
				strField+="."
	print(strField)
	
def createStoneLine(p1,p2):
	# p = [x,y]
	global numField
	if(p1[0] == p2[0]):
		if(p2[1]>p1[1]):
			numField[p1[0]][p1[1]:p2[1]] = 2
		else:
			numField[p1[0]][p2[1]:p1[1]] = 2
	else:
		if(p2[0]>p1[0]):
			for x in range(p1[0],p2[0]+1):
				numField[x][p1[1]] = 2
		else:
			for x in range(p2[0],p1[0]+1):
				numField[x][p2[1]] = 2

				#createStoneLine([453,1],[453,9])
				#createStoneLine([453,9],[455,9])	
def isGrounded():
	global numField
	grounded = False
	for i in range(0,xmax):
		if(numField[i][ymax-2] > 1):
			grounded = True
	return grounded

def simSand(x,y):
	global numField
	if(numField[x][y+1] > 1):
		if(numField[x-1][y+1]>1):
			if(numField[x+1][y+1]>1):
				numField[x][y] = 3
			else:
				simSand(x+1, y+1)
		else:
			simSand(x-1, y+1)
	else:
		simSand(x, y+1)

def createKillVolume():
	global numField
	for i in range(0,1000):
		numField[i][ymax-1] = 4

def countSandcorns():
	c = 0#-1
	for i in range(0,xmax):
		for j in range(0,ymax):
			if(numField[i][j]==3):
				c+=1
	return c

for i in input:
	co = i.split(" -> ")
	for j in range(1,len(co)):
		p1 = co[j-1].split(",")
		p2 = co[j].split(",")
		p1[0],p1[1],p2[0],p2[1] = int(p1[0]),int(p1[1]),int(p2[0]),int(p2[1])
		createStoneLine(p1, p2)

		#printField()
createKillVolume()


#while(not isGrounded()):
#	printField()
#	simSand(500, 0)
#print(countSandcorns())
	
while(numField[500][0] == 1):
	printField()
	simSand(500, 0)
print(countSandcorns())