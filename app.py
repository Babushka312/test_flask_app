# from crypt import methods
from distutils.debug import DEBUG
from flask import Flask, render_template, request, redirect
from peewee import *
from models import Instagram

app = Flask(__name__)

@app.route('/')
def lie():
    all_instagram = Instagram.select()
    return render_template("index.html", instagrams=all_instagram)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        user = request.form['user_name']
        password = request.form['password']
        users = request.form['user']
        emails = request.form['Email']

        Instagram.create(
            user_name = user,
            password = password,
            user = users,
            Email = emails
        )
        return redirect('/')
    return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)
    