#bot Миша
# -*- coding: utf-8 -*-
import os
import time
import speech_recognition as sr
import pyttsx3
import random
import datetime
import webbrowser
import subprocess
import urllib
import re
import base64
import youtube_dl
import googletrans
import pyautogui as auto

from bs4 import BeautifulSoup as soup
from fuzzywuzzy import fuzz
from urllib.request import urlopen
from googletrans import Translator


opts = {
	"name":('майкл','миша','миха','михаил','мишаня'),
	"tbr":('покажи мне','включи', 'открой', 'подруби', 'расскажи', 'найди', 'переведи'),
	"cmds": {
		"time":('сколько времени', 'который час','текущие время'),
		"radio":('радио', 'шарманку'),
		"joke":('анекдот', 'шутку', 'ржаку', 'прикол'),
		"google":('информацию в гугле', 'google'),
		"youtube":('youtube', 'ютуб'),
		"git":('github', 'гитхаб'),
		"mood":('шо ты', 'как дела', 'как ты', 'рассказывай как ты'),
		"news":('новости', 'известия', 'события'),
		"music":('музыку', 'музон', 'мелодию'),
		"translate":('слово', 'фразу', 'текст'),
		"bye":('пока', 'бай', 'до встречи')
	}
}

#Функции
def speak(what):
	speak_engine = pyttsx3.init()
	#Только если у вас стоит RHVoice
	voices = speak_engine.getProperty('voices')
	speak_engine.setProperty('voice', voices[10].id)
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
			#Обращение к Мише
			cmd = voice

			for x in opts['name']:
				cmd = cmd.replace(x, "").strip()

			for x in opts['tbr']:
				cmd = cmd.replace(x, "").strip()

			#распознаем и делаем команды
			cmd = recognize_cmd(cmd)
			execute_cmd(cmd['cmd'])

	except sr.UnknownValueError:
		print("[log] Голос не распознан. Попробуйте еще раз!")

	except sr.RequestError as e:
		print("[log] Нет подключения! Проверьте подключения к сети!")

def recognize_cmd(cmd):
	#Сравниваем нечеткий ввод с помощью библиотеки fuzzywuzzy
	RC = {'cmd': '', 'percent': 0}
	for c,v in opts['cmds'].items():

		for x in v:
			vrt = fuzz.ratio(cmd, x)
			if vrt > RC['percent']:
				RC['cmd'] = c
				RC['percent'] = vrt

	return RC

#Команды для Миши
def execute_cmd(cmd):
	if cmd == 'time':
		now = datetime.datetime.now()
		speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

	elif cmd == 'radio':
		music_folder = 'C:/Users/Grinvalera/Python/voicerecorder/radio/radio_ua.m3u'
		os.system(music_folder)
		
	elif cmd == 'google':
		speak('Какую информацию мне искать?') 
		r = sr.Recognizer()
		with sr.Microphone(device_index=1) as source:
			audio = r.listen(source)

		query = r.recognize_google(audio, language="ru-RU")
		info = query.lower()
		webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=" + info)
		speak("Открываю гугл")
		

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
		mydarkjoke = ['Шутки про утопленников обычно несмешные, потому что лежат на поверхности.',
						'У семьи каннибалов умер родственник. И грустно и вкусно.',
						'Как быстрее всего прекратить спор глухих? — Выключить свет.',
						'Акробат умер на батуте, но еще какое-то время продолжал радовать публику.',
						'Мужик имел лошадь, а лошадь ничего не имела против.',
						'Блоха голосовала на дороге. Хоть бы одна собака остановилась.',
						'При аварии машин ФСБ и ФСО правила нарушились сами.',
						'Ничто так не мешает радоваться жизни, как сама жизнь.']
		speak(random.choice(mydarkjoke))

	elif cmd == 'news':
		news_url="https://news.google.com/rss?hl=ru&gl=UA&ceid=UA:ru"  
		Client=urlopen(news_url) 
		xml_page=Client.read() 
		Client.close() 
		soup_page=soup(xml_page,"xml") 
		news_list=soup_page.findAll("item")
		for news in news_list[:5]: 
			speak(news.title.text)

	elif cmd == 'music':
		speak('Какую песню мне включить?') 
		r = sr.Recognizer()
		with sr.Microphone(device_index=1) as source:
			audio = r.listen(source)

		query = r.recognize_google(audio, language="ru-RU")
		mus = query.lower()
		webbrowser.open('https://music.youtube.com/search?q=' + mus)
		auto.sleep(3)
		auto.click(460, 368)

	elif cmd == 'translate':
		speak('Говорите фразу на русском языке')
		r = sr.Recognizer()
		with sr.Microphone(device_index=1) as source:
			audio = r.listen(source)

		query = r.recognize_google(audio, language="ru-RU")
		trans = query.lower()
		print(trans)

		translator = Translator()
		result = translator.translate(trans, dest='en')
		result1 = translator.translate(trans, dest='uk')
		result2 = translator.translate(trans, dest='german')		
		speak(result.text)
		speak(result1.text)
		speak(result2.text)

	elif cmd == 'bye':
		speak("До скорых встреч, хозяин!")
		exit()

#Запуск Миши
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)

with m as source:
    r.adjust_for_ambient_noise(source)

def greetMe():
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
while True: time.sleep(0.1)

