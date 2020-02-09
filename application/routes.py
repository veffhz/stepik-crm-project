from werkzeug import exceptions
from flask import render_template, redirect
from application import app


@app.route('/')
def main():
    return redirect('admin')


@app.errorhandler(exceptions.NotFound)
def not_found(e):
    return render_template("404.html"), e.code


@app.errorhandler(exceptions.InternalServerError)
def server_error(e):
    return render_template("500.html"), e.code
