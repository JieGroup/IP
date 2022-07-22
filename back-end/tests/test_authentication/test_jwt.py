import pytest

from pymongo.cursor import Cursor

from app._typing import MTurkID

from app.utils.api import (
    Constant,
    Time
)

from app.authentication.api import JwtManipulation


class TestJWT:

    # @pytest.mark.parametrize("token, expected_res", [
    #     (
    #         {
    #             'exp': Time.get_expiration_utc_time(time_period=Constant.UPDATE_TOKEN_INTERVAL)
    #         },
    #         True
    #     ),
    #     (
    #         {
    #             'exp': Time.get_expiration_utc_time(time_period=Constant.UPDATE_TOKEN_INTERVAL+40)
    #         },
    #         False
    #     )
    # ])
    # def test_is_jwt_needing_update(self, token, expected_res):
    #     assert expected_res == JwtManipulation.is_jwt_needing_update(
    #         token_payload=token
    #     )
    #     return

    # @pytest.mark.parametrize("id, name, level, exp, iat, expected_res", [
    #     (
    #         '1',
    #         '2',
    #         '3',
    #         4,
    #         5,
    #         {
    #             'user_id': '1',
    #             'username': '2',
    #             'authority_level': '3',
    #             'exp': 4,
    #             'iat': 5
    #         }
    #     )
    # ])
    # def test_form_userToken(self, id, name, level, exp, iat, expected_res):
        
    #     assert expected_res == JwtManipulation._JwtManipulation__form_userToken(
    #         user_id=id,
    #         username=name,
    #         authority_level=level,
    #         exp=exp,
    #         iat=iat
    #     )
    #     return
    
    # @pytest.mark.parametrize("id, mturk, level, exp, iat, expected_res", [
    #     (
    #         '1',
    #         '2',
    #         '3',
    #         4,
    #         5,
    #         {
    #             'survey_template_id': '1',
    #             'mturk_id': '2',
    #             'authority_level': '3',
    #             'exp': 4,
    #             'iat': 5
    #         }
    #     )
    # ])
    # def test_form_voterToken(self, id, mturk, level, exp, iat, expected_res):
        
    #     assert expected_res == JwtManipulation._JwtManipulation__form_voterToken(
    #         survey_template_id=id,
    #         mturk_id=mturk,
    #         authority_level=level,
    #         exp=exp,
    #         iat=iat
    #     )
    #     return

    @pytest.mark.parametrize("role, user_info", [
        (
            'user',
            {
                'user_id': '1',
                'username': '2',
                'authority_level': '3',
                'exp': 4,
                'iat': 5
            }
        ),
        (
            'voter',
            {
                'survey_template_id': '1',
                'mturk_id': '2',
                'authority_level': 'voter',
                'exp': 4,
                'iat': 5
            }
        )
    ])
    def test_encode_decode_token(self, role, user_info):
        '''
        Notes
        -----
        voter's authority level can only be voter
        '''
        token = JwtManipulation.get_jwt(
            role=role,
            cur_user_info=user_info
        )
        decode_token = JwtManipulation.decode_jwt(token)
        for key, val in decode_token.items():
            if key != 'exp' and key != 'iat':
                assert user_info[key] == val