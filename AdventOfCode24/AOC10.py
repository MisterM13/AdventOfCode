#!/usr/bin/env python3

import numpy as np
f = open("input10.txt", "r")
input = f.read()

#input = "89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732"

rows = input.split("\n")
for i in rows:
	if i == "":
		rows.remove(i)

def mapToNumbers(rows):
	x = len(rows)
	y = len(rows[0])
	intmap = np.ones((x,y))
	for xi in range(x):
		r = rows[xi]
		for yi in range(y):
			intmap[xi,yi]= int(r[yi])
	return intmap

def getInitPositions(intmap):
	[xmax,ymax] = intmap.shape
	positions = []
	for x in range(xmax):
		for y in range(ymax):
			if intmap[x,y]==0:
				positions.append((x,y))
	return positions

def ranktrail(intmap,startpos,step=1):
	#print(startpos)
	(x,y) = startpos
	[xmax,ymax] = intmap.shape
	ways = []
	dirs = [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]
	for d in dirs:
		#print(d)
		if d[0] < xmax and d[0] >=0 and d[1]<ymax and d[1]>=0:
			if(intmap[d[0],d[1]]==step):
				ways.append((d[0],d[1]))
	#print("ways:",ways)
	if step == 9:
		return ways
	else:
		endpos = []
		for w in ways:
			endpos += ranktrail(intmap, w, step+1)
		return endpos  #list(set(endpos)) #-> for a
	

intmap = mapToNumbers(rows)
positions = getInitPositions(intmap)
result = 0
print(positions)
for pos in positions:
	res = len(ranktrail(intmap,pos))
	print("res:",res)
	result+=res
print(result)