#!/usr/bin/env python3

f = open("input1.txt", "r")
input = f.read()

#input = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"
#input ="two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
#input = "one\n7\nnineighthree"

input = input.split("\n")

def getFirstDigit(strarr):
	for i in strarr:
		if i.isdigit():
			return i

def substituteTextNumbers(arr):
	for i in range(0,len(arr)):
		#arr[i] = findFirstWrittenNum(arr[i])
		arr[i] = substituteNums(arr[i])
		#print("arr:",arr)
	return arr

def substituteNums(strarr):
	numl = ["zero","one","two","three","four","five","six","seven","eight","nine"]
	indArr = []
	numArr = []
	for j in range(1, len(numl)):
		if(strarr.find(numl[j])>=0):
			indArr.append(strarr.find(numl[j]))
			numArr.append(j)
	
	subsArr = list(strarr)
	for i in range(0,len(indArr)):
		subsArr[indArr[i]] = str(numArr[i])
	for s in range(0,len(subsArr)):
		if not str(subsArr[s]).isdigit():
			#print(subsArr[s])
			subsArr[s] = ''
			
	return ''.join(subsArr)
	

def findFirstWrittenNum(strarr):
	numl = ["zero","one","two","three","four","five","six","seven","eight","nine"]
	s = ""
	for i in strarr:
		s+=i
		for j in range(0, len(numl)):
			n = numl[j]
			if(s.find(n)>=0):
				print(n,strarr)
				strarr = strarr.replace(n, str(j))
				break 
	s = ""
	for i in strarr[::-1]:
		s= i+s
		#print(s)
		for j in range(0, len(numl)):
			n = numl[j]
			if(s.find(n)>=0):
				print(strarr,n)
				strarr = strarr.replace(n, str(j))
				break 
	print(strarr)
	return strarr

#c = 0
#input = substituteTextNumbers(input)
#print(input)
#for i in input:
#	a = getFirstDigit(i)
#	b = getFirstDigit(i[::-1])
#	#print(a,b)
#	x = a+b
#	print(x)
#	c+=int(x)
#print(c)

#print(substituteNums("7srncljm5zmvvrtthreeninejjd85twonepvjeight"))
#print(substituteNums("twoneighthreesevenine"))
#print(substituteNums("onetwothreefourfivesixseveneightnine"))

c = 0
input = substituteTextNumbers(input)
for i in input:
	a = i[0]
	b = i[len(i)-1]
	x = a+b
	print(x)
	c+=int(x)
print(c)