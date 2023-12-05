#!/usr/bin/env python3

f = open("input4.txt", "r")
input = f.read()

#input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"

totalcards = 0
cards = input.split("\n")

def getPoints(card):
	winnum = card.split("|")[0].split(" ")
	cardnum = card.split("|")[1].split(" ")
	for i in winnum:
		if i == "":
			winnum.remove("")
	for i in cardnum:
		if i == "":
			cardnum.remove("")
	p = 0
	s = ""
	for i in winnum:
		for j in cardnum:
			if j == i and not i=="":
				s+=j+" "
				if p == 0:
					p+=1
				else:
					p*=2
	print(s,"--->",p)
	print(winnum)
	print(cardnum)
		
	return p

def getRealpoints(index):
	global cards
	global totalcards
	if(index > len(cards)):
		#print("card over",index+1)
		return 0
	else:
		#print("card",index+1)
		totalcards+=1
		card = cards[index]
		winnum = card.split("|")[0].split(" ")
		cardnum = card.split("|")[1].split(" ")
		for i in winnum:
			if i == "":
				winnum.remove("")
		for i in cardnum:
			if i == "":
				cardnum.remove("")
		p = 0
		for i in winnum:
			for j in cardnum:
				if j == i and not i=="":
					p+=1
		x = 0
		#print("matching numbers:",p)
		for i in range(1,p+1):
			#print("enter iteration ",i)
			x+= getRealpoints(index+i)
		p+=x
		return p
				
	
	#points = 0	
	#for c in cards:
#	#print(getPoints(c))
#	points+= getPoints(c)
	#print(points)

points = 0
for i in range(len(cards)):
	p = getRealpoints(i)
	print("number",i,p)
	points += p
print(points)
print(totalcards)