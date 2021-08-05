from flask import Flask, render_template
 
app = Flask(__name__)

@app.route("/play")
def start_play():
    return render_template("playground.html")

@app.route("/play/<int:num>")
def multiple_box(num):
    return render_template("playground.html", num = num)

@app.route("/play/<int:num>/<string:color>")
def add_color(num, color):
    return render_template("playground.html", num = num, color = color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  