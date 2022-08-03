from __future__ import annotations

import json
import pytest
import requests

from tests.conftest import (
    get_test_client,
    get_token_auth_headers
)

from .utils import (
    get_api_url,
    select_first_option,
    stop_first_topic
)

from app.utils.api import Constant

from app.process.api import (
    SurveyTemplate,
    VoterAnswerSurvey
)

from app.error import DBDocumentNotFound


class TestCeshi():

    def test_ceshi(self):
        
        client = get_test_client()
        headers = get_token_auth_headers()
        response = client.post(
            get_api_url('ceshiyixia'), 
            headers=headers, 
        )





