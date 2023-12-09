#!/usr/bin/env python3
import math
f = open("input8.txt", "r")
input = f.read()

#input = "RL\nAAA = (BBB, CCC)\nBBB = (DDD, EEE)\nCCC = (ZZZ, GGG)\nDDD = (DDD, DDD)\nEEE = (EEE, EEE)\nGGG = (GGG, GGG)\nZZZ = (ZZZ, ZZZ)"
#input = "LLR\nAAA = (BBB, BBB)\nBBB = (AAA, ZZZ)\nZZZ = (ZZZ, ZZZ)"
#input = "LR\n11A = (11B, XXX)\n11B = (XXX, 11Z)\n11Z = (11B, XXX)\n22A = (22B, XXX)\n22B = (22C, 22C)\n22C = (22Z, 22Z)\n22Z = (22B, 22B)\nXXX = (XXX, XXX)"

instructionSet = input.split("\n")[0]
nodes = input.split("\n")
nodes.remove(instructionSet)
#print(nodes)

def step(node,sc):
	print(node)
	if node == "ZZZ":
		print(sc)
	else:
		for i in nodes:
			if i[0:3] == node:
				ins = instructionSet[sc%len(instructionSet)]
				if ins == "L":
					#print(i[7:10])
					step(i[7:10], sc+1)
				else:
					step(i[12:15], sc+1)
					#print(i[12:15])

def stepIter(node,ins):
	for i in nodes:
		if i[0:3] == node:
			if ins == "L":
				return i[7:10]
			else:
				return i[12:15]

def getAllAnodes(nodes):
	anodes = []
	for i in nodes:
		#print(i)
		if i[2] == "A":
			anodes.append(i[0:3])
	return anodes

def a():
	nodeFound = False
	sc = 0
	node = "AAA"
	while not nodeFound:
		ins = instructionSet[sc%len(instructionSet)]
		node = stepIter(node, ins)
		print(node)
		if node == "ZZZ":
			nodeFound = True
		sc+=1
	print(sc)

def b():
	sc = 0
	startnodes = getAllAnodes(nodes)
	print(startnodes)
	allnodesFound = False
	statnodes = [0]*len(startnodes)
	f = [0]*len(startnodes)
	while not allnodesFound:
		ins = instructionSet[sc%len(instructionSet)]
		for i in range(0,len(startnodes)):
			if f[i] ==0:
				startnodes[i] = stepIter(startnodes[i], ins)
				statnodes[i] += 1
				if startnodes[i][2] == "Z":
					f[i] = 1
					
				
		if f == [1]*len(startnodes):
			print(statnodes)
			allnodesFound = True
		sc+=1
	print(len(statnodes))
	print(math.lcm(statnodes[0],statnodes[1],statnodes[2],statnodes[3],statnodes[4],statnodes[5],))
b()