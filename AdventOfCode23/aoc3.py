#!/usr/bin/env python3

f = open("input3.txt", "r")
input = f.read()

input = "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.."

map = input.split("\n")

def getNumber(x,y):
	global map
	s=""
	for i in range(y,len(map[x])):
		if map[x][i].isdigit():
			s+=map[x][i]
		else:
			break
	for i in range(y-1,-1,-1):
		if map[x][i].isdigit():
			s = map[x][i]+s
		else:
			break
	print(s)
	return int(s)

getNumber(0, 1)