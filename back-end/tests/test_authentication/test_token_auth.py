import pytest

from app.utils.api import (
    Constant,
    Time
)

from app.authentication.basic_auth import (
    verify_password
)

from app.authentication.token_auth import (
    get_voterToken,
    verify_token
)

from app.process.api import get_unique_id

from tests.conftest import register_account


class TestTokenAuth:

    @pytest.mark.parametrize("username, pwd, tem_id, mturk_id, expected_res", [
        (
            get_unique_id(),
            'Xie1@456',
            get_unique_id(),
            get_unique_id(),
            True
        ),
    ])
    def test_voterToken(self, username, pwd, tem_id, mturk_id, expected_res):
        register_account(username=username)

        verify_password(
            username=username,
            password=pwd
        )

        voterToken = get_voterToken(
            survey_template_id=tem_id,
            mturk_id=mturk_id
        )['voterToken']
        
        assert expected_res == verify_token(token=voterToken)