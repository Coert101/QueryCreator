from flask import render_template

import QueryBuilder
from app import app


@app.route('/')
@app.route('/index')
def index():
    builder = QueryBuilder.QueryBuilder
    return render_template('QueryCreatorInterface.html',
                           title='Query Creator', builder=builder)