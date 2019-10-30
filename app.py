#!flask/bin/python
from flask import Flask, jsonify, request, abort

from app.service import fetch_closer

app = Flask(__name__)
fibonaccisequence = [0, 1, 2, 3, 5]


@app.route('/fibonacci/closer', methods=['GET'])
def get_fibonaccisequence():
    try:
        looking_for_number = int(request.args.get('number'))
        return jsonify({'result': fetch_closer(looking_for_number)})
    except ValueError:
        abort(400, {'message': 'Vous devez saisir un nombre'})


@app.errorhandler(400)
def custom400(error):
    response = jsonify({'message': error.description['message']})
    response.status_code = 404
    response.status = 'error.Bad Request'
    return response


if __name__ == '__main__':
    app.run(debug=True)
