from enum import Enum

def clear_console() -> None :
	"""
	Deletes all lines from console.

	Удаляет все строки из консоли. 
	"""
	from os import system, name
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def clear_screen() -> None :
	"""
	Deletes only visible lines from console.
	
	Удаляет только видимые строки из консоли.
	"""
	print('\x1b[H\x1b[3J', end='')
	print('\n'*64)
	print('\x1b[H\x1b[3J', end='')


class Color(Enum):
	RESET_COLOR	:	str	=	'0'

#	Цвета текста
class FOREGROUND_COLOR(Color):
	BLACK	:	str	=	'30'
	RED		:	str	=	'31'
	GREEN	:	str	=	'32'
	YELLOW	:	str	=	'33'
	BLUE	:	str	=	'34'
	PURPLE	:	str	=	'35'
	CYAN	:	str	=	'36'
	WHITE	:	str	=	'37'
	STRONG_BLACK	:	str	=	'90'
	STRONG_RED		:	str	=	'91'
	STRONG_GREEN	:	str	=	'92'
	STRONG_YELLOW	:	str	=	'93'
	STRONG_BLUE		:	str	=	'94'
	STRONG_PURPLE	:	str	=	'95'
	STRONG_CYAN		:	str	=	'96'
	STRONG_WHITE	:	str	=	'97'

#	Цвета фона
class BACKGROUND_COLOR(Color):
	BLACK	:	str	=	'40'
	RED		:	str	=	'41'
	GREEN	:	str	=	'42'
	YELLOW	:	str	=	'43'
	BLUE	:	str	=	'44'
	PURPLE	:	str	=	'45'
	CYAN	:	str	=	'46'
	WHITE	:	str	=	'47'
	STRONG_BLACK	:	str	=	'100'
	STRONG_RED		:	str	=	'101'
	STRONG_GREEN	:	str	=	'102'
	STRONG_YELLOW	:	str	=	'103'
	STRONG_BLUE		:	str	=	'104'
	STRONG_PURPLE	:	str	=	'105'
	STRONG_CYAN		:	str	=	'106'
	STRONG_WHITE	:	str	=	'107'


DEFAULT_PREFIX_ALERT		:	str	=	'[ALERT]'
DEFAULT_PREFIX_ERROR		:	str	=	'[ERROR]'
DEFAULT_PREFIX_NOTIFICATION	:	str	=	'[NOTIFICATION]'




def set_color(_fg: Color = None, _bg: Color = None) -> None:
	"""
	Sets the colors of text and background.

	Устанавливает выбранные коды цветов для текста и фона.
	"""
	if _fg:
		print(f"\x1b[{_fg.value}m", end='')
	if _bg:
		print(f"\x1b[{_bg.value}m", end='')

def reset_color() -> None:
	"""
	Resets text color and background to default (white text, black background).
	"""
	print(f"\x1b[{Color.RESET_COLOR}m", end='')



def colored(*_msgs: tuple[str], _fg: Color = None, _bg: Color = None, _sep: str = ' ', _end: str = '\n') -> None:
	"""
	Prints colored text as set ForeGround and BackGround.
	"""
	set_color(_fg, _bg)
	print(*_msgs, sep=_sep, end=_end)
	reset_color()

def as_colored(_text: str, _fg: Color = None, _bg: Color = None) -> str :
	"""
	Returns colored text as set ForeGround and BackGround.
	"""
	return f"\x1b[{_fg};{_bg}m{_text}\x1b[0m"


def __error(_msg: str) -> None :
	print(f"\x1b[{FOREGROUND_COLOR.RED}m{_msg}\x1b[0m")

def error(*_msgs: tuple[str]) -> None:
	colored(*_msgs, _fg=FOREGROUND_COLOR.STRONG_RED)

def as_error(_text: str) -> str :
	return as_colored(_text, _fg=FOREGROUND_COLOR.STRONG_RED)

def custom_error(*_msgs : tuple[str], _prefix: str = DEFAULT_PREFIX_ERROR, _sep: str = ' ', _end: str = '\n') -> None:
	colored(*(_prefix, *_msgs), _fg=FOREGROUND_COLOR.STRONG_RED, _sep=_sep, _end=_end)


def __alert(_msg: str) -> None :
	print(f"\x1b[{FOREGROUND_COLOR.YELLOW}m{_msg}\x1b[0m")

def alert(*_msgs: tuple[str]) -> None:
	colored(*_msgs, _fg=FOREGROUND_COLOR.STRONG_YELLOW)

def as_alert(_text: str) -> str :
	return as_colored(_text, _fg=FOREGROUND_COLOR.STRONG_YELLOW)

def custom_alert(*_msgs : tuple[str], _prefix: str = DEFAULT_PREFIX_ALERT, _sep: str = ' ', _end: str = '\n') -> None:
	colored(*(_prefix, *_msgs), _fg=FOREGROUND_COLOR.STRONG_YELLOW, _sep=_sep, _end=_end)


def __notification(_msg: str) -> None :
	print(f"\x1b[{FOREGROUND_COLOR.GREEN}m{_msg}\x1b[0m")

def notification(*_msgs: tuple[str]) -> None:
	colored(*_msgs, _fg=FOREGROUND_COLOR.STRONG_GREEN)

def as_notification(_text: str) -> str :
	return as_colored(_text, _fg=FOREGROUND_COLOR.STRONG_GREEN)

def custom_notification(*_msgs : tuple[str], _prefix: str = DEFAULT_PREFIX_NOTIFICATION, _sep: str = ' ', _end: str = '\n') -> None:
	colored(*(_prefix, *_msgs), _fg=FOREGROUND_COLOR.STRONG_GREEN, _sep=_sep, _end=_end)



if __name__ == '__main__':
	abc = "[123]"
	x = [1, 2, 3, 4, 5]

	alert(x)
	error(x)
	notification(x)

	custom_error(x, 'abc')
	custom_error(x, 'abc', _prefix=abc)
	custom_alert(x, 'abc')
	custom_alert(x, 'abc', _prefix=abc)
	custom_notification(x, 'abc')
	custom_notification(x, 'abc', _prefix=abc)
