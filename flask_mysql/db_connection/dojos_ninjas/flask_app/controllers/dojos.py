from flask_app import app
from flask import render_template,redirect,request,session,Flask
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    
    dojos = Dojo.get_all()
    
    return render_template("Dojos.html", all_dojos = dojos)


@app.route('/create_dojo', methods=["POST"])
def create_user():
    data = {
        "dojoname" : request.form["dojoname"],
        }
    Dojo.create(data)
    return redirect('/')

@app.route("/dojos/<int:dojo_id>")
def dojo_ninjas(dojo_id):
    data = {
        "id":dojo_id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
        
    return render_template("Dojo_show.html", dojo = dojo)