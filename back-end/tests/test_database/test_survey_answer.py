import pytest

from .conftest import (
    get_all_documents_count,
    get_all_documents,
    create_document,
    search_document,
    update_document,
    delete_document,
    delete_multiple_documents
)

from pymongo.cursor import Cursor

from app._typing import MTurkID


class TestSurveyAnswer:

    @pytest.mark.parametrize("expected_res", [
        0
    ])
    def test_get_all_documents_count(self, expected_res):
        assert expected_res == get_all_documents_count(
            database_type='survey_answer'
        )
        return

    @pytest.mark.parametrize("expected_res", [
        Cursor
    ])
    def test_get_all_documents(self, expected_res):
        assert expected_res == type(get_all_documents(
            database_type='survey_answer'
        ))
        return

    @pytest.mark.parametrize("ans_id", [
        '412312',
        '66767'
    ])
    def test_search_document(self, ans_id):
        '''simply test if survey answer search document can be used'''
        msg = 'Cannot find the document'
        with pytest.raises(ValueError, match=msg):
            search_document(
                database_type='survey_answer',
                survey_answer_id=ans_id
            )
        return

    @pytest.mark.parametrize("ans_id, tem_id, mturk_id", [
        ('412312', '512412', 'dfsdf'),
        ('66767', '124123', '6123412')
    ])
    def test_create_document(self, ans_id, tem_id, mturk_id):
        '''simply test if survey answer create document can be used'''
        create_document(
            database_type='survey_answer',
            survey_answer_id=ans_id,
            survey_template_id=tem_id,
            mturk_id=mturk_id
        )
        return
    
    @pytest.mark.parametrize("rounds, tem_id, new_answers", [
        (1, '512412', {}),
        (2, '124123', {'5': '6'})
    ])
    def test_update_document(self, rounds, tem_id, new_answers):
        '''simply test if survey answer update document can be used'''
        msg = 'Cannot update the document'
        with pytest.raises(ValueError, match=msg):
            update_document(
                database_type='survey_answer',
                cur_rounds_num=rounds,
                survey_answer_id=tem_id,
                survey_new_answers=new_answers
            )
        return
    
    @pytest.mark.parametrize("ans_id", [
        'sdasd',
        'ascasca'
    ])
    def test_delete_document(self, ans_id):
        '''simply test if survey answer delete document can be used'''
        msg = 'Cannot delete the document'
        with pytest.raises(ValueError, match=msg):
            delete_document(
                database_type='survey_answer',
                survey_answer_id=ans_id,
            )
        return
    
    @pytest.mark.parametrize("ans_id, tem_id, mturk_id", [
        ('412312', '512412', '7766'),
        ('66767', '124123', '6123412')
    ])
    def test_create_document_storage(self, ans_id, tem_id, mturk_id):
        '''
        1. Create a document
        2. Check if we can search the above document
        '''
        create_document(
            database_type='survey_answer',
            survey_answer_id=ans_id,
            survey_template_id=tem_id,
            mturk_id=mturk_id
        )

        document = search_document(
            database_type='survey_answer',
            survey_answer_id=ans_id
        )

        assert document['survey_template_id'] == tem_id
        assert document['mturk_id'] == mturk_id

    @pytest.mark.parametrize("ans_id, tem_id, mturk_id", [
        ('412312', '512412', '7766'),
        ('66767', '124123', '6123412')
    ])
    def test_delete_multiple_documents(self, ans_id, tem_id, mturk_id):
        '''
        1. Create a document
        2. Check if we can search the above document
        '''
        create_document(
            database_type='survey_answer',
            survey_answer_id=ans_id,
            survey_template_id=tem_id,
            mturk_id=mturk_id
        )

        create_document(
            database_type='survey_answer',
            survey_answer_id=ans_id+'123',
            survey_template_id=tem_id,
            mturk_id=mturk_id+'123'
        )

        res = delete_multiple_documents(
            database_type='survey_answer',
            survey_template_id=tem_id
        )
        assert res.deleted_count == 2
        