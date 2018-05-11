from flask import render_template

from . import app

from .views.public.index import Index

app.add_url_rule('/', 'index', view_func=Index.as_view('index'), methods=['GET'])