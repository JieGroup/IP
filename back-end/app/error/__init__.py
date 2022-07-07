from __future__ import annotations
from multiprocessing.sharedctypes import Value

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

class DataTypeError(ValueError):
    """
    Error raised when the data is not serializable
    Now the code can serialize numpy, set and datetime
    """

    pass