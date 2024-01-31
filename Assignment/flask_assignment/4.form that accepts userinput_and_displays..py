#Create a Flask app with a form that accepts user input and displays it.
#url to run - https://orange-artist-ndptv.pwskills.app:5004/
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure secret key

class UserForm(FlaskForm):
    username = StringField('Enter your name:')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()

    if form.validate_on_submit():
        username = form.username.data
        return render_template('4.result.html', username=username)

    return render_template('6.index.html', form=form)

if __name__ == '__main__':
    app.run(host= "0.0.0.0" , port = 5004)
