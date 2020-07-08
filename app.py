# coding: utf-8
import requests
from bs4 import BeautifulSoup
from flask import Flask,request,render_template,redirect,url_for
import time
import urllib.request, urllib.error
from apiclient.discovery import build
from apiclient.errors import HttpError

url = []
t = []
akey = "test_9cw6Q6SJ87R"
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
    print(data)
    print(lat)
    print(lng)
    return ''

if __name__ == "__main__":
    app.run(debug=True)
