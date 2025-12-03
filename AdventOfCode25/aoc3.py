#!/usr/bin/env python3

f = open("input3.txt", "r")
input = f.read()

#input = "987654321111111\n811111111111119\n234234234234278\n818181911112111"
input = input.split("\n")
print(input)

def getBatteryJoltage(battery):
	f = 9
	s = 0
	found = False
	
	while not found:
		for i in range(len(battery)):
			if battery[i] == str(f) and i!=len(battery)-1:
				found = True
				for j in range(i+1,len(battery)):
					if int(battery[j]) > s:
						s = int(battery[j])
		if not found:
			f-=1
	
	return f*10+s

def getRecursiveBatteryJoltageSafetyOverrite(battery,level):
	energy = ""
	f = 9
	found = False
	
	while not found and level > 0:
		for i in range(len(battery)):
			if battery[i] == str(f) and i < len(battery)-(level-1):
				found = True
				energy = str(f)
				#print(level,energy,battery[i+1:],found)
				energy += getRecursiveBatteryJoltageSafetyOverrite(battery[i+1:], level-1)
				break
		if not found:
			f-=1	
	return energy
				
#print(getRecursiveBatteryJoltageSafetyOverrite("818181911112111", 12))

x=0
for battery in input:
	y = getBatteryJoltage(battery)
	y = getRecursiveBatteryJoltageSafetyOverrite(battery, 12)
	print(y)
	x+=int(y)
print("total:",x)
			
