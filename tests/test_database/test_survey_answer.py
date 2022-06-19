import pytest

from app.database.api import (
    get_all_documents_count,
    get_all_documents,
    create_document,
    search_document,
    update_document,
    delete_document
)

from tests.conftest import get_test_client

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

    # @pytest.mark.parametrize("expected_res", [
    #     None
    # ])
    # def test_get_all_documents(self, expected_res):

    #     assert expected_res == get_all_documents(
    #         database_type='survey_answer'
    #     )
    #     return

    @pytest.mark.parametrize("ans_id, expected_res", [
        ('412312', None),
        ('66767', None)
    ])
    def test_search_document(self, ans_id, expected_res):

        res = search_document(
            database_type='survey_answer',
            survey_answer_id=ans_id
        )
        print(f'res: {res}')
        assert expected_res == res
        return

    # @pytest.mark.parametrize("ans_id, tem_id, mturk_id, expected_res", [
    #     ('412312', '512412', 'dfsdf', None),
    #     ('66767', '124123', '6123412', None)
    # ])
    # def test_create_document(self, ans_id, tem_id, mturk_id, expected_res):

    #     assert expected_res == create_document(
    #         database_type='survey_answer',
    #         survey_answer_id=ans_id,
    #         survey_template_id=tem_id,
    #         mturk_id=mturk_id
    #     )
    #     return
    
    # @pytest.mark.parametrize("ans_id, tem_id, mturk_id, expected_res", [
    #     ('412312', '512412', 'dfsdf', None),
    #     ('66767', '124123', '6123412', None)
    # ])
    # def test_update_document(self, ans_id, tem_id, mturk_id, expected_res):

    #     assert expected_res == create_document(
    #         database_type='survey_answer',
    #         survey_answer_id=ans_id,
    #         survey_template_id=tem_id,
    #         mturk_id=mturk_id
    #     )
    #     return
    
    # def test_delete_document(self, DatabaseOperator_instance, test_record, expected_res):
    #     DatabaseOperator_instance.set_database(database_type='train_sponsor_metadata')
    #     response = DatabaseOperator_instance.get_record(
    #         user_id=test_record[0], 
    #         train_id=test_record[1], 
    #     )
    #     assert response == expected_res