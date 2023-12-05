#!/usr/bin/env python3

f = open("input20.txt", "r")
input = f.read()
input = "1\n2\n-3\n3\n-2\n0\n4"
opList = input.split("\n")
changeList = input.split("\n")
clen = len(changeList)

def merge(a,b,c):
	x = [""]*(len(a)+len(c)+1)
	ct = 0
	for i in a:
		x[ct] = i
		ct+=1
	x[ct] = b
	ct+=1
	for i in c:
		x[ct] = i
		ct+=1
	return x

def merge2(a1,a2,b,c):
	x = [""]*(len(a1)+len(a2)+len(c)+1)
	ct = 0
	for i in a1:
		x[ct] = i
		ct+=1
	for i in a2:
		x[ct] = i
		ct+=1
	x[ct] = b
	ct+=1
	for i in c:
		x[ct] = i
		ct+=1
	return x

def mixmove2(i):
	global changeList
	op = int(i)
	for j in range(0,clen):
		if(changeList[j]==i):
			if(op>0):
				ind = j + op
			else:
				ind = j - op
			el = changeList[j]
			a = ind%clen
			b = j%clen
			print("a:",a,"b:",b)
			if(a < b):
				x = merge(changeList[a:b+1],el,changeList[b+1:clen])
				print("min a",changeList[a:b+1],el,changeList[b+1:clen])
			else:
				x = merge2(changeList[0:b],changeList[b+1:a+1], el, changeList[a+1:clen])
				print("min b",changeList[0:b],changeList[b+1:a+1],el,changeList[a+1:clen])
			print("x",x)
			changeList = x
			break
			
def mixmove(i):
	global changeList
	op = int(i)
	#print("-----------")
	#print(op)
	#if(op<0):
	#	op = -((-op)%clen)
	#else:
	#	op = op%clen
	#print(op)
	for j in range(0,len(changeList)):
		if(changeList[j]==i):
			#if(op>0):
			#	op = op%clen+1
			#else:
			#	op = -(-op%clen)
			ind = j + op
			indup = ind+1%clen
			el = changeList[j]
			if(ind < j):
				for k in range(j,ind,-1):
					if(k%clen == indup):
						break
					changeList[k%clen]=changeList[(k-1)%clen]
				changeList[ind%clen] = el
			else:
				for k in range(j,ind+1):
					if(k%clen == indup):
						break
					changeList[k%clen]=changeList[(k+1)%clen]
				changeList[ind%clen] = el
			break
		
def getNthAZ(n):
	ind = 0
	for j in range(0,len(changeList)):
		if(changeList[j] == "0"):
			#print("found!",j)
			ind = (j+n)%clen
			break
	return changeList[ind]

#for i in range(0,clen):
#	changeList[i] = str((int(changeList[i])*811589153))
#	opList[i] = str((int(opList[i])*811589153))

for i in range(0,clen):
	c = ""
	for j in range(i+1,clen):
		if(changeList[i]==changeList[j]):
			#print("--------------")
			#print(changeList[j])
			#print(opList[j])
			c+="0"
			if(changeList[j][0]=="-"):
				changeList[j] = "-"+c+changeList[j][1:]
				opList[j] = "-"+c+opList[j][1:]
			else:
				changeList[j] = c+changeList[j]
				opList[j] = c+opList[j]
				#print(changeList[j])
				#print(opList[j])

#print(changeList)		
#for r in range(0,10):
#	print(r)
for i in opList:
	print(i)
	mixmove2(i)
	print(changeList)
	
print(getNthAZ(1000),getNthAZ(2000),getNthAZ(3000))
coordinate = int(getNthAZ(1000))+int(getNthAZ(2000))+int(getNthAZ(3000))
print(coordinate)