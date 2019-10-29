#!flask/bin/python
from flask import Flask, jsonify, abort

app = Flask(__name__)

fibonaccisequence = [0, 1, 2, 3, 5]


@app.route('/fibo/api/testsequence', methods=['GET'])
def get_fibonaccisequence():
    return jsonify({'sequence': fibonaccisequence})


@app.route('/fibo/api/number/<int:looking_for_number>', methods=['GET'])
def get_number(looking_for_number):
    for number in fibonaccisequence:
        if number == looking_for_number:
            return jsonify(looking_for_number)
    return jsonify("Ce nombre n'est pas un Fibo ! :-( ")


if __name__ == '__main__':
    app.run(debug=True)
