# coding: utf-8
import requests
from bs4 import BeautifulSoup
from flask import Flask,request,render_template,redirect,url_for
import time,json
import urllib.request, urllib.error
from apiclient.discovery import build
from apiclient.errors import HttpError

url = []
t = []
wkey = "ee0eb7be159c4dbb10ff08289856905c"
akey = "test_9cw6Q6SJ87R"
ep = "api.ekispert.jp"
DEVELOPER_KEY = 'AIzaSyC-daF5wvITHzm9y5pIHPvZiRfSYUW71xY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(
    YOUTUBE_API_SERVICE_NAME, 
    YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY
    )
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', data=zip(t,url))

@app.route("/result", methods=["post"])
def result():
    word = request.form["search"]
    print(word)
    return render_template('result.html',result=word)
@app.route("/train", methods=["post"])
def train():
    data = request,form["search"]
    print(data)

@app.route('/send-location', methods=['POST'])
def send():
    lat = request.form["lat"]
    lng = request.form["lng"]
    acc = request.form["acc"]
    print(lat)
    print(lng)
    print(acc)
    urlw = "http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&appid={2}".format(lat,lng,wkey)
    rw = requests.get(urlw).text
    rw = json.loads(rw)
    city = rw["name"]
    main = rw["weather"][0]["main"]
    tempmax = float(rw["main"]["temp_max"]) - 273.15
    tempmin = float(rw["main"]["temp_min"]) - 273.15
    temp = float(rw["main"]["temp"]) - 273.15
    feels = float(rw["main"]["feels_like"]) - 273.15
    print(city)
    print(main)
    print(temp)
    print(tempmin)
    print(tempmax)
    print(feels)
    return render_template('index.html',temp=str(temp))
if __name__ == "__main__":
    app.run(debug=True)
