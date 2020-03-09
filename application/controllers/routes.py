from flask import redirect

from application import app


@app.route('/')
def main():
    return redirect('admin')
