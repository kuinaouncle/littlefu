import urllib
import json
import requests
from aip import AipSpeech

WAVE_OUTPUT_FILENAME = r"record.wav"
ANSWER_PATH=r'audio1.mp3'

APP_ID = '15768502'
API_KEY = '9P8fb2GNI4ulXDjUHNSqEHGh'
SECRET_KEY = '67d0K5WllwYuNG48V6w7OPDnl3dpf3My'
tulingurl='http://openapi.tuling123.com/openapi/api/v2'
weatherurl='https://api.seniverse.com/v3/weather/now.json?key=S-_4jhdD2MCKbhIYV&location=fuzhou&language=zh-Hans&unit=c'

aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read()
		
def recognize(filepath):	#语音识别函数，返回识别后的字符串
	result = aipSpeech.asr(get_file_content(filepath), 'wav', 16000, {
	'dev_pid': 1536,
	})
	return result['result'][0]
	
def synthesis(text):		#语音合成
	result  = aipSpeech.synthesis(text, 'zh', 1, {
		'vol': 5,
		'per': 4,
	})

	# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
	if not isinstance(result, dict):
		with open(ANSWER_PATH, 'wb') as f:
			f.write(result)
			
def turing(text):			#图灵回答
	data ={
		"reqType":0,
		"perception": {
			"inputText": {
				"text": text
			}
		},
		"userInfo": {
			"apiKey": "5f8beddc4e0f4cb0976768149cb88103",
			"userId": "400646"
		}
	}
	# values = urllib.parse.urlencode(data).encode(encoding='UTF8')
	headers = {'Content-Type': 'application/json'}
	request = urllib.request.Request(url=tulingurl, headers=headers, data=json.dumps(data).encode())
	response = urllib.request.urlopen(request)
	responsedict=json.loads(response.read().decode())
	ans =responsedict['results'][0]['values']['text']
	return ans

def weather():
	r = requests.get(weatherurl)
	json = r.json()
	weather = json['results'][0]['now']['text']
	temperature = json['results'][0]['now']['temperature']
	ans='福州今天'+weather+'，温度是'+temperature+'摄氏度'
	print(ans)
	return ans
