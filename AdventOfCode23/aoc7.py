#!/usr/bin/env python3

f = open("input7.txt", "r")
input = f.read()

#input = "32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483"
#input = "2346J 1\n3JJ25 2\n9JJJJ 7\nJ32JJ 4\nJJJJJ 5\n77788 3\n7JJ7J 6"
input = "9JJJJ 6\n88JJJ 5\nJ99JJ 4\nJ98J2 3\n234JJ 1\n22888 2\nJ2345 1"

input = input.split("\n")

cards = []
bid = []

for i in input:
	cards.append(i.split(" ")[0])
	bid.append(i.split(" ")[1])
	#print(cards, bid)

def getValarr(arr):
	varr = []
	for i in arr:
		varr.append(getVal(i))
	return varr
		
def getVal(char):
	if char.isdigit():
		return int(char)
	elif char == "A":
		return 14
	elif char == "T":
		return 10
	elif char == "J":
		return 1
	elif char == "Q":
		return 12
	elif char == "K":
		return 13

def getPair(valarr):
	#print(valarr)
	pair = []
	j = 0
	for i in range(1,len(valarr)):
		if valarr[i]==valarr[i-1] and valarr[i] > 1:
			pair.append(valarr[i])
		elif valarr[i] == 1 :
			j+=1
		
	if len(pair) > 0:
		for i in range(j):
			pair.append(pair[0])
	else:
		for i in range(j):
			pair.append(valarr[0])
	if(valarr == [1,1,1,1,1]):
		#print("----------------------------JJJJJJJJJJJJJJJJJJJJJJ--------------------------")
		pair = [14,14,14,14]
	return pair
			
def getTupels(valarr):
	pair = getPair(valarr)
	#pair.sort(reverse = True)
	triple = getPair(pair)
	#triple.sort()
	quadruple = getPair(triple)
	#quadruple.sort()
	pentuple = getPair(quadruple)
	#pentuple.sort()
	#print(pair,triple,quadruple,pentuple)
	return[pair,triple,quadruple,pentuple]

def getTupelPoints(tuple):
	#print(tuple)
	if len(tuple[3])>0:
		#return (500 + tuple[3][0])*10000000000
		return 60000000000
	elif len(tuple[2])>0:
		#return (400 + tuple[2][0])*10000000000
		return 50000000000
	elif len(tuple[1])>0:
		if(len(tuple[0])==3):
			return 40000000000
		else:
		#return (300 + tuple[1][0])*10000000000
			return 30000000000
	elif len(tuple[0])>1:
		#return (200 + tuple[0][0])*10000000000#+ tuple[0][1]
		return 20000000000
	elif len(tuple[0])>0:
		#return (100 + tuple[0][0])*10000000000
		return 10000000000
	else:
		return 0

def getPoints(hand):
	valarr = getValarr(hand)
	valarr.sort(reverse=True)
	#print("valarr:", valarr)
	points = getTupelPoints(getTupels(valarr)) 
	handarr = getValarr(hand)
	m = 100000000
	for i in handarr:
		points+=m*i
		m/=100
	print(points)
	return points

def getRank(cards):
	pArr = []
	rArr = []
	rank = []
	for h in cards:
		#print(getPoints(h))
		pArr.append(getPoints(h))
	for i in pArr:
		rArr.append(i)
	rArr.sort()
	#print(rArr)
	#print(pArr)
	for i in range(0,len(pArr)):
		for j in range(0,len(rArr)):
			if pArr[i] == rArr[j]:
				rank.append(j+1)
	
				#print(len(pArr),len(rArr),len(rank))
	return rank

#print(getRank(cards))	

winnings = 0
rankArr = getRank(cards)
print("lens:",len(rankArr),len(cards), len(bid))
for i in range(0,len(rankArr)):
	print("rank:",rankArr[i],"card:",cards[i],"bid:",int(bid[i]))
	winnings+= rankArr[i]*int(bid[i])
print(winnings)