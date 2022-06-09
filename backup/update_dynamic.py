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



def gen_dynamic_questions(randseed):
    '''
        generate all the unique and allowed questions (MAXSHOW on one page)
        according to the order in the const TOPICS_TYPE

        it is a special case to gen one question on a page
    '''

    # init a dict of question, each as a topic-param pair
    questions = {}

    est_remain_count = 0  # the num of estimated remaining questions

    mongoDB_operator = select_mongoDB_operator('SurveyAnswer')
    survey_answer_document = mongoDB_operator.search_document(digits=session['digits'])
    # If there is no matched document, create one
    # Will modify later
    # if survey_answer_document == None:
    #     survey_answer_id = obtain_unique_digits()
    #     survey_template_id = obtain_unique_digits()
    #     mturk_id = obtain_unique_digits()
    #     way = 'dynamic'
    #     mongoDB_operator.create_document(survey_answer_id=survey_answer_id, survey_template_id=survey_template_id,
    #                                      mturk_id=mturk_id, way=way, digits=session['digits'])

    for topic in Constant.TOPICS:

        # init for the historical param-question pairs of this voter
        prev_answers = {'left': [], 'right': []}

        # # get all qustion-voter pairs, their count, and the latest answer
        # q_v_pair = db.session.query(QandA).filter_by(digits=session['digits'], topic=topic)
        # rounds = q_v_pair.count() # number of replications for a question-voter pair
        # # debug(rounds, 'rounds')
        # if rounds > 0:
        #     # ordered by descending to obtain the latest answer
        #     q_v_latest_a = q_v_pair.order_by(desc(QandA.rounds)).first()
        #     if (rounds >= Constant.MAXREP) or (q_v_latest_a.answer=='stop'):
        #         continue
        #     else:
        #         for item in q_v_pair:
        #             prev_answers[item.answer].append(item.param)

                # print('Jie debug, prev_answers', prev_answers, file=sys.stdout)
        
        cur_topic_answer = None
        if survey_answer_document and 'survey_answers' in survey_answer_document and \
            topic in survey_answer_document['survey_answers']:
            cur_topic_answer = survey_answer_document['survey_answers'][topic]
            print(f'cur_topic_answer: {cur_topic_answer}')
            
        rounds = len(cur_topic_answer) if cur_topic_answer else 0
        if rounds > 0: 
            # obtain the latest answer
            rounds_key = f'rounds_{rounds}'
            q_v_latest_a = cur_topic_answer[rounds_key]
            if (rounds >= Constant.MAXREP) or (q_v_latest_a['answer'] == 'stop'):
                continue
            else:
                for rounds_key, value in cur_topic_answer.items():
                    prev_answers[value['answer']].append(value['answer_type'])

        q = gen_dynamic_q(topic, randseed, prev_answers=prev_answers)
        print(f'NEW q: {q}')
        if q is not None:
            questions[topic] = q

        est_remain_count += (Constant.MAXREP - rounds)

    # debug(questions, 'questions')

    num = min(Constant.MAXSHOW, len(questions))
    myRandom = Random(randseed)

    session['progress_bar'] = 100 - int((est_remain_count-num) / (len(Constant.TOPICS) * Constant.MAXREP) * 100)
    
    # last page not random
    if num < Constant.MAXSHOW and session['entered_MTurk'] is False:
        questions['MTurk'] = gen_MTurk()
        num += 1
        # debug(questions, 'questions in the gen...')

        return questions

    return dict(myRandom.sample(questions.items(), num))

def gen_dynamic_q(topic, randseed, prev_answers):

    
    '''
        for each topic and the corresponding params, which is a random integer
        determine the question statement and the choices
        topic: string
        prev_answers: dict of existing param-answer pairs

    '''

    if topic == 'gender':

        sentence = f'Your sexual orientation is'
        param, choices = gen_random_type2(prev_answers, randseed, alph=Constant.ALPH_GENDER)
        if param is None:
            return None

    elif topic == 'race':
        # https://2020census.gov/en/about-questions/2020-census-questions-race.html

        sentence = f'Your race is'
        param, choices = gen_random_type2(prev_answers, randseed, alph=Constant.ALPH_RACE)
        if param is None:
            return None

    elif topic == 'age':

        sentence = f'Your age is '
        param = gen_random_type1(prev_answers, randseed, low0=Constant.NUM_AGE[0], high0=Constant.NUM_AGE[1])
        if param is None:
            return None
        choices=[
            ('left', f'<= {param}'),
            ('right', f'> {param}'),
            ('stop', f'Not wish to answer')
            ]

    elif topic == 'education':
        # https://www.bls.gov/careeroutlook/2014/article/education-level-and-jobs.htm
        # chose the most frequent from the figure

        sentence = f'Your education level is'
        param, choices = gen_random_type2(prev_answers, randseed, alph=Constant.ALPH_EDUCATION)
        if param is None:
            return None

    elif topic == 'zip':
        # http://phaster.com/zip_code.html

        sentence = f'The first two digits of your zipcode (e.g., 2 of 02138) is'
        param = gen_random_type1(prev_answers, randseed, low0=Constant.NUM_ZIP[0], high0=Constant.NUM_ZIP[1])
        if param is None:
            return None
        choices=[
            ('left', f'<= {param}'),
            ('right', f'> {param}'),
            ('stop', f'Not wish to answer')
            ]

    elif topic == 'hours_web':
        # http://phaster.com/zip_code.html

        sentence = f'How many hours do you browse web per day'
        param = gen_random_type1(prev_answers, randseed, low0=Constant.NUM_HOURS_WEB[0], high0=Constant.NUM_HOURS_WEB[1])
        if param is None:
            return None
        choices=[
            ('left', f'<= {param} hours per day'),
            ('right', f'> {param} hours per day'),
            ('stop', f'Not wish to answer')
            ]

    elif topic == 'politics':
        # https://en.wikipedia.org/wiki/Political_spectrum

        sentence = f'The best word to describe your political position is'
        param, choices = gen_random_type2(prev_answers, randseed, alph=Constant.ALPH_PHLITICS)
        if param is None:
            return None

    elif topic == 'sexual_orientation':

        sentence = f'Your sexual orientation is'
        param, choices = gen_random_type2(prev_answers, randseed, alph=Constant.ALPH_SEXUAL_ORIENTATION)
        if param is None:
            return None

    elif topic == 'spouse_age':

        sentence = f'Your spouse\'s age is'
        param = gen_random_type1(prev_answers, randseed, low0=Constant.NUMS_SPOUSE_AGE[0], high0=Constant.NUMS_SPOUSE_AGE[1])
        if param is None:
            return None
        choices=[
            ('left', f'<= {param}'),
            ('right', f'> {param}'),
            ('stop', f'Not wish to answer or not applicable')
            ]

    elif topic == 'social_class':
        # https://udel.edu/~cmarks/What%20is%20social%20class.htm

        sentence = f'You identify your social class as'
        param, choices = gen_random_type2(prev_answers, randseed, alph=Constant.ALPH_SOCIAL_CLASS)
        if param is None:
            return None

    elif topic == 'no_houses':
        # https://udel.edu/~cmarks/What%20is%20social%20class.htm

        sentence = f'The number of houses you own is'
        # param, choices = gen_random_type2(prev_answers, randseed, alph=alph_no_houses)
        # if param is None:
        #     return None
        param = gen_random_type1(prev_answers, randseed, low0=Constant.NUM_NO_HOUSES[0], high0=Constant.NUM_NO_HOUSES[1])
        if param is None:
            return None
        choices=[
            ('left', f'<= {param}'),
            ('right', f'> {param}'),
            ('stop', f'Not wish to answer')
            ]

    elif topic == 'health':
        # https://udel.edu/~cmarks/What%20is%20social%20class.htm

        sentence = f'At scale 1-10, you will score your health condition as'
        param = gen_random_type1(prev_answers, randseed, low0=Constant.NUM_HEALTH[0], high0=Constant.NUM_HEALTH[1])
        if param is None:
            return None
        choices=[
            ('left', f'<= {param}'),
            ('right', f'> {param}'),
            ('stop', f'Not wish to answer')
            ]

    elif topic == 'salary':

        sentence = f'Your yearly salary (before tax) is '
        param = gen_random_type1(prev_answers, randseed, low0=Constant.NUM_SALARY[0], high0=Constant.NUM_SALARY[1])
        if param is None:
            return None
        choices=[
            ('left', f'$<= {param}k'),
            ('right', f'> ${param}k'),
            ('stop', f'Not wish to answer')
            ]

    elif topic == 'cash':

        sentence = f'Your overall available cash is'
        param = gen_random_type1(prev_answers, randseed, low0=Constant.NUM_CASH[0], high0=Constant.NUM_CASH[1])
        if param is None:
            return None
        choices=[
            ('left', f'$<= {param}k'),
            ('right', f'> ${param}k'),
            ('stop', f'Not wish to answer')
            ]

    elif topic == 'stock':

        sentence = f'Your overall stock investment is'
        param = gen_random_type1(prev_answers, randseed, low0=Constant.NUM_STOCK[0], high0=Constant.NUM_STOCK[1])
        if param is None:
            return None
        choices=[
            ('left', f'$<= {param}k'),
            ('right', f'> ${param}k'),
            ('stop', f'Not wish to answer')
            ]

    elif topic == 'sex':

        sentence = f'How many times do you have sex in a month?'
        param = gen_random_type1(prev_answers, randseed, low0=Constant.NUM_SEX[0], high0=Constant.NUM_SEX[1])
        if param is None:
            return None
        choices=[
            ('left', f'<= {param}'),
            ('right', f'> {param}'),
            ('stop', f'Not wish to answer or not applicable')
            ]

    else:
        print('not valid topic!', file=sys.stdout)

    return (param, sentence, choices)