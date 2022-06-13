# from __future__ import annotations

# import json

# from base64 import b64encode
# from app import create_app, pyMongo
# from tests import TestConfig

# class UnittestBase:

#     def setUp(self):

#         '''
#         Execute before every test
#         '''

#         self.app = create_app(TestConfig)  # 创建Flask应用
#         self.app_context = self.app.app_context()  # 激活(或推送)Flask应用上下文
#         self.app_context.push()
#         # db.create_all()  # 通过SQLAlchemy来使用SQLite内存数据库，db.create_all()快速创建所有的数据库表
#         self.client = self.app.test_client()  # Flask内建的测试客户端，模拟浏览器行为

#     def tearDown(self, app_context):

#         '''
#         Execute after every test
#         '''

#         # db.session.remove()
#         self.drop_db_collections()
#         app_context.pop()  # 退出Flask应用上下文

#     def drop_db_collections(self):

#         '''
#         clean database
#         '''

#         for collecion_names in pyMongo.db.list_collection_names():
#             pyMongo.db.drop_collection(collecion_names)

#     def get_basic_auth_headers(self, username, password):
#         '''创建Basic Auth认证的headers'''
#         return {
#             'Authorization': 'Basic ' + b64encode(
#                 (username + ':' + password).encode('utf-8')).decode('utf-8'),
#             'Accept': 'application/json',
#             'Content-Type': 'application/json'
#         }

#     def get_token_auth_headers(self, username, password):
#         '''创建JSON Web Token认证的headers'''
#         headers = self.get_basic_auth_headers(username, password)
#         response = self.client.post('/auth/tokens', headers=headers)
#         assert response.status_code == 200
#         json_response = json.loads(response.get_data(as_text=True))
#         assert json_response is not None
#         token = json_response['token']
#         return {
#             'Authorization': 'Bearer ' + token,
#             'Accept': 'application/json',
#             'Content-Type': 'application/json'
#         }