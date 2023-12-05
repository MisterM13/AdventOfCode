#!/usr/bin/env python3
print(ord("A"))

def getPrio(char):
	if(ord(char) > 95):
		return ord(char)-96
	else:
		return ord(char)-38

f = open("input3.txt", "r")
input = f.read()
#input ="vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw"	
inArr = input.split("\n")
total = 0

#for i in inArr:
#	found = False
#	l = len(i)
#	a = i[0:int(l/2)]
#	b = i[int(l/2):l]
#	for x in a:
#		for y in b:
#			if(x == y and not found):
#				print(x, getPrio(x))
#				total += getPrio(x)
#				found = True
#				break
#print(total)

for i in range(0,len(inArr),3):
	found = False
	for x in inArr[i]:
		for y in inArr[i+1]:
			for z in inArr[i+2]:
				if(x == y == z and not found):
					print(x, getPrio(x))
					total += getPrio(x)
					found = True
					break
				
print(total)