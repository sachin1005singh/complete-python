import wget
from easygui import *

# weather result
def weather():
    global city
    if city == None:
        city = "Delhi"
    elif city == "":
        city = "Delhi"
    url = (("http://wttr.in/")+str(city)+str("_Fp_lang=")+str(lng)+str(".png"))
    filename = wget.download(url,out="meteo.png")


    image = "meteo 1.png"
    msg = "This is the weather report for this location"
    choices = ["Change city"]
    reply = buttonbox(msg, image=image,choices=choices)
    if reply == "Change city":
        location()


def location():
    global city
    msg ="Enter a city or a location\n\n By default it's Delhi"
    title = "Location"
    default ="Delhi"
    city = enterbox(msg,title,default)
    if city ==None:
        city =="Delhi"
    elif city =="":
        city =="Delhi"
    weather()


# location selection
def language():
    global lng
    msg = "What is your language ?"
    title = "Languages"
    choices = ["English","German","French","Danish","Persian","Italian","Russian"]
    choice = choicebox(msg,title,choices)

    if choice == "Aferikaans":
        lng = "af"
    elif choice == "Danish":
        lng= "da"
    elif choice == "German":
        lng = "de"
    elif choice == "French":
        lng = "fr"
        
    elif choice == "Persian":
        lng = "fa"
    elif choice== "Italian":
        lng = "it"
    elif choice == "Russian":
        lng = "ru"
    elif choice == None:
        lng = "en"
    else:
        lng = "en"


    location()
language()
    
    
