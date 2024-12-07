#!/usr/bin/env python3
#Warning: the input5.txt was edited for this task:
#Added an \n between rules and updates, removed \n at the end

f = open("input5.txt", "r")
input = f.read()

#input = "47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47"

rules = input.split("\n\n")[0]
updates = input.split("\n\n")[1]
updates = updates.split("\n")

print(rules)
norm_tuples = []
tuples = rules.split("\n")
for t in tuples:
	l = int(t.split("|")[0])
	r = int(t.split("|")[1])
	norm_tuples.append((l,r))
norm_tuples.sort()
	
def makeRuleArr(rules):
	rule_arr = []
	vall_tuples =[]
	tuples = rules.split("\n")
	norm_tuples = []
	for t in tuples:
		l = int(t.split("|")[0])
		r = int(t.split("|")[1])
		norm_tuples.append((l,r))
		rule_arr.append(l)
		rule_arr.append(r)
	ruleArr = list(set(rule_arr))
	norm_tuples.sort()
	#print(norm_tuples)
	#print(rule_arr)
	for i in range(len(rule_arr)):
		(left,right) = getLeftRight(rule_arr[i],norm_tuples)
		val = rule_arr[i]
		vall_tuple = (len(left),val)
		vall_tuples.append(vall_tuple)
		#print(len(left),"l:",left,"r:",right)
	vall_tuples.sort()
	vall_tuples = list(set(vall_tuples))
	#print(vall_tuples)
	rule_arr = []
	for i in vall_tuples:
		rule_arr.append(i[1])
	return rule_arr

def checkRules(norm_tuples,a,b):
	correct = True
	#print("analysing tuple",a,b)
	for t in norm_tuples:
		if t[0] == a and t[1]==b:
			#print("true",t)
			correct = True
		elif t[1] ==a and t[0]==b:
			correct = False
			#print("false",t)
		#elif t[0]==a:
			#print(t,t[0],t[1])
	return correct

def getLeftRight(value,norm_tuples):
	right = []
	left = []
	for t in norm_tuples:
		if (t[0]==value):
			right.append(t[1])
		elif(t[1]==value):
			left.append(t[0])
	return (left,right)

def classify(arr,ruleArr):
	cArr = []
	wrong_pages =[]
	for i in arr:
		for j in range(len(ruleArr)):
			if i==ruleArr[j]:
				cArr.append(j)
	print(cArr)
	for k in range(1,len(cArr)):
		if cArr[k-1] >= cArr[k]:
			wrong_pages.append(arr[k])
	return wrong_pages

def classify2(arr,norm_tuples):
	for i in range(1,len(arr)):
		if not checkRules(norm_tuples, arr[i-1], arr[i]):
			return False
	return True

def getMiddle(arr):
	el = 0
	if len(arr)%2==1:
		mid = (len(arr))//2
		el = arr[mid]
	return(el)

#print("updateds:",updates)
updateArr = []
for parr in updates:
	page_arr = parr.split(",")
	arr = []
	for p in page_arr:
		arr.append(int(p))
	updateArr.append(arr)


ruleArr = makeRuleArr(rules) #TODO:make Array circular
print("updateArr:",updateArr)
print("ruleArr:",ruleArr)

#wrong_pages = []
#correct_arr = []
#for i in updateArr:
#	wp = classify(i, ruleArr)
#	wrong_pages.append(wp)
#	if len(wp)==0:
#		correct_arr.append(i)
#print(wrong_pages)
#print(correct_arr)
#x = 0
#for c in correct_arr:
#	x+= getMiddle(c)
#print("result:",x)

correct_arr = []
x = 0
for i in updateArr:
	if classify2(i, norm_tuples):
		print(i)
		x+= getMiddle(i)
print(x)