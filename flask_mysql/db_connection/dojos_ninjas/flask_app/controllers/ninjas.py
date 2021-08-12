from flask_app import app
from flask import render_template,redirect,request,session,Flask
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route("/add")
def root():
    
    dojos = Dojo.get_all()
    
    return render_template("New_Ninja.html", all_dojos = dojos)

@app.route("/create_ninja", methods=["POST"])
def create_ninja():
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
        }
    Ninja.create(data)
    return redirect(f"/dojos/{request.form['dojo_id']}")
