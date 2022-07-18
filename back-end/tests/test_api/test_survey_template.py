from __future__ import annotations

import json
import pytest

from tests.conftest import (
    get_test_client,
    get_token_auth_headers
)

from .utils import get_api_url

from app.process.api import SurveyTemplate

from app.utils.api import Constant


class TestCreateSurveyTemplate():

    @pytest.mark.parametrize(
        "method, time, number, rounds, survey_topics, expected", 
        [
            (   
                'static',
                '5',
                Constant.MAX_NUMBER_OF_COPIES,
                Constant.MAX_ROUNDS,
                {
                    'age': {
                        'answer_type': 'continuous',
                        'continuous_range': {
                            'min': 0,
                            'max': 80
                        },
                        'topic_question': 'what is your choice?',
                        'unit': 'xx'
                    }
                }, 
                str
            ),
        ]
    )
    def test_create_survey_template(self, method, time, number, rounds, survey_topics, expected):
        
        client = get_test_client()
        data = json.dumps({
            'survey_update_method': method,
            'time_period': time,
            'number_of_copies': number,
            'max_rounds': rounds,
            'survey_topics': survey_topics
        })
        print(type(data))
        headers = get_token_auth_headers()
        response = client.post(
            get_api_url('create_survey_template'), 
            headers=headers, 
            data=data
        )
        assert response.status_code == 200
        json_response = json.loads(response.get_data(as_text=True))
        assert expected == type(json_response['survey_template_id'])
    
    