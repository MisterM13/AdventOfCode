#!/usr/bin/env python3

f = open("input2.txt", "r")
input = f.read()

#input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"

games = input.split("\n")


def normGame(game):
	print(game)
	game = game.removeprefix("Game ")
	game = game.replace(":", "")
	rounds = game.split(";")
	lr = len(rounds)
	print("rounds:",rounds)
	gnorm = [0]*(3*lr+1) # gameNr, red,green,blue
	c = 0
	for r in range(0,len(rounds)):
		rs = rounds[r].replace(",", "")
		rs =rs.removeprefix(" ")
		values = rs.split(" ")
		print("val:",values)
		if(r == 0):
			gnorm[0] = int(values[0])
			values = values[1:len(values)]
			print("r:",r)
		for i in range(1,len(values),2):
			if(values[i] == "red"):
				gnorm[1+c*3] = int(values[i-1])
			elif(values[i] == "green"):
				gnorm[2+c*3] = int(values[i-1])
			elif(values[i] == "blue"):
				gnorm[3+c*3] = int(values[i-1])
		c+=1
	print("gnorm:",gnorm)
	return(gnorm)
	

#color 0 = red, 1 = green, 2 = blue
def getColor(gnorm,color):
	colArr = []
	for i in range(1+color,len(gnorm),3):
		colArr.append(gnorm[i])
	return colArr

def getMaxColor(gnorm,color):
	colArr = getColor(gnorm, color)
	colArr.sort()
	colArr.reverse()
	return colArr[0]

def validGame(gnorm):
	colors = [12,13,14]
	valid = True
	for i in range(0,3):
		if getMaxColor(gnorm, i) > colors[i]:
			valid = False
			break
	return valid

def gamePower(gnorm):
	p = 1
	for c in range(0,3):
		p*=getMaxColor(gnorm, c)
	return p

vgl = 0
for i in games:
	n = normGame(i)	
	vgl += gamePower(n)
#	if validGame(n):
#		vgl+=n[0]
		
print(vgl)
