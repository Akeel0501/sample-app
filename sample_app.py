from flask import Flask
from flask import request
from flask import render_template

sample = Flask(_name_)

@sample.route("/")
def main():
    return render_template("index.html")

if __name__ == "_main_":
    sample.run(host="0.0.0.0",port=5000)


