# Import the Flask class from the flask module
from flask import Flask

# Create a Flask web application instance
app=Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
@app.route('/index')
def index():
    return '<h1> PRAVEEN </h1>'

@app.route('/about')
def about():
    return '<h2> I am web developer </h2>'

@app.route('/skills')
def skills():
    return '<h1> Python </h1>'

# create dynamic routing 
@app.route('/user/<name>')
def user(name):
    return '<h1> Welcome {} </h1>' .format(name)

# Start the Flask web server if this script is run directly
if __name__=='__main__':
    app.run(debug=True)
