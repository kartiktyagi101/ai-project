import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('9AE8VP-JURKGH4XHG')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')
        
greetMe()
speak("Starting all system applications") 
speak("Installing all drivers")
speak("Examining all core processes")
speak("Hello")
speak("My name is EVA")
speak("your digital assistant") 
speak('')
strTime = datetime.datetime.now().strftime("%H:%M:%S:%p")    
speak(f"the time is {strTime}")
strtime = datetime.datetime.now().strftime("%A:%d:%B:%Y")    
speak(f"It's {strtime}")
speak('How may i help you')



def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
            
        elif 'open facebook' in query:
            speak('okay')
            webbrowser.open('www.facebook.com')
            
        elif 'open wikipedia' in query:
            speak('okay')
            webbrowser.open('www.wikipedia.com')
            
        elif 'open instagram' in query:
            speak('okay')
            webbrowser.open('www.instagram.com')
            
        elif 'open whatsapp' in query:
            speak('okay')
            webbrowser.open('www.whatsapp.com')
            
        elif 'open github' in query:
            speak('okay')
            webbrowser.open('www.github.com')
            
        elif 'open stackoverflow' in query:
            speak('okay')
            webbrowser.open('www.stackoverflow.com')

        elif 'open u m s' in query:
            speak('okay')
            webbrowser.open('https://ums.lpu.in/lpuums/')
            
        elif 'open ums' in query:
            speak('okay')
            webbrowser.open('https://ums.lpu.in/lpuums/')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'the date' in query:
            strtime = datetime.datetime.now().strftime("%A:%d:%B:%Y")    
            speak(f"It's {strtime}")

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()
            webbrowser.open('www.gmail.com')
            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')
                
                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query or 'hi' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query or 'play songs':
            speak('here select your song')
            webbrowser.open('https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhbUhuZUdJdnVBQ25XcmhMUHpkMTRRVA%3D%3D')

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
        