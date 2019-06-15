#string_check.py
OPERATION_CODE=[0,11,12,13,14,21,22,23,24,31,32,41]	#操作码

DIR_OPEN_WORD=['打开电灯','开灯']					#直接操作11
DIR_BRIGHT_WORD=['提高亮度','亮一点']				#12
DIR_CLOSE_WORD=['关闭电灯','关灯']				#13
DIR_DARK_WORD=['降低亮度','暗一点']					#14

ASK_OPEN_WORD=['灯','打开','有点暗']				#询问操作21
ASK_BRIGHT_WORD=['亮','变亮']					#22
ASK_CLOSE_WORD=['关','不要']						#23
ASK_DARK_WORD=[]								#24

WEATHER_WORD=['天气','温度']						#32

QUIT_WORD=['退出','结束','再见']					#41

intext=['现在有点暗','请打开电灯','关灯','请降低亮度','在？开开灯？']
def checkstring(text):
	oprcode=0
	for word in QUIT_WORD:
		if word in text:
			oprcode=41
			return oprcode
	for word in DIR_OPEN_WORD:
		if word in text:
			oprcode=11
			return oprcode
	for word in DIR_BRIGHT_WORD:
		if word in text:
			oprcode=12
			return oprcode
	for word in DIR_CLOSE_WORD:
		if word in text:
			oprcode=13
			return oprcode
	for word in DIR_DARK_WORD:
		if word in text:
			oprcode=14
			return oprcode
	for word in ASK_OPEN_WORD:
		if word in text:
			oprcode=21
			return oprcode
	for word in ASK_BRIGHT_WORD:
		if word in text:
			oprcode=22
			return oprcode
	for word in ASK_CLOSE_WORD:
		if word in text:
			oprcode=23
			return oprcode
	for word in ASK_DARK_WORD:
		if word in text:
			oprcode=24
			return oprcode
	for word in WEATHER_WORD:
		if word in text:
			oprcode=32
			return oprcode
	oprcode=31
	return oprcode
