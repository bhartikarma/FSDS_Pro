#1.Create a Flask app that displays "Hello, World!" on the homepage.

from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return "<h1>Hello, World!</h1>"

# Run the application if this script is executed
if __name__ == '__main__':
    app.run(host= "0.0.0.0" , port = 5001)

#url to run https://orange-artist-ndptv.pwskills.app:5002/