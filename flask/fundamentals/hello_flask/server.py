from flask import Flask 
 
app = Flask(__name__)
    
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'

@app.route('/success')
def success():
    return "Success"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello {name}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.