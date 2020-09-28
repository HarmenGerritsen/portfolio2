from flask import Flask, render_template
app = Flask(__name__)
port = int(os.environ.get('PORT', 33507))


@app.route('/')
def hello():
    return render_template("main.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('page-not-found.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=33507)
