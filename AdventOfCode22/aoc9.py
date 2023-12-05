#!/usr/bin/env python3

f = open("input9.txt", "r")
input = f.read()
#input = "R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2"
#input = "R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20"
input = input.split("\n")
s = []
k = [0]*20
hx = 0
hy = 0
tx = 0
ty = 0
#print(k)
def printK(xlen,ylen):
	field = ""
	for i in range(ylen-1,-1,-1):
		field+="\n"
		for j in range(0,xlen):
			found = False
			for m in range(0,10):
				if(k[m] == j and k[m+10]==i and not found):
					field+=str(m)
					found = True
			if(not found):
				field+="."
	print(field)

def up(prt):
	global hy
	global ty
	if(prt == "H"):
		hy+=1
	else:
		ty+=1

def dn(prt):
	global hy
	global ty
	if(prt == "H"):
		hy-=1
	else:
		ty-=1
		
def rt(prt):
	global hx
	global tx
	if(prt == "H"):
		hx+=1
	else:
		tx+=1

def lt(prt):
	global hx
	global tx
	if(prt == "H"):
		hx-=1
	else:
		tx-=1

def up10(prt):
	global k
	k[prt+10]+=1
		
def dn10(prt):
	global k
	k[prt+10]-=1
		
def rt10(prt):
	global k
	k[prt]+=1
	
		
def lt10(prt):
	global k
	k[prt]-=1
	
		
def move(step,dir):
	global s
	global hx
	global hy
	if(dir == "U"):
		for i in range(0,step):
			up("H")
			movetail()
	elif(dir == "D"):
		for i in range(0,step):
			dn("H")
			movetail()
	elif(dir == "L"):
		for i in range(0,step):
			lt("H")
			movetail()
	else:
		for i in range(0,step):
			rt("H")
			movetail()

def move10(step,dir):
	global s
	if(dir == "U"):
		for i in range(0,step):
			up10(0)
			movetailArr()
	elif(dir == "D"):
		for i in range(0,step):
			dn10(0)
			movetailArr()
	elif(dir == "L"):
		for i in range(0,step):
			lt10(0)
			movetailArr()
	else:
		for i in range(0,step):
			rt10(0)
			movetailArr()

def movetail():
	global s
	global hx
	global tx
	global hy
	global ty
	if((hx-tx)**2+(hy-ty)**2 == 4):
		if(hx==tx):
			if(hy-ty < 0):
				dn("T")
				s.append([tx,ty])
			else:
				up("T")
				s.append([tx,ty])
		if(hy==ty):
			if(hx-tx < 0):
				lt("T")
				s.append([tx,ty])
			else:
				rt("T")
				s.append([tx,ty])
	elif((hx-tx)**2+(hy-ty)**2 > 4):
		if(hy-ty < 0):
			dn("T")
		else:
			up("T")
		if(hx-tx < 0):
			lt("T")
		else:
			rt("T")
		s.append([tx,ty])
		
def movetailArr():
	for i in range(1,10):
		movetail10(i-1,i)
		#printK(100,100)
		
def movetail10(hindex,tindex):
	global s
	global k
	last = tindex==9
	print(last,tindex)
	#print("index:",hindex,tindex)
	hx = k[hindex]
	hy = k[hindex+10]
	tx = k[tindex]
	ty = k[tindex+10]
	if((hx-tx)**2+(hy-ty)**2 == 4):
		print("==")
		if(hx==tx):
			if(hy-ty < 0):
				dn10(tindex)
			else:
				up10(tindex)
		elif(hy==ty):
			if(hx-tx < 0):
				lt10(tindex)
			else:
				rt10(tindex)
	elif((hx-tx)**2+(hy-ty)**2 > 4):
		print(">")
		if(hy-ty < 0):
			dn10(tindex)
		else:
			up10(tindex)
		if(hx-tx < 0):
			lt10(tindex)
		else:
			rt10(tindex)
	if(last):
		print("append:",[tx,ty])
		s.append([tx,ty])


s.append([0,0])
for i in input:
	print("---------------------------------")
	print(i)
	print("---------------------------------")
	op = i.split(" ")
	move10(int(op[1]),op[0])
	print(op)
	#print("k",k)

print(s)
print(len(s))
x = [0]*20
ended = False
while(not ended):
	for j in range(0,20):
		x[j]= k[j]
	print("x:",x)
	movetailArr()
	print("k:",k)
	ended = x == k
print(len(s))
print(s)

c = 0
for j in range(0,len(s)):
	first = True
	for i in range(0,j):
		if(s[i]==s[j]):
			first = False
	if(first):
		c+=1
print(c)