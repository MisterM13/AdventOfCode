#!/usr/bin/env python3

f = open("input13.txt", "r")
input = f.read()

#input = "#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.\n\n#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#"
#input = ".##.##.##....\n#.######.##..\n##......###..\n...####......\n...####...###\n..#....#..#..\n.#.####.#.###\n..#....#..###\n.##.##.##....\n..######..###\n#.##..##.####\n#.#.##.#.....\n##..##..##.##\n.#..##..#....\n#.##..##.##.."
#input = "#..#..##.#.\n#..#..##.#.\n......#..##\n##########.\n..####.#.##\n#.#.##....#\n#.#.##....#\n..####.#.##\n##########.\n......#..##\n#..#..##.#."

patterns = input.split("\n\n")

for i in patterns:
	print(i)
	print("\n")
	
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

def getCandidates(arr):
	candidates = []
	for i in range(0,len(arr)-1):
		if arr[i] == arr[i+1]:
				candidates.append([i,i+1])
	return candidates

def testCanidates(cand,arr):
	x = []
	for i in cand:
		a = i[0]
		b = i[1]
		valid = True
		if len(arr)-((a+b)/2) <= 0+((a+b)/2):
			for j in range(b,len(arr)):
				if not arr[j]==arr[a]:
					#print(arr[j],arr[a],j,a)
					valid = False
					break
				a-=1
		else:
			for j in range(a,-1,-1):
				#print(arr[j],arr[b],j,b)
				if not arr[j]==arr[b]:
					#print(arr[j],arr[b],j,b)
					valid = False
					break
				b+=1
		if valid:
			x.append(i[1])
	return x
			
def getVariants(pattern):
	variants = []
	for i in range(0,len(pattern)):
		if pattern[i] == ".":
			v = pattern[0:i]+"#"+pattern[(i+1):(len(pattern))]
			variants.append(v)
		elif pattern[i] == "#":
			v = pattern[0:i]+"."+pattern[(i+1):(len(pattern))]
			variants.append(v)
	return variants
	
def printVariants(pattern):
	v = getVariants(pattern)
	print("--------- Original ----------\n")
	print(pattern)
	print("--------- Variants ----------\n")
	for j in v:
		print("--- Variant",v.index(j),"---")
		print(j)
		print()

sum = 0			
for i in patterns:
	r = getRows(i)
	c = getColumns(i)
	rcand = getCandidates(r)
	ccand = getCandidates(c)
	rt = testCanidates(rcand, r)
	ct = testCanidates(ccand, c)
	#print(rcand,ccand,rt,ct)
	print("rt:",rt,"ct:",ct)
	v = getVariants(i)
	#printVariants(patterns[0])
	symr = []
	symc = []
	for j in v:
		vr = getRows(j)
		vc = getColumns(j)
		vrcand = getCandidates(vr)
		vccand = getCandidates(vc)
		vrt = testCanidates(vrcand, vr)
		vct = testCanidates(vccand, vc)
		#print("variant:",v.index(j),"vrt:",vrt,"vct:",vct)
		if len(vrt) >= 0:
			#print("length vrt:",len(vrt),vrt)
			for i in vrt:
				if len(rt) > 0:
					for j in rt:
						if i != j:
							row = i
						else:
							row = -1
					symr.append(row)
				else:
					symr.append(i)
		if len(vct) >= 0:
			#print("length vct:",len(vct),vct)
			for i in vct:
				if len(ct) > 0:
					for j in ct:
						if i != j:
							col = i
						else:
							col = -1
					symc.append(col)
				else:
					symc.append(i)
					#print("symr:",symr,"symc:",symc)
	for j in range(1000):
		if -1 in symr:
			symr.remove(-1)
		if -1 in symc:
			symc.remove(-1)
	print("symr:",symr,"symc:",symc)
	if len(symr)>0 and symr[0] >= 0:
		sum += (100*symr[0])
		print(symr[0])
	elif len(symc)>0 and symc[0] >= 0:
		sum += symc[0]
		print(symc[0])
	else:
		print("-1")
print("Sum:",sum)

#printVariants("...\n...\n...")
#printVariants("###\n###\n###")