# All imports here
import os

from flask import Flask, session, render_template, flash, request, json

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
        return render_template('login.html', name=user)


@app.route("/admin", methods=['POST'])
def login(user=None):
    '''
    Authenticates the username and password of the user
    :return: Call to the home page
    '''
    if request.form['password'] == 'password' and request.form['user_name'] == 'pavan':
        session['admin'] = True
        user = request.form['user_name']
        print(user)
    else:
        flash('wrong password!')
    # return index(request.form['user_name'])
    return index(user)



@app.route('/post_string', methods=['GET', 'POST'])
def post_string():
    jsdata = request.form['var1']
    if request.method == 'POST':
        print(jsdata)
        flash(jsdata)
        global data_send
        data_send = jsdata
        # response = make_response(render_template('store.html', delta=str(jsdata).upper()))
        # response.
        # return render_template("store.html", delta="hey")
        # return jsonify(username='peter', id=123), 200
        # return homepage("hey")
        return get_python_data()
    elif request.method == 'GET':
        delta = jsdata
        return render_template("store.html", delta="hey")


@app.route('/getpythondata')
def get_python_data():
    obj = [{"name": "Hello World!"}, {"name": "Pavan"}]
    return json.dumps(obj)

@app.route("/admin/<username>", methods=['POST'])
def homepage(username=None):
    '''

    :param username:
    :return:
    '''
    return render_template("store.html", username=username, count=0)


# Loads the Flask application
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug="True")
