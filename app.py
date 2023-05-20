from flask import Flask, render_template, url_for, redirect, session, request, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Python'
db = SQLAlchemy(app)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form["username"]
        return redirect(url_for("hello my new user"))
    return render_template('login.html')
@app.route("/books", methods=['GET', 'POST'])
def Books():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        price = request.form["price"]
        book = Books(title=title, author=author, price=price)
        db.session.add(book)
        db.session.commit()
        flash("Added Successfully! ")
        return redirect(url_for("hello_world"))
    return render_template("books.html")


if __name__ == '__main__':
    app.run()