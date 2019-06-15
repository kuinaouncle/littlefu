from string_check import *
from api import *
from speaker import *
from operation import *

WAVE_OUTPUT_FILENAME = r"record.wav"
ANSWER_PATH=r'audio1.mp3'

def conversation():
	recording()
	try:
		recans=recognize(WAVE_OUTPUT_FILENAME)
		print("heard:"+recans)
	except BaseException as e:
		opc = 42
		operation(opc,'')
	else:
		opc = checkstring(recans)
		print("operation:"+str(opc))
		operation(opc,recans)
	

while 1:
	conversation()
