import pyaudio
import wave
import time
import os
import sys

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = r"record.wav"
ANSWER_PATH=r'audio1.mp3'
RECORD_STRAT_MUSIC=r'ding.wav'
RECORD_END_MUSIC=r'dong.wav'

def recording():		#录音函数，生成wav文件
	p = pyaudio.PyAudio()
	
	os.system('mplayer %s' % RECORD_STRAT_MUSIC)
	time.sleep(0.2)
	
	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)

	print("recording...")
	
	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)

	
	print("done")

	stream.stop_stream()
	stream.close()
	p.terminate()
	
	os.system('mplayer %s' % RECORD_END_MUSIC)
	time.sleep(0.2)

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

def play(filepath):			#播放录音
	os.system('mplayer %s' % filepath)
	time.sleep(1)
