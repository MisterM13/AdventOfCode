#!/usr/bin/env python3
import numpy as np
f = open("input6.txt", "r")
input = f.read()

#input = "....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."

rows = input.split("\n")
for i in rows:
	if i == "":
		rows.remove(i)
guard=["^",">","v","<"]

#Mapping thoughts
# Obstacles = 0
# Free Fields = 1
# Position cursors ^ = 2, > = 3, v = 4, < = 5
# Route X = 6

def mapToNumbers(rows):
	x = len(rows)
	y = len(rows[0])
	intmap = np.ones((x,y))
	for xi in range(x):
		r = rows[xi]
		for yi in range(y):
			co = r[yi]
			if co == "#":
				intmap[xi,yi]=0 # obstacles get mapped to 0
	return intmap

def NumbersToMap(intmap,pos=0):
	if not pos == 0:
		(x,y,d) = pos
		intmap[x,y] = int(d+2)
	[x,y] = intmap.shape
	map = ""
	for xi in range(x):
		row = ""
		for yi in range(y):
			if intmap[xi,yi] == 0:
				row+= "#"
			elif intmap[xi,yi]== 1:
				row+= "."
			elif intmap[xi,yi]== 2:
				row+= "^"
			elif intmap[xi,yi]== 3:
				row+= ">"
			elif intmap[xi,yi]== 4:
				row+= "v"
			elif intmap[xi,yi]== 5:
				row+= "<"
			elif intmap[xi,yi]== 6:
				row+= "X"
		map+=row
		map += "\n"
	return map

def getInitPos(rows):
	x = len(rows)
	y = len(rows[0])
	for xi in range(x):
		r = rows[xi]
		for yi in range(y):
			co = r[yi]
			for g in range(len(guard)):
				if co == guard[g]:
					return(xi,yi,g)
	return (0,0,0)


# 2 -> x-1 -2:  0 -> x-1
# 3 -> y+1		1 -> y+1
# 4 -> x+1		2 -> x+1
# 5 -> y-1		3 -> y-1
def move(intmap,pos):
	(x,y,i) = pos  # i+2 = guard[0]
	intmap[x,y] = 6 # setting an X
	[xmax,ymax] = intmap.shape
	newmap = []
	xi = 0
	yi = 0
	if i == 0:
		xi = -1
	elif i== 1:
		yi = 1
	elif i== 2:
		xi = 1
	elif i== 3:
		yi =-1
	if x+xi < xmax and y+yi < ymax and x+xi >=0 and y+yi >=0 :
		if intmap[x+xi,y+yi] < 1:
			pos = (x,y,(i+1)%4)
			return (intmap, pos)
		else:
			pos = (x+xi,y+yi,i)
			return (intmap, pos)
	return (intmap,(-1,-1,-1))

def isin(el,array):
	for i in array:
		if i==el:
			return True
	return False

def runMap(intmap,pos,printout = False):
	coordold = (0,0)
	dirchanges = []
	#dirchanges = np.array(dirchanges)
	ccount = 0
	cycle = False
	while not pos == (-1,-1,-1) and not cycle:
		(intmap,pos) = move(intmap, pos)
		if printout:
			print(NumbersToMap(intmap, pos),"pos:",pos,"ccount:",ccount)
		(x,y,d) = pos
		coord = (x,y)
		if coord == coordold: 
			if not isin(coord,dirchanges):
				dirchanges.append(coord)
			else:
				ccount+=1
		coordold = coord
		if ccount > 100:
			cycle = True
	return (cycle,np.count_nonzero(intmap == 6))


pos = getInitPos(rows)
print(pos)
intmap = mapToNumbers(rows)

amap = intmap.copy()
(cycle,count) = runMap(amap, pos)
print("\n----- a -----\n",count)

map_variants = []
[xmax,ymax] = intmap.shape
for x in range(xmax):
	for y in range(ymax):
		if not intmap[x,y] == 0:
			newmap = intmap.copy()
			newmap[x,y] = 0
			map_variants.append(newmap)

cycles = 0
for v in map_variants:
	(cycle,count) = runMap(v, pos,True)
	if cycle:
		cycles+=1
		

print("\n----- b -----\n",cycles)