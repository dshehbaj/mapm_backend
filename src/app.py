import flask
from flask_cors import CORS
from states import states
from counties import counties
from risk import risk

app = flask.Flask(__name__)
app.register_blueprint(states)
app.register_blueprint(counties)
app.register_blueprint(risk)

CORS(app)

app.config["DEBUG"] = True

@app.route('/what', methods=["GET"])
def home():
    return "<h1>YOOOOOOOOOdjsf</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
