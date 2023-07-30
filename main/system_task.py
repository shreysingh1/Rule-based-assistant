import time
from playsound import playsound
from datetime import datetime
import speak_module
from input_module import take_input
from output_module import output
import os
from os.path import isfile, join
import time
import ctypes
import random

def set_alarm():
    output("It is based on 24 hours clock format...")
    # printing the current time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("current_time is : "+current_time)
    # Enter the time(Hours and minute)
    output("Tell the Hour and minute")
    Time= take_input()
    # starting the loop
    while True:
        # Getting the standard time with the
        # help of datetime module
        Standard_time=datetime.now().strftime("%H:%M")
        # sleep the program for about 1 sec
        time.sleep(1)
        # if condition to check wether the input
        # time has matched or not
        if Time==Standard_time:
            count=0
            while count<=2:
                count=count+1
                speak_module.speak("time to wake up sir")
                playsound("C:/Users/shrey/downloads/clock.wav")
            return "alarm executed"



def wallpaper():
    path = r"D:\pythonProject\wallpapers"
    allfile = [f for f in os.listdir(path) if isfile(join(path, f))]
    for image in allfile:
        image = random.choice(allfile)
        # print(image)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path + "\\" + image, 0)
        time.sleep(3)
        return "wallpaper changed"

def excel():
    speak_module.speak("Here You go with MS Excel")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
    return "Opening MS excel"

def close_excel():
    speak_module.speak("closing ms excel")
    browserExe = "EXCEL.EXE"
    os.system("taskkill /f /im " + browserExe)
    return ("MS excel closed")

def powerpoint():
    speak_module.speak("Here You go with MS Powerpoint")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
    return ("Opening MS powerpoint")

def close_powerpoint():
    speak_module.speak("Closing MS powerpoint")
    browserExe= "POWERPNT.EXE"
    os.system("taskkill /f /im " + browserExe)
    return ("MS powerpoint closed")

def word():
    speak_module.speak("Here you go with MS word")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
    return ("Opening MS word")

def close_word():
    speak_module.speak("closing MS word")
    browserExe="WINWORD.EXE"
    os.system("taskkill /f /im " + browserExe)
    return ("MS word closed ")

def shell():
    speak_module.speak("Here you go with python shell")
    os.startfile(r"C:\python39\python.exe")
    return ("opening python shell")

def close_shell():
    speak_module.speak("Closing python shell")
    browserExe = "python.exe"
    os.system("taskkill /f /im " + browserExe)
    return ("shell closed")

def vs_code():
    speak_module.speak("here you go with vs code")
    os.startfile(r"D:\Microsoft VS Code\Code.exe")
    return ("opening vs code")

def close_vs_code():
    speak_module.speak("closing vs code")
    browserExe = "code.exe"
    os.system("taskkill /f /im " + browserExe)
    return ("vs code closed")

def close_browser():
    os.system("taskkill /im chrome.exe /f")
    return "closed chrome"
