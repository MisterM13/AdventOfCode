#A*aX + B*bX = yX
#A*aY + B*bY = yY
import numpy as np
f = open("input12.txt", "r")
input = f.read()
#input = "Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=8400, Y=5400\n\nButton A: X+26, Y+66\nButton B: X+67, Y+21\nPrize: X=12748, Y=12176\n\nButton A: X+17, Y+86\nButton B: X+84, Y+37\nPrize: X=7870, Y=6450\n\nButton A: X+69, Y+23\nButton B: X+27, Y+71\nPrize: X=18641, Y=10279"

machines = input.split("\n\n")

def extractmachine(machine):
	lines = machine.split("\n")
	axs = lines[0].find("X+")
	axe = lines[0].find(",")
	ays = lines[0].find("Y+")
	aXVal = int(lines[0][axs+2:axe])
	aYVal = int(lines[0][ays+2:])
	bxs = lines[1].find("X+")
	bxe = lines[1].find(",")
	bys = lines[1].find("Y+")
	bXVal = int(lines[1][bxs+2:bxe])
	bYVal = int(lines[1][bys+2:])
	pxs = lines[2].find("X=")
	pxe = lines[2].find(",")
	pys = lines[2].find("Y=")
	pXVal = int(lines[2][pxs+2:pxe])+10000000000000 #comment the +100.. out for the a part
	pYVal = int(lines[2][pys+2:])+10000000000000
	#print((aXVal,aYVal),(bXVal,bYVal),(pXVal,pYVal))
	return 	(aXVal,aYVal),(bXVal,bYVal),(pXVal,pYVal)
		
def getMinMax(xVal,yVal,pXVal,pYVal):
	a = pXVal//xVal
	b = pYVal//yVal
	if a < b:
		return (a,b)
	else:
		return (b,a)
	
def getdynamicMinMax(val,range=100):
	if val-range < 0:
		min = 0
	else:
		min = val-range
	max = val+range
	return (min,max)
	
def solveMachine(machine):
	(aXVal,aYVal),(bXVal,bYVal),(pXVal,pYVal) = extractmachine(machine)
	(aMin,aMax) = getMinMax(aXVal, aYVal, pXVal, pYVal)
	(bMin,bMax) = getMinMax(bXVal, bYVal, pXVal, pYVal)
	solutions = []
	priceA = 3
	priceB = 1
	for a in range(0, aMax, 1):
		for b in range(0,bMax,1):
			if a*aXVal + b*bXVal == pXVal and a*aYVal + b*bYVal == pYVal:
				#print(a,b,"price:",priceA*a+priceB*b)
				solutions.append((a,b,priceA*a+priceB*b))
	return solutions

def solveMachineEquation(machine):
	(aXVal,aYVal),(bXVal,bYVal),(pXVal,pYVal) = extractmachine(machine)
	(aMin,aMax) = getMinMax(aXVal, aYVal, pXVal, pYVal)
	(bMin,bMax) = getMinMax(bXVal, bYVal, pXVal, pYVal)
	solutions = []
	priceA = 3
	priceB = 1
	#made with help of Claude from Antrophic:
	A = np.array([[aXVal, bXVal],
				[aYVal, bYVal]])
	b = np.array([pXVal, pYVal])
	det = np.linalg.det(A)
	if abs(det) > 1e-10:
		#print(abs(det))
		res = np.linalg.solve(A, b)
		a = round(res[0])
		b = round(res[1])
		#print(a,b)
		#(amin,amax) = getdynamicMinMax(a,10)
		#(bmin,bmax) = getdynamicMinMax(b,10)
		#for a in range(amin, amax, 1):
		#	for b in range(bmin,bmax,1):
		if a*aXVal + b*bXVal == pXVal and a*aYVal + b*bYVal == pYVal:
			#print(a,b,"price:",priceA*a+priceB*b)
			solutions.append((a,b,priceA*a+priceB*b))
	return solutions

def a():
	total = 0
	for m in machines:
		x = solveMachine(m)
		#print(x)
		for i in x:
			(a,b,p) = i
			total+=p
	print("----- a -----\n",total)

def b():
	total = 0
	for m in machines:
		x = solveMachineEquation(m)
		#print(x)
		for i in x:
			(a,b,p) = i
			total+=p
	print("----- b -----\n",total)
	
b()