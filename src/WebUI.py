# All imports here
import os

# Importing support libraries
from flask import Flask, redirect, render_template, flash, request, json, url_for
from flask_bootstrap import Bootstrap

from ListOfProducts import *
from Product import *
from QueryList import *
from Security import RegisterForm, LoginForm
# Importing support classes
from StoreUser import StoreUser, user_db

# Flask App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:secret@localhost/user_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bootstrap = Bootstrap(app)
user_db.init_app(app)


@app.route("/")
def index(user=None):
    '''
    Landing Page of the Web Application
    :param user: The user of the application
    :return: HTML content
    '''
    return render_template('index.html')


@app.route("/register", methods=['GET', 'POST'])
def register(user=None):
    '''
    Authenticates the username and password of the user
    :return: Call to the home page
    '''
    form = RegisterForm()
    user_db.create_all()
    if request.method == "POST":
        if form.validate_on_submit():
            user_validation = StoreUser.query.filter_by(username=form.username.data).first()
            if user_validation:
                flash("User already exists!")
                return render_template('register.html', form=form)
            else:
                set_user = StoreUser(email=form.email.data, username=form.username.data, password=form.password.data)
                user_db.session.add(set_user)
                user_db.session.commit()
                return redirect(url_for('login'))
        else:
            return render_template('register.html', form=form)
    elif request.method == "GET":
        return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    '''
    Authenticates the username and password of the user
    :return: Call to the home page
    '''
    form = LoginForm()
    if form.validate_on_submit():
        user_validation = StoreUser.query.filter_by(username=form.username.data).first()
        if user_validation:
            if user_validation.check_password(form.password.data):
                return redirect(url_for('store'))
            else:
                flash("Password entered is incorrect!")
        else:
            flash("Username entered is incorrect!")
    return render_template('login.html', form=form)

data_send = []


@app.route('/remove_product', methods=['GET', 'POST'])
def remove_product():
    '''
    
    :return: 
    '''
    try:
        global obj
        product_id = str(request.form['pid'])
        obj.remove_data(product_id)
        if len(data_send) == 0:
            flash("No product to remove!")
        else:
            return json.dumps([prod.dump() for prod in obj.get_data()])
    except Exception as e:
        flash(e)


@app.route('/post_product', methods=['GET', 'POST'])
def post_string():
    '''
    
    :return: 
    '''
    try:
        global obj, queries
        product_id = str(request.form['pid'])
        product_name = str(request.form['name'])
        product_price = str(request.form['price'])
        product_category = str(request.form['category'])
        prod = Product(product_id, product_name, product_price, product_category)
        obj.set_data(prod)
        queries.add_query()
        for i in obj.get_data():
            print(i.name + ",", end="")
        print()
        return json.dumps([prod.dump() for prod in obj.get_data()])
    except Exception as e:
        flash(e)


@app.route('/getpythondata')
def get_python_data():
    '''
    
    :return: 
    '''
    global obj
    for i in obj.get_data():
        print(i.name + ",", end="")
    print()
    return json.dumps([prod.dump() for prod in obj.get_data()])


@app.route('/call_ids', methods=['GET', 'POST'])
def call_ids():
    try:
        return send_to_ids()
    except Exception as e:
        flash(e)


@app.route("/admin/send_to_ids", methods=['POST'])
def send_to_ids():
    '''

    :param username:
    :return:
    '''
    return render_template("send_to_ids.html")


@app.route("/store", methods=['GET', 'POST'])
def store(username=None):
    '''

    :param username:
    :return:
    '''
    return render_template("store.html", username=username)


# Loads the Flask application
if __name__ == '__main__':
    global obj, queries
    obj = ListOfProducts()
    queries = QueryList()
    app.secret_key = os.urandom(12)
    app.run(debug="True")
