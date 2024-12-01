#!/usr/bin/env python3

f = open("input21.txt", "r")
input = f.read()

input = "...........\n.....###.#.\n.###.##..#.\n..#.#...#..\n....#.#....\n.##..S####.\n.##..#...#.\n.......##..\n.##.#.####.\n.##..##.##.\n..........."
map = input.split("\n")
plots = []

def recWalk(map, pos, numToDie):
	global plots
	#print(numToDie)
	if numToDie == 0:
		plots.append(pos)
	else:
		x = pos[0]
		y = pos[1]
		up = [x,y-1]
		right = [x+1,y]
		down = [x,y+1]
		left = [x-1,y]
		dirs = [up,down,right,left]
		for d in dirs:
			if getInfSign(d) != "#":
				recWalk(map, d, numToDie-1)

def getSign(pos):
	x = pos[0]
	y = pos[1]
	if 0 <= y < len(map):
		if 0 <= x < len(map[y]):
			return map[y][x]
		else:
			return "#"
	else:
		return "#"
	
def getInfSign(pos):
	x = pos[0]
	y = pos[1]
	#print("before: ",x,y)
	if y > (len(map)-1):
		y = y%(len(map)-1)
	if y < 0:
		y = y%(len(map)-1)
	if x > (len(map[y])-1):
		x = x%(len(map[y])-1)
	if x < 0:
		x = x%(len(map[y])-1)
		#print("after:   ",x,y)
	return map[y][x]
	
	
def getStartPos():
	startPos = [-1,-1]
	for y in range(len(map)):
		for x in range(len(map[y])):
			if getSign([x,y])=="S":
				startPos = [x,y]
				break
	return startPos

unique_array = [getStartPos()]
#print(getStartPos())
for i in range(50):
	print(i)
	plots = []
	maxdept = 2
	print("max pathts:",4**maxdept)
	for u in unique_array:
		recWalk(map, u, maxdept)
	unique_array = []
	[unique_array.append(item) for item in plots if item not in unique_array] #from chatGPT
	print("len:",len(unique_array))
	
	#print(plots)
count = 0
print("len:",len(plots))
print(unique_array)
print("len:",len(unique_array))
print(len(map),len(map[0]))
		