from __future__ import annotations

import json
import pytest

from tests.conftest import UnittestBase
from app.process.api import VoterAnswerSurvey

class TestVoterAnswerSurvey(UnittestBase):

    def test_start_answering(self):
        VoterAnswerSurvey.start_answering(
            survey_template_id=5,
            mturk_id=5
        )
        pass

    def test_update_survey_topics(self):
        pass

    
    