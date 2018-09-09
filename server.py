from flask import Flask, render_template, request, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show-all-full-name')
def full_name():
    full_name = data_manager.get_full_name()
    return render_template('result.html', full_name=full_name)


@app.route('/add-new-personal')
def add_new_personal():
    return render_template('add.html')


@app.route('/add-new-personal', methods=['POST'])
def insert_into_new_personal():
    if request.method == 'POST':
        first = request.form['first']
        last = request.form['last']
        data_manager.add_new_personal(first, last)
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
