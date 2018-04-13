import os

import click
from flask import (
    Flask, render_template, request, url_for, send_from_directory, abort)


app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def index():
    click.echo(url_for('static', filename='css/style.css'))
    if request.method == 'POST':
        abort(404)
    else:
        return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
