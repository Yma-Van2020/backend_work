from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'the secret is here' 

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

    
    
    return redirect("/result")

@app.route("/result")
def res():
    return render_template("result.html", name =  session['name'], loca = session["loca_select"],
                           lang = session["lang_select"], comment = session["comment"])

        
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  
