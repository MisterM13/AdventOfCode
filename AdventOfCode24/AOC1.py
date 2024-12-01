#!/usr/bin/env python3
f = open("input1.txt", "r")
input = f.read()

input = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
input = input.split("\n")
print(input)

arr1 = []
arr2 = []
for i in input:
	arr1.append(i.split("   ")[0])
	arr2.append(i.split("   ")[1])
arr1.sort()
arr2.sort()

print("array1:",arr1)
print("array2:",arr2)

def a():
	x = 0
	for i in range(len(arr1)):
		d =  abs(int(arr1[i])-int(arr2[i]))
		print(d)
		x+=d
	
	print("total distance:",x)

def b():
	x = 0
	for i in range(len(arr1)):
		m = 0 #multiplyer
		for j in range(len(arr2)):
			if arr2[j]== arr1[i]:
				m+=1
		d = int(arr1[i])*m
		print(int(arr1[i]),"*",m,"=",d)
		x+=d
	print("similarity score:",x)

a()
b()