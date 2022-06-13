from __future__ import annotations
from ctypes import Union

import sys
import uuid
import random
import string
import numpy as np

from numpy.random import randint
from random import Random
from flask import session

from app.utils.constant import Constant

from typing import (
    Any,
    final,
    Final
)

CATEGORICAL_RANGE_KEY: Final[str] = 'categorical_range'
CONTINUOUS_RANGE_KEY: Final[str] = 'continuous_range'



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


gen_random_type2(
    prev_answers={
        'left': '12',
        'right': '23'
    }, 
    randseed=5, 
    alph=['1','2','3','4']
)