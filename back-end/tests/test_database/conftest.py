from __future__ import annotations

import pytest

from app.database.api import (
    get_all_documents_count,
    get_all_documents,
    delete_multiple_documents,
    create_document,
    search_document,
    search_multiple_documents,
    update_document,
    delete_document
)

from app.utils.api import Constant

from pymongo.results import (
    InsertOneResult,
    UpdateResult,
    DeleteResult
)