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

class FileTooLarge(ValueError):
    """
    Error raised when the data uploaded by the voter is too large
    """
    
    pass
