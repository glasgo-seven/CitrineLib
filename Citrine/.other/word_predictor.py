from sys import argv

pronoun_list = ["I", "ME", "MY", "MINE", "WE", "US", "OUR", "OURS", "YOU", "YOUR", "YOURS", "HE", "HIM", "HIS", "SHE", "HER", "HERS", "IT", "ITS", "THEY", "THEM", "THEIR", "THEIRS", "THIS", "THESE", "THAT", "THOSE", "FORMER", "LATTER", "WHO", "WHOM", "WHOSE", "WHAT", "WHICH", "THAT", "ONE", "ONE'S", "SOMETHING", "ANYTHING", "NOTHING", "THINGS", "SOMEONE", "ANYONE", "PEOPLE", "SOMEBODY", "ANYBODY", "NOBODY"]
articles_list = ["THE", "A", "AN"]
conjunction_list = ["FOR", "AND", "NOR", "BUT", "OR", "YET", "SO"]
preposition_list = ["ON", "TO", "IN", "FROM", "WITH", "UNDER", "BEFORE", "THROUGHOUT", "ATOP", "FOR", "UNTIL", "OF"]
link_verb_list = ["IS", "AM", "ARE", "WERE", "WAS", "BEING", "BEEN", "HAVE", "HAS", "HAD", "WILL", "BE"]
number_list = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE", "TWENTY", "THIRTY", "FOURTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY", "HUNDRED", "THOUTHAND", "MILLION", "BILLION"]
none_list = ["DON'T"]

tab = "\t"
emp = ""

total = 0

def check(test, num):
	file_check = open("./true", 'r')
	word_n = 0
	for lc in file_check:
		line_check = lc.split()
		for true in line_check:
			if num == word_n:
				if test == true.upper():
					global total
					total += 1
					return ('\x1b[32m' + test + '\x1b[0m (' + true.upper() + ')')
				else:
					return ('\x1b[31m' + test + '\x1b[0m (' + true.upper() + ')')
			word_n += 1

def reset():
	return '\x1b[0m'

def make_prediction(line, word):
	_word = line[word].upper().rstrip(".,?!:;")
	if _word in none_list:
		return "--------"
	if _word in number_list:
		return "Noun"
	if _word in pronoun_list:
		return "Pronoun"
	if _word in conjunction_list:
		return "Conjunction"
	if _word in preposition_list:
		return "Preposition"
	if _word in articles_list:
		return "Article"
	if _word in link_verb_list:
		return "LinkVerb"

	if word > 0:
		if line[word - 1].upper() in ["IN", "FROM", "WITH"]:
			return "Noun"
	if word < len(line) - 1:
		if line[word + 1].upper() in ["FOR", "UNTIL"]:
			return "Adjective"
	if word < len(line) - 1:
		if line[word + 1].upper() in ["THROUGHOUT", "ATOP", "FOR", "WITH"]:
			return "Verb"
	
	if "ing" in _word or "ed" in _word:
		return "Verb"
	if _word[len(_word) - 1] == 'S':
		return "Verb"
	if word > 0:
		if make_prediction(line, word - 1) == "Verb":
			return "Adverb"
	if _word[len(_word) - 1] == 'Y':
		return "Adjective"
	if word > 0:
		if make_prediction(line, word - 1) == "Adverb":
			return "Adjective"
	if word > 0:
		if make_prediction(line, word - 1) == "LinkVerb":
			if word < len(line) - 1:
				if make_prediction(line, word + 1) == "Adjective":
					return "Adverb"
			return "Verb"
	return "Verb"

def predictor(file_path):
	file = open(file_path, 'r')
	num = 0
	for l in file:
		line = l.split()
		print(l, end = '')
		print("----------------------------------------------------------------")
		for word in range(len(line)):
			print(f"WORD : {line[word]}\t{tab if len(line[word]) <= 8 else emp}PREDICTION : {check(make_prediction(line, word).upper(), num)}")
			num += 1
		print()
		#break
	global total
	print(f"------------ TOTAL : {total} -------- ACCURACY : {round(total / num * 100, 0)}% ------------")

predictor(str(argv[1]))
