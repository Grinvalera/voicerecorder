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
import opts
import youtube_dl
import vlc
import urllib2
from bs4 import BeautifulSoup as soup
import urllib
import smtplib
from pygame import mixer

opts = {
	"name":('Michael','Micle','Misha'),
	"tbr":('tell me','show me','turn on', 'open'),
	"cmds": {
		"time":('what time is it now', 'current time'),
		"music":('music', 'open music'),
		"mem":('show meme', 'show picture'),
		"joke":('joke', 'anecdote'),
		"google":('google', 'doogle', 'gle'),
		"youtube":('youtube', 'youtabe'),
		"git":('github', 'git'),
		"mood":('how are you?', 'whats up?', 'how do you feel')
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
			#cmd = " "
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
		#music_folder = '#!/sh ~/programs/Music/'
		#music = ['music1', 'music2', 'music3', 'music4']
		#random_music = music_folder + random.choice(music) + '.mp3'
		#if subprocess.Popen(random_music, shell=True):
		#	speak('Okay, here is your music! Enjoy!')
		#else:
		#	speak('sorry')
		path = vlc.MediaPlayer('/home/valeriy/programs/Music') 
		folder = path 
		#for the_file in os.listdir(folder): 
		#	player = vlc.MediaPlayer(the_file)
		#	file_path = os.path.join(folder, the_file) 
		try: 
			if os.path.isfile(file_path): 
				os.unlink(file_path) 
				player.play()
				speak('Okay, here is your music! Enjoy!')
		except Exception as e: 
			print(e) 
			speak('What song shall I play Sir?') 
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
						path.play()
						with youtube_dl.YoutubeDL(ydl_opts) as ydl: ydl.download([url]) 
						play() 
						if flag == 0: 
							speak('I have not found anything in Youtube ') 

	elif cmd == 'google':
		speak("Opened google")
		webbrowser.open("https://www.google.com/")

	elif cmd == 'youtube':
		speak('Opened youtube')
		webbrowser.open('https://www.youtube.com/')

	elif cmd == 'github':
		speak('Opended github')
		webbrowser.open('https://github.com/Grinvalera')

	elif cmd == 'mood':
		mymood = ['Things are good', 'All perfectly', 'Nice!', 'I m nice']
		speak(random.choice(mymood))

	elif cmd == 'joke':
		myjoke = ['the fish drowned',
				  'the mermaid sat on the twine',
				  'gingerbread man hanged himself']
		speak(random.choice(myjoke))
		speak('ha-ha-ha-ha-ha')

#Запуск Michael
r = sr.Recognizer()
m = sr.Microphone(device_index = 6)
 
speak_engine = pyttsx3.init()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 6 and currentH < 12:
        speak('Good Morning! My creator!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon! My creator!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening! My creator!')

    if currentH >= 0 and currentH < 6:
    	speak('Good Night! My creator!')

greetMe()

speak("Michael listening to")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.5)