import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
engine=pyttsx3.init()
def speak(audio):
  engine.say(audio)
  engine.runAndWait()
def time():
    Time=datetime.datetime.now().strftime("%I:%H:%M")
    speak("the time is")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("the date is")
    speak(year)
    speak(month)
    speak(date)
def wishme():
    speak("hello how are you")
    time()
    date()
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("good morning")
    elif hour >=12 and hour<18:
        speak("good afternoon")
    elif hour>=18 and hour<24:
        speak("good evening")
    else:
        speak("good night")
def takecommand():
  r=sr.Recognizer()
  with sr.Microphone() as source:
     print("listening..")
     r.adjust_for_ambient_noise(source, duration=1)
     audio=r.listen(source)
  try:
      print("recognising")
      query=r.recognize_google(audio,language='en-in')
      print(query)
  except Exception as e:
      print(e)
      speak("please tell again")
      return "None"
  return query     
def sendEmail(to,content):
    server=smtplib.SMTP("stmp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("dsharanya2001@gmail.com"," ")
    server.sendmail("dsharanya2001@gmail.com",to,content)
    server.close()
def screenshot():
    img=pyautogui.screenshot()
    img.save("D:\Jarvis\ss.png")
def cpu():
    usage=str(psutil.cpu_percent())
    speak("cpu battery is"+usage)
    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(battery .percentage)
def jokes():
    speak(pyjokes.get_joke())
if __name__=="__main__":
    
    while True:
        queryy=takecommand().lower()

        if 'time' in queryy:
            time()
        elif 'date' in queryy:
            date()
        elif 'wikipedia' in queryy:
            speak("Searching..")
            queryy=queryy.replace("wikipedia","")
            result=wikipedia.summary(queryy,sentences=2)
            print(result)
            speak(result)
        elif 'send email' in queryy:
            try:
              speak("what should i say")
              content=takecommand()
              to="201810100180@presidencyuniversity.in"
              sendEmail(to,content)
              speak(content)
              speak("email is sent")
            except Exception as e: 
              print(e)
              speak("unable to send")
        elif 'search in chrome' in queryy:
            speak("what should i search?")
            chromepath='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search+ '.com' )
        elif 'logout' in queryy:
            os.system("shutdown -l")
        elif 'shutdown' in queryy:   
            os.system("shutdown /s /t 1")
        elif 'restart' in queryy:
            os.system("shutdown /r /t 1")
        elif 'play song' in queryy:
            songs_dir='D:\Music'
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif 'remember that' in queryy:
            speak("what should I remember")
            data = takecommand()
            speak("you said me to remember that" + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in queryy:    
            remember = open('data.txt','r')
            speak("you said me to remember that" + remember.read())
        elif 'screenshot' in queryy:
             screenshot()
             speak("done")
        elif 'cpu' in queryy:
             cpu()
        elif 'joke' in queryy:
            jokes()
        else:
            exit()