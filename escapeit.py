import speech_recognition as sr  
from pynput.keyboard import Key, Controller

r = sr.Recognizer()
Keyboard = Controller()

while True:              
    with sr.Microphone() as source: 
        print("Say escape : ")
        audio = r.listen(source)     
        try:
            text = r.recognize_google(audio)    
            print("{}".format(text))
            if 'escape' in text:
                Keyboard.press(Key.esc)
                Keyboard.release(Key.esc)

        except:
            print("Sorry could not recognize your voice")   