import speak_module
import database

def take_input():
    if database.speech_is_on():
        i = speak_module.get_audio()
        return i
    else:
        i = input("Me :")
        return i