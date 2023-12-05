#!/usr/bin/env python3

f = open("input21.txt", "r")
input = f.read()
#input = "root: pppw + sjmn\ndbpl: 5\ncczh: sllz + lgvd\nzczc: 2\nptdq: humn - dvpt\ndvpt: 3\nlfqf: 4\nhumn: 5\nljgn: 2\nsjmn: drzm * dbpl\nsllz: 4\npppw: cczh / lfqf\nlgvd: ljgn * ptdq\ndrzm: hmdt - zczc\nhmdt: 32"
inp = input.split("\n")
print(inp)
names = []
num = []
opn = []
op = []

for i in inp:
	n = i.split(" ")
	#print(n,len(n))
	if(len(n)==4):
		monk = n[0]
		opn.append(monk[0:4])
		op.append(n[1:])
	else:
		monk = n[0]
		names.append(monk[0:4])
		num.append(n[1])

def makeOp(arr):
	x = int(getVal(arr[0]))
	y = int(getVal(arr[2]))
	res = -1
	#print(x,y)
	if(arr[1]=="+"):
		res = x+y
	elif(arr[1]=="-"):
		res = x-y
	elif(arr[1]=="*"):
		res = x*y
	elif(arr[1]=="/"):
		res = x/y
	elif(arr[1]=="="):
		if(x==y):
			res = 0
		#print(arr,res)
	return res

def getVal(name):
	c = 0
	res = -1
	found = False
	for i in names:
		if(i == name):
			res = num[c]
			found = True
		c+=1
	c=0
	if(not found):
		for j in opn:
			if(j == name):
				#print(op[c])
				res = makeOp(op[c])
			c+=1
	return res
			
	

print("names:",names)
print("num:",num)
print(opn)
print(op)

#print(getVal("root"))

		
indh = 0
for i in range(0,len(names)):
	if(names[i]=="humn"):
		indh = i
		
def bruteForce(min,max):
	for i in range(0,len(op)):
		if (opn[i]=="root"):
			print(op[i])
			op[i][1] = "-"
			print(op[i])
			
	for i in range(min,max):
		num[indh]= str(i)
		r = getVal("root")
		if(i%100==0):
			print("round:",i,"val:",r)
		if(r==0):
			print("Right Value:",i)
			break

def divideAndConquer():
		for i in range(0,len(op)):
			if (opn[i]=="root"):
				print(op[i])
				op[i][1] = "-"
				print(op[i])
				
		x = 1
		min = 0
		max = 4234067021641
		last = 4234067021641**2
		found = False
		c = 0
		while(not found):
			c+=1
			num[indh]= str(x)
			r = getVal("root")
			if(c%1 ==0):
				print("Round:",c,min,x,max,r)
			if(r==0):
				print("Right Value:",x)
				print("Round:",c,min,x,max,r)
				found = True
			elif(r**2 < last):
				last = x**2
				min = x
			else:
				max = x
			x = int((min+max)/2)
			if(min==max):
				print("no result found!")
				break
			

bruteForce(3243420789000,31654727830000)
#divideAndConquer()