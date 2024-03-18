
ANSI_NORMAL = [
	'\x1b[30m',
	'\x1b[31m',
	'\x1b[32m',
	'\x1b[33m',
	'\x1b[34m',
	'\x1b[35m',
	'\x1b[36m',
	'\x1b[37m',
]
ANSI_BRIGHT = [
	'\x1b[30;1m',
	'\x1b[31;1m',
	'\x1b[32;1m',
	'\x1b[33;1m',
	'\x1b[34;1m',
	'\x1b[35;1m',
	'\x1b[36;1m',
	'\x1b[37;1m',
]
ANSI_DARK = [
	'\x1b[30;2m',
	'\x1b[31;2m',
	'\x1b[32;2m',
	'\x1b[33;2m',
	'\x1b[34;2m',
	'\x1b[35;2m',
	'\x1b[36;2m',
	'\x1b[37;2m',
]
ANSI_EXIT = '\x1b[0m'
SYMBOL = '█'

def newLine(line):
	# print("l:" + str(len(line)))
	new = ""
	for sy in line:
		if sy == ' ':
			new += sy
		elif sy != '\n':
			new += (ANSI_BRIGHT[int(sy)] + SYMBOL + ANSI_EXIT)
	return new

file = open('test.txt', 'r')
image = [newLine(line) for line in file]
file.close()

# print("r:" + str(len(image)))
# print(len(image[0]))

print()
for y in range(len(image)):
	for x in range(len(image[0])):
		print(image[y][x], end="")
	print()
print()
