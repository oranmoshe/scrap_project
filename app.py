from flask import Flask, request , Blueprint, jsonify
import controller

app = Flask(__name__)

@app.route('/stories', methods=['GET'])
def stories_get():
    return controller.get_metadata(request.args.get('id')).toJSON()


@app.route('/stories', methods=['POST'])
def stories_post():
    return controller.get_id(request.args.get('url'))

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(Exception)
def handle_unexpected_error(error):
    status_code = 500
    success = False
    response = {
        'success': success,
        'error': {
            'type': 'UnexpectedException',
            'message': 'An unexpected error has occurred.'
        }
    }
    return jsonify(response), status_code

def _initialize_errorhandlers(application):
    application.register_blueprint(errors)

if __name__ == '__main__':
    _initialize_errorhandlers(app)
    app.run(threaded=True)