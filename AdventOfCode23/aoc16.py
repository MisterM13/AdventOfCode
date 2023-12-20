#!/usr/bin/env python3

f = open("input16.txt", "r")
input = f.read()

#input = ".|...\\....,|.-.\\.....,.....|-...,........|.,..........,.........\\,..../.\\\\..,.-.-/..|..,.|....-|.\\,..//.|...."

map = input.split(",")
imgMap = []
print(map)

def makeImgMap(map):
	imgMap = []
	for i in map:
		l =""
		for j in i:
			l+="."
		imgMap.append(l)
	return imgMap
		

def printMap(map,title):
	print("---- "+title+" ----")
	for m in map:
		print(m)

def goDir(pos, dir):
	#global map
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
	#global map
	x = pos[0]
	y = pos[1]
	print(x,y)
	imgMap[y] = imgMap[y][0:x]+"#"+imgMap[y][(x+1):len(imgMap[y])]
	print(map[0][0])
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
	else:
		print("Error: newPos", dir,x,y)
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
			
def goDirItInPlace(pos, dir,imgMap,map):
	x = pos[0]
	y = pos[1]
	#print(x,y)
	#print(map[0][0])
	#print(newPos)
	#printMap(map, str(dir))
	if 0 <= y < len(map):
		if 0 <= x < len(map[y]):
			imgMap[y] = imgMap[y][0:x]+"#"+imgMap[y][(x+1):len(imgMap[y])]
			p = map[y][x]
			#print(p)
			if p == "." or p =="*":
				#print("*")
				map[y] = map[y][0:x]+"*"+map[y][(x+1):len(map[y])]
				return[getNewPos(pos, dir),dir]
			elif p == "/":
				return[getNewPos(pos, connect(dir, 0, 1, 3, 2)), connect(dir, 0, 1, 3, 2)]
			elif p == "\\":
				return[getNewPos(pos, connect(dir, 0, 3, 1, 2)), connect(dir, 0, 3, 1, 2)]
			elif p =="|":
				return[getNewPos(pos, splitter(dir,1,3,0)), splitter(dir,1,3,0),getNewPos(pos,splitter(dir,1,3,2)) , splitter(dir,1,3,2)]
			elif p =="-":
				return[getNewPos(pos, splitter(dir,0,2,1)), splitter(dir,0,2,1),getNewPos(pos, splitter(dir,0,2,3)), splitter(dir,0,2,3)]
			
def getNewPos(pos,dir):
	x = pos[0]
	y = pos[1]
	#if map[y][x] == ".":
	#	map[y] = map[y][0:x]+"*"+map[y][(x+1):len(map[y])]
	if dir == 0: #Up
		newPos = [x,y-1]
	elif dir == 1: #right
		newPos = [x+1,y]
	elif dir == 2: #down
		newPos = [x,y+1]
	elif dir == 3: #left
		newPos = [x-1,y]
	else:
		print("Error: newPos", dir,x,y)
	return newPos
				
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

def getEnergy(imgMap):
	x = "".join(imgMap)
	c = 0
	for i in x:
		if i == "#":
			c+=1
	return c

print("---- lengths: ----")
for i in map:
	print(len(i))

def engage(startingPoint, map):
	imgMap = makeImgMap(map)
	printMap(map,"Original")
	running = True
	arr = [startingPoint]
	c = 0
	#maxlen = len("".join(imgMap))
	#maxlen = len(imgMap)
	#maxlen = 350
	#print("maxlen:",maxlen)
	history = []
	history.append(arr[0])
	while running:
		arr2 = []
		for i in arr:
			x = goDirItInPlace(i[0], i[1],imgMap,map)
			if x != None and len(x)>1:
				for j in range(1,len(x),2):
					inhist = False
					for h in history:
						#print([x[j-1],x[j]],h)
						if [x[j-1],x[j]] == h:
							inhist = True
					if not inhist:
						arr2.append([x[j-1],x[j]])
						history.append([x[j-1],x[j]])
						#print("arr:",arr,"arr2:",arr2)
		if c%10 == 0:
			#printMap(imgMap, str(c))
			printMap(map, str(c))
			print("                                                                              												number:",str(c),"StartingPoint:",startingPoint)
		if len(arr2)<1: #or c>maxlen:
			running = False
		else:
			arr = arr2
			c+=1
	
	
	printMap(map,"after traverse")
	printMap(imgMap,"imgMap")
	print(getEnergy(imgMap),"tiles energized")
	return getEnergy(imgMap)
	
start = [[0,0], 1]

startpoints = []
energypoints = []
for i in range(len(map)):
	startpoints.append([[0,i],1])
	startpoints.append([[len(map)-1,i],3])
for i in range(len(map[0])):
	startpoints.append([[i,0],2])
	startpoints.append([[i,len(map[0])-1],0])

for s in startpoints:
	map = input.split(",")
	energypoints.append(engage(s,map))

energypoints.sort(reverse=True)
print("largest number:",energypoints[0])