from flask import Flask, render_template
import scratchattach as sa
from dotenv import load_dotenv
import os

SCRATCHPASS = os.environ.get("SCRATCHPASS")
SCRATCHUSER = os.environ.get("SCRATCHUSER")
session = sa.login(SCRATCHUSER, SCRATCHPASS)

app = Flask(__name__)

@app.route('/<path:sub_path>')
def home(sub_path):
    path_info = sub_path.split("/")
    if path_info[0] != "projects":
        return "bad link dickhead"
    project = session.connect_project(int(path_info[1]))
    titl = project.title
    instructions = project.instructions
    notes = project.notes
    desc = f"**Instructions**\n{instructions}\n\n**Notes and Credits**\n{project.notes}"
    id = project.id
    image = project.thumbnail_url
    return render_template(
        "project.html",
        title = titl,
        description = desc,
        id = id,
        img = image
    )