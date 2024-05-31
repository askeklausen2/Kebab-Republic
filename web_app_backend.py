from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Add authentication logic here (e.g., check username and password in database)
        session['username'] = username
        return redirect(url_for("user", name=username))
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Add account creation logic here (e.g., save username and password in database)
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/user/<name>")
def user(name):
    if 'username' in session:
        return f"Hello, {name}"
    return redirect(url_for("login"))

@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="admin"))

if __name__ == "__main__":
    app.run(debug=True)
