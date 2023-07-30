import webbrowser
import requests
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from input_module import take_input
from output_module import output
import speak_module
import smtplib


def open_facebook():
    webbrowser.open("https://facebook.com")


def search_google():
    output("What should i search")
    command = take_input()
    webbrowser.open("https://www.google.com/search?q=" + command + "&start=")


def search_youtube():
    output("What should i search")
    command = take_input()
    wb = str(webbrowser.open('https://www.youtube.com/results?search_query=' + command))
    return wb


def open_google():
    webbrowser.open("https://www.google.com/")


def open_youtube():
    webbrowser.open("https://www.youtube.com/")


def openWebsite(url='https://www.google.com/'):
    webbrowser.open(url)


def maps():
    output("Of which city sir")
    text = take_input()
    text = text.replace('maps', '')
    text = text.replace('map', '')
    text = text.replace('google', '')
    wb = openWebsite("https://www.google.com/maps/place/" + text)
    return text


def get_directions():
    output("Okay, tell me the starting point")
    startingPoint = take_input()
    output("and the destination point")
    destinationPoint = take_input()
    output("getting the direction sir")

    geolocator = Nominatim(user_agent='assistant')
    if 'current' in startingPoint:
        res = requests.get("https://ipinfo.io/")
        data = res.json()
        startinglocation = geolocator.reverse(data['loc'])
    else:
        startinglocation = geolocator.geocode(startingPoint)

    destinationlocation = geolocator.geocode(destinationPoint)
    startingPoint = startinglocation.address.replace(' ', '+')
    destinationPoint = destinationlocation.address.replace(' ', '+')

    openWebsite('https://www.google.co.in/maps/dir/' + startingPoint + '/' + destinationPoint + '/')

    startinglocationCoordinate = (startinglocation.latitude, startinglocation.longitude)
    destinationlocationCoordinate = (destinationlocation.latitude, destinationlocation.longitude)
    total_distance = great_circle(startinglocationCoordinate, destinationlocationCoordinate).km  # .mile
    speak_module.speak("Have a safe journey")
    round_off = str(round(total_distance, 2))
    return "The distance in between is " + round_off + "kilometer"


def sendEmail():  # SENDING EMAIL
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('shreysingh4999@gmail.com', 'Shrey@123*****')
    output("tell me what should i say")
    content = take_input()
    output("Okay,to whom should i send it")
    to = take_input()
    server.sendmail('shreysingh4999@gmail.com', to, content)
    server.close()

