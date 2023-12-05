#!/usr/bin/env python3
import numpy as np
f = open("input8.txt", "r")
input = f.read()
input = "30373\n25512\n65332\n33549\n35390"
input = input.split("\n")

#field = []
lenx = len(input[0])
leny = len(input)
totvis = 0

field = np.zeros((lenx,leny))
sfield = np.zeros((lenx,leny))


for i in range(0,lenx):
	for j in range(0,leny):
		field[i][j] = int(input[i][j])
		
for i in range(0,lenx):
		print(field[i])
		
	#print("fieldx",field[3:4][0])

def getCollumn(y):
	r = []
	for i in range(0,lenx):
		r.append(field[i][y])
	return r

def getCollReverse(y):
	r = []
	for i in range(lenx-1,-1,-1):
		r.append(field[i][y])
	return r

def isVisUp(x,y):
	vis = True
	c = getCollumn(y)
	#print(c)
	for i in range(0,x):
		#print("--",i,x,c[i],field[x][y],c[i]>=field[x][y])
		if(c[i]>=field[x][y]):
			vis = False
			#print(vis)
	return vis

def isVisLt(x,y):
	vis = True
	c = field[x]
	#print(c)
	for i in range(0,y):
		#print("--",i,x,c[i],field[x][y],c[i]>=field[x][y])
		if(c[i]>=field[x][y]):
			vis = False
			#print(vis)
	return vis


def isVisDn(x,y):
	vis = True
	c = getCollumn(y)
	#c = getCollReverse(y)
	#print(c)
	for i in range(x+1,lenx):
		#print("--",i,y,c[i],field[x][y],c[i]>=field[x][y])
		if(c[i]>=field[x][y]):
			vis = False
			#print(vis)
	return vis

def isVisRt(x,y):
	vis = True
	c = field[x]
	#print(c)
	for i in range(y+1,leny):
		#print("--",i,x,c[i],field[x][y],c[i]>=field[x][y])
		if(c[i]>=field[x][y]):
			vis = False
			#print(vis)
	return vis

def lookUp(x,y):
	vis = True
	dist = 1
	c = getCollumn(y)
	#print(c)
	for i in range(0,x):
		#print("--",i,x,c[i],field[x][y],c[i]>=field[x][y])
		if(c[i]>=field[x][y] or not vis):
			vis = False
		else:
			dist+=1
			#print(vis)
	if(vis):
		dist-=1
	return dist

def lookLt(x,y):
	vis = True
	dist = 1
	c = field[x]
	#print(c)
	for i in range(0,y):
		#print("--",i,x,c[i],field[x][y],c[i]>=field[x][y])
		if(c[i]>=field[x][y] or not vis):
			vis = False
		else:
			dist+=1
			#print(vis)
	if(vis):
		dist-=1
	return dist


def lookDn(x,y):
	dist = 1
	vis = True
	c = getCollumn(y)
	#c = getCollReverse(y)
	#print(c)
	for i in range(x+1,lenx):
		#print("--",i,y,c[i],field[x][y],c[i]>=field[x][y])
		if(c[i]>=field[x][y] or not vis):
			vis = False
		else:
			dist+=1
			#print(vis)
	if(vis):
		dist-=1
	return dist

def lookRt(x,y):
	dist = 1
	vis = True
	c = field[x]
	#print(c)
	for i in range(y+1,leny):
		#print("--",i,x,c[i],field[x][y],c[i]>=field[x][y])
		if(c[i]>=field[x][y] or not vis):
			vis = False
		else:
			dist+=1
	if(vis):
		dist-=1
			#print(vis)
	return dist

#print(getCollumn(3))

#arr = ""	
#for i in range(0,lenx):
#	arr+="\n"
#	for j in range(0,leny):
#		#print(i,j)
#		if(isVisUp(i,j)):
#			arr+="U   "
#			totvis+=1
#		elif(isVisDn(i,j)):
#			arr+="D   "
#			totvis+=1
#		elif(isVisLt(i,j)):
#			arr+="L   "
#			totvis+=1
#		elif(isVisRt(i,j)):
#			arr+="R   "
#			totvis+=1
#		else:
#			arr+=str(field[i][j])+" "
			
arr = ""	
for i in range(0,lenx):
	for j in range(0,leny):
		print(i,j,"|",lookUp(i, j),lookDn(i, j),lookLt(i, j),lookRt(i, j),lookUp(i, j) * lookDn(i, j) *lookLt(i, j) *lookRt(i, j))
		sfield[i][j] = lookUp(i, j) * lookDn(i, j) *lookLt(i, j) *lookRt(i, j)
			
#print(arr)
print(sfield)
#print(totvis)