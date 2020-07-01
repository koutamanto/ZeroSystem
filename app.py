# coding: utf-8
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/index")
def index():
    html = requests.get('https://www.timeanddate.com/worldclock/').text
    soup = BeautifulSoup(html)
    time = soup.find(id='c248').text
    print(time)
    message = time
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run()
