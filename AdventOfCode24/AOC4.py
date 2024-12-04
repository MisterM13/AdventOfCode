#!/usr/bin/env python3
f = open("input4.txt", "r")
input = f.read()

#input = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX"

sequences = input.split("\n")
for i in sequences:
	if i == "":
		sequences.remove(i)
		
		
def sequencialreader(sequence):
	result = 0
	mflag = 0
	opcode = "XMAS"
	for s in sequence:
		#print(s)
		if s == opcode[mflag]: #findes opcodes in sequence
					mflag+=1
					#print(mflag)
					if(mflag == len(opcode)):
						result+=1
						mflag = 0
		else:
			mflag = 0
			if s == opcode[mflag]: #findes opcodes in sequence
						mflag+=1
						#print(mflag)
	return result

def generateColumns(sequences):
	columns = []
	for i in range(len(sequences[0])):
		word = ""
		for seq in sequences:
			word += seq[i]
		columns.append(word)
	return columns

def generateUL(sequences):
	diagr = []
	for i in range(len(sequences)):
		k = 0
		word = ""
		for j in range(i,-1,-1):
			sequence = sequences[j]
			word+= sequence[k]
			k+=1
		diagr.append(word)
	return(diagr)

def generateDiagonalsRight(sequences):
	UL = generateUL(sequences)
	LRR = generateUL(makeReverseWordSequence(sequences)[::-1])
	LR = []
	for i in LRR[::-1]:
		LR.append(i[::-1])
	diagR = UL + LR[1:]
	#print(UL,LR[1:])
	return diagR

def generateDiagonalsLeft(sequences):
	diagL = generateDiagonalsRight(sequences[::-1])
	return(diagL)

def makeReverseWordSequence(sequences):
	sequences_reverse_words = []
	for i in sequences:
		sequences_reverse_words.append(i[::-1])
	return sequences_reverse_words
	
total = 0
for i in sequences:
	total += sequencialreader(i)
	total += sequencialreader(i[::-1])
	
columns = generateColumns(sequences)
for i in columns:
	total += sequencialreader(i)
	total += sequencialreader(i[::-1])

diagR = generateDiagonalsRight(sequences)
diagL = generateDiagonalsLeft(sequences)
diagonals = diagL + diagR

for i in diagonals:
	total += sequencialreader(i)
	total += sequencialreader(i[::-1])

print("a:",total)

patterns = ["M.S.A.M.S","M.M.A.S.S","S.M.A.S.M","S.S.A.M.M"]

def checkPattern(pattern):
	if(pattern[4]=="A"):
		var = ["M","S"]
		m1 = pattern[0]
		m2 = pattern[2]
		s2 = pattern[6]
		s1 = pattern[8]
		for i in range(2):
			if m1 == var[i] and s1 == var[i-1]:
				if m2 == var[i] and s2 == var[i-1]:
					return True
				if m2 == var[i-1] and s2 == var[i]:
					return True

result2 = 0
imax = len(sequences[0])
jmax = len(sequences)
for i in range(len(sequences[0])):
	for j in range(len(sequences)):
		pattern = ""
		if j+2 < jmax:
			seq =  sequences[j]
			seq2 = sequences[j+1]
			seq3 = sequences[j+2]
			if i+2 < imax:
				pattern+=seq[i:i+3]
				pattern+=seq2[i:i+3]
				pattern+=seq3[i:i+3]
		if len(pattern) > 0:
			if checkPattern(pattern):
				result2+=1
print("b:",result2)