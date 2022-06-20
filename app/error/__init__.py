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

class TopicNoNeedUpdate(ValueError):
    """
    Error raised when the topic is not needed to update
    """

    pass