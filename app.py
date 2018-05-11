from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/test/<search_query>')
def search(search_query):
    return search_query
@app.route('/name/<name>')
def index(name):
    if name.lower()=='Tiedaner':
        return 'Hello,{}'.format(name),200
    else:
        return 'Not Found',404

if __name__ == '__main__':
    app.run(debug=True)
