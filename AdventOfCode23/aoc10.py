#!/usr/bin/env python3

f = open("input10.txt", "r")
input = f.read()

#input = "-L|F7\n7S-7|\nL|7||\n-L-J|\nL|-JF"
#input = "..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ..."

map = input.split("\n")
pipeCircle = []

def getStartPos():
	for y in range(0,len(map)):
		for x in range(0,len(map[y])):
			if(map[y][x]=="S"):
				return [x,y]

def connect(pipe,pos):
	x = pos[0]
	y = pos[1]
	if pipe == "-":
		pos1 = [x+1,y]
		pos2 = [x-1,y]
	elif pipe == "|":
		pos1 = [x,y+1]
		pos2 = [x,y-1]
	elif pipe == "7":
		pos1 = [x-1,y]
		pos2 = [x,y+1]
	elif pipe == "J":
		pos1 = [x,y-1]
		pos2 = [x-1,y]
	elif pipe == "L":
		pos1 = [x+1,y]
		pos2 = [x,y-1]
	elif pipe == "F":
		pos1 = [x,y+1]
		pos2 = [x+1,y]	
	else:
		print("connect Error:",pipe,pos)
	return [pos1,pos2]

def follow(startPos,nextPos):
	nextPipe = map[nextPos[1]][nextPos[0]]
	if(nextPipe == "S"):
		print("Circle finished")
		print("farthest point:",(len(pipeCircle)+1)/2)
	else:
		#print("next Pipe:",nextPipe)
		pipeCircle.append(nextPipe)
		connections = connect(nextPipe, nextPos)
		if connections[0] == startPos:
			follow(nextPos, connections[1])
		elif connections[1] == startPos:
			follow(nextPos, connections[0])
		else:
			print("follow Error:",connections,startPos,nextPos,map[startPos[1]][startPos[0]],map[nextPos[1]][nextPos[0]])

def iterFollow(startPos,nextPos):
	nextPipe = map[nextPos[1]][nextPos[0]]
	if(nextPipe == "S"):
		return [0]
		print("Circle finished")
		print("farthest point:",(len(pipeCircle)+1)/2)
	else:
		#print("next Pipe:",nextPipe)
		pipeCircle.append(nextPipe)
		connections = connect(nextPipe, nextPos)
		if connections[0] == startPos:
			return [nextPos, connections[1]]
		elif connections[1] == startPos:
			return[ nextPos, connections[0]]
		else:
			print("follow Error:",connections,startPos,nextPos,map[startPos[1]][startPos[0]],map[nextPos[1]][nextPos[0]])
	
	
start = getStartPos()
end = False
next = iterFollow(start, [start[0],start[1]+1])
#next = iterFollow(start, [start[0]+1,start[1]])
while not end:
	if len(next) < 2:
		end = True
	else:
		next = iterFollow(next[0],next[1])
print("farthest point:",(len(pipeCircle)+1)/2)