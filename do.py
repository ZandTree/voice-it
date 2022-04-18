import pyttsx3 as pyt
from gtts import gTTS



# engine = pyt.init()
# engine.say("I will speak this text")
# engine.runAndWait()
# print("done")

class MakeVoice:
    def __init__(self,path) -> None:
        self.engine = pyt.init()
        with open(path,"r") as fh:
            self.file = fh.read()

    def say(self):
        """ voice -> text"""
        self.engine.say(self.file)    
        self.engine.runAndWait()    

    def save(self,filename):
        """ filename .mp3"""
        tts = gTTS(text = self.file,lang="es")    
        tts.save(filename)

MakeVoice("src_es.txt").say()        