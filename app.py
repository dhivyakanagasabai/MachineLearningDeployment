from flask import Flask, render_template, request
from test import OOPStest


#initialize the app
app = Flask(__name__)

#trying OOPS function call
oops = OOPStest()
print("*******************************")
oops.testOOPS()
print("*******************************")

@app.route('/')
def hello_word():
    return render_template('form.html')

@app.route('/home')
def home():
    return render_template('hello.html')

# welcome
@app.route('/welcome')
def welcome():
    return render_template('home.html')

# contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

#blog
@app.route('/blog')
def blog():
    return render_template('blog.html')

#Gallery
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/predict', methods = ['post'])
def predict():
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    email = request.form.get('email')
    phone = request.form.get('Phone')

    print(first_name)
    print(last_name)
    print(email)
    print(phone)

    return "Prediction parameters submitted"

#run the app
app.run(debug=True)
