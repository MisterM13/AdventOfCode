#!/usr/bin/env python3
f = open("input12.txt", "r")
input = f.read()

input = "???.### 1,1,3\n.??..??...?##. 1,1,3\n?#?#?#?#?#?#?#? 1,3,1,6\n????.#...#... 4,1,1\n????.######..#####. 1,6,5\n?###???????? 3,2,1"

input = input.split("\n")
map = []
cond =[]
for i in input:
	map.append(i.split(" ")[0])
	cond.append(i.split(" ")[1])

print(map)
print(cond)

def checkCond(map,cond):
	cond = cond.split(",")
	x = map.split(".")
	x = list(filter(lambda a: a is not None and a != "", x))
	valid = True
	#print(len(x),len(cond),x,cond)
	if(len(x)==len(cond)):
		for m in range(0,len(x)):
			if not len(x[m]) == int(cond[m]):
				valid = False
				break
	else:
		valid = False
	return valid
		
#def makeGuess(map,cond):
#	cond = cond.split(",")
#	x = map.split(".")
#	x = list(filter(lambda a: a is not None and a != "", x))
#	cond = cond.sort(reverse = True)
#	for c in cond:
#		for i in x:
#			if len(i) == int(c):
#				cond.remove(c)
#				x.remove(i)

def getPos(map):
	pos = []
	for i in range(len(map)):
		if map[i] =="?":
			pos.append(i)
	return pos

def getOnePosGuess(map,pos):
	guess = []
	for m in map:
		a = m[0:pos]+"."+m[pos+1:len(m)]
		b = m[0:pos]+"#"+m[pos+1:len(m)]
		#print(a,b)
		guess.append(a)
		guess.append(b)
	return guess

def bruteGuess(map,pos,cond):
	map = [map]
	c = 0
	for i in pos:
		#print(i)
		map = getOnePosGuess(map, i)
	for j in map:
		if(checkCond(j, cond)):
			c+=1
	return c
	
for i in range(len(map)):
	map[i]=map[i]+map[i]+map[i]+map[i]+map[i]
	cond[i]=cond[i]+","+cond[i]+","+cond[i]+","+cond[i]+","+cond[i]

print(map)
print(cond)
c = 0
for i in range(len(map)):
	print(i, "of",len(map))
	c+= bruteGuess(map[i], getPos(map[i]),cond[i])
print(c)
