import sys
import uuid
import numpy as np

from numpy.random import randint
from random import Random
from flask import session

from app import mongoDB, pyMongo
from app.utils.constant import Constant
from app.mongoDB import select_mongoDB_operator

def obtain_unique_digits():
    unique_id = str(uuid.uuid1())
    return unique_id

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
        
        cur_topic_answer = survey_answer_document['survey_answers'][topic]
        rounds = len(cur_topic_answer)
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
        cur_topic_answer = survey_answer_document['survey_answers'][topic]
        rounds = len(cur_topic_answer)

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


def gen_random_type1(prev_answers, randseed, low0, high0):

    '''
        generate a random paramber within [low, high] (boundary inclusive)
        where low, high are determined from historical answers in the form of <=thresh or >thresh
    '''
    # https://stackoverflow.com/questions/12368996/what-is-the-scope-of-a-random-seed-in-python
    myRandom = Random(randseed)

    len_left = len(prev_answers['left'])
    len_right = len(prev_answers['right'])

    # determine the upper bound of the interval
    if len_left == 0:
        high = high0-1
    elif min(prev_answers['left']) <= low0:
        # if we already knew the answer is low0
        return None
    else:
        high = min(prev_answers['left'])-1

    # determine the lower bound of the interval
    if len_right == 0:
        low = low0
    elif max(prev_answers['right'])+1 >= high:
        # if we already knew the answer is high0
        return None
    else:
        low = max(prev_answers['right'])+1

    # debug([low, high], 'low, high')
    param = myRandom.randint(low, high) # inclusive

    return param


def decode_category(d):
    '''
        map an integer to a sorted list of int, each representing a category (1-9)
        e.g. 143->{'1', '3', '4'}
    '''
    s = [int(i) for i in str(int(d))]
    s.sort()
    return s


def encode_category(l):
    '''
        map a list of int (each 1-9) to an integer, where digits are in ascending order
        e.g. {'1', '3', '4'}->134, {'4', '2'}->24 (ascending order)
    '''
    l.sort()
    return int(''.join([str(i) for i in l]))


def or_statement(s):
    '''
        return string in the form of or-statement
        Input:
            s: a list of strings, with size > 1
        Output:
            s[0], s[1], ..., or s[5]
            s[0] or s[1]
    '''
    if len(s) > 2:
        return ', '.join(s[:-1])+f', or {s[-1]}'
    elif len(s) == 2:
        if len(s[0]) > 5 or len(s[1]) > 5:
            return  f'{s[0]}, or {s[1]}'
        else:
            return  f'{s[0]} or {s[1]}'
    else:
        print('Jie debug, wrong length in or_statement', file=sys.stdout)
        return ''


def gen_random_type2(prev_answers, randseed, alph):
    '''
        generate a random subset within a list alph (boundary exclusive)
        set size is assumed to be no larger than 9, so that the elements are denoted by numbers

        alph: list of strings, with size >= 2
        param: an integer, whose digits represent categories
    '''
    if len(alph) < 2:
        return None, None

    myRandom = Random(randseed)

    #. the respresenting digit should be within 1-9 to avoid degeneracy
    complete_set = [i+1 for i in range(len(alph))]
    # narrow the "in" set
    in_set = set(complete_set)
    if prev_answers['left']:
        for s in prev_answers['left']:
            s = set(decode_category(s))
            in_set = s.intersection(in_set)

    # narrow the "out" set
    out_set = set()
    if prev_answers['right']:
        for s in prev_answers['right']:
            s = set(decode_category(s))
            out_set = s.union(out_set)

    # feasible set represented by strings such as ['1', '2']
    allowed_set = list(in_set.difference(out_set))

    # if we narrow down the exact answer or the voter lied about the answers
    if len(allowed_set) <= 1:
        return None, None

    # half-sample to obtain the subset to ask
    nsamp = np.ceil(len(allowed_set)/2.0).astype(int)
    s = myRandom.sample(allowed_set, nsamp)
    param = encode_category(s)

    # map back to the original semantics
    subset = [alph[i-1] for i in s]
    choices = get_choices_from_subset(subset)

    return param, choices


def get_choices_from_subset(subset):
    '''
        user-friendly phrasing
    '''
    if len(subset) > 1:
        choices=[
            ('left', 'Either '+or_statement(subset)),
            ('right', f'None of the above categories'),
            ('stop', f'Not wish to answer')
            ]
    elif len(subset) == 1:
        choices=[
            ('left', f'{subset[0].capitalize()}'),
            ('right', f'Not {subset[0].capitalize()}'),
            ('stop', f'Not wish to answer')
            ]
    else:
        print('not valid param!', file=sys.stdout)
        choices = ''

    return choices


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


def gen_MTurk():
    '''last questionL MTurk User ID'''
    sentence = f'Your M-Turk User ID is '
    param = 'StringField'
    choices = None

    return (param, sentence, choices)


def debug(var, msg=''):
    print('Jie debug '+msg, file=sys.stdout)
    print(var, file=sys.stdout)
