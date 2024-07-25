from flask import Flask

app = Flask(__name__)

# decorators
def make_bold(func):
    def wrapper():
        return '<b>'+func()+'</b>'
    return wrapper

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/bye')
@make_bold
def bye():
    return 'Bye'

@app.route('/greet/<name>/34')
def greet(name):
    return f"Hello {name}"

@app.route('/greetings/<path:name>/<int:num>')
def greetings(name, num):
    return f"Hello {name} and you are {num} years old"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload the server
    app.run(debug= True)