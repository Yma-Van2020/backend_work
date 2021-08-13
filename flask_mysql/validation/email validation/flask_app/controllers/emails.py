from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/success")
def dis_email():
    
    emails = Email.get_all()
    return render_template("display.html", emails = emails)

@app.route('/create', methods=["POST"])
def create_email():
    data = {
        "address" : request.form["address"],
        }
    
    if not Email.validate_email(request.form):
        return redirect("/")
    else:
        Email.create(data)
        return redirect("/success")