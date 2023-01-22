from http import HTTPStatus

from wtforms.validators import ValidationError

from settings import LETTERS, MAX_LENGTH, MIN_LENGTH
from .api_error_handlers import InvalidAPIUsage


class Letters:
    def __init__(self, sighns=LETTERS, message=None) -> None:
        self.sighns = sighns
        if not message:
            message = (
                'Допустимые символы: '
                'большие латинские буквы, '
                'маленькие латинские буквы, '
                'цифры в диапазоне от 0 до 9.'
            )
        self.message = message

    def __call__(self, form, field) -> None:
        string = field.data
        for sighn in string:
            if sighn not in self.sighns:
                raise ValidationError(self.message)


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