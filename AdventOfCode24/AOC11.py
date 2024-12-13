#!/usr/bin/env python3
import threading

input = "9759 0 256219 60 1175776 113 6 92833" # input11
#input = "0 1 10 99 999" #dummy input
#input = "125 17" #dummy input2
#input = "2"
line = input


def envolveline(line):
	newline = ""
	stones = line.split(" ")
	for stone in stones:
		if stone == "0":
			newline+="1"
		elif len(stone)%2 ==0:
			mid = len(stone)//2
			newline+= str(int(stone[:mid]))+" "+str(int(stone[mid:]))
		else:
			newline+= str(int(stone)*2024)
		newline+=" "
	newline = newline[:len(newline)-1]
	return newline

def envolvelinethread(line,result,index):
	newline = ""
	stones = line.split(" ")
	for stone in stones:
		if stone == "0":
			newline+="1"
		elif len(stone)%2 ==0:
			mid = len(stone)//2
			newline+= str(int(stone[:mid]))+" "+str(int(stone[mid:]))
		else:
			newline+= str(int(stone)*2024)
		newline+=" "
	newline = newline[:len(newline)-1]
	result[index] = newline

def recursivenvolve(word,iter,groundset = [],rainbowTables=[]):
	evolution = ""
	wordindex = -1
	if len(groundset) > 0:
		for i in range(len(groundset)):
			if word == groundset[i]:
				wordindex = i
	#print(iter,word,wordindex)
	if wordindex > 0:
		table = rainbowTables[wordindex]
		if iter-1 < len(table):
			#print("iter:",iter-1,len(table),len(table[iter-1]))
			return table[iter-1]
		else:
			words = table[len(table)-1]
			for w in words:
				if w != " ":
					#print(w,type(w))
					evolution += " "
					evolution +=recursivenvolve(w, iter-(len(table)), groundset, rainbowTables)
			evolution = evolution[1:]
	elif iter == 0:
		return word
	else:
		if word == "0":
			evolution = recursivenvolve("1", iter-1)
		elif len(word)%2==0:
			mid = len(word)//2
			evolution = recursivenvolve(str(int(word[:mid])), iter-1) + " " + recursivenvolve(str(int(word[mid:])), iter-1)
		else:
			evolution = recursivenvolve(str(int(word)*2024), iter-1)
	return evolution
			
def getGroundset(line,safetylimit=30):
	i = 0
	gs = 0
	gsold = 1
	while gs != gsold and i < safetylimit:
		gsold = gs
		line = envolveline(line)
		gs = list(set(line.split(" ")))
		gs.sort()
		#print(i,len(gs),gs)
		i+=1
	return gs

def runepochs(epochs,line,use_threading = True,num_threads = 10):
	for i in range(epochs):
		#print(i,":",line)
		if i%10==0:
			print(i,":",len(line.split(" ")),len(set(line.split(" "))))
		if i > 30 and use_threading:
			threads = []
			sline = line.split(" ")
			step = len(sline)//num_threads
			rest = len(sline)-step*num_threads
			newline = ""
			results = [""]*num_threads
			for t in range(num_threads):
				min = t*step+rest*(t>0)
				max = (t+1)*step+rest
				part = " ".join(sline[min:max])
				#print(min,max,type(part))
				thread = threading.Thread(target=envolvelinethread,args=(part,results,t))
				threads.append(thread)
				thread.start()
			for thread in threads:
				thread.join()
			line = " ".join(results)
			#print("resultline:",line)
		else:
			line = envolveline(line)
	#print(epochs,":",len(line.split(" ")),line.split(" "))
	return line.split(" ")
	

word = "256219"
	#runepochs(30, "1")
gs_size = 20
groundset = getGroundset(word,gs_size)
rainbowTables = [[]]*len(groundset)
for i in range(0,len(groundset)):
	rainbowtable = []
	line = envolveline(groundset[i])
	#print(groundset[i],line)
	for j in range(gs_size):
		rainbowtable.append(line)
		line = envolveline(line)
	rainbowTables[i] = rainbowtable.copy()

table = rainbowTables[1]

e = 32
x1 = runepochs(e, word)
x2 = recursivenvolve(word,e,groundset,rainbowTables).split(" ")
#print(x2)
print(len(x1),len(x2),x1==x2)

words = input.split(" ")
x = 0
for w in words:
	y = len(recursivenvolve(w,75,groundset,rainbowTables))
	x+=y
	print(y)