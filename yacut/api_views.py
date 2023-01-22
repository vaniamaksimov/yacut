from http import HTTPStatus
from typing import Any, Dict, Hashable

from flask import jsonify, request

from . import app
from .models import URLMap
from .utils import get_or_create_urlmap
from .validators import ApiURLMapValidator
from .api_error_handlers import InvalidAPIUsage

is_valid = ApiURLMapValidator()


@app.route('/api/id/', methods=('POST',))
def create_id():
    data: Dict[Hashable, Any] = request.get_json()
    is_valid(data)
    original = data.get('url')
    short = data.get('custom_id')
    if short and URLMap.query.filter_by(short=short).first():
        raise InvalidAPIUsage(f'Имя "{short}" уже занято.')
    urlmap = get_or_create_urlmap(original, short)
    return jsonify(urlmap.to_dict()), HTTPStatus.CREATED.value


@app.route('/api/id/<string:short_id>/', methods=('GET',))
def get_url(short_id: str):
    urlmap: URLMap = URLMap.query.filter_by(short=short_id).first()
    if not urlmap:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND.value)
    return jsonify({'url': urlmap.original}), HTTPStatus.OK.value
