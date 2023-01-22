from random import choices

from settings import LETTERS, MAX_LENGTH

from . import db
from .models import URLMap


def get_unique_short_id() -> str:
    short = ''.join(choices(LETTERS, k=MAX_LENGTH))
    while URLMap.query.filter_by(short=short).first():
        short = ''.join(choices(LETTERS, k=MAX_LENGTH))
    return short


def get_or_create_urlmap(original, short) -> URLMap:
    if short:
        urlmap = URLMap(original=original, short=short)
        db.session.add(urlmap)
        db.session.commit()
        return urlmap
    urlmap = URLMap.query.filter_by(original=original).first()
    if urlmap:
        return urlmap
    urlmap = URLMap(original=original, short=get_unique_short_id())
    db.session.add(urlmap)
    db.session.commit()
    return urlmap
