import random
from datetime import datetime,date
from django.shortcuts import render, HttpResponse
from newsapi.newsapi_client import NewsApiClient
from myApp.Myfunctions import *
from . models import YTClist

def Shuffle(querySet):
    set_items = list(querySet)
    random.shuffle(set_items)
    return set_items

# Create your views here.
def ChannelNews(request):
    context={}
    ChannelName=None
    ChannelList=["abc-news","al-jazeera-english","bbc-news","bbc-sport","business-insider","buzzfeed","cbc-news","cnn",
    "espn","fortune","fox-news","google-news","google-news-in","mtv-news","news24","the-washington-times","bleacher-report","usa-today"]
    if request.method=="GET":
        ChannelName=random.choice(ChannelList)
    if request.method=="POST":
        ChannelName=request.POST['ChannelName']
    print(ChannelName)
    context={'data':NewsByChannel(ChannelName),'ChannelName':ChannelName}
    return render(request, 'NewsPage.html',context)


def CategoryNews(request,category):
    context={'data':NewsByCategory(category)}
    return render(request, 'NewsPage.html',context)

def Weather(request):
    week=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    city=""
    if request.method=="POST":
        city=request.POST['cityname']
        city=city.strip().title()
        try:
            latitude,longitude,state_country=GetCityLocation(city)
            weather_data=WeatherUpdates(latitude,longitude,week)
            _,date=DayDate(week)
            context={'weather_data':weather_data, 'city':city, 'state_country':state_country, 'date':date}
        except:
            context={}
        return render(request,'WeatherPage.html', context)
    return render(request,'WeatherPage.html', {})  

def Livenews(request):
    YTchannels=YTClist.objects.all()
    YTchannels=Shuffle(YTchannels)
    context={'YTchannels':YTchannels}
    return render(request, 'LiveNews.html',context)