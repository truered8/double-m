import speech_recognition as sr

r = sr.Recognizer()

while True:
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration=0.5)
		audio = r.listen(source)
        
	try:
		result = r.recognize_google(audio)
		if result == 'stop':
			quit()
		print(result)
		words = result.split(' ')
		chars = 0
		row = 0
	except sr.UnknownValueError:
		print('Couldn\'t recognize speech')