from __future__ import annotations

from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

class DBDocumentNotFound(ValueError):
    """
    Error raised when the document

    """
    pass

class SurveyAnswerError(ValueError):
    """
    Error raised when the key in dict is duplicated
    """

    pass

class SurveyAnswerTooLarge(ValueError):
    """
    Error raised when the data uploaded by the voter is too large
    """
    
    pass


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response

def bad_request(message):
    '''400: Wrong Request'''
    return error_response(400, message)


# # Capture the global status code and perform custom exception handling
# @exception_bp.app_errorhandler(404)
# def not_found_error(error):
#     print('errorrrrr')
#     return error_response(404, 'error')

# @exception_bp.app_errorhandler(500)
# def internal_error(error):
#     # db.session.rollback()
#     return error_response(500)