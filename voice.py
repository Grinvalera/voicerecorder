import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone(device_index=6) as source:
	print("say anyway")
	audio = r.listen(source)

query = r.recognize_google(audio, language="ru-RU")
print("You say: " + query.lower())