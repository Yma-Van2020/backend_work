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

@app.route("/info1")
def show_input():
    users = User.get_all()
    return render_template("Read(One).html", all_users = users)

@app.route("/info2")
def show_input2():
    users = User.get_all()
    return render_template("Read2.html", all_users = users)

@app.route("/info3")
def show_input3():
    users = User.get_all()
    return render_template("Read3.html", all_users = users)

@app.route("/info4")
def show_input4():
    users = User.get_all()
    return render_template("Read4.html", all_users = users)

@app.route('/edit_user')
def edit_user():
    return render_template("Edit.html")
           
if __name__ == "__main__":app.run(debug=True)

