__ver__ = "0.0.1"
__author__ = "Eramind"
__github__ = "https://github.com/eramind/crappy-fbbot"
__contact__  = "eracnt69@outlook.com


import fbchat as fb #pip install fbchat
from fbchat.models import *
from gtts import gTTS
import urbandictionary as ud #see file urbandictionary.py for modified version
from joke.jokes import * #from pip axju-jokes
from joke.facts import *
from datetime import date
import youTube as yt #file youTube
from googletrans import Translator #mass queries can lead to ip ban 
import wiki #function for wikipedia
import mtg_search #not complete
#some web scrapers are running on html5lib which is slow,
#termux won't let me get lxml for some reason. i recommend using lxml instead.




# Subclass fbchat.Client and override required methods
class EchoBot(fb.Client):	#on_message->onMessage
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        msg = message_object
        
        if msg.text.startswith(".test"):
            msg.text="Successful!"
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
               
        elif msg.text.startswith(".poohead"): #dont judge me
            sep = msg.text.split(" ")
            name = msg.text.replace(sep[0] + " ","").capitalize()
            msg.text=name + (" is a poo poo head")
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
                
        elif msg.text.startswith(".lift"):
            sep = msg.text.split(" ")
            name = msg.text.replace(sep[0] + " ","").capitalize()
            msg.text=name + (" I bet you don't even lift faggot")
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
                
        elif msg.text.startswith(".tts"):
            sep = msg.text.split(" ")
            say = msg.text.replace(sep[0] + " ","")
            lang = 'en'
            tts = gTTS(text=say, lang=lang)
            tts.save("result.mp3")
            self.sendLocalVoiceClips("result.mp3", thread_id=thread_id, thread_type=thread_type)
                
        elif msg.text.startswith(".grabemails"): #returns your email, would not recommend using publicly
            msg.text = str(self.getEmails())
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
            
        elif msg.text.startswith(".grabinfo"): #same recommendation as above, you can delete these btw
            msg.text = str(self.fetchUserInfo())
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
            
        elif msg.text.startswith(".ud"): #urban dictionary serach
            defs = ud.define(msg.text.replace(".ud ", ""))
            msg.text = defs[0]
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
            
        elif msg.text.startswith(".bigbadbodes"):
            result = chucknorris()
            msg.text = result
            msg.text = msg.text.replace("Chuck Norris", "Big Bad Bodes")
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
            
        elif msg.text.startswith(".chuck"): #chucknorris jokes
            result = chucknorris()
            msg.text = result
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
            
        elif msg.text.startswith(".catfacts"): #self explanatory
            result = cat()
            msg.text = result
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
            
        elif msg.text.startswith(".moviestoday"): 
            d = date.today().strftime("%Y-%m-%d") #may have to reformat based on your local cinema
            msg.text = "https://www.hoyts.com.au/movies?selectedDate=" + d + "&view=list" #change this to your local cinema movie page
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
            
        elif msg.text.startswith(".bodymp3"): #template to send local audio (audio from your directory)
            self.sendLocalVoiceClips("Loud Luxury ft. Brando - Body.mp3", thread_id=thread_id, thread_type=thread_type)
            
        elif msg.text.startswith(".yt"): #youtube search
            sep = msg.text.replace(".yt ", "").split(" ")
            term = msg.text.replace(" ", "+")
            msg.text = yt.search(term)
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
            
        elif msg.text.startswith(".trans-"): #translator works for all the language codes, example: .trans-en bonjour monsier (automatically detects source language)
            sep = msg.text.split(" ")
            x = sep[0].split("-")
            lang = str(x[1])
            subject = " ".join(sep[1:])
            translator = Translator()
            result = translator.translate(subject, dest=lang)
            msg.text = result.text
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
            
            
        elif msg.text.startswith(".wiki"): #wikipedia search returns first two sentences and url to full article
            sep = msg.text.split(" ")
            term = msg.text.replace(sep[0], "")
            msg.text = wiki.searchWiki(term)
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
            
        elif msg.text.startswith(".mtg_search"): #not functional yet
            kwargs = msg.text.replace(".cardSearch ", "")
            mtg_search.card_search(kwargs)
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
            
        elif msg.text.startswith(".mtg_help"):
            msg.text = mtg_search.filters()
            self.send(msg, thread_id=thread_id, thread_type=thread_type)
           
        elif msg.text.lower().startswith(".logout"): #logs out of facebook (no login at the moment)
            self.stopListening()
            self.logout()
              
            
            
         

client = EchoBot("<Email>", "<Password>") #Enter the login for the messenger account you intend to use.
print("Own id: {}".format(client.uid))
client.listen()