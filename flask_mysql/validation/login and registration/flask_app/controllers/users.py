from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_bcrypt import Bcrypt   
bcrypt = Bcrypt(app)  
from flask_app.models.user import User

@app.route("/")
def index():
    
    return render_template("form.html")

@app.route('/register', methods=['POST'])
def register():
    
    if not User.validate_user(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
        
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email'],
        "password" : pw_hash
    }

    user_id = User.create(data)
    session["user_id"] = user_id #store user id into session
    return redirect('/success')

    
@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["lemail"] }
    user_in_db = User.get_by_email(data)
    
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['lpassword']):
        flash("Invalid Email/Password")
        return redirect("/")
    
    session['user_id'] = user_in_db.id
    return redirect("/success")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/logout")
def logout():
    session.clear()   
    return redirect('/')