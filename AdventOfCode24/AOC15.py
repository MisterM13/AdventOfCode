#!/usr/bin/env python3

import numpy as np
f = open("input15.txt", "r")
input = f.read()

#input = "##########\n#..O..O.O#\n#......O.#\n#.OO..O.O#\n#..O@..O.#\n#O#..O...#\n#O..O..O.#\n#.OO.O.OO#\n#....O...#\n##########\n\n<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^\nvvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v\n><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<\n<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^\n^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><\n^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^\n>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^\n<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>\n^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>\nv^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"
#input = "########\n#..O.O.#\n##@.O..#\n#...O..#\n#.#.O..#\n#...O..#\n#......#\n########\n\n<^^>>>vv<v>>v<<"

instructionset = input.split("\n\n")[1]
objectmap = input.split("\n\n")[0]
instructionset = instructionset.replace("\n","")
rows = objectmap.split("\n")
print(instructionset)
print(objectmap)
guard=["^",">","v","<"]

def largemapToNumbers(rows):
	x = len(rows)//2
	y = len(rows[0])//2
	intmap = np.ones((x,y))
	for xi in range(0,):
		r = rows[xi:xi+1]
		for yi in range(0,len(rows[0]),2):
			co = r[yi:yi+1]
			if co == "##":
				intmap[xi//2,yi//2]=0 # obstacles get mapped to 0
			elif co == "[]":
				intmap[xi//2,yi//2]=2
			elif co == "@.":
				intmap[xi//2,yi//2]=3
	return intmap
	

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
			elif co == "O":
				intmap[xi,yi]=2
			elif co == "@":
				intmap[xi,yi]=3
	return intmap

def NumbersToMap(intmap,pos=0):
	if not pos == 0:
		(x,y) = pos
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
				row+= "O"
			elif intmap[xi,yi]== 3:
				row+= "@"
		map+=row
		map += "\n"
	return map

def getInitPos(intmap):
	indices = np.where(intmap == 3)
	return indices

def getBoxesPos(intmap):
	indices = np.where(intmap == 2)
	return indices

def getBoxSum(intmap):
	sum = 0
	[y,x] = getBoxesPos(intmap)
	for i in range(len(y)):
		z = y[i]*100 + x[i]
		#print(z)
		sum+=z
	return sum

def move(pos,dir,intmap):
	[x,y] = pos
	item = intmap[x,y]
	[xmax,ymax] = intmap.shape
	xi = 0
	yi = 0
	for i in range(len(guard)):
		if guard[i] == dir:
			if i == 0:
				xi = -1
			elif i== 1:
				yi = 1
			elif i== 2:
				xi = 1
			elif i== 3:
				yi =-1
	if x+xi < xmax and y+yi < ymax and x+xi >=0 and y+yi >=0:
		if intmap[x+xi,y+yi] < 1:
			return (pos,intmap)
		elif intmap[x+xi,y+yi] == 2:
			(newpos,newintmap) = move([x+xi,y+yi], dir, intmap)
			if newpos == [x+xi,y+yi]:
				return (pos,intmap)
			return move(pos,dir,newintmap)
		else:
			intmap[x+xi,y+yi] = intmap[x,y]
			intmap[x,y] = 1
			return([x+xi,y+yi],intmap)

	

intmap = mapToNumbers(rows)
pos = getInitPos(intmap)

for i in instructionset:
	print("Move "+i+":")
	(pos,intmap) = move(pos, i, intmap)
	print(NumbersToMap(intmap, pos))

	#print("pos:",pos)
	#print(intmap[pos])

print("total:",getBoxSum(intmap))
