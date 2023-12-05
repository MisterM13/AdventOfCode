#!/usr/bin/env python3
f = open("input13.txt", "r")
input = f.read()
#input = "[1,1,3,1,1]\n[1,1,5,1,1]\n\n[[1],[2,3,4]]\n[[1],4]\n\n[9]\n[[8,7,6]]\n\n[[4,4],4,4]\n[[4,4],4,4,4]\n\n[7,7,7,7]\n[7,7,7]\n\n[]\n[3]\n\n[[[]]]\n[[]]\n\n[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]"
input = input.split("\n\n")

def takeOne(arr1,arr2):
	#-1 -> initstate
	# 0 -> not determinable, next element
	# 1 -> l smaller, right order
	# 2 -> l bigger, false order
	# 3 -> r not array, make []
	# 4 -> l not array, make []
	
	#	x	y
	#	a	a	0
	#	[	a	3
	#	[	]	2
	#	a	]	2
	#	]	a	1
	#	]	[	1
	#	a	[	4
	
	
	x = ""
	y = ""
	cf = -1
	if(len(arr1)> 0):
		x = arr1[0]
		if(len(arr2) < 1):
			cf = 2
		else:
			y = arr2[0]
	else:
		if(len(arr2) > 0):
			cf = 1
			
	if(len(arr1) > 1):
		if(arr1[0:2]=="10"):
			x = arr1[0:2]
	if(len(arr2) > 1):
		if(arr2[0:2]=="10"):
			y = arr2[0:2]
	if(x==y):
		cf = 0
	elif(x == "["):
		if(y=="]"):
			cf = 2
		else:
			cf = 3
	elif(y=="]"):
		cf = 2
	elif(x == "]"):
		cf = 1
	elif(y=="["):
		cf = 4
	else:
		print(x,y,len(x),len(y))
		if(len(x) < 1):
			x = 0
		if(len(y) < 1):
			y=0
		if(int(x) < int(y)):
			cf = 1
		else:
			cf = 2
	print(x,y,cf)
	return cf

def compare(arr1, arr2):
	running = True
	ordering = False
	while(running):
		cf = takeOne(arr1, arr2)
		if(cf < 0):
			running = False
			print("Error:",arr1,arr2)
			if(cf == -2):
				print("false shift on comas")
			if(cf == -3):
				print("false brackets")
		elif(cf == 0):
			#print("shortening arrays:",arr1,arr2)
			arr1 = arr1[1:]
			arr2 = arr2[1:]
			if(len(arr1) < 1 and len(arr2) < 1):
				ordering = True
				running = False
			#print("shortend arrays:",arr1,arr2)
		elif(cf == 1):
			#print("right Order")
			ordering = True
			running = False
		elif(cf == 2):
			#print("false Order")
			running = False
		elif(cf == 3):
			#print("changin brackets in arr2:",arr2)
			arr1 = arr1[1:]
			i = arr2.find(",")
			if(i>0):
				arr2 = arr2[0:i]+"]"+arr2[i:]
				#print("changed arr2:",arr2,i)
		elif(cf == 4):
			#print("changin brackets in arr1:",arr1)
			arr2 = arr2[1:]
			i = arr1.find(",")
			if(i>0):
				arr1 = arr1[0:i]+"]"+arr1[i:]
				#print("changed arr1:",arr1)
	return ordering

c = 1
s = 0
signalList = []
for i in input:
	arr = i.split("\n")
	signalList.append(arr[0])
	signalList.append(arr[1])
	#print("arr:",arr)
#	print("------------------ Pair",c,"------------------")
#	res = compare(arr[0],arr[1])
#	print(res)
#	print(arr, "result:", res )
#	if(res):
#		s+=c
#	c+=1
#	print(s)

signalList.append("[[2]]")	
signalList.append("[[6]]")	
print(signalList)

ordered = False
while(not ordered):
	ordered = True
	for i in range(0, len(signalList)):
		for j in range(i,len(signalList)):
			x = signalList[i]
			y = signalList[j]
			if(not compare(x,y)):
				signalList[i],signalList[j] = y,x
				ordered = False
print(signalList)
c = 1
d1 =0
d2 =0
for i in signalList:
	if(i=="[[2]]"):
		d1 = c
	if(i=="[[6]]"):
		d2 = c
	c+=1
print(d1*d2)