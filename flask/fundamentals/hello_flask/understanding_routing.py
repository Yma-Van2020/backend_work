from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<string:noun>")
def greet_person(noun):
    return f"Hi {noun}!"

@app.route("/repeat/<string:ran_noun>/<int:num>")
def repeat(ran_noun, num):
    return ran_noun * num

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.