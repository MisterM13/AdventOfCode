#!/usr/bin/env python3

f = open("input7.txt", "r")
input = f.read()
input = "$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k"
print(input)
input = input.split("$")[1:]
print(input)
x = []
c = 0
dirarr = []
dir =""
for i in input:
	if(i.find("cd ") > 0 and not i.find("..") > 0 ):
		dir = i[3:]
		dirarr.append(i[3:])
		x.append("||"+i[3:])
		#print("dir:",dir)
	if(i.find("ls") > 0):
		x.append(i[3:])
		c+=1
		#print(x)
print("dirarr:",dirarr)
memArr = [0]*len(dirarr)

print(x)

def getSubDir(dir):
	for i in range (0,len(x)):
		if (x[i]=="||"+dir):
			ls = x[i+1].split("\n")[1:]
			print("ls:",ls)
			for j in ls:
				if(j[0:3] == "dir"):
					d = j[4:]
					print("d:",d)
					getSubDir(" "+d+"\n")

def getInd(dir):
	c = 0
	for i in dirarr:
		if(dir == i):
			break
		else:
			c+=1
	return c

def getRecMem(x,dir,it):
	global memArr
	#print("it:",it)
	mem = 0
	if(it < 995):
		if(memArr[getInd(dir)]>0):
			mem =  memArr[getInd(dir)]
			print("already found")
		else:
			it+=1
			for i in range (0,len(x)):
				if (x[i]=="||"+dir):
					ls = x[i+1].split("\n")[1:]
					print("ls:",ls)
					for j in ls:
						if(j[0:3] == "dir" and mem>=0):
							d = j[4:]
							print("d:",d)
							me= getRecMem(x[(i+1):]," "+d+"\n",it)
							if(me == -1):
								print("--------------------------------------------------return")
								mem = me
							else:
								mem+= me
						else:
							if(len(j)>0 and mem >= 0):
								m = j.split(" ")
								#print("mem++")
								mem+=int(m[0])
			if(mem > 0):
				memArr[getInd(dir)] = mem
				print("added: ",mem,dir)
	else:
		mem = -1
	print("returned from ",dir,mem)
	return mem
					

mem = 0				
z=0
#for k in range(len(dirarr)-1,-1,-2):
#	print("----------------------------------------------------------------------------------",k)
#	m = getRecMem(x[(k+1):],dirarr[k],0)
#	print("dir:",dirarr[k],"mem:",m)
#print(memArr)	

m = getRecMem(x, " /\n", 0)	
print("m",m)
	
#for i in range(0,len(dirarr)):
#	if(memArr[i]==0):
#		me = getRecMem(x,dirarr[i], 0)
#		if(me > memArr[i]):
#			memArr[i] = me
		
for m in memArr:
	if(m < 100000):
		mem+=m

checksum = 0
for j in range(1,len(memArr)):
	checksum += memArr[j]


print(memArr)
print("checksumtest: ", checksum <= memArr[0],"| checksum",checksum,"<= /:",memArr[0],)		
print(mem)