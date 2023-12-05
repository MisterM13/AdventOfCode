#!/usr/bin/env python3
import numpy as np

input = "        ...#\n        .#..\n        #...\n        ....\n...#.......#\n........#...\n..#....#....\n..........#.\n        ...#....\n        .....#..\n        .#......\n        ......#.\n\n10R5L5R10L4R5L5"
inp = input.split("\n")
plan = inp[len(inp)-1]
print(plan)
inp = inp[:len(inp)-2]
#print(inp)

facing = 0
pos = [0,0]
maxInp = len(inp[0])
for i in inp:
	if(len(i)>maxInp):
		maxInp = len(i)
		
field = np.zeros((len(inp),maxInp))
print(field.shape)

for i in inp:
	print(i)

for i in range(0,len(inp)):
	for j in range(0,len(inp[i])):
		print(inp[i])
		if(inp[i][j]=="."):
			print(i,j)
			field[i][j] = 1
		elif(inp[i][j]=="#"):
			field[i][j] = 2	

def turn(dir):
	global facing
	if(dir == "R"):
		facing = (facing+1)%4
	else:
		facing = (facing-1)%4
		
print(facing,pos)

def testTurning():
	print(facing)
	for i in range(0,4):
		print("turn right")
		turn("R")
		print(facing)
	for i in range(0,4):
		print("turn left")
		turn("L")
		print(facing)
		
def move(step):
	global pos
	[xmax,ymax] = field.shape
	i = 0
	step = int(step)
	while(i < step):
		print("pos:",pos,"dir:",facing,"i:",i)
		x = pos[0]
		y = pos[1]
		if(facing==1):
			if(field[(x+1)%xmax][y]==2):
				i = step
			elif(field[(x+1)%xmax][y]==1):
				pos = [(x+1)%xmax,y]
				i+=1
			else:
				pos = [(x+1)%xmax,y]
		elif(facing==0):
			if(field[x][(y+1)%ymax]==2):
				i = step
			elif(field[x][(y+1)%ymax]==1):
				pos = [x,(y+1)%ymax]
				i+=1
			else:
				pos = [x,(y+1)%ymax]		
		elif(facing==3):
			if(field[(x-1)%xmax][y]==2):
				i = step
			elif(field[(x-1)%xmax][y]==1):
				pos = [(x-1)%xmax,y]
				i+=1
			else:
				pos = [(x-1)%xmax,y]
		elif(facing==2):
			if(field[x][(y-1)%ymax]==2):
				i = step
			elif(field[x][(y-1)%ymax]==1):
				pos = [x,(y-1)%ymax]
				i+=1
			else:
				pos = [x,(y-1)%ymax]
				
plan = plan.replace("R", ",R,")
plan = plan.replace("L", ",L,")
plan = plan.split(",")
print(plan)

print(field)

for i in plan:
	if(i=="R" or i =="L"):
		turn(i)
	else:
		move(i)
		
print(pos,facing)