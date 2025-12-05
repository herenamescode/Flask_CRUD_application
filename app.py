import os
import redis
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET", "POST", "PUT", "DELETE"])
# redis connection
app.redis = redis.Redis(   
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    password=os.getenv("REDIS_PASSWORD"),
    ssl=True,
    decode_responses=True
)
print("Redis Connected Successfully")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/profile.html")
def userProf():
    return render_template("profile.html")


@app.route("/login.html")
def user_log():
    return render_template("login.html")


@app.route("/signup.html")
def user_sig():
    return render_template("signup.html")

@app.route('/fetch')
def display():
    return render_template("view.html")

from controller import user_controller  

# testing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
