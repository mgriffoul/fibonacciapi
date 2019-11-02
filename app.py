#!flask/bin/python

from flask import Flask, jsonify, request, abort

from app.bdd.dao import init_db
from app.service import fetch_closer
from app.utils.logger_factory import create_logger

app = Flask(__name__)
logger = create_logger()


@app.before_first_request
def init_app():
    logger.info('Initialising APP')
    init_db()


@app.route('/fibonacci/closer', methods=['GET'])
def get_fibonaccisequence():
        request_number = request.args.get('number')
        logger.info('Receiving request for number : ' + str(request_number))
        closer_result = fetch_closer(int(request_number))
        logger.info('Result is : ' + str(closer_result))
        return jsonify({'result': closer_result})


@app.errorhandler(400)
def custom400(error):
    response = jsonify({'message': error.description['message']})
    response.status_code = 404
    response.status = 'error.Bad Request'
    return response


if __name__ == '__main__':
    app.run(debug=True)
