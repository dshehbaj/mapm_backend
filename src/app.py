import flask
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

app.config["DEBUG"] = True

@app.route('/what', methods=["GET"])
def home():
    return "<h1>YOOOOOOOOOdjsf</h1>"

app.run()

