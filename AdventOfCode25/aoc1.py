#!/usr/bin/env python3

f = open("input1.txt", "r")
input = f.read()

#input = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
input = input.split("\n")
print(input)

digit = 50
count = 0

def rotate(instr):
	global digit
	global count
	dir = instr[0]
	val = int(instr[1:])
	if dir == "L":
		digit -=val
	elif dir == "R":
		digit +=val
	digit = digit%100
	print(digit)
	if digit == 0:
		count+=1

def rotate0x434C49434B(instr): #use rotSimulation, i somehow messed up with the special cases...
	global digit
	global count
	dir = instr[0]
	val = int(instr[1:])
	dprepre = digit
	if dir == "L":
		digit -=val
	elif dir == "R":
		digit +=val
	dpre = digit
	digit = digit%100
	if dpre != digit:
		if val > 100:							#special case big rotations (larger than 100)
			count+= val//100
			if (dir =="L" and dprepre!=0) or dprepre > digit:	#special cases - counts one more, or if rest smaller than 100 adds up to 100
				count+=1
		else:
			if dprepre !=0:
				count+=1
	elif dpre != 0:
		count+=1
		
	print(count,dpre,digit)
	
def rotSimulation(instr): #simulates the exact rotations
	global digit
	global count
	dir = instr[0]
	val = int(instr[1:])
	if dir == "L":
		for i in range(val):
			digit-=1
			if digit == 100:
				digit = 0
				count+=1
			elif digit == 0:
				count+=1
			elif digit == -1:
				digit = 99
	elif dir == "R":
		for i in range(val):
			digit+=1
			if digit == 100:
				digit = 0
				count+=1
			elif digit == 0:
				count+=1
			elif digit == -1:
				digit = 99	
	print(digit)
	
for i in input:
	#rotate(i)
	#rotate0x434C49434B(i)
	rotSimulation(i)

print("times on 0:",count)