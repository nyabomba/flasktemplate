from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def show_index():
    return render_template("index.html", hoge="Learn Haskell")

@app.route("/hoge", methods=["POST"])
def hoge():
    hoge = request.form["hoge"]
    if not hoge:
        return redirect("/")