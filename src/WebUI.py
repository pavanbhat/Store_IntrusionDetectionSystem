# All imports here
from flask import Flask, session, render_template,  flash, request
import os

# Flask App
app = Flask(__name__)

@app.route("/")
def index(user=None):
    '''
    Landing Page of the Web Application
    :param user: The user of the application
    :return: HTML content
    '''
    if not session.get('logon'):
        return render_template('form.html')
    else:
        return "Hello {{user}}!"

@app.route("/admin", methods=['POST'])
def form(user=None):
    '''
    Authenticates the username and password of the user
    :return: Call to the home page
    '''
    if request.form['password'] == 'password' and request.form['user_name'] == 'admin':
        session['admin'] = True
    else:
        flash('wrong password!')
    return index(user)


# Loads the Flask application
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run()