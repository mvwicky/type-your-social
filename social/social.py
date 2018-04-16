import os
import multiprocessing as mp

from flask import (
    Flask,
    render_template,
    request,
    url_for,
    send_from_directory,
    redirect,
)
from flask_sslify import SSLify

HERE = os.path.split(os.path.abspath(__file__))[0]

app = Flask(__name__)
sslify = SSLify(app)
COUNT_FILE = os.path.join(HERE, 'static', 'count')
COUNTER = mp.Value('I', 0)
with COUNTER.get_lock():
    with open(COUNT_FILE, 'rt') as f:
        COUNTER.value = int(f.read())


DESC = ' '.join(
    (
        'Type your Social Security number into this clearly legitimate page.',
        'Do not actually do this.',
        'For real, this is a bad idea.',
        'Take measures to protect your data.',
    )
)
KEYWORDS = ','.join(('Social', 'Security', 'Social Security', ))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        return render_template(
            'index.html', desc=DESC, kw=KEYWORDS, count=COUNTER.value)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon',
    )


@app.route('/incr', methods=['POST'])
def incr():
    with COUNTER.get_lock():
        COUNTER.value += 1
        with open(COUNT_FILE, 'wt') as f:
            f.write(str(COUNTER.value))
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.debug = True
    app.run(threaded=True)
