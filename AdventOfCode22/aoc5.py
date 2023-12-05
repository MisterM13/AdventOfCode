#!/usr/bin/env python3

f = open("input5.txt", "r")
input = f.read()
#input = "    [D]     \n[N] [C]    \n[Z] [M] [P]\n1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2"
input = input.split("\n\n")
plan = input[0]
instructions = input[1].split("\n")
plan = plan.split("\n")
stacks = plan[-1].split("   ")
plan = plan[:-1]
plan.reverse()
#print(plan)
#print(stacks)
l = len(stacks)
s = [[]]*l

def procesInstr(instruction):
	ins = instruction.split(" ")
	print(ins)
	for i in range(0,int(ins[1])):
		x = fill(s[int(ins[5])-1])
		x.append(s[int(ins[3])-1].pop())
		s[int(ins[5])-1] = x 
		#print(s)
		
def procesInstr9001(instruction):
	ins = instruction.split(" ")
	print(ins)
	a = int(ins[1])
	b = int(ins[3])-1
	c = int(ins[5])-1
	d = len(s[b]) - a
	arr = s[b][d:]
	print(arr)
	s[c] = combine(s[c],arr)
	s[b] = s[b][:d]
	
def combine(arr1,arr2):
	a = len(arr1)
	b = len(arr2)
	ab = a+b
	x = [""]*ab
	c = 0
	for i in range(0,a):
		x[c] = arr1[i]
		c+=1
	for i in range(0,b):
		x[c] = arr2[i]
		c+=1
	return x
	
def fill(arr):
	x = [""]*len(arr)
	for i in range(0,len(arr)):
		x[i] = arr[i]
	return x

# make configuration

for i in plan:
	c = -1
	for j in range(0,len(i),4):
		c+=1
		if(not i[j+1] == " "):
			x = fill(s[c])
			x.append(i[j+1])
			s[c] = x
			#print(c,i[j+1])
			#print(s)

print(s)

#print(instructions)
for i in instructions:
	procesInstr9001(i)

x = ""
for j in s:
	x+= j.pop()
print(x)