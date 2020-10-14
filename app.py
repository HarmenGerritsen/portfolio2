import os
basedir = os.path.dirname(os.path.abspath(__file__))

from flask import Flask, render_template, redirect, flash
from models import Message
from forms import ContactForm
from extentions import (
    db,
    migrate
)

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    register_extensions(app)

    return app

def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    migrate.init_app(app, db)

    return None

app = create_app()

@app.route('/')
def hello():
    return render_template("main.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        message = Message(fname=form.fname.data, lname=form.lname.data, email=form.email.data, message=form.message.data)
        db.session.add(message)
        db.session.commit()
        flash('Bericht is verstuurd!')
        return redirect('/contact')

    return render_template("contact.html", form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('page-not-found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)