from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/')
def hello():
    return 'Hello, AirBnB!'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
