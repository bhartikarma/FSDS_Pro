#3.Develop a Flask app that uses URL parameters to display dynamic content.
#URL to run- https://orange-artist-ndptv.pwskills.app:5003/greet/YourName
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Dynamic Content App!'

@app.route('/greet/<name>')
def greet(name):
    return render_template('3.greet.html', name=name)

if __name__ == '__main__':
    app.run(host= "0.0.0.0" , port = 5003)
