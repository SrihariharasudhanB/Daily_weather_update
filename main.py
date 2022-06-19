from urllib import request
from send_mail import Mail
import requests

API_KEY = "< YOUR API KEY >"
CITY_NAME = "< YOUR CITY NAME >"
REQUEST  = "http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}".format(CITY_NAME=CITY_NAME,API_KEY=API_KEY)

if __name__ == "__main__":
    
    request = requests.get(REQUEST)
    
    if request.status_code == 200:
        
        data = request.json()
        weather = data["weather"][0]["description"]
        message = "Climate: " + weather + "\n"
        temperature = data["main"]["temp"]
        message +="Temperature: " + str(round(temperature-273.15,2))+"°C"
        print(message)
        mailer = Mail()
        mailer.sendMail(message)
        
    else:
        
        print("An error occured!")
