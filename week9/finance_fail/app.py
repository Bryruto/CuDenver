import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

app.secret_key = 'justkey'

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    own = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM own WHERE user_id == ? GROUP BY symbol", session["user_id"])
    total_together = 0
    holdings = []
    for holding in own:
        symbol = holding['symbol']
        shares = holding['total_shares']
        price_info = lookup(symbol)
        current_price = price_info['price']
        total_value = current_price * shares
        total_together += total_value
        holdings.append({
            "symbol": symbol,
            "shares": shares,
            "price": current_price,
            "total": total_value
        })
    cash1 = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = cash1[0]["cash"]
    grand_total = total_together + cash

    return render_template("index.html", cash=cash, grand_total=grand_total, total_together=total_together, holdings=holdings)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    print(session)
    # get the users input
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        # error check amount cant buy 0
        if not shares:
            return apology("not a number ")
        if shares < 0:
            return apology("postive please")
        # look up the price of stock using a api didnt build this function
        price = lookup(symbol.upper())
        # if symbol not in the symbols for stock error check
        if price is None:
            return apology("not a thing")
        # price times the amount of shares
        total = price["price"] * shares
        # get how much mooney the user has
        user_id = session["user_id"]
        user_cash_db = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        # becuase sql returns a list of dicts i index to the 1st in the list list is only size of 1 and go to the key cash sets its value to user_cash
        user_cash = user_cash_db[0]["cash"]
        # update money after buy
        if total > user_cash:
            return apology("your poor")
        user_cash = user_cash - total
        # update in the db
        db.execute("UPDATE users SET cash = ? WHERE id = ?", user_cash, user_id)
        # insert to the purchases table

        db.execute("INSERT INTO purchases (user_id , cash , type) VALUES (?,?,?)",
                   user_id, total, "buy")
        db.execute("INSERT INTO own (symbol,shares,user_id) VALUES (?,?,?)", symbol, shares, user_id)

        flash("bought")
        return redirect("/")
    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    stuff = []
    history_db = db.execute(
        "SELECT cash,symbol,shares,type FROM purchases JOIN own ON own.user_id = purchases.user_id ")
    for row in history_db:
        symbol = row["symbol"]
        shares = row["shares"]
        price = row["cash"]
        type = row["type"]
        type
        stuff.append({
            "type": type,
            "symbol": symbol,
            "shares": shares,
            "price": price,
        })
    return render_template("history.html", stuff=stuff)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        data = lookup(symbol)
        return render_template("quoted.html", data=data)
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if password != password2:
            return apology("passwoord not the same")
        elif not username:
            return apology("must fill in username")
        elif not password or not confirmation:
            return apology("must fill in both password")
        else:
            hashed = generate_password_hash(password)
            try:
                new_user = db.execute(
                    "INSERT INTO users (username,hash) VALUES (?,?)", username, hashed)
            except:
                return apology("username in use pick different username")
            session["user_id"] = new_user
            return redirect("/")
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    user_id = session["user_id"]

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares_to_sell = request.form.get("shares")

        # Validate input
        if not shares_to_sell or not shares_to_sell.isdigit() or int(shares_to_sell) <= 0:
            return apology("Enter a positive integer for shares")

        shares_to_sell = int(shares_to_sell)

        # Lookup current price
        stock = lookup(symbol)
        if stock is None:
            return apology("Invalid symbol")

        price = stock["price"]
        total_sale = shares_to_sell * price

        # Update user's cash
        cash_row = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = cash_row[0]["cash"]
        new_cash = cash + total_sale
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, user_id)

        # Record sale in purchases table
        db.execute(
            "INSERT INTO purchases (user_id, cash, type) VALUES (?, ?, 'sell')",
            user_id, total_sale
        )

        # Record negative shares in own table (for tracking)
        db.execute(
            "INSERT INTO own (symbol, shares, user_id) VALUES (?, ?, ?)",
            symbol, shares_to_sell, user_id
        )

        return redirect("/")

    return render_template("sell.html")
