from __future__ import annotations

import json
import pytest


class ErrorHandler():

    '''
    Test @application.errorhandler(Exception) wrapper
    in app.__init__.py.configure_errorhandlers()
    '''

    @pytest.mark.parametrize("key, container, expected", [
        (['key1', 'key2', 'key3'], {}, {'key1': {'key2': {}}}),
        (['key1'], {}, {})
    ])
    def test_error_handler(self):
        
        # with pytest.raises():
        print('zzzz')
        # for rule in self.client.url_map.iter_rules():
        #     print('shima:', rule)
        for rule in self.app.url_map.iter_rules():
            print('tiana', rule)
        # response = self.client.post('/api/ceshierror')
        # response = self.client.post('/ceshierror')
        # with pytest.raises(KeyError):
        response = self.client.post('/api/ceshierror')
        self.assertEqual(response.status_code, 500)
        json_response = json.loads(response.get_data(as_text=True))
        print(f'~~###: {response.status_code, json_response}')

        assert 5 == 5
        # print('**', key, container)
        # assert container == expected 

    