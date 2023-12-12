#!/usr/bin/env python3

f = open("input11.txt", "r")
input = f.read()

input = "...#......\n.......#..\n#.........\n..........\n......#...\n.#........\n.........#\n..........\n.......#..\n#...#....."

map = input.split("\n")

def getGalaxies():
	coordinates = []
	for y in range(0,len(map)):
		for x in range(0,len(map[y])):
			if map[y][x] == "#":
				coordinates.append([x,y])
	return coordinates

def step(pos1,pos2,l):
	sv = 99 #stretch value x-1 -> 99 = 100 Times lager
	x1 = pos1[0]
	x2 = pos2[0]
	y1 = pos1[1]
	y2 = pos2[1]
	a = map[pos1[1]][pos1[0]]
	b = map[pos2[1]][pos2[0]]
	if((x1-x2)**2>(y1-y2)**2):
		if(x1>x2):
			x = x1-1
		else:
			x = x1+1
		y = y1
		c = map[y][x]
		#print("x-change",c)
		if(c == "|"):
			#print("passed streched space",l)
			l+=sv
			#print(l)
		
	else:
		if(y1>y2):
			y = y1-1
		else:
			y = y1+1
		x = x1
		c = map[y][x]
		#print("y-change",c)
		if(c == "-"):
			#print("passed streched space",l)
			l+=sv
			#print(l)
	l+=1
	if c =="+":
		#print("crossing")
		l+=sv
		#print("final l:",l,a,b)
	return [[x,y],l]

def getPathlen(pos1,pos2):
	arrived = False
	path =[]
	l = 0
	while not arrived:
		if (pos1 == pos2):
			arrived = True
		else:
			pos1,l = step(pos1, pos2,l)
			#print(pos1)
			path.append(map[pos1[1]][pos1[0]])
			#print(path)
	#for i in path:
	#	l+=1
	#	if i == "0":
	#		l+=1
	#l+=1
	return l

def strechSpace():
	global map
	lines = []
	cols = ["."]*len(map[0])
	for i in range(0,len(map)):
		#print(map[i],map[i].split("."),len(map[i].split(".")))
		if len(map[i].split(".")) == len(map[i])+1:
			#print(len(map[i].split(".")),len(map[i])+1)
			lines.append(i)
		for j in range(0,len(map[i])):
			if map[i][j] == "#":
				cols[j] = "#"
				#print(lines,cols)
	for i in range(0,len(map)):
		for l in lines:
			if i==l:
				for j in map[i]:
					map[i] = map[i].replace(".","-")
					#line = map[i].split(".")
		line = list(map[i])
		#print(line)
		for j in range(0,len(line)):
			if cols[j] == ".":
				if line[j] == ".":
					line[j] = "|"
				elif line[j] == "-":
					line[j] = "+"
				else:
					print("Error in stretchspace: expected . or - but found:",line[j])
				#print("line",line)
		map[i] = "".join(line)
				
def printmap():
	for i in map:
		print(i)
	print("\n")

printmap()
print("========= after streching: ============\n")
strechSpace()
galaxies = getGalaxies()
#print(galaxies)
printmap()

sum = 0
c = 0
for i in range(0,len(galaxies)):
	for j in range(i+1,len(galaxies)):
		l = getPathlen(galaxies[i], galaxies[j])
		print(i+1,j+1,l)
		sum += l
		c+=1
print("Pairs:",c)
print("Sum:",sum)
	
#print(getPathlen(galaxies[0], galaxies[6]))
#print(getPathlen(galaxies[2], galaxies[5]))
#print(getPathlen(galaxies[7], galaxies[8]))
#print(getPathlen(galaxies[4], galaxies[8]))
