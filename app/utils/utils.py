import sys
import uuid
import random
import string
import numpy as np

from numpy.random import randint
from random import Random
from flask import session

from app import database, pyMongo
from app.utils.constant import Constant
from app.database import select_mongoDB_operator

def clean_db_utils():
    for collecion_names in pyMongo.db.list_collection_names():
        pyMongo.db.drop_collection(collecion_names)

def combine_response(response, new_response):
    for key, val in new_response.items():
        response[key] = val
    return

SIMPLE_CHARS = string.digits
def get_random_digits(length=8):
    return ''.join(random.choice(SIMPLE_CHARS) for i in range(length))

def obtain_unique_id():
    unique_id = str(uuid.uuid1())
    return unique_id

def gen_MTurk():
    '''last questionL MTurk User ID'''
    # sentence = f'Your M-Turk User ID is '
    sentence = f'Please input 4 digits randomly '
    param = 'StringField'
    choices = None

    return (param, sentence, choices)


def debug(var, msg=''):
    print('Jie debug '+msg, file=sys.stdout)
    print(var, file=sys.stdout)
