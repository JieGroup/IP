import sys
import numpy as np
from numpy.random import randint
from random import Random
from app import db
from app.models import Voter, QandA
from sqlalchemy import desc
from flask import session


MAXREP = 3  # max num of repetitions per question
MAXSHOW = 5  # max num of question shown in a page
SURVEY_WAY = ['dynamic', 'static']  # survey way to use

# param = 1
# TOPICS_TYPE = {
#     'age': param,
#     'salary': param
# }

# class Question():
#     '''
#         topic: question topic
#         ip_type: type of interval privacy (e.g., paramerical, categorical)
#     '''

#     def __init__(self, topic, ip_type):
#         self.topic = topic
#         self.param = param

# ordered from less private to more private, according to the original survey excel
TOPICS = [
    'gender',
    'race',
    'age', 
    'education',
    'zip',
    'hours_web',
    'politics',
    'sexual_orientation',
    'spouse_age',
    'social_class',
    'no_houses',
    'health',
    'salary',
    'cash',
    'stock',
    'sex'
    ]
alph_gender = ['Male', 'Female', 'Transgender', 'Gender neutral', 'Others']
alph_race = ['White', 'Black or African American', 'American Indian or Alaska Native', 'Asian',
        'Native Hawaiian and Pacific Islander', 'others']
num_age = [18, 60] # inclusive
alph_education = ['Less than high school', 'High school', 'Bachelor’s degree',
        'Master’s degree', 'Doctoral or professional degree']
num_zip=[2, 99]
num_hours_web = [1, 6]
alph_politics = ['Conservatism', 'Socialism', 'Social Liberalism', 'Classical liberalism', 'Others']
alph_sexual_orientation = ['Heterosexuality', 'Bisexuality', 'Homosexuality', 'Asexuality', 'Others']
num_spouse_age = [18, 60] #[0, 100] 
alph_social_class = ['Upper (elite)', 'Upper middle', 'Lower middle', 'Working', 'Poor']
# alph_no_houses = ['None', '1', '2', 'More than 2']
num_no_houses = [0, 5]
num_health = [1, 10]
num_salary = [0, 150]
num_cash = [0, 300]
num_stock = [0, 300]
num_sex = [0, 100]


def gen_dynamic_questions(randseed):
    '''
        generate all the unique and allowed questions (MAXSHOW on one page)
        according to the order in the const TOPICS_TYPE

        it is a special case to gen one question on a page
    '''

    # init a dict of question, each as a topic-param pair
    questions = {}

    est_remain_count = 0  # the num of estimated remaining questions

    for topic in TOPICS:

        # init for the historical param-question pairs of this voter
        prev_answers = {'left': [], 'right': []}

        # get all qustion-voter pairs, their count, and the latest answer
        q_v_pair = db.session.query(QandA).filter_by(digits=session['digits'], topic=topic)
        rounds = q_v_pair.count() # number of replications for a question-voter pair
        # debug(rounds, 'rounds')
        if rounds > 0:
            # ordered by descending to obtain the latest answer
            q_v_latest_a = q_v_pair.order_by(desc(QandA.rounds)).first()
            if (rounds>=MAXREP) or (q_v_latest_a.answer=='stop'):
                continue
            else:
                for item in q_v_pair:
                    prev_answers[item.answer].append(item.param)

                # print('Jie debug, prev_answers', prev_answers, file=sys.stdout)

        q = gen_dynamic_q(topic, randseed, prev_answers=prev_answers)
        if q is not None:
            questions[topic] = q

        est_remain_count += (MAXREP-rounds)

    # debug(questions, 'questions')

    num = min(MAXSHOW, len(questions))
    myRandom = Random(randseed)

    session['progress_bar'] = 100 - int((est_remain_count-num) / (len(TOPICS) * MAXREP) * 100)
    
    # last page not random
    if num < MAXSHOW and session['entered_MTurk'] is False:
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

    for topic in TOPICS:

        # get all qustion-voter pairs, their count, and the latest answer
        q_v_pair = db.session.query(QandA).filter_by(digits=session['digits'], topic=topic)
        rounds = q_v_pair.count() # number of replications for a question-voter pair

        # debug(rounds, 'rounds')
        if rounds > 0:
            continue

        est_remain_count += 1

        q = gen_static_q(topic)
        if q is not None:
            questions[topic] = q

    # debug(questions, 'questions')

    num = min(MAXSHOW, est_remain_count)

    session['progress_bar'] = 100 - int((est_remain_count-num) / len(TOPICS) * 100)
    
    myRandom = Random(randseed)

    # last page not random
    if num < MAXSHOW and session['entered_MTurk'] is False:
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
        param, choices = gen_random_type2(prev_answers, randseed, alph=alph_gender)
        if param is None:
            return None

    elif topic == 'race':
        # https://2020census.gov/en/about-questions/2020-census-questions-race.html

        sentence = f'Your race is'
        param, choices = gen_random_type2(prev_answers, randseed, alph=alph_race)
        if param is None:
            return None

    elif topic == 'age':

        sentence = f'Your age is '
        param = gen_random_type1(prev_answers, randseed, low0=num_age[0], high0=num_age[1])
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
        param, choices = gen_random_type2(prev_answers, randseed, alph=alph_education)
        if param is None:
            return None

    elif topic == 'zip':
        # http://phaster.com/zip_code.html

        sentence = f'The first two digits of your zipcode (e.g., 2 of 02138) is'
        param = gen_random_type1(prev_answers, randseed, low0=num_zip[0], high0=num_zip[1])
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
        param = gen_random_type1(prev_answers, randseed, low0=num_hours_web[0], high0=num_hours_web[1])
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
        param, choices = gen_random_type2(prev_answers, randseed, alph=alph_politics)
        if param is None:
            return None

    elif topic == 'sexual_orientation':

        sentence = f'Your sexual orientation is'
        param, choices = gen_random_type2(prev_answers, randseed, alph=alph_sexual_orientation)
        if param is None:
            return None

    elif topic == 'spouse_age':

        sentence = f'Your spouse\'s age is'
        param = gen_random_type1(prev_answers, randseed, low0=num_spouse_age[0], high0=num_spouse_age[1])
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
        param, choices = gen_random_type2(prev_answers, randseed, alph=alph_social_class)
        if param is None:
            return None

    elif topic == 'no_houses':
        # https://udel.edu/~cmarks/What%20is%20social%20class.htm

        sentence = f'The number of houses you own is'
        # param, choices = gen_random_type2(prev_answers, randseed, alph=alph_no_houses)
        # if param is None:
        #     return None
        param = gen_random_type1(prev_answers, randseed, low0=num_no_houses[0], high0=num_no_houses[1])
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
        param = gen_random_type1(prev_answers, randseed, low0=num_health[0], high0=num_health[1])
        if param is None:
            return None
        choices=[
            ('left', f'<= {param}'),
            ('right', f'> {param}'),
            ('stop', f'Not wish to answer')
            ]

    elif topic == 'salary':

        sentence = f'Your yearly salary (before tax) is '
        param = gen_random_type1(prev_answers, randseed, low0=num_salary[0], high0=num_salary[1])
        if param is None:
            return None
        choices=[
            ('left', f'$<= {param}k'),
            ('right', f'> ${param}k'),
            ('stop', f'Not wish to answer')
            ]

    elif topic == 'cash':

        sentence = f'Your overall available cash is'
        param = gen_random_type1(prev_answers, randseed, low0=num_cash[0], high0=num_cash[1])
        if param is None:
            return None
        choices=[
            ('left', f'$<= {param}k'),
            ('right', f'> ${param}k'),
            ('stop', f'Not wish to answer')
            ]

    elif topic == 'stock':

        sentence = f'Your overall stock investment is'
        param = gen_random_type1(prev_answers, randseed, low0=num_stock[0], high0=num_stock[1])
        if param is None:
            return None
        choices=[
            ('left', f'$<= {param}k'),
            ('right', f'> ${param}k'),
            ('stop', f'Not wish to answer')
            ]

    elif topic == 'sex':

        sentence = f'How many times do you have sex in a month?'
        param = gen_random_type1(prev_answers, randseed, low0=num_sex[0], high0=num_sex[1])
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
        choices = [(v, v) for v in alph_gender] #+ [stp]

    elif topic == 'race':

        sentence = f'Your race is'
        param = 'RadioField'
        choices = [(v, v) for v in alph_race] #+ [stp]

    elif topic == 'age':

        sentence = f'Your age is'
        param = 'IntegerField'
        choices = num_age

    elif topic == 'education':

        sentence = f'Your education level is'
        param = 'RadioField'
        choices = [(v, v) for v in alph_education] #+ [stp]

    elif topic == 'zip':

        # TODO: this is an interesting design to test the correctness of the answer
        sentence = f'The first two digits of your zipcode (e.g., 2 of 02138) is'
        param = 'IntegerField'
        choices = num_zip

    elif topic == 'hours_web':

        sentence = f'How many hours do you browse web per day'
        # param = 'SelectField'
        # step = 1
        # l = np.arange(num_hours_web[0], num_hours_web[1], step).astype(int).tolist()
        # choices = [('', 'Please select')]
        # choices += [(f'{v}', f'{v} to {v+step}') for v in l]
        # choices += [(f'>{l[-1]}', f'greater than {l[-1]}')] #+ [stp]

        param = 'IntegerField'
        choices = num_hours_web

    elif topic == 'politics':

        sentence = f'The best word to describe your political position is'
        param = 'RadioField'
        choices = [(v, v) for v in alph_politics] #+ [stp]

    elif topic == 'sexual_orientation':

        sentence = f'Your sexual orientation is'
        param = 'RadioField'
        choices = [(v, v) for v in alph_sexual_orientation] #+ [stp]

    elif topic == 'spouse_age':

        sentence = f'Your spouse\'s age is (note: if not applicable please leave it blank or 0)'
        param = 'IntegerField'
        choices = num_spouse_age

    elif topic == 'social_class':

        sentence = f'You identify your social class as'
        param = 'RadioField'
        choices = [(v, v) for v in alph_social_class] #+ [stp]

    elif topic == 'no_houses':

        sentence = f'The number of houses you own is'
        # param = 'RadioField'
        # choices = [(v, v) for v in alph_no_houses] + [stp]
        param = 'IntegerField'
        choices = num_no_houses
        
    elif topic == 'health':

        sentence = f'At scale 1-10, you will score your health condition as'
        param = 'IntegerField'
        choices = num_health

    elif topic == 'salary':

        sentence = f'Your yearly salary is (unit: $1,000, e.g., 30 for $30,000) '
        # param = 'SelectField'
        # step = 10
        # l = np.arange(num_salary[0], num_salary[1], 10).astype(int).tolist()
        # choices = [('', 'Please select')]
        # choices += [(f'{v}', f'${v}k to ${v+10}k') for v in l]
        # choices += [(f'>{l[-1]+step}', f'greater than ${l[-1]+step}k')] + [stp]

        param = 'IntegerField'
        choices = num_salary

    elif topic == 'cash':

        sentence = f'Your overall available cash is (unit: $1,000, e.g., 30 for $30,000) '
        # param = 'SelectField'
        # step = 10
        # l = np.arange(num_cash[0], num_cash[1], 10).astype(int).tolist()
        # choices = [('', 'Please select')]
        # choices += [(f'{v}', f'${v}k to ${v+10}k') for v in l]
        # choices += [(f'>{l[-1]+step}', f'greater than ${l[-1]+step}k')] + [stp]

        param = 'IntegerField'
        choices = num_cash

    elif topic == 'stock':

        sentence = f'Your overall stock investment is (unit: $1,000, e.g., 30 for $30,000) '
        # param = 'SelectField'
        # step = 10
        # l = np.arange(num_stock[0], num_stock[1], step).astype(int).tolist()
        # choices = [('', 'Please select')]
        # choices += [(f'{v}', f'${v}k to ${v+step}k') for v in l]
        # choices += [(f'>{l[-1]+step}', f'greater than ${l[-1]+step}k')] + [stp]

        param = 'IntegerField'
        choices = num_stock

    elif topic == 'sex':

        sentence = f'How many times do you have sex in a month?'
        # param = 'SelectField'
        # step = 5
        # l = np.arange(num_sex[0], num_sex[1], step).astype(int).tolist()
        # choices = [('', 'Please select')]
        # choices += [(f'{v}', f'{v} to {v+step}') for v in l]
        # choices += [(f'>{l[-1]+step}', f'greater than {l[-1]+step}')] + [stp]

        param = 'IntegerField'
        choices = num_sex

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
