#!/usr/bin/env python3

f = open("input10.txt", "r")
input = f.read()
#input = "addx 15\naddx -11\naddx 6\naddx -3\naddx 5\naddx -1\naddx -8\naddx 13\naddx 4\nnoop\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx -35\naddx 1\naddx 24\naddx -19\naddx 1\naddx 16\naddx -11\nnoop\nnoop\naddx 21\naddx -15\nnoop\nnoop\naddx -3\naddx 9\naddx 1\naddx -3\naddx 8\naddx 1\naddx 5\nnoop\nnoop\nnoop\nnoop\nnoop\naddx -36\nnoop\naddx 1\naddx 7\nnoop\nnoop\nnoop\naddx 2\naddx 6\nnoop\nnoop\nnoop\nnoop\nnoop\naddx 1\nnoop\nnoop\naddx 7\naddx 1\nnoop\naddx -13\naddx 13\naddx 7\nnoop\naddx 1\naddx -33\nnoop\nnoop\nnoop\naddx 2\nnoop\nnoop\nnoop\naddx 8\nnoop\naddx -1\naddx 2\naddx 1\nnoop\naddx 17\naddx -9\naddx 1\naddx 1\naddx -3\naddx 11\nnoop\nnoop\naddx 1\nnoop\naddx 1\nnoop\nnoop\naddx -13\naddx -19\naddx 1\naddx 3\naddx 26\naddx -30\naddx 12\naddx -1\naddx 3\naddx 1\nnoop\nnoop\nnoop\naddx -9\naddx 18\naddx 1\naddx 2\nnoop\nnoop\naddx 9\nnoop\nnoop\nnoop\naddx -1\naddx 2\naddx -37\naddx 1\naddx 3\nnoop\naddx 15\naddx -21\naddx 22\naddx -6\naddx 1\nnoop\naddx 2\naddx 1\nnoop\naddx -10\nnoop\nnoop\naddx 20\naddx 1\naddx 2\naddx 2\naddx -6\naddx -11\nnoop\nnoop\nnoop"
eeprom = input.split("\n")

cycles = 0
regX = 1
signalStrengthSum = 0
screen = ""


def nextCycle():
	global cycles
	global signalStrengthSum
	crt()
	cycles+=1
	if(cycles%40 == 20):
		signalStrengthSum+= regX*cycles
		print("new signalStrength:",regX*cycles,"regX:",regX,"cycles:",cycles)
	

def noop():
	nextCycle()
	
def addx(val):
	global regX
	nextCycle()
	nextCycle()
	regX+= val

def getSpritePos():
	global regX
	spritePos = ""
	for i in range(0,41):
		pos = i
		if(pos==40):
			spritePos+="\n"
		elif(pos == regX or pos+1 == regX or pos-1==regX):
			spritePos+="#"
		else:
			spritePos+="."
			#print(i,pos == regX,pos+1 == regX,pos-1==regX)
	print(spritePos)

def crt():
	global screen
	pos = cycles%40
	if(pos==0 and cycles >= 40):
		screen+="\n"
	elif(pos == regX or pos+1 == regX or pos-1==regX):
		screen+="#"
	else:
		screen+=" "
		#print(pos,regX,pos == regX,pos+1 == regX,pos-1==regX)
		#print(screen)
		#getSpritePos()

		#print(eeprom)
for i in eeprom:
	print(i)
	if(i == "noop"):
		noop()
	else:
		val = int(i.split(" ")[1])
		addx(val)

#print(signalStrengthSum)
print()
print(screen)