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
        0
    ])
    def test_get_all_documents_count(self, expected_res):
        assert expected_res == get_all_documents_count(
            database_type='voter'
        )
        return

    @pytest.mark.parametrize("expected_res", [
        Cursor
    ])
    def test_get_all_documents(self, expected_res):
        assert expected_res == type(get_all_documents(
            database_type='voter'
        ))
        return

    @pytest.mark.parametrize("mturk_id", [
        '412312',
        '66767'
    ])
    def test_search_document(self, mturk_id):
        '''simply test if voter search document can be used'''
        msg = 'Cannot find the document'
        with pytest.raises(ValueError, match=msg):
            search_document(
                database_type='voter',
                mturk_id=mturk_id
            )
        return

    @pytest.mark.parametrize("mturk_id, participated_survey_template_id, expected", 
        [
            (
                '412312', 
                {},
                InsertOneResult 
            ),
            (
                'sdfasdf', 
                {'a': 6},
                InsertOneResult 
            ),
        ]
    )
    def test_create_document(self, mturk_id, participated_survey_template_id, expected):
        '''simply test if voter create document can be used'''
        assert expected == type(create_document(
            database_type='voter',
            mturk_id=mturk_id,
            participated_survey_template_id=participated_survey_template_id,
        ))
        return