from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form
@app.route('/')
def index():
    print(request)
    return render_template("form_test.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
   
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect("/show")	 
   
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html", name_on_template=session['username'], email_on_template=session['useremail'])

if __name__ == "__main__":
    app.run(debug=True)