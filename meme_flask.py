#!/bin/python3
from flask import Flask, render_template #use external html script
import requests #interact with reddit apis
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET",url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    #return meme_pic # json format
    return render_template("meme_index.html",meme_pic=meme_pic, subreddit=subreddit)# html format

app.run(host="0.0.0.0",port=80)
