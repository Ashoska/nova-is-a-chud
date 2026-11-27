import datetime
import requests
import random
import serpapi
import discord
import pytz
import os
from dotenv import load_dotenv



#get api key from .env
load_dotenv()
api_serpapi = os.getenv("api_key")
api_keyWeather = os.getenv("api_keyWeather")
client1 = serpapi.Client(api_key=api_serpapi)




#weather
def get_weather(city):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_keyWeather}")
        data = response.json()
        weather = data["weather"][0]["description"]
        name = data["name"]
        tempf = (data["main"]["temp"] - 273.15) * 9/5 + 32
        tempc = data["main"]["temp"] - 273.15
        feeltempf = (data["main"]["feels_like"] - 273.15) * 9/5 + 32
        feeltempc = data["main"]["feels_like"] - 273.15
        return f"The weather in {name} is {weather} and a temperature of {round(tempf, 1)}°F or {round(tempc, 1)}°C but feels like {round(feeltempf, 1)}°F or {round(feeltempc, 1)}°C"
    except Exception as e:
        print(f"error: {e}")
        return "error try different location"









#genterate content
def analyze_job_results(job_title, city, state, region):
    if region.lower() == "usa" or region.lower() == "us":
        region = "United States"
    elif region.lower() == "id":
        region = "India"
    elif region.lower() == "uk":
        region = "United Kingdom"
    elif region.lower() == "ca":
        region = "Canada"
    elif region.lower() == "au":
        region = "Australia"
    elif region.lower() == "mx":
        region = "Mexico"
    elif region.lower() == "de":
        region = "Germany"
    elif region.lower() == "fr":
        region = "France"
    elif region.lower() == "jp":
        region = "Japan"
    elif region.lower() == "nl":
        region = "Netherlands"
    elif region.lower() == "no":
        region = "Norway"
    elif region.lower() == "nz":
        region = "New Zealand"
    elif region.lower() == "pk":
        region = "Pakistan"
    elif region.lower() == "pl":
        region = "Poland"
    elif region.lower() == "pt":
        region = "Portugal"
    elif region.lower() == "ro":
        region = "Romania"
    elif region.lower() == "se":
        region = "Sweden"
    elif region.lower() == "tr":
        region = "Türkiye"
    elif region.lower() == "za":
        region = "South Africa"
    elif region.lower() == "ae":
        region = "United Arab Emirates"
    elif region.lower() == "bg":
        region = "Bulgaria"
    elif region.lower() == "br":
        region = "Brazil"
    elif region.lower() == "by":
        region = "Belarus"
    elif region.lower() == "ch":
        region = "Switzerland"
    elif region.lower() == "fi":
        region = "Finland"
    elif region.lower() == "gr":
        region = "Greece"
    elif region.lower() == "it":
        region = "Italy"
    elif region.lower() == "ke":
        region = "Kenya"
    elif region.lower() == "lb":
        region = "Lebanon"
    elif region.lower() == "mu":
        region = "Mauritius"
    elif region.lower() == "my":
        region = "Malaysia"
    else:
        region = region
    location = f"{city}, {state}, {region}"
    try:
        results = client1.search({
            "engine": "google_jobs",
            "q": "software engineer",
            "location": location,
           "hl": "en",
            "gl": "us"
        })
        random_file_name = random.randint(1, 1000000000000000000000000000)
        for x in range(10):
            with open(f"jobs_files/{random_file_name}.txt", "a") as file:
                file.write(f"({x + 1}) Job: {results["jobs_results"][x]["title"]}\nCompany: {results['jobs_results'][x]['company_name']}\nLocation: {results['jobs_results'][x]['location']}\nExtensions: {results['jobs_results'][x]['extensions']}\nDescription: {results['jobs_results'][x]['description']}\nApply_options: {results['jobs_results'][x]['apply_options'][0]['link']}\n\n\n\n\n\n\n")
        print(f"file has been made: jobs_files/{random_file_name}.txt")
        return discord.File(f"jobs_files/{random_file_name}.txt", filename=f"Jobs.txt")
    except Exception as e:
        print(f"error: {e}")
        random_file_name = random.randint(1, 10000000000)
        with open(f"jobs_files/error{random_file_name}.txt", "a") as file:
            file.write(f"error: try different location")
        return discord.File(f"jobs_files/error{random_file_name}.txt", filename=f"Error.txt")




#time and date
def get_time(timetype):
    datetime2 = datetime.datetime.now(tz=pytz.timezone(timetype))
    time1 = datetime2.strftime(f"%I:%M:%S %p %a %Z\n%B %d, %Y")
    return time1