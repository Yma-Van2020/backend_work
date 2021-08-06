import random 
from flask import Flask, render_template, request, redirect,session

app = Flask(__name__)
app.secret_key = 'banana' 

@app.route("/")
def page():
       
   context = {
   "random_num1" : random.randint(1, 100), 
   "random_num2" : random.randint(1, 100), 
   "random_num3" : random.randint(1, 100), 
   "random_num4" : random.randint(1, 100), 
   "random_num5" : random.randint(1, 100),
   "random_num6" : random.randint(1, 100),
   }
   
   return render_template("index.html", **context)

@app.route("/clear_session")
def clear_visit():
   session.clear()   
   return redirect('/')
    
@app.route("/guess", methods=['POST'])
def guess_random():
   session['num'] = int(request.form["comp_select"])
   
   return redirect("/show")	 

@app.route("/show")  
def show_guess():
   random_num = random.randint(1, 100) 
   	
   if random_num == session['num']:
      session['reply'] = 'You got it right, wanna play again?'
      session['style'] = "green_style"
   
   elif random_num > session['num']: 
      session['reply'] = 'Too low!'
      session['style'] = "reg_style"
   elif random_num < session['num']:
      session['reply'] = 'Too high!'  
      session['style'] = "reg_style"
 
   return redirect("/")
       
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  
