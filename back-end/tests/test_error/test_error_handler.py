from __future__ import annotations

from tests.conftest import get_test_client
import json
import pytest


class TestErrorHandler:
    '''
    Test @application.errorhandler(Exception) wrapper
    in app.__init__.py.configure_errorhandlers()
    '''
    def test_error_handler(self):
        
        # with pytest.raises():
        print('zzzz')
        # for rule in self.client.url_map.iter_rules():
        #     print('shima:', rule)
        # for rule in self.app.url_map.iter_rules():
        #     print('tiana', rule)
        client = get_test_client()
        # response = self.client.post('/api/ceshierror')
        # response = self.client.post('/ceshierror')
        # with pytest.raises(KeyError):
        response = client.post('/api/ceshierror')
        assert response.status_code == 500
        json_response = json.loads(response.get_data(as_text=True))
        print(f'~~###: {response.status_code, json_response}')

        assert 5 == 5
        # print('**', key, container)
        # assert container == expected 

    