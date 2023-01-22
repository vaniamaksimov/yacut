from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

from settings import MAX_LENGTH, MIN_LENGTH
from .validators import Letters


class URLForm(FlaskForm):
    original_link = StringField(
        label='Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
        ],
    )
    custom_id = StringField(
        label='Ваш вариант короткой ссылки',
        validators=[
            Optional(strip_whitespace=False),
            Length(
                min=MIN_LENGTH,
                max=MAX_LENGTH,
                message=f'Длинна ссылки должна быть от {MIN_LENGTH} до {MAX_LENGTH} символов'
            ),
            Letters(),
        ],
    )
    submit = SubmitField(
        label='Создать',
    )
