from __future__ import annotations

import json
import pytest

from app.utils.api import Constant

from app.process.api import (
    SurveyTemplate,
    VoterAnswerSurvey
)

from app.error import DBDocumentNotFound


class TestVoterAnswerSurvey():

    @pytest.mark.parametrize(
        "method, time, number, rounds, survey_topics, mturk_id", 
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
                '123'
            ),
        ]
    )
    def test_start_answering(self, method, time, number, rounds, survey_topics, mturk_id):

        survey_template_id = SurveyTemplate.create_survey_template(
            survey_update_method=method,
            time_period=time,
            number_of_copies=number,
            max_rounds=rounds,
            survey_topics=survey_topics
        )
        res = VoterAnswerSurvey.start_answering(
            survey_template_id=survey_template_id,
            mturk_id=mturk_id
        )
        assert res['survey_template_id'] == survey_template_id
        assert res['survey_topics'] == survey_topics

    @pytest.mark.parametrize(
        "method, time, number, rounds, survey_topics, mturk_id", 
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
                '123'
            ),
        ]
    )
    def test_start_answering_exception(self, method, time, number, rounds, survey_topics, mturk_id):

        survey_template_id = SurveyTemplate.create_survey_template(
            survey_update_method=method,
            time_period=time,
            number_of_copies=number,
            max_rounds=rounds,
            survey_topics=survey_topics
        )
        msg = 'Cannot find the document'
        with pytest.raises(ValueError, match=msg):
            VoterAnswerSurvey.start_answering(
                survey_template_id='11',
                mturk_id=mturk_id
            )

    
    
    