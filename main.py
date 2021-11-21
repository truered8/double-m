'''
This program is for converting spoken word to text, then saving the text to a grbl file. It uses the Google Cloud Speech-To-Text API as well as the SpeechRecognition library.

TODO - send files to Arduino
'''

import speech_recognition as sr
from convert_to_grbl import convert_to_grbl

# initialize speech recognition library
r = sr.Recognizer()

while True:
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration=0.5)
		audio = r.listen(source)
		
	try:
		# pass the audio to the Google Cloud Speech-To-Text API
		result = r.recognize_google(audio)
		if result == 'stop':
			quit()
		print(result)
		convert_to_grbl(result, "result_grbl")

	except sr.UnknownValueError:
		# in this case, the API could not recognize the speech
		print('Couldn\'t recognize speech')