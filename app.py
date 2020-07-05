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
    search_response = youtube.search().list(
        q='ヒカキン',
        part='id,snippet',
        maxResults=50,
        ).execute()

    items = search_response["items"]

    for item in items:
        title = item["snippet"]["title"]
        print(title)
        thumb = item["snippet"]["thumbnails"]["high"]['url']
        print(thumb)
        url.append(thumb)
        t.append(title)
        print(t)
        print(url)
    message = 'aaa'
    return render_template('index.html', data=zip(t,url))

@app.route("/result", methods=["post"])
def result():
    url = []
    t = []
    word = request.form["word"]
    search_response = youtube.search().list(
        q=word,
        part='id,snippet',
        maxResults=50,
        ).execute()

    items = search_response["items"]

    for item in items:
        title = item["snippet"]["title"]
        print(title)
        thumb = item["snippet"]["thumbnails"]["high"]['url']
        print(thumb)
        url.append(thumb)
        t.append(title)
        print(t)
        print(url)
    message = 'aaa'

    return render_template('index.html', data=zip(t,url))
if __name__ == "__main__":
    app.run(debug=True)
