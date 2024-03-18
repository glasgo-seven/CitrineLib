import le_speaker as speaker

# TEXT FORMATTING EXAMPLE
# Sub_Line test...$Completed!
# Line@I am a simple line!@bright_yellow
# &Line is blushing
# 	I want home.
# 	Who are you?
# 	Get lost!
# 	%You@green
# #Line@You can go now.@bright_yellow
# #Line@I am The Line! Nice to meet you.@bright_yellow
# #Line@Don't be so rude...@bright_yellow
# &Line vanished into thin air

def im_sub_line(line):
	_line = line.split('$')
	if len(_line) != 1:
		speaker.line(_line[0])
		speaker.sub_line(_line[1])
		return 1
	else:
		return 0

def im_phrase(line):
	_line = line.split('@')
	if len(_line) != 1:
		speaker.phrase(_line[0], _line[1], _line[2])
		return 1
	else:
		return 0

def im_emote(line):
	_line = line.split('&')
	if len(_line) != 1:
		speaker.emote(_line[1])
		return 1
	else:
		return 0

def input_manager(file_name):
	f = open('./chapters/' + file_name)
	choice = list()
	ans = 0
	for line in f:
		line = line.split('\n')[0]
		if ans > 1:
			ans -= 1
		elif ans == 1 and line[0] == '#':
			line = line.split('#')[1]
			ans = 0
		if ans == 0 and line[0] == '#':
			pass
		elif line[0] != '#':
			if line[0] == '\t':
				if line[1] == '%':
					line = line.split('%')[1].split('@')
					ans = speaker.answer_handler(choice)
					speaker.phrase(line[0], ans[1], line[1])
					ans = ans[0]
					choice.clear()
				else:
					choice.append(line.split('\t')[1])
			elif not (im_sub_line(line) or im_phrase(line) or im_emote(line)):
				speaker.line(line)
