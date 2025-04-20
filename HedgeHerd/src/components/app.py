from flask import Flask, jsonify, render_template
from livenews import app 
from flask_cors import CORS

backend = app("ct1nmb9r01qoprggpfk0ct1nmb9r01qoprggpfkg")
backend.fetch("general")

app_flask = Flask(__name__)
CORS(app_flask)

@app_flask.route("/")
def mainpage():
    return render_template("mainpage.html")

@app_flask.route("/news")
def get_news():
    news = backend.n.data.get("general", [])
    return jsonify(news[:20])

if __name__ == "__main__":
    app_flask.run(debug=True)
