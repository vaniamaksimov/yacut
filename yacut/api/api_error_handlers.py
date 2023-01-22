from http import HTTPStatus

from flask import jsonify

from . import api
from settings import LETTERS, MAX_LENGTH, MIN_LENGTH


class ApiURLMapValidator:
    def __init__(self,
                 sighns=LETTERS,
                 message=None,
                 min_length=MIN_LENGTH,
                 max_length=MAX_LENGTH) -> None:
        self.sighns = sighns
        self.min_length = min_length
        self.max_length = max_length
        if not message:
            message = "Отсутствует тело запроса"
        self.message = message

    def __call__(self, data):
        if not data:
            raise InvalidAPIUsage("Отсутствует тело запроса")
        original = data.get('url')
        if not original:
            raise InvalidAPIUsage('"url" является обязательным полем!')
        if not isinstance(original, str):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для оригинальной ссылки'
            )
        short = data.get('custom_id')
        if short:
            if not isinstance(short, str):
                raise InvalidAPIUsage(
                    'Указано недопустимое имя для короткой ссылки'
                )
            if not self.min_length <= len(short) <= self.max_length:
                raise InvalidAPIUsage(
                    'Указано недопустимое имя для короткой ссылки',
                    HTTPStatus.BAD_REQUEST.value
                )
            for letter in short:
                if letter not in self.sighns:
                    raise InvalidAPIUsage(
                        'Указано недопустимое имя для короткой ссылки'
                    )


class InvalidAPIUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST.value

    def __init__(self, message, status_code: int = None) -> None:
        super().__init__()
        self.message = message
        if status_code:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


@api.app_errorhandler(InvalidAPIUsage)
def invalid_api_usage(error: InvalidAPIUsage):
    return jsonify(error.to_dict()), error.status_code
