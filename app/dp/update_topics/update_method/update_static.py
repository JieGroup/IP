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




def gen_static_questions(randseed):
    '''
        generate all the unique questions (MAXSHOW on one page)
        according to the order in the const TOPICS_TYPE

        it is a special case to gen one question on a page
    '''

    # init a dict of question, each as a topic-param pair
    questions = {}

    est_remain_count = 0  # the num of estimated remaining questions

    for topic in Constant.TOPICS:

        # get all qustion-voter pairs, their count, and the latest answer
        # q_v_pair = db.session.query(QandA).filter_by(digits=session['digits'], topic=topic)
        # rounds = q_v_pair.count() # number of replications for a question-voter pair
        
        mongoDB_operator = select_mongoDB_operator('SurveyAnswer')
        # get all qustion-voter pairs, their count, and the latest answer
        survey_answer_document = mongoDB_operator.search_document(digits=session['digits'])
        # If there is no matched document, create one
        # Will modify later
        

        cur_topic_answer = None
        if survey_answer_document and 'survey_answers' in survey_answer_document and \
            topic in survey_answer_document['survey_answers']:
            cur_topic_answer = survey_answer_document['survey_answers'][topic]
        rounds = len(cur_topic_answer) if cur_topic_answer else 0

        # debug(rounds, 'rounds')
        if rounds > 0:
            continue

        est_remain_count += 1

        q = gen_static_q(topic)
        if q is not None:
            questions[topic] = q

    # debug(questions, 'questions')

    num = min(Constant.MAXSHOW, est_remain_count)

    session['progress_bar'] = 100 - int((est_remain_count-num) / len(Constant.TOPICS) * 100)
    
    myRandom = Random(randseed)

    # last page not random
    if num < Constant.MAXSHOW and session['entered_MTurk'] is False:
        questions['MTurk'] = gen_MTurk()
        num += 1
        # debug(questions, 'questions in the gen...')

        return questions

    return dict(myRandom.sample(questions.items(), num))


def gen_static_q(topic):
    '''
        for each topic determine the static question statement and the choices
        topic: string
        param: string that indicates the type of field
        choices: list of tuples for param='RadioField' or 'SelectField', or
                 list of two integers (lower and upper limits) for param='IntegerField'

    '''

    # stp = ('stop', f'not wish to answer') 

    if topic == 'gender':

        sentence = f'Your gender is'
        param = 'RadioField'
        choices = [(v, v) for v in Constant.ALPH_GENDER] #+ [stp]

    elif topic == 'race':

        sentence = f'Your race is'
        param = 'RadioField'
        choices = [(v, v) for v in Constant.ALPH_RACE] #+ [stp]

    elif topic == 'age':

        sentence = f'Your age is'
        param = 'IntegerField'
        choices = Constant.NUM_AGE

    elif topic == 'education':

        sentence = f'Your education level is'
        param = 'RadioField'
        choices = [(v, v) for v in Constant.ALPH_EDUCATION] #+ [stp]

    elif topic == 'zip':

        # TODO: this is an interesting design to test the correctness of the answer
        sentence = f'The first two digits of your zipcode (e.g., 2 of 02138) is'
        param = 'IntegerField'
        choices = Constant.NUM_ZIP

    elif topic == 'hours_web':

        sentence = f'How many hours do you browse web per day'
        # param = 'SelectField'
        # step = 1
        # l = np.arange(num_hours_web[0], num_hours_web[1], step).astype(int).tolist()
        # choices = [('', 'Please select')]
        # choices += [(f'{v}', f'{v} to {v+step}') for v in l]
        # choices += [(f'>{l[-1]}', f'greater than {l[-1]}')] #+ [stp]

        param = 'IntegerField'
        choices = Constant.NUM_HOURS_WEB

    elif topic == 'politics':

        sentence = f'The best word to describe your political position is'
        param = 'RadioField'
        choices = [(v, v) for v in Constant.ALPH_PHLITICS] #+ [stp]

    elif topic == 'sexual_orientation':

        sentence = f'Your sexual orientation is'
        param = 'RadioField'
        choices = [(v, v) for v in Constant.ALPH_SEXUAL_ORIENTATION] #+ [stp]

    elif topic == 'spouse_age':

        sentence = f'Your spouse\'s age is (note: if not applicable please leave it blank or 0)'
        param = 'IntegerField'
        choices = Constant.NUMS_SPOUSE_AGE

    elif topic == 'social_class':

        sentence = f'You identify your social class as'
        param = 'RadioField'
        choices = [(v, v) for v in Constant.ALPH_SOCIAL_CLASS] #+ [stp]

    elif topic == 'no_houses':

        sentence = f'The number of houses you own is'
        # param = 'RadioField'
        # choices = [(v, v) for v in alph_no_houses] + [stp]
        param = 'IntegerField'
        choices = Constant.NUM_NO_HOUSES
        
    elif topic == 'health':

        sentence = f'At scale 1-10, you will score your health condition as'
        param = 'IntegerField'
        choices = Constant.NUM_HEALTH

    elif topic == 'salary':

        sentence = f'Your yearly salary is (unit: $1,000, e.g., 30 for $30,000) '
        # param = 'SelectField'
        # step = 10
        # l = np.arange(num_salary[0], num_salary[1], 10).astype(int).tolist()
        # choices = [('', 'Please select')]
        # choices += [(f'{v}', f'${v}k to ${v+10}k') for v in l]
        # choices += [(f'>{l[-1]+step}', f'greater than ${l[-1]+step}k')] + [stp]

        param = 'IntegerField'
        choices = Constant.NUM_SALARY

    elif topic == 'cash':

        sentence = f'Your overall available cash is (unit: $1,000, e.g., 30 for $30,000) '
        # param = 'SelectField'
        # step = 10
        # l = np.arange(num_cash[0], num_cash[1], 10).astype(int).tolist()
        # choices = [('', 'Please select')]
        # choices += [(f'{v}', f'${v}k to ${v+10}k') for v in l]
        # choices += [(f'>{l[-1]+step}', f'greater than ${l[-1]+step}k')] + [stp]

        param = 'IntegerField'
        choices = Constant.NUM_CASH

    elif topic == 'stock':

        sentence = f'Your overall stock investment is (unit: $1,000, e.g., 30 for $30,000) '
        # param = 'SelectField'
        # step = 10
        # l = np.arange(num_stock[0], num_stock[1], step).astype(int).tolist()
        # choices = [('', 'Please select')]
        # choices += [(f'{v}', f'${v}k to ${v+step}k') for v in l]
        # choices += [(f'>{l[-1]+step}', f'greater than ${l[-1]+step}k')] + [stp]

        param = 'IntegerField'
        choices = Constant.NUM_STOCK

    elif topic == 'sex':

        sentence = f'How many times do you have sex in a month?'
        # param = 'SelectField'
        # step = 5
        # l = np.arange(num_sex[0], num_sex[1], step).astype(int).tolist()
        # choices = [('', 'Please select')]
        # choices += [(f'{v}', f'{v} to {v+step}') for v in l]
        # choices += [(f'>{l[-1]+step}', f'greater than {l[-1]+step}')] + [stp]

        param = 'IntegerField'
        choices = Constant.NUM_SEX

    else:
        debug('not valid topic!')

    # return (param, sentence, choices) triplet
    return (param, sentence, choices)
