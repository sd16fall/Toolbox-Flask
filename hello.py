"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
app = Flask(__name__)


def bad():
    return render_template("bad.html")

def result():
    return render_template("result.html")

@app.route('/', methods = ["GET","POST"])
def hello_world():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        faveninja = request.form["faveninja"]
        if name == "eric" and age == "21":
            return result()
        elif name == "anderson" and age == "20":
            return result()
        elif name == "kim" and age == "20":
            return result()
        elif name == "diego" and age == "20":
            return result()
        elif name == "chloe" and age == "20":
            return result()
        else:
            return bad()

    return render_template("index.html")



if __name__ == '__main__':
    app.run()
