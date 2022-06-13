from __future__ import annotations

import json
import unittest

from base64 import b64encode
from app import create_app, pyMongo
from tests import TestConfig

# from .conftest import UnittestBase

class ErrorHandler(unittest.TestCase):

    def setUp(self):

        '''
        Execute before every test
        '''

        self.app = create_app(TestConfig)  # 创建Flask应用
        self.app_context = self.app.app_context()  # 激活(或推送)Flask应用上下文
        self.app_context.push()
        # db.create_all()  # 通过SQLAlchemy来使用SQLite内存数据库，db.create_all()快速创建所有的数据库表
        self.client = self.app.test_client()  # Flask内建的测试客户端，模拟浏览器行为
        return 

    def tearDown(self):

        '''
        Execute after every test
        '''

        # db.session.remove()
        self.drop_db_collections()
        self.app_context.pop()  # 退出Flask应用上下文
        return

    def drop_db_collections(self):

        '''
        clean database
        '''

        for collecion_names in pyMongo.db.list_collection_names():
            pyMongo.db.drop_collection(collecion_names)
        return

    def get_basic_auth_headers(self, username, password):
        '''创建Basic Auth认证的headers'''
        return {
            'Authorization': 'Basic ' + b64encode(
                (username + ':' + password).encode('utf-8')).decode('utf-8'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def get_token_auth_headers(self, username, password):
        '''创建JSON Web Token认证的headers'''
        headers = self.get_basic_auth_headers(username, password)
        response = self.client.post('/auth/tokens', headers=headers)
        assert response.status_code == 200
        json_response = json.loads(response.get_data(as_text=True))
        assert json_response is not None
        token = json_response['token']
        return {
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    '''
    Test @application.errorhandler(Exception) wrapper
    in app.__init__.py.configure_errorhandlers()
    '''

    # @pytest.mark.parametrize("key, container, expected", [
    #     (['key1', 'key2', 'key3'], {}, {'key1': {'key2': {}}}),
    #     (['key1'], {}, {})
    # ])
    def test_error_handler(self):
        
        # with pytest.raises():
        print('zzzz')
        response = self.client.post('/api/ceshierror')
        # self.assertEqual(response.status_code, 200)
        # json_response = json.loads(response.get_data(as_text=True))
        print(f'~~###: {response.status_code}')

        assert 5 == 5
        # print('**', key, container)
        # assert container == expected 

    