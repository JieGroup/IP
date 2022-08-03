# -*- coding: utf-8 -*-
import logging

from flask import Flask
from flask import current_app

from app.extensions import (
    cors, 
    mail,
    pyMongo
)

from app.api import api
from app.authentication import authentication_bp

def create_app(config_class=None):
    '''Factory Pattern: Create Flask app.'''
    # pymysql.install_as_MySQLdb()
    application = Flask(__name__, template_folder='./process/templates/')

    # Initialization flask app
    configure_app(application, config_class)
    configure_blueprints(application)
    configure_extensions(application)

    configure_before_handlers(application)
    configure_after_handlers(application)
    configure_errorhandlers(application)
    
    handler = logging.FileHandler('flask.log', encoding='UTF-8')   # 设置日志字符集和存储路径名字
    logging_format = logging.Formatter(                            # 设置日志格式
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    application.logger.addHandler(handler)
    return application


def configure_app(application, config_class):
    application.config.from_object(config_class)
    
    # 不检查路由中最后是否有斜杠/
    application.url_map.strict_slashes = False


def configure_blueprints(application):
    # 注册 blueprint

    application.register_blueprint(authentication_bp)
    application.register_blueprint(api)

def configure_extensions(application):
    '''Configures the extensions.'''

    # Enable CORS
    cors.init_app(application)

    # Init email service
    mail.init_app(application)

    pyMongo.init_app(application)
    create_MongoDB_Collections()


def create_MongoDB_Collections():

    collection_list = pyMongo.db.list_collection_names()
    if 'SurveyTemplate' not in collection_list:
        pyMongo.db.SurveyTemplate.insert_one({"survey_template_id": 'placeholder'})
        pyMongo.db.SurveyTemplate.create_index([("survey_template_id", 1)], unique=True)

    if 'SurveyAnswer' not in collection_list:
        pyMongo.db.SurveyAnswer.create_index([("survey_answer_id", 1)], unique=True)
        pyMongo.db.SurveyAnswer.create_index([("survey_template_id", 1)], unique=False)
        # TODO: 也许survey_template_id和mturk_id要一个联合索引

    if 'SurveySummary' not in collection_list:
        pyMongo.db.SurveySummary.create_index([("survey_template_id", 1)], unique=True)

    if 'Voter' not in collection_list:
        pyMongo.db.Voter.create_index([("mturk_id", 1)], unique=True)

    if 'User' not in collection_list:
        pyMongo.db.User.create_index([("user_id", 1)], unique=True)


def configure_before_handlers(application):
    '''Configures the before request handlers'''
    pass


def configure_after_handlers(application):
    '''Configures the after request handlers'''
    pass


def configure_errorhandlers(application):
    from werkzeug.exceptions import HTTPException
    # from app.utils.api import handle_response
    '''Configures the error handlers'''
    from flask.json import jsonify
    @application.errorhandler(Exception)
    def handle_error(e):
        print('errorrrzaizhe', e, type(e).__name__, dir(e))
        # print(e.args)
        print('exception', Exception)
        # print('resssponses', e.name)
        # unauthorized error
        # if e == 401:
        #     return jsonify(
        #         error_msg='please login',
        #         error_name='unauthorized'
        #     ), 401
        current_app.logger.warning({
            'error_msg': str(e),
            'error_name': type(e).__name__
        })

        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        return jsonify(
            error_msg=str(e),
            error_name=type(e).__name__
        ), code