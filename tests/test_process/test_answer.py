from __future__ import annotations

import json
import pytest

from tests.conftest import UnittestBase

from app.process.api import VoterAnswerSurvey

from app.utils.api import Constant


class TestVoterAnswerSurvey(UnittestBase):

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
    
    @pytest.mark.parametrize(
        "number_of_copies, expected", 
        [
            (Constant.MAX_NUMBER_OF_COPIES+1, False),
            (Constant.MAX_NUMBER_OF_COPIES, True),
            (0, False)
        ]
    )
    def test_is_number_of_copies_valid(self, number_of_copies, expected):

        assert expected == SurveyTemplate._SurveyTemplate__is_number_of_copies_valid(
            number_of_copies=number_of_copies
        )

    @pytest.mark.parametrize(
        "max_rounds, expected", 
        [
            (Constant.MAX_ROUNDS+1, False),
            (Constant.MAX_ROUNDS, True),
            (0, False)
        ]
    )
    def test_is_max_rounds_valid(self, max_rounds, expected):

        assert expected == SurveyTemplate._SurveyTemplate__is_max_rounds_valid(
            max_rounds=max_rounds
        )

    @pytest.mark.parametrize(
        "method, time, number, rounds, survey_topics, expected", 
        [
            (   
                'static',
                Constant.TIME_PERIOD_LOWER_LIMIT,
                Constant.MAX_NUMBER_OF_COPIES,
                Constant.MAX_ROUNDS,
                {
                    'age': {
                        'answer_type': 'continuous',
                        'continuous_range': {
                            'min': 0,
                            'max': 80
                        }
                    }
                }, 
                str
            ),
        ]
    )
    def test_create_survey_template(self, method, time, number, rounds, survey_topics, expected):
        
        assert expected == type(SurveyTemplate.create_survey_template(
            survey_update_method=method,
            time_period=time,
            number_of_copies=number,
            max_rounds=rounds,
            survey_topics=survey_topics
        ))
    
    