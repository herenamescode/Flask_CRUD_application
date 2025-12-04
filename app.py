import os
import redis
from flask import Flask
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET", "POST", "PUT", "DELETE"])
# redis connection
redis_cilent = redis.Redis(   
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    password=os.getenv("REDIS_PASSWORD"),
    ssl=True
)

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


from model.user_create import create_user
from model.user_delete import delete_user
from model.user_login import login_user
from model.user_update import update_user
from model.user_read import read_user
from controller import user_controller  

# testing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
