from random import randint
from time import sleep

def strReverse(string):
	newStr = ""
	for i in range(len(string) - 1, -1, -1):
		newStr += string[i]
	return newStr

def binToOctets(binary):
	newBin = "00000000"
	return newBin[:8 - len(binary)] + binary

def decToBin(number):
	binary = ""
	while number != 0:
		binary += str(number % 2)
		number //= 2
	return strReverse(binary)

def makeRule(number):
	ruleBin = binToOctets(decToBin(number))
	RULE_DICT = {
		'111'	:	ruleBin[0],
		'110'	:	ruleBin[1],
		'101'	:	ruleBin[2],
		'100'	:	ruleBin[3],
		'011'	:	ruleBin[4],
		'010'	:	ruleBin[5],
		'001'	:	ruleBin[6],
		'000'	:	ruleBin[7]
	}
	return RULE_DICT

def wolfram_ca():
	ruleNumber = input("\n Enter cellular automaton rule number (0..255, otherwise - random): ")
	ruleNumber = int(ruleNumber) if ruleNumber != '' and 0 <= int(ruleNumber) <= 255 else randint(0, 255)
	RULE = makeRule(ruleNumber)

	planeLength = 64
	plane = [' ' for _ in range(planeLength)]
	# plane = ' ' * planeLength
	plane[planeLength // 2] = '■'

	print(" CHOOSEN RULE %d" % ruleNumber)
	gen = 0
	while gen != planeLength:
		print(" #", end='')
		for j in range(planeLength):
			print(plane[j], end='')
		print(" #")
		# start = plane[254] + plane[0] + plane[1]
		plane[0] = RULE.get(str(plane[planeLength - 1]) + str(plane[0]) + str(plane[1]))
		for i in range(1, planeLength - 1):
			# pos = plane[i - 1] + plane[i] + plane[i + 1]
			# print(i + plane[i - 1] + plane[i] + plane[i + 1])
			plane[i] = RULE.get(str(plane[i - 1]) + str(plane[i]) + str(plane[i + 1]))
		plane[planeLength - 1] = RULE.get(str(plane[planeLength - 2]) + str(plane[planeLength - 1]) + str(plane[0]))
		gen += 1

wolfram_ca()
