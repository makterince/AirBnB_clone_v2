from flask import Flas

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ initializing the  routing handler for root url"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    """ start flask application"""
    app.run(host='0.0.0.0', port=5000)
