"""
Site that requests name, age, and favorite softdes ninja and displays user profile
"""
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

#Index Page
@app.route('/')
def hello_world():
    return render_template('index.html')

#Form results page

@app.route('/login', methods = ['GET','POST'])
def login():
    #if post request(form submit)
    if request.method == 'POST':
        #read form results, if present return profile page template
        name = request.form['firstname']
        age = request.form['age']
        ninja = request.form['favoriteninja']
        if name and age and ninja:
            return render_template('profile.html' ,name = name, age = age, ninja = "Patrick Huston")
        else:
        #otherwise return error page template
            return render_template('error.html')
    #if get request return form for submit
    else:
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run()
    
