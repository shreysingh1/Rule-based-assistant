import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 180)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening..")
        audio = r.listen(source)
    said = ""
    try:
        print("recognizing..")
        said = r.recognize_google(audio)
        print("Me :" +said)
    except sr.UnknownValueError:
        print("Cant recognise your voice")
    except sr.RequestError:
        print("Check Your internet connectivity")
    return str(said.lower())