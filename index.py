from flask import Flask,request,render_template
import requests
from datetime import datetime
import json
app = Flask(__name__)
@app.route("/",methods = ['GET'])
def stampa():
    login = "f262159d0119f50d46a8"
    key = "LvjZZg6RVzUR2lA"
    url="https://www.twitch.tv/heisuten"
    name=datetime.now().strftime("%x")
    folder="eD58x7LFpxY"
    a=requests.get(f'https://api.streamtape.com/remotedl/add?login={login}&key={key}&url={url}&folder={folder}&name={name}')
    text="failed"
    if(a.status_code == 200):
        text="successful"
    return 'ciao'
    #return render_template('file.html',result=text)
