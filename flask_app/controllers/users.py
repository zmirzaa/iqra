from flask_app import app 
from flask import render_template, redirect, session, request, flash 
from flask_app.models.user import User 
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index(): 
    return render_template('dashboard.html') 


@app.route('/register', methods=['POST']) 
def register(): 
    newUser = {
        'admin': request.form['admin'], 
        'password': bcrypt.generate_password_hash(request.form['password'])  
    }

    id = User.save(newUser) 
    session['user_id'] = id 
    return redirect('/')

