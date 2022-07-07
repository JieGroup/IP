import pytest

from app.database.api import (
    get_all_documents_count,
    get_all_documents,
    create_document,
    search_document,
    update_document,
    delete_document
)

from pymongo.cursor import Cursor

from app._typing import MTurkID


class TestSurveySummary:

    '''
    We currently havent implemented the SurveySummary.
    Unittest not needed.
    '''