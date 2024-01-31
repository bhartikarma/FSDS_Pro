#Build a Flask app with static HTML pages and navigate between them.
#url to run - https://orange-artist-ndptv.pwskills.app:5003/
from flask import Flask , render_template, request
import requests 
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('2.home.html')

@app.route('/about')
def about():
    return render_template('2.about.html')

if __name__ == '__main__':
    app.run(host= "0.0.0.0" , port = 5003)