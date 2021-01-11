import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import datetime


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[10].id)
languages=['en_US']
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command() :   
    try:
        with sr.Microphone() as source:
            print("listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace("alexa",'')
                print(command)
    except:
        pass
    return command 

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk("playing" + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M %p")
        print(time)
        talk ("Current time is " + time)
        
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    elif "send message" in command :
        pywhatkit.sendwhatmsg("+918279219943", "Hello from Navendra",16, 39) 
        print("Successfully Sent!")
    elif 'how are you ' in command:
        talk('I am good how about you')
        
    elif'i am good' in command:
        talk ("how can i do for you ")
    
    elif "search" in command :
        person = command.replace('search' , '')
        info = pywhatkit.search(person)
        print(info)
        talk(info)    
    else:
        talk('Please say the command again.')
        
