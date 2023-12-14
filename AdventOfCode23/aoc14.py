#!/usr/bin/env python3

f = open("input14.txt", "r")
input = f.read()

#input = "O....#....\nO.OO#....#\n.....##...\nOO.#O....O\n.O.....O#.\nO.#..O.#.#\n..O..#O..O\n.......O..\n#....###..\n#OO..#...."
#input = "OOOO.#.O..\nOO..#....#\nOO..O##..O\nO..#.OO...\n........#.\n..#....#.#\n..O..#.O.O\n..O.......\n#....###..\n#....#...." #already shifted input to proof calculation

patterns = input.split("\n\n")

def getRows(pattern):
	return pattern.split("\n")

def getColumns(pattern):
	p = pattern.split("\n")
	cols = []
	for i in range(len(p[0])):
		col = ""
		for j in p:
			col+=j[i]
		cols.append(col)
	return cols

def shiftNW(arr):
	arr = arr.split("#")
	#print(arr)
	for i in range(0,len(arr)):
		arr[i] = strToIntarr(arr[i])
		arr[i].sort(reverse=True)
		arr[i] = IntarrToStr(arr[i])
		#print(arr)
	shiftArr = "#".join(arr)
	return shiftArr

def shiftSE(arr):
	arr = arr.split("#")
	#print(arr)
	for i in range(0,len(arr)):
		arr[i] = strToIntarr(arr[i])
		arr[i].sort()
		arr[i] = IntarrToStr(arr[i])
		#print(arr)
	shiftArr = "#".join(arr)
	return shiftArr

def strToIntarr(str):
	arr = []
	for i in str:
		if i == ".":
			arr.append(0)
		if i == "O":
			arr.append(1)
	return arr

def IntarrToStr(arr):
	str = ""
	for i in arr:
		if i == 0:
			str+="."
		if i == 1:
			str+="O"
	return str

def getLoad(pattern):
	p = getRows(pattern)
	sum = 0
	for i in range(0,len(p)):
		for j in p[i]:
			if j == "O":
				sum += (len(p)-i)
	return sum

def shiftPatternN(pattern):
	pat = getColumns(pattern)
	spat = []
	for c in pat:
		#print("c :",c)
		c = shiftNW(c)
		spat.append(c)
		#print("c':",c)
	flipat = "\n".join(spat)
	#print("flipat:",flipat)
	pattern = getColumns(flipat)
	pattern = "\n".join(pattern)
	return pattern

def shiftPatternS(pattern):
	pat = getColumns(pattern)
	spat = []
	for c in pat:
		#print("c :",c)
		c = shiftSE(c)
		spat.append(c)
		#print("c':",c)
	flipat = "\n".join(spat)
	#print("flipat:",flipat)
	pattern = getColumns(flipat)
	pattern = "\n".join(pattern)
	return pattern

def shiftPatternE(pattern):
	pat = getRows(pattern)
	spat = []
	for c in pat:
		#print("c :",c)
		c = shiftSE(c)
		spat.append(c)
	pattern = "\n".join(spat)
	return pattern
	
def shiftPatternW(pattern):
	pat = getRows(pattern)
	spat = []
	for c in pat:
		#print("c :",c)
		c = shiftNW(c)
		spat.append(c)
	pattern = "\n".join(spat)
	return pattern

def shiftCycle(pattern):
	return shiftPatternE(shiftPatternS(shiftPatternW(shiftPatternN(pattern))))

def printPattern(pattern,text):
	print("-------- "+text+" --------")
	pat = pattern.split("\n")
	for i in pat:
		print(i)

def getOneBil(versions,c):
	print(len(versions),c)
	czero = c[0]
	bzero = 1000000000-c[0]
	dif = c[1]-c[0]
	return(versions[bzero%dif-1])

#print(getLoad(patterns[0]))
#print(shiftN("O.#..O.#.#"))
		#print("North:")
		#printPattern(shiftPatternN(patterns[0]))
		#print("East:")
		#printPattern(shiftPatternE(patterns[0]))
		#print("South:")
		#printPattern(shiftPatternS(patterns[0]))
		#print("West:")
		#printPattern(shiftPatternW(patterns[0]))

p = patterns[0]
versions = []
versions.append(p)
c = [0,0]
bilPat = ""
load = []
for i in range(1000):
	pat = shiftCycle(p)
	found = False
	for v in versions:
		if pat == v:
			if c[0] == 0:
				c[0] = i
			else:
				c[1] = i
				bilPat = getOneBil(versions, c)
				#printPattern(bilPat, "Billion Pattern")
				load.append(getLoad(bilPat))
				c[0]=0
				#print("Load:", getLoad(bilPat))
			#printPattern(pat, "Pat")
			#printPattern(v, "V")
			found = True
			versions = []
			versions.append(pat)
	if not found:
		versions.append(pat)
	p = pat
printPattern(bilPat, "Billion Pattern")
load.sort()
print("Load:", load)
	#printPattern(p,"p")
	#printPattern(pat,"pat")
	


x=0
for i in patterns:
	x += getLoad(shiftPatternN(i))
print(x)