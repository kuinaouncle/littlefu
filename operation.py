from string_check import *
from api import *
from speaker import *

def operation(opcode,word):		#根据操作码来进行相应的操作
	if opcode<15 and opcode>10:
		if opcode == 11:
			syn_and_play('已经为您打开电灯')
		elif opcode == 12:
			syn_and_play('已经为您提高亮度')
		elif opcode == 13:
			syn_and_play('已经为您关闭电灯')
		elif opcode == 13:
			syn_and_play('已经为您降低亮度')
		return 0
	elif opcode>20 and opcode<25:
		if opcode == 21:
			syn_and_play('是否打开电灯')
			if ask() == 1:
				syn_and_play('已经为您打开电灯')
			else:syn_and_play('电灯')
			
			
		elif opcode == 22:
			syn_and_play('是否提高亮度')
			if ask() == 1:
				syn_and_play('已经为您提高亮度')
			else:syn_and_play('电灯')
		elif opcode == 23:
			syn_and_play('是否关闭电灯')
			if ask() == 1:
				syn_and_play('已经为您关闭电灯')
			else:syn_and_play('电灯')
		elif opcode == 24:
			syn_and_play('是否降低亮度')
			if ask() == 1:
				syn_and_play('已经为您降低亮度')
			else:syn_and_play('电灯')
		return 0
	elif opcode>30 and opcode<40:
		if opcode == 31:
			ans=turing(word)
			syn_and_play(ans)
		elif opcode == 32:
			ans=weather()
			syn_and_play(ans)
	elif opcode>40:
		if opcode == 41:
			syn_and_play('感谢使用小福,再见')
			exit()
		elif opcode == 42:
			syn_and_play('抱歉,没有听清,请再说一遍')

def ask():			#询问操作
	recording()
	reans=recognize(WAVE_OUTPUT_FILENAME)
	if '是' in reans:
		return 1
	else:return 0

def syn_and_play(text):		#语音合成播放录音
	synthesis(text)
	play(ANSWER_PATH)
