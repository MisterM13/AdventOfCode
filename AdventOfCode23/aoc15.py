#!/usr/bin/env python3

f = open("input15.txt", "r")
input = f.read()

#input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
#input = "HASH"

initSeq = input.split(",")
boxes = [[]]*256
nr = 0

def hashString(str):
	value = 0
	for i in str:
		value += ord(i)
		value *= 17
		value %= 256
		#print(i,value)
	return value

def a():
	sum = 0
	for i in initSeq:
		hash = hashString(i)
		print(hash)
		sum += hash
	print(sum)
	
def boxOp(instr):
	global boxes
	replaced = False
	if len(instr.split("=")) > 1:
		#print(instr, "=")
		#print("=")
		x = instr.split("=")
		y = " ".join(x)
		boxnr = hashString(x[0])
		for i in range(len(boxes[boxnr])):
			if boxes[boxnr][i].startswith(x[0]):
				#print(boxes[boxnr][i],y)
				boxes[boxnr][i] = y
				replaced = True
		if not replaced:		
			if len(boxes[boxnr])==0:
				boxes[boxnr] = [y]
			else:
				boxes[boxnr].append(y)
	else:
		#print(instr, "-")
		x = instr.split("-")[0]
		boxnr = hashString(x)
		for i in boxes[boxnr]:
			if i.startswith(x[0]):
				boxes[boxnr].remove(i)

def focusPower(i):
	global boxes
	global nr
	pow = 0
	x = boxes[i]
	for j in range(len(x)):
		val = int(x[j].split(" ")[1])
		pow += (i+1)*(j+1)*val
		print((i+1),(j+1),val,(i+1)*(j+1)*val)
	if pow >0:
		nr+=1
	return pow


def b():
	sum = 0
	for s in initSeq:
		boxOp(s)
	print(boxes)
	for b in range(len(boxes)):
		sum += focusPower(b)
	
	print("Sum:",sum)
	
b()