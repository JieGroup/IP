from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

'''
Notes
-------
Must import files here, otherwise app instance cant
add the url
'''

from app.api import (
    answer_question,
    features,
    summary,
    survey_template,
    users,
    test_connection
)