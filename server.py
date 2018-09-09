from flask import Flask, render_template

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show-all-full-name')
def full_name():
    full_name = data_manager.get_full_name()
    return render_template('result.html', full_name=full_name)


if __name__ == '__main__':
    app.run(debug=True)
