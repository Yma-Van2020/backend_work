from flask_app import app
from flask import render_template,redirect,request,session,Flask
from flask_app.models.author import Author
# from flask_app.models... import ..(optional)

@app.route("/")
def root():
   return redirect("/authors")

@app.route("/authors")
def dis_authors():
    authors = Author.get_all()
    
    return render_template("authors.html", authors = authors)

@app.route("/authors/<int:author_id>")
def dis_fav(author_id):
    data = {
        "id": author_id
    }
    
