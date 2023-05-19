from flask import Blueprint, render_template, request, flash
import re

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')

        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            flash('Please enter a valid email address.', category='error')
        elif len(firstName) < 1:
            flash('Please enter a name', category='error')
        elif pass1 != pass2:
            flash('Passowrds do not match', category='error')
        elif len(pass1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            flash('Account created', category='success')

    return render_template("sign_up.html")