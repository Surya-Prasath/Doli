from gtts import gTTS
import beta
import playsound
import speech_recognition as sr
from mutagen.mp3 import MP3
from rasp import hand,mouth
from threading import Thread
from os import system
#from pyctrl import hi,talk

r = sr.Recognizer()
path = "ED-Doll-Audio/"
extension = ".mp3"
mode = "on"
waitTime = 0
song = ""

def talkSong():
	mouth(int(MP3(song).info.length))

def talkOutput():
	mouth(int(MP3("output.wav").info.length))

def wakeup(text):
	if "dhoni" in text or "darling" in text or "duri" in text or "idli" in text or "dori" in text or "dali" in text or "dol" in text:
		return True
	else:
		return False
	

def listening():
	with sr.Microphone() as source:
		audio = r.listen(source, phrase_time_limit=3)
		with open('speech.wav','wb') as f:
			f.write(audio.get_wav_data())
		try:
			text = r.recognize_google(audio).lower()
			print("[-] You Said : {}".format(text))	
			return text						
		except:
			#print("Sorry could not recognize what you said")
			return ' '
			
def sending(text):
	global song
	replyText = beta.req(text)
	if replyText[-1]=="&":
		if replyText[0]=="1":
			replyText=replyText[1:]
			#hi()
			print("hi")
			hand()
		ttf = " ".join(replyText[:-1].split()[:-1])
		if ttf!="":
			print(ttf)
			gTTS(ttf).save("output.wav")
			#talk(audio_open("output.wav").duration)
			Thread(target=talkOutput).start()
			playsound.playsound("output.wav")
		song = path+(replyText[:-1].split()[-1])+extension
		#talk(audio_open(song).duration)
		Thread(target=talkSong).start()
		playsound.playsound(song)
	
	else:
		if replyText[0]=="1":
			replyText=replyText[1:]
			#hi()
			hand()
		print(replyText)
		gTTS(replyText).save("output.wav")
		#talk(audio_open("output.wav").duration)
		Thread(target=talkOutput).start()
		playsound.playsound("output.wav")
		
while mode in ["on", "listen"]:	
	text = listening()	
	if text in ["nevermind", "never mind"]:
		mode="on"
		waitTime=0
		print("[+]----------------------Passive Listening Mode----------------------[+]")
	elif text != ' ':
		if mode == "listen":
			sending(text)
			waitTime=0
		elif "dhoni" in text or "darling" in text or "duri" in text or "idli" in text or "dori" in text or "dali" in text or "dol" in text:
			mode="listen"
			waitTime=0
			print("[+]----------------------Active Listening Mode Triggered----------------------[+]")
	else:
		if(waitTime==8 and mode=="listen"): 
			mode="on"
			waitTime=0
			print("[+]----------------------Passive Listening Mode----------------------[+]")
		print("[-] == Idle Count: == ", waitTime)
		waitTime+=1
