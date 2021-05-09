###------IT'S A BOT ON ARTIFICIAL INTELLIGENCE-------------####

#----Firstly we will import all the modules we need to access------
import pyttsx3                      #---its a library for text to speech conversation-----
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

'''--FIRSTLY WE HAVE TO SET A VOICE FOR OUR BOT TO SPEAK ----'''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

'''------SO WE ALREADY SET A VOICE AS ENGINE VARIABLE ,NOW WE WANT IT TO SPEAK----SO WILL DEFINE FUNCTONS-----'''
def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

'''---NOW WE DEFINE A WISHME FUNCTION SO THE BOT ALISSA WILL WISH YOU MORNING-----'''
def Wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <=12:
        Speak('Goodmorning....')
    elif hour>=12 and hour<=18:
        Speak('Good afternoon....')
    else:
        Speak('Good evening....')

'''---------NOW WE WANT OUR BOT TO TAKE COMMANDS, SO WE USE TO SET A MICROPHONE TO TAKE OUR VOICE-----'''
def takecommand():
    r = sr.Recognizer() #it's a module which helps in recognizing voice...
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=0.5   #it is used for pitch of your voice...
        audio = r.listen(source)
    try:
        # we will try to run try case for taking queries from the user...
        print('recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f'user said:{query}\n')
        '''Here try nd except case will use ,first try other wise exception will run'''
    except Exception as e:

        print('say that again please...')
        return 'None'
    return query


if __name__ == '__main__':
    Speak('Ziraa Initialising.....')
    Wishme()
    while True: #it always true to run the code
        '''logic for executing tasks based on a query...'''
        query =takecommand().lower() #incase if you use lowercase letters so it will adjust

        if 'wikipedia' in query:
            Speak('searching wikipedia...')
            query = query.replace('wikipedia', " ")
            results = wikipedia.summary(query,sentences=2)
            Speak("According to wikipedia....")
            print(results)
            Speak(results)

        if "veera" in query:
            f=open('info.txt','r')
            data=f.read()
            print(data)
            Speak(data)
            f.close()






