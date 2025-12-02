#!/usr/bin/env python3

f = open("input2.txt", "r")
input = f.read()

#input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
input = input.split(",")
input
print(input)

invalid_IDs = []

def analyse(datarange):
	global invalid_IDs
	[min,max] = datarange.split("-")
	min = int(min)
	max = int(max)+1
	for num in range(min,max):
		data = str(num)
		l = len(data)
		if l%2==0:
			if data[0:l//2] == data[(l//2):]:
				invalid_IDs.append(num)

def numbersequencing(num):
	global invalid_IDs
	sequence=[0,0,0,0,0,0,0,0,0,0]
	for i in str(num):
		sequence[int(i)]+=1
	cleanedSeq = [x for x in sequence if x != 0]
	if len(cleanedSeq) == 1 and len(str(num)) > 1:
		if cleanedSeq[0]!=0:
			invalid_IDs.append(num)
	elif len(cleanedSeq) > 1:
		cleanedSeq.sort()
		#print(cleanedSeq)
		ancor = cleanedSeq[0]
		isInvalid = True
		if len(cleanedSeq) < len(str(num)):
			for i in cleanedSeq:
				if ancor==1: #checks if some digits are not repeating
					isInvalid = False
					break
			if isInvalid and check(ancor, str(num)):
				print(cleanedSeq)
				invalid_IDs.append(num)

def check(ancor,strnum): #checks if the real pattern is repeating
	isInvalid = True
	prepart = ""
	if ancor%2 == 0:
		ancor = 2
	partlen = len(strnum)//ancor
	for i in range(0,len(strnum),partlen):
		part = strnum[i:i+partlen]
		if i!=0 and part!=prepart:
			isInvalid = False
			print("failed Check:",strnum,partlen,ancor)
			break
		prepart = part
	return isInvalid
			
			

def analyse2(datarange):
	[min,max] = datarange.split("-")
	min = int(min)
	max = int(max)+1
	for num in range(min,max):
		numbersequencing(num)

for i in input:
	analyse2(i)
invalid_IDs.sort()

print(invalid_IDs, len(invalid_IDs))
print(sum(invalid_IDs))
	