from http import HTTPStatus

from flask import jsonify

from . import app


class InvalidAPIUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST.value

    def __init__(self, message, status_code: int = None) -> None:
        super().__init__()
        self.message = message
        if status_code:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error: InvalidAPIUsage):
    return jsonify(error.to_dict()), error.status_code
