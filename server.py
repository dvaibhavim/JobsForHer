# server file for weather app
from flask import Flask, render_template

#Api key to establish handshake between Accu weather
API_KEY = "qQgGRb1A0A6R5HvKx7T37JCKdaAYG8GT"

app = Flask(__name__)


@app.route('/')
def search():
	return render_template("weather.html")


