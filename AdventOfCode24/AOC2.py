#!/usr/bin/env python3

f = open("input2.txt", "r")
input = f.read()

#input = "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9"

reports = input.split("\n")
for i in reports:
	if i == "":
		reports.remove(i)

def isSafe(report):
	results = report.split(" ")
	inc = isIncreasing(int(results[0]), int(results[1]))
	for i in range(1,len(results)):
		change = isIncreasing(int(results[i-1]), int(results[i]))
		dif = abs(int(results[i-1])-int(results[i]))
		if dif < 1 or dif > 3 or change != inc:
			return False
	return True

def makeResultVariant(results,index):
	variant =[]
	for i in range(len(results)):
		if i != index:
			variant.append(results[i])
	return " ".join(variant)

def isSafeProblemDampener(report):
	results = report.split(" ")
	inc = isIncreasing(int(results[0]), int(results[1]))
	for i in range(1,len(results)):
		change = isIncreasing(int(results[i-1]), int(results[i]))
		dif = abs(int(results[i-1])-int(results[i]))
		if dif < 1 or dif > 3 or change != inc:
			reportV1 = makeResultVariant(results, i-1)
			reportV2 = makeResultVariant(results, i)
			#print(reportV1," ",reportV2)
			s1 = isSafe(reportV1)
			s2 = isSafe(reportV2)
			#print(s1,s2)
			if(not s1 and not s2):
				return False
			else:
				return True
	return True

def isIncreasing(a,b):
	return a-b < 0

def a():
	print("\n-------- a ---------")
	x = 0
	for i in reports:
		#print(i,isSafe(i))
		if isSafe(i):
			x+=1
	print("safe reports:",x)
	
def b(): #would be more efficient than bbrute() but there's somwhere a mistake
	print("\n-------- b ---------")
	t = 0
	f = 0
	for i in reports:
		s = isSafeProblemDampener(i)
		print(i,s)
		if s:
			t+=1
		else:
			f+=1
	print("safe reports:",t)
	print("unsafe reports:",f)

def bbrute():
	print("\n-------- b ---------")
	t = 0
	f = 0
	
	for report in reports:
		variations = []
		results = report.split(" ")
		#print(report)
		for i in range(len(results)):
			x = results[:i]+results[i+1:]
			var = " ".join(x)
			variations.append(var)
		#print(variations)
		safe = False
		for v in variations:
			if isSafe(v):
				safe = True
		if safe:
			t+=1
		else:
			f+=1
	print("safe reports:",t)
	print("unsafe reports:",f)
		
a()	

bbrute()