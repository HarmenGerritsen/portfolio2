from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("main.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/form')
def form():
    return render_template("form.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('page-not-found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)