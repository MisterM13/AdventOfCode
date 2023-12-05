#!/usr/bin/env python3

f = open("input1a.txt", "r")
input = f.read()
inArr = input.split("\n")
print(inArr)
x = 0
#maxC = 0
maxC = [0,0,0]
for i in inArr:
	if(i==''):
		if(x > maxC[0]):
			maxC[1] = maxC[0]
			maxC[0] = x
		elif(x > maxC[1]):
			maxC[2] = maxC[1]
			maxC[1] = x
		elif(x > maxC[2]):
			maxC[2] = x
		x = 0
	else:
		x+=int(i)
		#print(maxC)

maxTot = maxC[0]+maxC[1]+maxC[2]
print(maxTot)