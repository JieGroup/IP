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
            database_type='user'
        )
        return

    @pytest.mark.parametrize("expected_res", [
        Cursor
    ])
    def test_get_all_documents(self, expected_res):
        assert expected_res == type(get_all_documents(
            database_type='user'
        ))
        return

    @pytest.mark.parametrize("user_id", [
        '412312',
        '66767'
    ])
    def test_search_document(self, user_id):
        '''simply test if survey template search document can be used'''
        msg = 'Cannot find the document'
        with pytest.raises(ValueError, match=msg):
            search_document(
                database_type='user',
                user_id=user_id
            )
        return

    @pytest.mark.parametrize("user_id, username, email, hashed_password, authority_level, confirm_email, designed_survey_template, expected", 
        [
            (
                '412312', 
                'static', 
                '55444',
                '66666',
                'user',
                True,
                {},
                InsertOneResult
            ),
            (
                '412312', 
                'static', 
                '55444',
                '66666',
                'user',
                False,
                {},
                InsertOneResult
            ),
        ]
    )
    def test_create_document(self, user_id, username, email, hashed_password, authority_level, confirm_email, designed_survey_template, expected):
        '''simply test if survey template create document can be used'''
        assert expected == type(create_document(
            database_type='user',
            user_id=user_id,
            username=username,
            email=email,
            hashed_password=hashed_password,
            authority_level=authority_level,
            confirm_email=confirm_email,
            designed_survey_template=designed_survey_template
        ))
        return