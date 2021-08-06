
from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'banana' 
# set a secret key for security purposes
@app.route("/")
def counter():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return render_template("counter.html", visit = session['visits'])

@app.route("/destroy_session")
def clear_visit():
    session.clear()   
    return redirect('/')
    
@app.route("/increase_visit")
def increa_visit():
     session['visits'] = session['visits'] + 1
     
     return render_template("counter.html", visit = session['visits'])
 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  