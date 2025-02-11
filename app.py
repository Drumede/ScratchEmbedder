from flask import Flask
import scratchattach as sa
from dotenv import load_dotenv
import os

SCRATCHPASS = os.environ.get("SCRATCHPASS")
SCRATCHUSER = os.environ.get("SCRATCHUSER")
session = sa.login(SCRATCHUSER, SCRATCHPASS)

app = Flask(__name__)

@app.route("/")
def home():
    user = session.connect_user("drumede")
    name = user.name
    return f"<p>{name}</p>"