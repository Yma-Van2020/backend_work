
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def poke_the_dragon():
    return render_template("index.html")

@app.route("/dragon")
def run():
    return render_template("index2.html")

@app.route("/dragon/run")
def horror():
    return render_template("index3.html")


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 