#bot Ivan
# -*- coding: utf-8 -*-
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime


opts = {
	"name":('Иван','Ваня','Ванечка','Ванька',
			'Вано','Виня'),
	"tbr":('скажи', 'проясни', 'покажи', 'расскажи', 'включи'),
	"cmd": {
		"time":('Который час', 'Сколько время', 'Текущее время'),
		"music":('Включи музыку', 'Подруби музон', 'Врубай шарманку'),
		"mem":('Дай поорать', 'Покажи картинку', 'Кинь годноту'),
	}
}

#Функции
def speak(what):
	print( what )
	speak_engine.say( what )
	speak_engine.runAndWait()
	speak_engine.stop()

def callback(recognizer, audio):
	pass

def recognizer_cmd(cmd):
	pass

def execute_cmd(cmd):
	pass

#Запуск Вани
r = sr.Recognizer()
m = sr.Microphone(device_index = 6)

#with m as source:
	#r.abjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

#voices = speak.engine.getProperty('voices')
#speak_engine.setProperty('voice', voices[2].id)

speak("Hello")
speak("Vanya na svyazi")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)