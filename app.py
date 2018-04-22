from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message': 'Hai world (Intentional hai instead of hello :) )'})


if __name__ == '__main__':
    app.run()