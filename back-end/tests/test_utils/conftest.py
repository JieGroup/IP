from __future__ import annotations

import json
import unittest

from base64 import b64encode

from tests import TestConfig

from bson import ObjectId

from app import (
    create_app, 
    pyMongo
)

from app.database.api import (
    search_document,
    create_document,
    update_document
)

from app.process.api import (
    get_hashed_password,
    get_unique_id
)


