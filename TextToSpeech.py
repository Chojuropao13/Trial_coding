import pyttsx3

data = input("masukan kata-kata yang ingin diucapkan : \n")
engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()