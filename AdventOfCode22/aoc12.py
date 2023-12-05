#!/usr/bin/env python3

f = open("input12.txt", "r")
input = f.read()
#input = "Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi"
input = input.split("\n")
lenx = len(input[0])
leny = len(input)
lfield = "".join(input)
ofield = [""]*lenx*leny
sPos = 0
print(lenx,leny,lfield)

def getOptions(el):
	global ofield
	global sPos
	#print("---",lfield[el],"---")
	if(lfield[el] == "S"):
		sPos = el
		if(el-1 > 0):
			ofield[el] +="<"
		if(el+1 < len(lfield)):
			ofield[el] +=">"
		if(el-lenx > 0):
			ofield[el] +="^"
		if(el+lenx < len(lfield)):
			ofield[el] +="v"
	elif(lfield[el] == "E"):
		ofield[el] +="x"
	if(el+1<len(lfield) and ord(lfield[el])>=ord(lfield[el+1])-1):
		#print(lfield[el+1])
		ofield[el]+=">"
	if(el-1>0 and ord(lfield[el])>=ord(lfield[el-1])-1):
		#print(lfield[el-1])
		ofield[el]+="<"
	if(el+lenx<len(lfield) and ord(lfield[el])>=ord(lfield[el+lenx])-1):
		#print(lfield[el+lenx])
		ofield[el]+="v"
	if(el-lenx>0 and ord(lfield[el])>=ord(lfield[el-lenx])-1):
		#print(lfield[el-lenx])
		ofield[el]+="^"

'''def findPath(step,el,prel):
	p = [0]*(len(prel)+1)
	nel = 0
	sstep = [100000]*len(ofield[el])
	optionleft = False
	print("el:",el)
	if(not ofield[el]=="x"):
		for i in range(0,len(ofield[el])):
			if(ofield[el][i] == ">"):
				nel = el+1
				#print(el,">")
			elif(ofield[el][i] == "<"):
				nel = el-1
				#print(el,"<")
			elif(ofield[el][i] == "v"):
				nel = el+lenx
				#print(el,"v")
			elif(ofield[el][i] == "^"):
				nel = el-lenx
				#print(el,"^")
			again = False
			for j in prel:
				if(nel == j):
					again = True
			if(not again):
				for z in range(0,len(prel)):
					p[z] = prel[z]
				p[len(prel)] = nel
				optionleft = True
				#print("prel:",prel,el,nel)
				x = step+1
				sstep[i] = findPath(x, nel, p)
				
	elif(ofield[el]=="x"):
		print("---------------------------------------- Path found with",step+1, "steps")
		optionleft = True
		sstep[0] = step+1
	
	if(optionleft):
		sstep.sort()
		print(el,"sstep:",sstep)
		step = sstep[0]
	else:
		step = 100000
	print(step,"returned from",nel)
	return step
'''
		
def findPath(step,el,prel):
	p = [-1]*(len(prel)+1)
	if(ofield[el] == "x"):
		print("---------------------------------------- Path found with",step+1, "steps")
		step = step+1
	else:
		nel = 0
		sstep = [100000]*len(ofield[el])
		for i in range(0,len(ofield[el])):
			#print(sstep)
			if(ofield[el][i] == ">"):
				nel = el+1
				#print(el,">")
			elif(ofield[el][i] == "<"):
				nel = el-1
				#print(el,"<")
			elif(ofield[el][i] == "v"):
				nel = el+lenx
				#print(el,"v")
			elif(ofield[el][i] == "^"):
				nel = el-lenx
				#print(el,"^")
			again = False
			for j in prel:
				if(nel == j):
					again = True
			if(not again):
				for z in range(0,len(prel)):
					p[z] = prel[z]
				p[len(prel)] = nel
				sstep[i] = findPath(step+1, nel, p)
				sstep.sort()
				step = sstep[0]
				#print(sstep)
				
	return step
		
def printOfield():
	ofieldstr = ""
	for i in range(0,len(ofield)):
		if(i%lenx == 0):
			ofieldstr+="\n\n"
		ofieldstr+=ofield[i]
		for j in range(0,4-len(ofield[i])):
			ofieldstr+=" "
		ofieldstr+="\t"
	print(ofieldstr)

for i in range(0,len(lfield)):
	getOptions(i)

print(ofield)

printOfield()

print(findPath(2, sPos, [0]))