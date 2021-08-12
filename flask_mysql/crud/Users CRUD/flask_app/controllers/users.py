from flask_app import app
from flask import render_template,redirect,request,session,Flask
from flask_app.models.user import User

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

@app.route("/info/<int:user_id>")
def show_input(user_id):
    user = User.show_one(user_id)
    return render_template("Read(One).html", dis_user=user)

@app.route("/info/<int:user_id>/edit")
def show_user(user_id):
   
    user = User.show_one(user_id)
    return render_template("Edit.html", ed_user=user)

@app.route('/update/<int:user_id>', methods=["POST"])
def update_user(user_id):
    
    User.update_one(user_id)
    return redirect('/')

@app.route("/delete/<int:user_id>")
def delete_user(user_id):
   
    User.delete_one(user_id)
    return redirect('/')


if __name__ == "__main__":app.run(debug=True)