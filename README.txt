!IF YOU USING WINDOWS!
1)pip install pywin
2)pip install pypiwin32
3)pip install pyttsx3
4)pip install SpeechRecognition
5)pip install PyAudio
	If you are having trouble installing PyAudio:
	1.Download the assembled package - https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
	2.cd <your_donwload_path>
	3.pip install PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl
6)pip install fuzzywuzzy==0.3.0
7)Enter this code to test your microphone
	import speech_recognition as sr
	for index, name in enumerate(sr.Microphone.list_microphone_names()):
    	print("Microphone with name \"{1}\" found for 						`Microphone(device_index={0})`".format(index, name))
8)Choose your microphone index
	Microphone(device_index={0})
9)Congratulations! You have completed the installation
!IF YOU USING LINUX/UBUNTU!
1)pip install pyttsx3
2)pip install SpeechRecognition
3)pip install PyAudio
4)pip install fuzzywuzzy==0.3.0
5)Enter this code to test your microphone
	import speech_recognition as sr
	for index, name in enumerate(sr.Microphone.list_microphone_names()):
    	print("Microphone with name \"{1}\" found for 						`Microphone(device_index={0})`".format(index, name))
6)Choose your microphone index
	Microphone(device_index={0})
7)Congratulations! You have completed the installation
