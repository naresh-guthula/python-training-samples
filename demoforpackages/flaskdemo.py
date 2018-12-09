from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def home(name):
    return '<b> Hello {}</b>'.format(name)

@app.route('/listrecords')
def listrecords():
    return ('1', '2', '3'),


if __name__ == '__main__':
    app.run(debug=True)
