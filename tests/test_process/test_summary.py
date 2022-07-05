from __future__ import annotations

import json
import pytest

from app.process.api import Summary

from app.utils.api import Constant


class TestSummary():

    @pytest.mark.usefixtures('network_instance')
    @pytest.mark.parametrize(
        "survey_update_method, expected", 
        [
            ('randomUpdate', False),
            ('static', True),
            ('uniform', True)
        ]
    )
    def test_if_survey_update_method_valid(self, survey_update_method, expected):
        
        assert expected == SurveyTemplate._SurveyTemplate__if_survey_update_method_valid(
            survey_update_method=survey_update_method
        )
    
    