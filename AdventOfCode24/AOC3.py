#!/usr/bin/env python3

f = open("input3.txt", "r")
input = f.read()

#input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))\n"
#input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))" #input b

sequences = input.split("\n")
for i in sequences:
	if i == "":
		sequences.remove(i)
		
def mul(a,b):
	
	return int(a)*int(b)

def sequencialreader(sequence):
	result = 0
	mflag = 0
	inProc = False
	term = 0
	terms = [""]*2
	dflag = 0
	do = True
	opcode = "mul("
	opdo = "do()"
	opdont = "don't()"
	separator = ","
	finisher = ")"
	for s in sequence:
		if inProc:
			if s == separator:
				term +=1
				mflag+=1
			elif s == finisher and mflag == len(opcode)+1:
				if do:
					result += mul(terms[0],terms[1])
					print("made calculation:",terms[0],"*",terms[1],"=",mul(terms[0],terms[1]))
				else:
					print("calculation surpressed by don't()")
				#Reset -> calculation successfully made
				terms = [""]*2
				inProc = False
				mflag = 0
				term = 0
			elif s.isdigit():
				terms[term]+=s
			else:
				#Reset -> due to wrong code
				terms = [""]*2
				inProc = False
				mflag = 0
				term = 0
		elif s == opcode[mflag]: #findes opcodes in sequence
			mflag+=1
			#print(mflag)
			if(mflag == len(opcode)):
				inProc = True
				terms = [""]*2
				term = 0
				#print("found opcode")
		elif s == opdont[dflag]:		#-> b-Part
			dflag+=1
			if(dflag == len(opdont)):
				do = False
				dflag = 0
		elif s == opdo[dflag]:			#-> b-Part
			dflag+=1
			if(dflag == len(opdo)):
				do = True
				dflag = 0
		else:
			mflag = 0
			dflag = 0
			
			
	return result

sequence = "".join(sequences)

print(sequence)

print("result:",sequencialreader(sequence))
	