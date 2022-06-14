# -*- coding: utf-8 -*-
''' Create instance of these flask extensions '''
from flask_cors import CORS
from flask_mail import Mail
from flask_pymongo import PyMongo

cors = CORS()
mail = Mail()
pyMongo = PyMongo()
