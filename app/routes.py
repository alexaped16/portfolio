from app import app, db
from flask import redirect, render_template, url_for, flash


@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html',  title=title)


@app.route('/my_portfolio')
def my_portfolio():
    return render_template('my_portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/extra1')
def extra1():
    return render_template('extra1.html')

@app.route('/extra2')
def extra2():
    return render_template('extra2.html')