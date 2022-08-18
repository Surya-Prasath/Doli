from gtts import gTTS
import beta
import playsound
import speech_recognition as sr
import mutagen

r = sr.Recognizer()
path = "/home/candy/Downloads/ed/ED-Doll-Audio/"
extension = ".mp3"
mode = "on"
waitTime = 0

def hi():
	print("hi 1")
	
def talk(duration):
	print("talk 2", duration)
	
def wakeup(text):
	if "doli" in text or "dolly" in text or "dhoni" in text or "darling" in text or "duri" in text or "idli" in text or "dori" in text or "dali" in text:
		return True
	else:
		return False
	

def listening():
	with sr.Microphone() as source:
		audio = r.listen(source, phrase_time_limit=2)
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
	replyText = beta.req(text)
	if replyText[-1]=="&":
		if replyText[0]=="1":
			replyText=replyText[1:]
			hi()
		ttf = " ".join(replyText[:-1].split()[:-1])
		if ttf!="":
			gTTS(ttf).save("output")
			talk(WAVE("output").info.length)
			playsound.playsound("output")
		song = path+(replyText[:-1].split()[-1])+extension
		talk(WAVE(song).info.length)
		playsound.playsound(song)
	else:
		if replyText[0]=="1":
			replyText=replyText[1:]
			hi()
		gTTS(replyText).save("output")
		talk(WAVE("output").info.length)
		playsound.playsound("output")
		
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
		elif "doli" in text or "dolly" in text or "dhoni" in text or "darling" in text or "duri" in text or "idli" in text or "dali" in text:
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
