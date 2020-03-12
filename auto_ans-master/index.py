from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/distribution', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('answer.html')

    elif request.method == 'POST':
        people = request.form.get('about').split(', ')
        return render_template('auto_answer.html', people=people)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
