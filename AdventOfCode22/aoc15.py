#!/usr/bin/env python3

input = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15\nSensor at x=9, y=16: closest beacon is at x=10, y=16\nSensor at x=13, y=2: closest beacon is at x=15, y=3\nSensor at x=12, y=14: closest beacon is at x=10, y=16\nSensor at x=10, y=20: closest beacon is at x=10, y=16\nSensor at x=14, y=17: closest beacon is at x=10, y=16\nSensor at x=8, y=7: closest beacon is at x=2, y=10\nSensor at x=2, y=0: closest beacon is at x=2, y=10\nSensor at x=0, y=11: closest beacon is at x=2, y=10\nSensor at x=20, y=14: closest beacon is at x=25, y=17\nSensor at x=17, y=20: closest beacon is at x=21, y=22\nSensor at x=16, y=7: closest beacon is at x=15, y=3\nSensor at x=14, y=3: closest beacon is at x=15, y=3\nSensor at x=20, y=1: closest beacon is at x=15, y=3"
input = "Sensor at x=3844106, y=3888618: closest beacon is at x=3225436, y=4052707\nSensor at x=1380352, y=1857923: closest beacon is at x=10411, y=2000000\nSensor at x=272, y=1998931: closest beacon is at x=10411, y=2000000\nSensor at x=2119959, y=184595: closest beacon is at x=2039500, y=-250317\nSensor at x=1675775, y=2817868: closest beacon is at x=2307516, y=3313037\nSensor at x=2628344, y=2174105: closest beacon is at x=3166783, y=2549046\nSensor at x=2919046, y=3736158: closest beacon is at x=3145593, y=4120490\nSensor at x=16, y=2009884: closest beacon is at x=10411, y=2000000\nSensor at x=2504789, y=3988246: closest beacon is at x=3145593, y=4120490\nSensor at x=2861842, y=2428768: closest beacon is at x=3166783, y=2549046\nSensor at x=3361207, y=130612: closest beacon is at x=2039500, y=-250317\nSensor at x=831856, y=591484: closest beacon is at x=-175938, y=1260620\nSensor at x=3125600, y=1745424: closest beacon is at x=3166783, y=2549046\nSensor at x=21581, y=3243480: closest beacon is at x=10411, y=2000000\nSensor at x=2757890, y=3187285: closest beacon is at x=2307516, y=3313037\nSensor at x=3849488, y=2414083: closest beacon is at x=3166783, y=2549046\nSensor at x=3862221, y=757146: closest beacon is at x=4552923, y=1057347\nSensor at x=3558604, y=2961030: closest beacon is at x=3166783, y=2549046\nSensor at x=3995832, y=1706663: closest beacon is at x=4552923, y=1057347\nSensor at x=1082213, y=3708082: closest beacon is at x=2307516, y=3313037\nSensor at x=135817, y=1427041: closest beacon is at x=-175938, y=1260620\nSensor at x=2467372, y=697908: closest beacon is at x=2039500, y=-250317\nSensor at x=3448383, y=3674287: closest beacon is at x=3225436, y=4052707"

input = input.split("\n")
sx = []
sy = []
bx = []
by = []

wantedy = 10
#wantedy = 2000000
wantedBeacon = []

def getDist(p1,p2):
	d = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
	return d

def getDisty(p1,p2):
	d=0
	if(p1[1] > p2[1]):
		d += p1[1]-p2[1]
	else:
		d += p2[1]-p1[1]
	return d

def isRelevant(s,b):
	distY = getDist(s, b)
	distWanted = getDisty(s, [0,wantedy])
	return distY >= distWanted
	

def isCloser(b,s,p):
	distanceSB = getDist(b,s)
	distancePS = getDist(p, s)
	#print(distanceSB,">=",distancePS)
	return distancePS <= distanceSB
	
for i in input:
	inp = i[10:]
	inp = inp.split(": closest beacon is at ")
	sx.append(inp[0].split(", ")[0])
	sy.append(inp[0].split(", ")[1])
	bx.append(inp[1].split(", ")[0])
	by.append(inp[1].split(", ")[1])
	print(inp)
	
for i in range(0,len(sx)):
	sx[i] = int(sx[i][2:])
	sy[i] = int(sy[i][2:])
	bx[i] = int(bx[i][2:])
	by[i] = int(by[i][2:])

	#nearestSensors = []

for j in range(0,len(by)):
	if(by[j]==wantedy):
		wantedBeacon = [bx[j],by[j]]	
		
ypoints = []


print("bx:",bx)
print("sx:",sx)
'''
foundPoints = [0]*5300000
#ypoints.append(wantedBeacon)	
for i in range(0,len(sx)):
	s = [sx[i],sy[i]]
	b = [bx[i],by[i]]
	#print(i,"/",len(sx)-1)
	if(isRelevant(s, b)):
		for x in range(-300000,5000000,1):
			if(isCloser(b, s, [x,wantedy])):
				if(foundPoints[x]==0):
					ypoints.append([x,wantedy])
					foundPoints[x]=1
					
for i in ypoints:
	print("i:",i,"Dist:",getDist(i, wantedBeacon))
print(len(ypoints)-1)
'''

max = 20
maxrange = 4000000

beaconPoint = []
dist = []
for i in range(0,len(sx)):
	dist.append(getDist([sx[i],sy[i]], [bx[i],by[i]]))
	
	
for y in range(3000000,maxrange):
	print(y,"/",maxrange-1)
	for x in range(0,maxrange):
		isNotCloser = True
		for i in range(0,len(sx)):
			s = [sx[i],sy[i]]
			if(getDist(s, [x,y]) <= dist[i]):
				isNotCloser = False
				break
		if(isNotCloser):
			beaconPoint = [x,y]
			print("found BeaconPoint:",beaconPoint)
			break


print("Beacon position:",beaconPoint,"Frequency:",beaconPoint[0]*4000000+beaconPoint[1])