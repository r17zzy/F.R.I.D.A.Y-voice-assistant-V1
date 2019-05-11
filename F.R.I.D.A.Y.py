# Created by <------------Prerit Rathi--------------------->
# Dated 22/5/18.
# description:  F.R.I.D.A.Y. Simulation through GTTS(Google_Text_To_Speech) API



#======================IMPORTING REQUIRED LIBRARIES:=======================================


from gtts import gTTS
from time import ctime
import speech_recognition as sr
import smtplib
import os
import webbrowser as wb





#===========================INITIATION FUNCTIONS====================================

def Initiation(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123.mp3')
    



def my_order():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/Chrome.exe %s'
    r = sr.Recognizer()

    with sr.Microphone()as source:
        print("anything I could open or search for you?\n")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration = 1)
        audio = r.listen(source)
        
    try:
        text = r.recognize_google(audio)
        print('I think you said:\n' + text+"\n")

        f_text = ('https://www.google.co.in/search?q='+ text)

        
        if (".com") in text:
            wb.get(chrome_path).open(text)

        else:
            wb.get(chrome_path).open(f_text)

        

            
            
        


    except Exception as ex:
        print(ex)

    
	


#==========================================================================================================




print ("... \n")

    
  
    
        
	




#==================================================================================================

Initiation(" Hello sir I am now online , please wait for a moment till I initiate me on the cloud servers")

while True:
	my_order()




