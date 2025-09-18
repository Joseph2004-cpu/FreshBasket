
from flask import Flask, render_template,url_for
from datetime import timedelta

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")   

@app.route("/payment")
def payment():
    return render_template("payment.html")   

if __name__ == '__main__':
    app.run(debug=True)
