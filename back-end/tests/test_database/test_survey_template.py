import pytest

from .conftest import (
    get_all_documents_count,
    get_all_documents,
    create_document,
    search_document,
    update_document,
    delete_document,
    Constant,
    InsertOneResult
)

from pymongo.cursor import Cursor

from app._typing import MTurkID


class TestTemplate:

    @pytest.mark.parametrize("expected_res", [
        1
    ])
    def test_get_all_documents_count(self, expected_res):
        assert expected_res == get_all_documents_count(
            database_type='survey_template'
        )
        return

    @pytest.mark.parametrize("expected_res", [
        Cursor
    ])
    def test_get_all_documents(self, expected_res):
        assert expected_res == type(get_all_documents(
            database_type='survey_template'
        ))
        return

    @pytest.mark.parametrize("survey_template_id", [
        '412312',
        '66767'
    ])
    def test_search_document(self, survey_template_id):
        '''simply test if survey template search document can be used'''
        msg = 'Cannot find the document'
        with pytest.raises(ValueError, match=msg):
            search_document(
                database_type='survey_template',
                survey_template_id=survey_template_id
            )
        return

    @pytest.mark.parametrize("tem_id, update_method, exp_time, number_of_copies, max_rounds, topics, expected", 
        [
            (
                '412312', 
                'static', 
                54545.5,
                500,
                3,
                {   
                    'test_key_1':
                    {
                        'answer_type': 'categorical',
                        Constant.CATEGORICAL_RANGE_KEY: 
                        {
                            'inclusion': [str(i) for i in range(10)]
                        }
                    }
                },
                InsertOneResult
            ),
            (
                '41231289689', 
                'static', 
                666666,
                600,
                2,
                {   
                    'test_key_1':
                    {
                        'answer_type': 'categorical',
                        Constant.CATEGORICAL_RANGE_KEY: 
                        {
                            'inclusion': [str(i) for i in range(10)]
                        }
                    }
                },
                InsertOneResult
            ),
        ]
    )
    def test_create_document(self, tem_id, update_method, exp_time, number_of_copies, max_rounds, topics, expected):
        '''simply test if survey template create document can be used'''
        assert expected == type(create_document(
            database_type='survey_template',
            survey_template_id=tem_id, 
            survey_update_method=update_method,
            expiration_time=exp_time,
            number_of_copies=number_of_copies,
            max_rounds=max_rounds,
            survey_topics=topics
        ))
        return