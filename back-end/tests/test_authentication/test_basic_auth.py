import pytest

from app.utils.api import (
    Constant,
    Time
)

from app.authentication.basic_auth import verify_password

from app.process.api import get_unique_id

from tests.conftest import register_account


class TestBasicAuth:

    @pytest.mark.parametrize("username, password, msg", [
        (
            get_unique_id(),
            get_unique_id(),
            'Cannot find the document'
        ),
    ])
    def test_verify_password_username_exception(self, username, password, msg):
        with pytest.raises(ValueError, match=msg):
            verify_password(
                username=username,
                password=password
            )
        return
    
    @pytest.mark.parametrize("username, password, msg", [
        (
            get_unique_id(),
            get_unique_id(),
            'password wrong'
        ),
    ])
    def test_verify_password_password_exception(self, username, password, msg):
        register_account(username=username)
        with pytest.raises(ValueError, match=msg):
            verify_password(
                username=username,
                password=password
            )
        return