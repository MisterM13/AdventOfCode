#!/usr/bin/env python3

f = open("input5.txt", "r")
input = f.read()

input ="seeds: 79 14 55 13\nseed-to-soil map:\n50 98 2\n52 50 48\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\nwater-to-light map:\n88 18 7\n18 25 70\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\ntemperature-to-humidity map:\n0 69 1\n1 0 69\nhumidity-to-location map:\n60 56 37\n56 93 4"


maps = input.split("map:")

def mapto(number,map):
	conmap = maps[map].split("\n")
	destination = number
	for j in range(3):
		for i in conmap:
			if i =='' :
				conmap.remove(i)
			elif not i[0].isdigit():
				conmap.remove(i)
				#print(conmap)
	for i in conmap:
		arr = i.split(" ")
		dest = int(arr[0])
		src = int(arr[1])
		rng = int(arr[2])
		if src <= number < src+rng:
			dif = number-src
			destination = dest+dif
	return destination

#divide and conquer try, but did not work...
def napoleon(min, max):
	a = mapto(mapto(mapto(mapto(mapto(mapto(mapto(min, 1),2),3),4),5),6),7)
	b = mapto(mapto(mapto(mapto(mapto(mapto(mapto(max, 1),2),3),4),5),6),7)
	c = mapto(mapto(mapto(mapto(mapto(mapto(mapto((min+max)/2, 1),2),3),4),5),6),7)
	print(min,max,"-->",a,c,b)
	if a == b:
		return a
	elif a < b:
		max = (min+max)/2
		return napoleon(min, max)
	else:
		min = (min+max)/2
		return napoleon(min, max)
#print(mapto(79,1))

seed = maps[0].split("\n")[0]
seed = seed.removeprefix("seeds: ")
seed = seed.split(" ")

locations = []
for s in seed:
	loc = mapto(mapto(mapto(mapto(mapto(mapto(mapto(int(s), 1),2),3),4),5),6),7)
	locations.append(loc)
	#print("Seed:",s,"maps to Location:",loc)
locations.sort()
print("min Location:",locations[0])

#this would work in theory for the second star. 
#In reality the input numbers are too big (it would take maybe years to calculate it all...)
locations = []
for s in range(0,len(seed),2):
	start = int(seed[s])
	rng = int(seed[s+1])
	for i in range(start,start+rng):
		loc = mapto(mapto(mapto(mapto(mapto(mapto(mapto(i, 1),2),3),4),5),6),7)
		locations.append(loc)
locations.sort()
print(locations)
print("min Location:",locations[0])