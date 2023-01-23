from datetime import datetime
from typing import Any, Dict, Hashable
from urllib.parse import urljoin

from flask import request

from . import db


class IdMixin:
    id = db.Column(db.Integer, primary_key=True)


class TimestampMixin:
    timestamp = db.Column(db.DateTime,
                          nullable=False,
                          default=datetime.utcnow)


class URLMap(IdMixin, TimestampMixin, db.Model):
    original = db.Column(db.String(length=255),
                         nullable=False,)
    short = db.Column(db.String(length=6),
                      nullable=False,
                      unique=True,
                      index=True,)

    def repr_full_short_path(self) -> str:
        return urljoin(request.host_url, self.short)

    def from_dict(self, data: Dict[str, Any]) -> None:
        for field in ('original', 'short'):
            if field in data:
                setattr(self, field, data.get(field))

    def to_dict(self) -> Dict[Hashable, Any]:
        return dict(url=self.original, short_link=self.repr_full_short_path())

    def __html__(self):
        url = self.repr_full_short_path()
        return f'<a href="{url}">{url}</a>'
