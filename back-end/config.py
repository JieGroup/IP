import os
from datetime import timedelta
from redis import Redis
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    
    DEBUG = True
    SECRET_KEY = 'adasdaxcwxq4213'

    # JWT secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Survey'

    # sqlite
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # MongoDB
    # local_host = '127.0.0.1'
    # Database_name = 'mysynspot_db'
    # Database_name = 'unittest_db'
    # MONGO_URI = "mongodb://%s:27017/%s" % (local_host, Database_name)

    database_root_user_password = '11ZWcXeLjFSm1k0Y'
    database_name = 'survey_db'
    # Database_name = 'unittest_db'
    MONGO_URI = 'mongodb+srv://dingj-umnedu:%s@surveycluster.kspby.mongodb.net/%s?retryWrites=true&w=majority' % (database_root_user_password, database_name)
    # MONGO_URI = "mongodb://%s:27017" % (local_host)
    

    # MESSAGES_PER_PAGE = 10

    # gmail for email validation
    # gmail account: apolloumn.email@gmail.com
    # gmail password: apolloumn
    # app password: wvduhthxrmktdxjb
    # MAIL_SERVER ='smtp.gmail.com'
    # MAIL_PORT = 465
    # MAIL_USERNAME = 'apolloumn.email@gmail.com'
    # MAIL_PASSWORD = 'wvduhthxrmktdxjb'
    # MAIL_USE_SSL = True
    # MAIL_DEFAULT_SENDER = 'apolloumn.email@gmail.com'
    # SECURITY_PASSWORD_SALT = 'zxsdfasdvasdafwe'


class ProductionConfig(Config):

    pass

class DevelopmentConfig(Config):
  
    pass
    

class TestingConfig(Config):
    
    pass