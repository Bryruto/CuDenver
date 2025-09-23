import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from clean import get_data
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQL("sqlite:///spot.db")

gen = ["indie","rock","pop","meltal"]

table = ("""
                    CREATE TABLE songs(
                        id INTEGER,
                        song TEXT,
                        popularity INT,
                        artist TEXT,
                        genre TEXT,
                        PRIMARY KEY(id)
                    )
                    """)
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET" , "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        csv = request.files.get("csv")
        if not csv:
            return redirect("home.html")

        csvname= secure_filename(csv.filename)
        csv.save(os.path.join(csvname))
        try:
            db.execute(table)
        except:
            db.execute("drop table songs")
            db.execute(table)


        get_data(csvname)

        os.remove(csvname)

        rock = db.execute("SELECT song,artist FROM songs WHERE genre LIKE ? ORDER BY popularity DESC LIMIT 30","%" + "rock" + "%")

        return render_template("home.html",rock = rock)


