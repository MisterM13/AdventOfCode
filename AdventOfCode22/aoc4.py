#!/usr/bin/env python3

f = open("input4.txt", "r")
input = f.read()
#input = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"
inArr = input.split("\n")
score = 0
	
def isIn(arr1,arr2):
	global score
	if(int(arr1[0])>=int(arr2[0]) and int(arr1[1])<=int(arr2[1])):
		print(arr1,arr2,"a fully contained")
		score+=1
	elif(int(arr2[0])>=int(arr1[0]) and int(arr2[1])<=int(arr1[1])):
		print(arr1,arr2,"b fully contained")
		score+=1

def overlaps(arr1,arr2):
	print("testing:",arr1,arr2)
	global score
	found = False
	for x in range(int(arr1[0]),int(arr1[1])+1):
		for y in range(int(arr2[0]),int(arr2[1])+1):
			#print(x,y)
			if(x==y and not found):
				print(arr1,arr2,x,"overlabs")
				score+=1
				found = True
	
for i in inArr:
	a = i.split(",")
	for j in range(0,len(a)):
		a[j] = a[j].split("-")
		#isIn(a[0],a[1])
	overlaps(a[0], a[1])
print(score)