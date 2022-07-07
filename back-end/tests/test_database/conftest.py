from __future__ import annotations

import pytest

from app.database.api import (
    get_all_documents_count,
    get_all_documents,
    create_document,
    search_document,
    update_document,
    delete_document
)

from app.utils.api import Constant

from pymongo.results import (
    InsertOneResult,
    UpdateResult,
    DeleteResult
)