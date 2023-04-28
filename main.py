from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def root():
    return "<center>I use arch btw</center>"


if __name__ == "__main__":
    app.run()
