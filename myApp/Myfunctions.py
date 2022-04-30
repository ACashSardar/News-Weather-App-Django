import requests
import numpy as np
import pandas as pd
from datetime import datetime, date
from geopy.geocoders import Nominatim
from newsapi.newsapi_client import NewsApiClient

city="Kolkata"
country="India"
week=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

def GetCityLocation(city):
    loc=Nominatim(user_agent="GetLoc")
    getLoc=loc.geocode(city)
    return str(getLoc.latitude),str(getLoc.longitude),str(getLoc.address)

def DayDate(week):
    value=datetime.today().strftime("%A")
    today=date.today()
    today=today.strftime("%B %d, %Y")
    index=0
    for x in week:
        if x==value:
            return index,today
        index=index+1

def WeatherUpdates(latitude,longitude,week):
    api="https://api.openweathermap.org/data/2.5/onecall?lat="+latitude+"&lon="+longitude+"&exclude=current,minutely,hourly&appid=7f7fb990c0d07404f86fb5f5a6922579"
    JSON_data=requests.get(api).json()
    weatherlist=JSON_data['daily']
    day,date=DayDate(week)
    current_day=[]
    icon=[]
    sky_condition=[]
    avg_day_temp=[]
    temp_max=[]
    temp_min=[]
    humidity=[]
    wind_speed=[]
    for i in range(len(weatherlist)):
        index=(i+day)%7
        if(i==0):
            current_day.append('Today')
        elif(i==1):
            current_day.append('Tomorrow')
        else:
            current_day.append(week[index])
        icon.append(weatherlist[i]['weather'][0]['icon'])
        sky_condition.append(weatherlist[i]['weather'][0]['description'])
        avg_day_temp.append(int(weatherlist[i]['temp']['day']-273.15))
        temp_max.append(int(weatherlist[i]['temp']['max']-273.15))
        temp_min.append(int(weatherlist[i]['temp']['min']-273.15))
        humidity.append(weatherlist[i]['humidity'])
        wind_speed.append(str(weatherlist[i]['wind_speed']))
    return zip(current_day,icon,sky_condition,avg_day_temp,temp_max,temp_min,humidity,wind_speed)


def NewsByChannel(channel):
    news_api=NewsApiClient(api_key='97b67ff1d2fb4d7794e9e4c77ff87876')
    top_headlines=news_api.get_top_headlines(sources=channel) # returns a dictionary
    # top_headlines.keys() -> ['status', 'totalResults', 'articles']
    articles=top_headlines['articles'] # returns a List
    img=[]
    src=[]
    desc=[]
    news=[]
    date=[]
    txt_link=[]
    for i in range(len(articles)):
        my_articles=articles[i]
        news.append(my_articles['title'])
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])
        temp=' at '.join(str(my_articles['publishedAt']).split('T'))[:19]
        temp=temp[:14]+datetime.strptime(temp[14:19], "%H:%M").strftime("%I:%M %p")
        date.append(temp)
        src.append(my_articles['source']['name'])
        txt_link.append(my_articles['url'])
    return zip(date,news,img,desc,src,txt_link)

def NewsByCategory(category):
    url=f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey=97b67ff1d2fb4d7794e9e4c77ff87876"
    data=requests.get(url).json()
    articles=data['articles'] # returns a List
    img=[]
    src=[]
    desc=[]
    news=[]
    date=[]
    txt_link=[]
    # print(articles)
    for i in range(len(articles)):
        my_articles=articles[i]
        news.append(my_articles['title'])
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])
        temp=' at '.join(str(my_articles['publishedAt']).split('T'))[:19]
        temp=temp[:14]+datetime.strptime(temp[14:19], "%H:%M").strftime("%I:%M %p")
        date.append(temp)
        src.append(my_articles['source']['name'])
        txt_link.append(my_articles['url'])
    return zip(date,news,img,desc,src,txt_link)

