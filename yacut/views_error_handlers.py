from http import HTTPStatus

from flask import render_template

from . import app


@app.errorhandler(HTTPStatus.NOT_FOUND.value)
def page_not_found(error):
    return (render_template('404.html'),
            HTTPStatus.NOT_FOUND.value)


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR.value)
def internal_error(error):
    return (render_template('500.html'),
            HTTPStatus.INTERNAL_SERVER_ERROR.value)
