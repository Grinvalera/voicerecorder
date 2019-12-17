#bot Michael
# -*- coding: utf-8 -*-
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import webbrowser
import random
import subprocess


opts = {
	"name":('Michael','Micle','Misha'),
	"tbr":('tell me','show me','turn on', 'open'),
	"cmds": {
		"time":('what time is it now', 'current time'),
		"music":('music', 'open music'),
		"mem":('show meme', 'show picture'),
		"joke":('joke'),
		"google":('google', 'doogle', 'gle'),
		"youtube":('youtube', 'youtabe'),
		"git":('github', 'git'),
	}
}

#Функции
def speak(what):
	print( what )
	speak_engine.say( what )
	speak_engine.runAndWait()
	speak_engine.stop()

def callback(recognizer, audio):
	try:
		voice = recognizer.recognize_google(audio)
		print("[log] Recognized: " + voice)

		if voice.startswith(opts["name"]):
			#Обращение к Майклу
			cmd = voice

			for x in opts['name']:
				cmd = cmd.replace(x, "").strip()

			for x in opts['tbr']:
				cmd = cmd.replace(x, "").strip()

			#распознаем и делаем команды
			cmd = recognize_cmd(cmd)
			execute_cmd(cmd['cmd'])

	except sr.UnknownValueError:
		print("[log] voice not recognized")

	except sr.RequestError as e:
		print("[log] Unknown error! Сheck Internet")

def recognize_cmd(cmd):
	#Сравниваем нечеткий ввод с помощью библеотеки fuzzywuzzy
	RC = {'cmd': '', 'percent': 0}
	for c,v in opts['cmds'].items():

		for x in v:
			vrt = fuzz.ratio(cmd, x)
			if vrt > RC['percent']:
				RC['cmd'] = c
				RC['percent'] = vrt

	return RC

def execute_cmd(cmd):
	if cmd == 'time':
		now = datetime.datetime.now()
		speak("Now " + str(now.hour) + ":" + str(now.minute))

	elif cmd == 'music':
		music_folder = '#!/sh ~/programs/Music/'
		music = ['music1', 'music2', 'music3', 'music4']
		random_music = music_folder + random.choice(music) + '.mp3'
		if subprocess.Popen(random_music, shell=True):
			speak('Okay, here is your music! Enjoy!')
		else:
			speak('sorry')

	elif cmd == 'google':
		speak("Opened google")
		webbrowser.open("https://www.google.com/")

	elif cmd == 'youtube':
		speak('Opened youtube')
		webbrowser.open('https://www.youtube.com/')

	elif cmd == 'github':
		speak('Opended github')
		webbrowser.open('https://github.com/Grinvalera')




#Запуск Michael
r = sr.Recognizer()
m = sr.Microphone(device_index = 6)
 
speak_engine = pyttsx3.init()

speak("Hello, my creator! How are you?")
speak("You need help?")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)