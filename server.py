from flask import Flask, render_template

import data_manager

app = Flask(__name__)


@app.route('/')
def hello_world():
    full_name = data_manager.get_full_name()
    return render_template('index.html', full_name=full_name)


if __name__ == '__main__':
    app.run(debug=True)
