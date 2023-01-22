from flask import Markup, flash, redirect, render_template

from . import main
from .forms import URLForm
from ..models import URLMap
from ..utils import get_or_create_urlmap


@main.route('/', methods=('GET', 'POST',))
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        original = form.original_link.data
        custom = form.custom_id.data
        if custom and URLMap.query.filter_by(short=custom).first():
            flash(message=f'Имя {custom} уже занято!')
            return render_template('index.html', form=form)
        urlmap = get_or_create_urlmap(original, custom)
        flash(message='Ваша новая ссылка готова:')
        flash(message=Markup(urlmap))
    return render_template('index.html', form=form)


@main.route('/<string:short>')
def redirect_view(short):
    urlmap = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(urlmap.original)
