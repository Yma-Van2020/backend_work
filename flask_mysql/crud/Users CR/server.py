from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
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

@app.route("/info/<int:user_id>")
def show_input(user_id):
    query = "SELECT * FROM users WHERE users.id = %(id)s;"
    data = {
        "id":user_id
    }
    results = connectToMySQL("users").query_db(query,data)
    
    return render_template("Read(One).html", dis_user=results[0])


@app.route("/info/<int:user_id>/edit")
def show_user(user_id):
    query = "SELECT * FROM users WHERE users.id = %(id)s;"
    data = {
        "id":user_id
    }
    results = connectToMySQL("users").query_db(query,data)
    
    return render_template("Edit.html", ed_user=results[0])

@app.route('/update/<int:user_id>', methods=["POST"])
def update_user(user_id):
    query = "UPDATE users SET first_name = %(new_fname)s, last_name = %(new_lname)s, email = %(new_email)s WHERE id = %(id)s;"
    data = {
        'id': user_id,
        "new_fname" : request.form["new_fname"],
        "new_lname" : request.form["new_lname"],
        "new_email" : request.form["new_email"]
        }

    user = connectToMySQL("users").query_db(query,data)
    return redirect('/')

@app.route("/delete/<int:user_id>")
def delete_user(user_id):
    query = "DELETE FROM user WHERE id = %(id)s;"
    data = {
        "id": user_id
    }
    connectToMySQL('users').query_db(query,data)
    return redirect('/')
     
if __name__ == "__main__":app.run(debug=True)

