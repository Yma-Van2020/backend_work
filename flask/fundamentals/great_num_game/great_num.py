import random 
from flask import Flask, render_template, request, redirect,session

app = Flask(__name__)
app.secret_key = 'banana' 

@app.route("/")
def page():
   random_num1 = random.randint(1, 100) 
   random_num2 = random.randint(1, 100) 
   random_num3 = random.randint(1, 100) 
   random_num4 = random.randint(1, 100) 
   random_num5 = random.randint(1, 100) 
   random_num6 = random.randint(1, 100) 
   
   style = ""
   if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
   else:
        session['visits'] = 1 # setting session data
   return render_template("index.html", visit = session['visits'], style = style, 
                          random_num1 = random_num1,random_num2 = random_num2,random_num3 = random_num3
                          ,random_num4 = random_num4,random_num5 = random_num5,random_num6= random_num6)

@app.route("/clear_session")
def clear_visit():
   session.clear()   
   return redirect('/')
    
@app.route("/guess", methods=['POST'])
def guess_random():
   session['num'] = int(request.form['num_dis'])
   
   return redirect("/show")	 

@app.route("/show")  
def show_guess():
   random_num = random.randint(1, 100) 
   	
   if random_num == session['num']:
      reply = 'You got it right, wanna play again?'
      style = "green_style"
   
   elif random_num > session['num']: 
      reply = 'Too low!'
      style = "reg_style"
   elif random_num < session['num']:
      reply = 'Too high!'  
      style = "reg_style"
 
   return render_template("index.html", reply = reply, style = style)
       
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  
