#!/usr/bin/env python3

f = open("input6.txt", "r")
input = f.read()
#input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" # 7 19
#input = "bvwbjplbgvbhsrlpgdmjqwftvncz" # 5 23
#input = "nppdvjthqldpwncqszvftbrmjlhg" # 6 23
#input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" # 10 29
#input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" # 11 26

def hasDublicate(str):
	dublicate = False
	c = 1
	for i in str:
		x = str.find(i,c)
		if(x>0):
			dublicate = True
			break
		else:
			c+=1
	return dublicate

#for i in range(4,len(input)):
#	#print(input[i-4:i])
#	if(not hasDublicate(input[i-4:i])):
#		print(i)
#		break
		
for i in range(14,len(input)):
	#print(input[i-4:i])
	if(not hasDublicate(input[i-14:i])):
		print(i)
		break