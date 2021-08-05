from flask import Flask, render_template
 
app = Flask(__name__)

@app.route("/")
def display_8():
    return render_template("checker.html", num = 8, num2 = 8)

@app.route("/4")
def display_4():
    return render_template("checker.html", num = 8, num2 = 4, width = 12.5, height = 25)

@app.route("/<int:num>/<int:num2>")
def display_input(num, num2):
    return render_template("checker.html",num = num, num2 = num2, width = 100/num, height = 100/num2)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  