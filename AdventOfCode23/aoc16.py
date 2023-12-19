#!/usr/bin/env python3

f = open("input16.txt", "r")
input = f.read()

input = ".|...\\....,|.-.\\.....,.....|-...,........|.,..........,.........\\,..../.\\\\..,.-.-/..|..,.|....-|.\\,..//.|...."

map = input.split(",")
imgMap = []
print(map)

def makeImgMap():
	global imgMap
	for i in map:
		l =""
		for j in i:
			l+="."
		imgMap.append(l)
		

def printMap(map,title):
	print("---- "+title+" ----")
	for m in map:
		print(m)

def goDir(pos, dir):
	global map
	x = pos[0]
	y = pos[1]
	imgMap[y] = imgMap[y][0:x]+"#"+imgMap[y][(x+1):len(imgMap[y])]
	if map[y][x] == ".":
		map[y] = map[y][0:x]+"*"+map[y][(x+1):len(map[y])]
	if dir == 0: #Up
		newPos = [x,y-1]
	elif dir == 1: #right
		newPos = [x+1,y]
	elif dir == 2: #down
		newPos = [x,y+1]
	elif dir == 3: #left
		newPos = [x-1,y]
	#print(newPos)
	printMap(map, str(dir))
	if 0 <= newPos[1] < len(map):
		if 0 <= newPos[0] < len(map[newPos[1]]):
			p = map[newPos[1]][newPos[0]]
			#print(p)
			if p == ".":
				#print("*")
				map[newPos[1]] = map[newPos[1]][0:newPos[0]]+"*"+map[newPos[1]][(newPos[0]+1):len(map[newPos[1]])]
				goDir(newPos, dir)
			elif p == "/":
				goDir(newPos, connect(dir, 0, 1, 3, 2))
			elif p == "\\":
				goDir(newPos, connect(dir, 0, 3, 1, 2))
			elif p =="|":
				goDir(newPos, splitter(dir,1,3,0))
				goDir(newPos, splitter(dir,1,3,2))
			elif p =="-":
				goDir(newPos, splitter(dir,0,2,1))
				goDir(newPos, splitter(dir,0,2,3))
	
def goDirIt(pos, dir):
	global map
	x = pos[0]
	y = pos[1]
	imgMap[y] = imgMap[y][0:x]+"#"+imgMap[y][(x+1):len(imgMap[y])]
	if map[y][x] == ".":
		map[y] = map[y][0:x]+"*"+map[y][(x+1):len(map[y])]
	if dir == 0: #Up
		newPos = [x,y-1]
	elif dir == 1: #right
		newPos = [x+1,y]
	elif dir == 2: #down
		newPos = [x,y+1]
	elif dir == 3: #left
		newPos = [x-1,y]
	#print(newPos)
	#printMap(map, str(dir))
	if 0 <= newPos[1] < len(map):
		if 0 <= newPos[0] < len(map[newPos[1]]):
			p = map[newPos[1]][newPos[0]]
			#print(p)
			if p == "." or p =="*":
				#print("*")
				map[newPos[1]] = map[newPos[1]][0:newPos[0]]+"*"+map[newPos[1]][(newPos[0]+1):len(map[newPos[1]])]
				return[newPos,dir]
			elif p == "/":
				return[newPos, connect(dir, 0, 1, 3, 2)]
			elif p == "\\":
				return[newPos, connect(dir, 0, 3, 1, 2)]
			elif p =="|":
				return[newPos, splitter(dir,1,3,0),newPos, splitter(dir,1,3,2)]
			elif p =="-":
				return[newPos, splitter(dir,0,2,1),newPos, splitter(dir,0,2,3)]
	
				
def connect(x,a,b,c,d):
	arr1 = [a,b]
	arr2 = [c,d]
	y = -1
	for i in range(2):
		if x == arr1[i]:
			y = arr1[i-1]
		elif x == arr2[i]:
			y = arr2[i-1]
	return y

def splitter(x,a,b,c):
	if x == a or x == b:
		return c
	else:
		return x

def getEnergy():
	x = "".join(imgMap)
	c = 0
	for i in x:
		if i == "#":
			c+=1
	return c

makeImgMap()
printMap(map,"Original")
running = True
arr = [[0,0], 1]
c = 0
maxlen = len("".join(imgMap))
#maxlen = len(imgMap)
#maxlen = 350
#print("maxlen:",maxlen)
history = [[0,0], 1]
while running:
	arr2 = []
	for i in range(1,len(arr),2):
		x = goDirIt(arr[i-1], arr[i])
		if x != None and len(x)>1:
			for j in x:
				arr2.append(j)
	#print("arr:",arr,"arr2:",arr2)
	if c%10 == 0:
		printMap(imgMap, str(c)+"/"+str(maxlen))
	if len(arr2)<1 or c>maxlen:
		running = False
	else:
		arr = arr2
		c+=1
	

printMap(map,"after traverse")
printMap(imgMap,"imgMap")
print(getEnergy(),"tiles energized")