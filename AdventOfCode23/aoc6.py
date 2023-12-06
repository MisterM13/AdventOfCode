#!/usr/bin/env python3

f = open("input6.txt", "r")
input = f.read()

#input = "Time:      7  15   30\nDistance:  9  40  200"
time = input.split("\n")[0]
distance = input.split("\n")[1]

time = time.removeprefix("Time:    ")
distance = distance.removeprefix("Distance:")
time = time.split(" ")
distance = distance.split(" ")
for j in range(10):
	for i in time:
		if i =='':
			time.remove(i)
	for i in distance:
		if i =='':
			distance.remove(i)

print(time)
print(distance)

def beatsRecord(pushtime,racetime,record):
	return getDist(pushtime, racetime) > record
	
def getDist(pushtime,racetime):
	lefttime = racetime-pushtime
	dist = pushtime*lefttime
	return dist

def getWinningRaces(racetime,record):
	c = 0
	for i in range(0,racetime+1):
		if beatsRecord(i, racetime, record):
			c+=1
	return c

#c = 1
#for i in range(0,len(time)):
#	c*= getWinningRaces(int(time[i]), int(distance[i]))
#print(c)
t = ""
d = ""
for i in time:
	t +=i
for j in distance:
	d +=j
print(t,d)
print(getWinningRaces(int(t), int(d)))