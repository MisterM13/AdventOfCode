#!/usr/bin/env python3

#f = open("input18.txt", "r")
#input = f.read()

input = "R 6 (#70c710)\nD 5 (#0dc571)\nL 2 (#5713f0)\nD 2 (#d2c081)\nR 2 (#59c680)\nD 2 (#411b91)\nL 5 (#8ceee2)\nU 2 (#caa173)\nL 1 (#1b58a2)\nU 2 (#caa171)\nR 2 (#7807d2)\nU 3 (#a77fa3)\nL 2 (#015232)\nU 2 (#7a21e3)"

plan = input.split("\n")

def getBorderlen():
	x = 0
	y = 0
	for p in plan:
		dir = p.split(" ")[0]
		if dir == "R":
			x+=1
		elif dir == "L":
			x-=1
		elif dir == "D":
			y+=1
		elif dir == "U":
			y-=1
	return [x,y]

def createMap(x,y):
	s =""
	for i in range(x):
		s += "."
	map = [s]*y
	return map

def printMap(map,title):
	print("---- "+title+" ----")
	for m in map:
		print(m)
		
		

def goDirIt(pos, dir):
	#global map
	x = pos[0]
	y = pos[1]
	print(x,y)
	map[y] = map[y][0:x]+"#"+map[y][(x+1):len(map[y])]
	if map[y][x] == ".":
		map[y] = map[y][0:x]+"*"+map[y][(x+1):len(map[y])]
	if dir == "U": #Up
		newPos = [x,y-1]
	elif dir == "R": #right
		newPos = [x+1,y]
	elif dir == "D": #down
		newPos = [x,y+1]
	elif dir == "L": #left
		newPos = [x-1,y]
	else:
		print("Error: newPos", dir,x,y)
	return newPos


def walk(instr, pos):
	dir = instr.split(" ")[0]
	steps = instr.split(" ")[1]
	color = instr.split(" ")[2]
	for s in range(int(steps)):
		pos = goDirIt(pos, dir)
	return pos

def fillTrench():
	a = False
	b = False
	for m in map:
		print("m:",m)
		for d in range(len(m)):
			if m[d] == "." and a:
				m = m[0:d]+"#"+m[d+1:len(m)]
				if a:
					b = True
				print(m)
			if m[d] == "#":
				if not b:
					a = True
				else:
					a = False
					b = False
				print(a)

map = createMap(10,10)
pos = [0,0]
for p in plan:
	pos = walk(p,pos)
printMap(map,"terrain")
fillTrench()
printMap(map,"filled")


	