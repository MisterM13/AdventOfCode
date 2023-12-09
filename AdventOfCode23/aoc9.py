#!/usr/bin/env python3

f = open("input9.txt", "r")
input = f.read()

#input = "0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45"
histories= input.split("\n")

def getIntArr(arr):
	intArr = []
	arr = arr.split(" ")
	for i in arr:
		intArr.append(int(i))
	return intArr

def isZeroArr(arr):
	isZero = True
	for i in arr:
		if i != 0:
			isZero = False
	return isZero
	
def getdif(arr):
	dif = []
	for i in range(1,len(arr),1):
		dif.append(arr[i]-arr[i-1])
	return dif
	
def recursivePredict(arr):
	e = len(arr)-1
	dif = getdif(arr)
	print(dif)
	if isZeroArr(dif):
		return arr[e]+dif[len(dif)-1]
	else:
		return arr[e]+recursivePredict(dif)

def recursivePredictLeft(arr):
	dif = getdif(arr)
	print(dif)
	if isZeroArr(dif):
		#print(arr[0]-dif[0])
		return arr[0]-dif[0]
	else:
		#print(arr[0]-recursivePredictLeft(dif))
		return arr[0]-recursivePredictLeft(dif)
	
	#print(recursivePredictLeft(getIntArr(histories[0])))
	
sum = 0
for h in histories:
	#sum+=recursivePredict(getIntArr(h))
	a = recursivePredictLeft(getIntArr(h))
	#print(a)
	sum+=a
print(sum)