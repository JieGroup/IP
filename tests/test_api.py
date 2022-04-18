import json
import unittest

from base64 import b64encode
from datetime import datetime, timedelta
from bson import ObjectId
from app import create_app, pyMongo

from tests import TestConfig

class user_API_TestCase(unittest.TestCase):

    def setUp(self):
        '''每个测试之前执行'''
        self.app = create_app(TestConfig)  # 创建Flask应用
        self.app_context = self.app.app_context()  # 激活(或推送)Flask应用上下文
        self.app_context.push()
        # db.create_all()  # 通过SQLAlchemy来使用SQLite内存数据库，db.create_all()快速创建所有的数据库表
        self.client = self.app.test_client()  # Flask内建的测试客户端，模拟浏览器行为

    def tearDown(self):
        '''每个测试之后执行'''
        # db.session.remove()
        # db.drop_all()  # 删除所有数据库表
        self.drop_db_collections()
        self.app_context.pop()  # 退出Flask应用上下文

    def drop_db_collections(self):
        for collecion_names in pyMongo.db.list_collection_names():
            pyMongo.db.drop_collection(collecion_names)

    def test_placeholder(self):
        pass