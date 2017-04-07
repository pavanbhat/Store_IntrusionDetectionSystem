# All imports here
import os

from flask import Flask, session, render_template, flash, request, json

from Product import *

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


data_send = []


@app.route('/post_product', methods=['GET', 'POST'])
def post_string():
    try:
        global data_send
        product_id = str(request.form['pid'])
        product_name = str(request.form['name'])
        product_price = str(request.form['price'])
        product_category = str(request.form['category'])
        prod = Product(product_id, product_name, product_price, product_category)
        data_send.append(prod)
        for i in data_send:
            print(i.name + ",", end="")
        print()
        return json.dumps([obj.dump() for obj in data_send])
    except Exception as e:
        flash(e)


@app.route('/remove_product', methods=['GET', 'POST'])
def remove_product():
    try:
        global data_send
        product_id = str(request.form['pid'])
        print(product_id)
        for x in data_send:
            if x.pid == product_id:
                print("Removing " + x.name)
                data_send.remove(x)
        for i in data_send:
            print(i.name + ",", end="")
        print()
        return json.dumps([obj.dump() for obj in data_send])
    except Exception as e:
        flash(e)

@app.route('/getpythondata')
def get_python_data():
    global data_send
    return json.dumps([obj.dump() for obj in data_send])

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
