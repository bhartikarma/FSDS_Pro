#Implement user sessions in a Flask app to store and display user-specific data.
#url to run -
from flask import Flask, render_template, request, session, redirect, url_for
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
        session['username'] = username
        return redirect(url_for('dashboard'))

    return render_template('5.index.html', form=form)

@app.route('/dashboard')
def dashboard():
    username = session.get('username')
    if username:
        return render_template('5.dashboard.html', username=username)
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host= "0.0.0.0" , port = 5005)

