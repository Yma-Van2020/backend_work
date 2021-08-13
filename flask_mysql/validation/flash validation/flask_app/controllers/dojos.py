from flask_app import app
from flask import flash,render_template,redirect,request,session
from flask_app.models.dojo import Dojo

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    
    session['name'] = request.form['name']
    session["loca_select"] = request.form["loca_select"]
    session["lang_select"] = request.form["lang_select"]
    session["comment"] = request.form["comment"]
    
    session["checks"] = request.form["checks"]
    session["options"] = request.form["options"]

    if not Dojo.validate_dojo(request.form):
        
        return redirect("/")
    
    return redirect("/result")

@app.route("/result")
def res():
    return render_template("result.html", name =  session['name'], loca = session["loca_select"],
                           lang = session["lang_select"], comment = session["comment"])
