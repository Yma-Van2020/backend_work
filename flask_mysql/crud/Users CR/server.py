from flask import Flask, render_template, request, redirect

from user import User
app = Flask(__name__)
@app.route("/")
def index():
    users = User.get_all()
    return render_template("Read(All).html", all_users = users)

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
        }
    User.save(data)
    return redirect('/')

@app.route("/form")
def add_new():
    return render_template("Create.html")
           
if __name__ == "__main__":app.run(debug=True)

