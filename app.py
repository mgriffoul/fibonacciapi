#!flask/bin/python

from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from app.bdd.dao import init_db
from app.service import fetch_closest
from app.utils.logger_factory import create_logger

app = Flask(__name__)
CORS(app)
logger = create_logger()


@app.before_first_request
def init_app():
    logger.info('Initialising APP')
    init_db()


@app.route('/fibonacci/closest', methods=['GET'])
@cross_origin()
def get_closest_in_fibonacci_sequence():
    try:
        request_number = request.args.get('requestNumber')
        logger.info('Receiving request for number : ' + str(request_number))
        closest_result = fetch_closest(int(request_number))
        logger.info('Result is : ' + str(closest_result))
        return jsonify({'result': closest_result})
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
