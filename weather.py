from bs4 import BeautifulSoup
import requests
from speaker import speaker

# If you want this to work, make a file called secret_weather_data.txt and
# put a weather.com link into it.
# Example: https://weather.com/weather/today/l/96f2f84af9a5f5d452eb0574d4e4d8a840c71b05e22264ebdc0056433a642c84
with open("secret_weather_data.txt") as f:
    secret_url = f.read()


def weather(url=secret_url):
    try:
        result = requests.get(url).text

        doc = BeautifulSoup(result, "html.parser")
        temp = doc.find(class_="CurrentConditions--tempValue--3a50n").string
        conditions = doc.find(class_="CurrentConditions--phraseValue--2Z18W").string
        sunrise = doc.find(class_="SunriseSunset--dateValue--N2p5B").string
        sunset = doc.find_all(class_="SunriseSunset--dateValue--N2p5B")[1].string
        air_quality = doc.find(class_="AirQualityText--severity--1fu5k").string
        air_quality_desc = doc.find(class_="AirQualityText--severityText--1wT_O").string
        high_low = doc.find(class_="WeatherDetailsListItem--wxData--2s6HT").children
        for i, child in enumerate(high_low):
            child = child.string
            if i == 0:
                high = child
            if i == 1:
                high = high + child
            if i == 2:
                high_low = high + child
                del high

        speaker.say(f"The temperature is: {temp}. The current condition is: {conditions}. Sunrise: {sunrise} Sunset: {sunset} "
                    f" High/low: {high_low} Air quality: {air_quality}. {air_quality_desc}")
        speaker.runAndWait()
    except requests.exceptions.ConnectionError:
        speaker.say("I couldn't connect to the internet.")
        speaker.runAndWait()
