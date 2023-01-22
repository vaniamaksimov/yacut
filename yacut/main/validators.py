from wtforms.validators import ValidationError

from settings import LETTERS


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
