from googletrans import Translator
from googletrans import LANGUAGES
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, Clock, ObjectProperty, StringProperty
import speech_recognition as sr 


class MainWidget(BoxLayout):

    translator = Translator()
    
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
    
    def detect_lang(self, text):
        language = self.translator.detect(text)
        return LANGUAGES[language.lang]
    
    def convert_lang(self, text):
        translated = self.translator.translate(text)
        return translated.text
            
    def on_button_press(self):
        text = self.ids.input.text
        self.ids.l.text = text + " in language: " + self.detect_lang(text)
        print(self.convert_lang(text))
    
    def speach_to_text(self):
        rObject = sr.Recognizer()
        audio = ''
  
        with sr.Microphone() as source:
            print("Speak...")
          
            # recording the audio using speech recognition
            audio = rObject.listen(source) 
            #print("Stop.") # limit 5 secs
  
        try:
  
            text = rObject.recognize_google(audio, language ='en-US')
            print("You : ", text)
            return text
  
        except:
  
            print("Could not understand your audio, PLease try again !")
            return 0
    
    
class TranslatorApp(App):
    pass

TranslatorApp().run()