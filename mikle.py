#bot Michael
# -*- coding: utf-8 -*-
import os
import sys
import time
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import random
import subprocess
from fuzzywuzzy import fuzz
import youtube_dl
#import vlc
import urllib.request
#import urllib2
#from urllib2 import urlopen
from bs4 import BeautifulSoup as soup
import smtplib
from pygame import mixer

opts = {
	"name":('майкл','миша','миха','михаил','мишаня'),
	"tbr":('расскажи мне','покажи мне','включи', 'открой', 'подруби'),
	"cmds": {
		"time":('сколько времени', 'который час','текущие время'),
		"music":('музон', 'музлишко', 'музыку', 'шарманку'),
		"joke":('анекдот', 'шутку', 'ржаку', 'прикол'),
		"google":('гугл', 'google'),
		"youtube":('youtube', 'ютуб'),
		"git":('github', 'гитхаб'),
		"mood":('шо ты', 'как дела', 'как ты', 'рассказывай как ты')
	}
}

#Функции
def speak(what):
	print( what )
	speak_engine.say( what )
	speak_engine.runAndWait()
	speak_engine.stop()

def callback(recognizer, audio):
	speak_engine = pyttsx3.init()
	try:
		voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
		print("[log] Распознано: " + voice)

		if voice.startswith(opts["name"]):
			#Обращение к Майклу
			cmd = voice

			for x in opts['name']:
				cmd = cmd.replace(x, "").strip()

			for x in opts['tbr']:
				cmd = cmd.replace(x, "").strip()

			#распознаем и делаем команды
			#cmd = " "
			cmd = recognize_cmd(cmd)
			execute_cmd(cmd['cmd'])

	except sr.UnknownValueError:
		print("[log] Голос не распознан. Попробуйте еще раз!")

	except sr.RequestError as e:
		print("[log] Нет подключения! Проверьте подключения к сети!")

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
	speak_engine = pyttsx3.init()
	if cmd == 'time':
		now = datetime.datetime.now()
		speak("Now " + str(now.hour) + ":" + str(now.minute))

	elif cmd == 'music':
		#music_folder = '#!/sh ~/programs/Music/'
		#music = ['music1', 'music2', 'music3', 'music4']
		#random_music = music_folder + random.choice(music) + '.mp3'
		#if subprocess.Popen(random_music, shell=True):
		#	speak('Okay, here is your music! Enjoy!')
		#else:
		#	speak('sorry')
		path = ('C:/Users/Grinvalera/Music/') 
		folder = path 
		for the_file in os.listdir(folder): 
			file_path = os.path.join(folder, the_file) 
		try: 
			if os.path.isfile(file_path): 
				os.unlink(file_path) 
				speak('Ок, вот ваша музыка, вперед!')
		except Exception as e: 
			print(e) 
			speak('Какую песню мне включить?') 
			cmd = recognize_cmd(cmd)
			if cmd: 
				flag = 0 
				url = "https://www.youtube.com/results?search_query=" + 'Say+say+say'
				response = urllib2.urlopen(url) 
				html = response.read() 
				soup1 = soup(html,"lxml") 
				url_list = [] 
				for vid in soup1.findAll(attrs={'class':'yt-uix-tile-link'}): 
					if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="): 
						flag = 1 
						final_url = 'https://www.youtube.com' + vid['href'] 
						url_list.append(final_url) 
						url = url_list[0] 
						ydl_opts = {} 
						os.chdir(path) 
						with youtube_dl.YoutubeDL(ydl_opts) as ydl: ydl.download([url]) 
						os.system(path)
						if flag == 0: 
							speak('I have not found anything in Youtube ') 

	elif cmd == 'google':
		speak("Открываю гугл")
		webbrowser.open("https://www.google.com/")

	elif cmd == 'youtube':
		speak('Открываю ютуб')
		webbrowser.open('https://www.youtube.com/')

	elif cmd == 'github':
		speak('Открываю гитхаб')
		webbrowser.open('https://github.com/Grinvalera')

	elif cmd == 'mood':
		mymood = ['Все хорошо!', 'Все отлично! А у тебя?', 'Прекрасно!', 'Просто класс']
		speak(random.choice(mymood))

	elif cmd == 'joke':
		myjoke = ['Рыба утонула',
				  'Русалка села на шпагат',
				  'Колобок повесился ']
		speak(random.choice(myjoke))
		speak("ха-ха-ха-ха")

#Запуск Michael
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)

#with m as source:
#    r.adjust_for_ambient_noise(source)
 
speak_engine = pyttsx3.init()

voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[9].id)

def greetMe():
	#speak_engine = pyttsx3.init()
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 6 and currentH < 12:
        speak('Доброе утро мой создатель!')

    if currentH >= 12 and currentH < 18:
        speak('Доброе день мой создатель!')

    if currentH >= 18 and currentH != 0:
        speak('Добрый вечер мой создатель')

    if currentH >= 0 and currentH < 6:
    	speak('Доброй ночи мой создатель!')

greetMe()

speak("Миша слушает")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.3)