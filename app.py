# coding: utf-8
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
app = Flask(__name__) #インスタンス生成

@app.route("/") #アリケーションルートにアクセスが合った場合
def hello(): #hello関数が動作します。
  return "Hello World!" #ブラウザ画面に"Hello World!"と出力されます。

@app.route("/index")
def index():
    html = requests.get('https://www.timeanddate.com/worldclock/').text
    soup = BeautifulSoup(html)
    time = soup.find(id='c248').text
    print(time)
    message = time
    return render_template('index.html', message=message)

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run()
