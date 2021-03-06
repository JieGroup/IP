# # from abc import ABC, abstractmethod
from __future__ import annotations
# # class A(ABC):

# #     @classmethod
# #     @abstractmethod
# #     def ceshi(cls):
# #         pass

# #     @classmethod
# #     @abstractmethod
# #     def dier(cls):
# #         pass

# # class B(A):

# #     @classmethod
# #     def ceshi(cls):
# #         print('lihaine')
# #         return

# #     # @classmethod
# #     # def wow(cls):
# # #     #     print('wudi')

# # import rpy2.robjects.packages as rpackages
# # import rpy2.robjects as robjects
# # import rpy2.robjects.numpy2ri

# # print(5)
# # # B.ceshi()
# # # ceshi = B()
# # # B.wow()

# # # a = {'a':{'b': 1, 'c':2}, 'b':{'b': 1, 'c':2}}

# # # for key, val in a.items():
# # #     print(f'key{key}')
# # #     print(f'val{val}')

# # import uuid
# # a  = uuid3()


# from types import ClassMethodDescriptorType


# # class fulei:

# #     @classmethod
# #     def fulei(
# #         cls,
# #         func,
# #     ):  
# #         print('fulei')
# #         func()
    

# # class zilei(fulei):

# #     @classmethod
# #     def zilei(cls):
# #         super().fulei(cls.zilei1)
    
# #     @classmethod
# #     def zilei1(cls):
# #         print('zilei1', cls)
# #         cls.zilei2()
    
# #     @classmethod
# #     def zilei2(cls):
# #         print('zilei2', cls)
# #         cls.zilei3()
    
# #     @classmethod
# #     def zilei3(cls):
# #         print('zilei3')

# # zilei.zilei()



# import sys
# from random import Random
# import numpy as np

# def decode_category(d):
#     '''
#         map an integer to a sorted list of int, each representing a category (1-9)
#         e.g. 143->{'1', '3', '4'}
#     '''
#     s = [int(i) for i in str(int(d))]
#     s.sort()
#     return s

# def encode_category(l):
#     '''
#         map a list of int (each 1-9) to an integer, where digits are in ascending order
#         e.g. {'1', '3', '4'}->134, {'4', '2'}->24 (ascending order)
#     '''
#     l.sort()
#     return int(''.join([str(i) for i in l]))

# def gen_random_type1(prev_answers, randseed, low0, high0):

#     '''
#         generate a random paramber within [low, high] (boundary inclusive)
#         where low, high are determined from historical answers in the form of <=thresh or >thresh
#     '''
#     # https://stackoverflow.com/questions/12368996/what-is-the-scope-of-a-random-seed-in-python
#     myRandom = Random(randseed)

#     len_left = len(prev_answers['left'])
#     len_right = len(prev_answers['right'])

#     # determine the upper bound of the interval
#     if len_left == 0:
#         high = high0-1
#     elif min(prev_answers['left']) <= low0:
#         # if we already knew the answer is low0
#         return None
#     else:
#         high = min(prev_answers['left'])-1

#     # determine the lower bound of the interval
#     if len_right == 0:
#         low = low0
#     elif max(prev_answers['right'])+1 >= high:
#         # if we already knew the answer is high0
#         return None
#     else:
#         low = max(prev_answers['right'])+1

#     # debug([low, high], 'low, high')
#     param = myRandom.randint(low, high) # inclusive

#     return param

# def gen_random_type2(prev_answers, randseed, alph):
#     '''
#         generate a random subset within a list alph (boundary exclusive)
#         set size is assumed to be no larger than 9, so that the elements are denoted by numbers

#         alph: list of strings, with size >= 2
#         param: an integer, whose digits represent categories
#     '''
#     if len(alph) < 2:
#         return None, None

#     myRandom = Random(randseed)

#     #. the respresenting digit should be within 1-9 to avoid degeneracy
#     complete_set = [i+1 for i in range(len(alph))]
#     # narrow the "in" set
#     in_set = set(complete_set)
#     print(f'in_set: {in_set}')
#     if prev_answers['left']:
#         for s in prev_answers['left']:
#             s = set(decode_category(s))
#             print(f's: {s}')
#             in_set = s.intersection(in_set)

#     print(f'in_set: {in_set}')
#     # narrow the "out" set
#     out_set = set()
#     if prev_answers['right']:
#         for s in prev_answers['right']:
#             s = set(decode_category(s))
#             out_set = s.union(out_set)

#     print(f'out_set: {out_set}')
#     # feasible set represented by strings such as ['1', '2']
#     print(f'diff: {in_set.difference(out_set)}')
#     allowed_set = list(in_set.difference(out_set))
#     print(f'allowed_set: {allowed_set}')
#     # if we narrow down the exact answer or the voter lied about the answers
#     if len(allowed_set) <= 1:
#         return None, None

#     # half-sample to obtain the subset to ask
#     nsamp = np.ceil(len(allowed_set)/2.0).astype(int)
#     print(f'nsamp: {nsamp}')
#     s = myRandom.sample(allowed_set, nsamp)
#     print(f's: {s}')
#     param = encode_category(s)
#     print(f'param: {param}')
#     # map back to the original semantics
#     subset = [alph[i-1] for i in s]
#     print(f'subset: {subset}')
#     choices = get_choices_from_subset(subset)
#     print(f'choices: {choices}')

#     return param, choices


# def get_choices_from_subset(subset):
#     '''
#         user-friendly phrasing
#     '''
#     if len(subset) > 1:
#         choices=[
#             ('left', 'Either '+or_statement(subset)),
#             ('right', f'None of the above categories'),
#             ('stop', f'Not wish to answer')
#             ]
#     elif len(subset) == 1:
#         choices=[
#             ('left', f'{subset[0].capitalize()}'),
#             ('right', f'Not {subset[0].capitalize()}'),
#             ('stop', f'Not wish to answer')
#             ]
#     else:
#         print('not valid param!', file=sys.stdout)
#         choices = ''

#     return choices


# def or_statement(s):
#     '''
#         return string in the form of or-statement
#         Input:
#             s: a list of strings, with size > 1
#         Output:
#             s[0], s[1], ..., or s[5]
#             s[0] or s[1]
#     '''
#     if len(s) > 2:
#         return ', '.join(s[:-1])+f', or {s[-1]}'
#     elif len(s) == 2:
#         if len(s[0]) > 5 or len(s[1]) > 5:
#             return  f'{s[0]}, or {s[1]}'
#         else:
#             return  f'{s[0]} or {s[1]}'
#     else:
#         print('Jie debug, wrong length in or_statement', file=sys.stdout)
#         return ''


# gen_random_type2(
#     prev_answers={
#         'left': [],
#         'right': []
#     }, 
#     randseed=5, 
#     alph=['1','2','3','4', '5', '6']
# )

# # a = {5,6,7}

# # import json
# # b = json.dumps(a)

# def ceshi(a: str):
#     print(a)

# ceshi(5)
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Hashable,
    Iterator,
    Literal,
    Mapping,
    Optional,
    Protocol,
    Sequence,
    TypeVar,
    Union,
    List,
    Dict
)

from datetime import datetime

# a = datetime.utcnow()
# print(a, type(a))
# b = datetime.utcnow().timestamp()
# print(b, type(b))

# c = datetime.utcfromtimestamp(b)
# print(c, type(c))


# from datetime import datetime, timezone
# ts = 1571595618.0
# x = datetime.fromtimestamp(ts, tz=timezone.utc)
# x_ts = x.timestamp()
# assert ts == x_ts, f"{ts} != {x_ts}"  # This assertion succeeds

# ts = datetime.now(tz=timezone.utc).timestamp()
# x = datetime.fromtimestamp(ts, tz=timezone.utc)
# x_ts = x.timestamp()
# print(ts, x_ts)
# assert ts == x_ts, f"{ts} != {x_ts}"  # This assertion succeeds
# Database_Type = Literal[
#     'survey_answer',
#     'survey_summary',
#     'survey_template',
#     'voter'
# ]

# def ceshi(a: Database_Type):
#     print(a in Database_Type.__args__)

# ceshi(5)

# import bson
# file = {
#     '5': [4,5]
# }

# res = bson.BSON.encode({'file': file})

# print(f'res: {res}')
# import json
# a = '5'
# b = 5
# res1 = json.dumps(a)
# res2 = json.dumps(b)
# print(res1, type(res1))
# print(res2, type(res2))

# c = '5'
# d = "5"
# res3 = json.loads(c)
# res4 = json.loads(d)
# print(res3, type(res3))
# print(res4, type(res4))

# print('ucl' > 'ucb')

# a = {}

# print(a == None)

# if a:
#     print('zz')

# class base:
#     # ceshi = 5
#     # def __init__(self):
#     #     self.ceshi = 5
#     def ceshi(self):
#         self.ceshi = 10

# class sub(base):

#     # def __init__(self):
#     #     # super().__init__()
#     #     print(self.ceshi)
#     #     print(base.ceshi)
#     def base_ceshi(self):
#         print(self.ceshi)

# a = sub()
# a.ceshi()
# a.base_ceshi()

# from itsdangerous import URLSafeTimedSerializer

# serializer = URLSafeTimedSerializer('str')
# res = serializer.dumps('c')
# print('%%', type(res))

# class Ceshi:
#     @classmethod
#     def __siyou(cls):
#         print(5)

# Ceshi._Ceshi__siyou()

# import jwt
# class Ceshi:

#     def ceshi(self) -> int:
#         token_payload = {
#             'user_id': '666',
#         }

#         return jwt.encode(
#             token_payload,
#             '7777',
#             algorithm='HS256'
#         )

# a = Ceshi()
# print(a.ceshi())
# print(type(a.ceshi()))


# def ceshi():
#     a = {}

#     try:
#         b = a['5']
#     except KeyError:
#         # raise e('cuowu')

#         raise KeyError(
#             "String passed to weights not a valid column"
#         )

#     # except ValueError as err:

#     #     raise ValueError(
#     #         "String passed to weights not a valid column"
#     #     )

# ceshi()

# from app._typing import Survey_Update_Method

from typing import Literal

from typeguard import (
    check_type,
    check_argument_types,
    typechecked
)

Survey_Update_Method = Literal[
    'static',
    'uniform',
]

# Serializable_Datatype = Union[
#     dict,
#     list,
#     tuple,
#     str,
#     int,
#     float,
#     bool,
#     None,
# ]

# print(type(Survey_Update_Method))
# print(type(Serializable_Datatype))
# # print(isinstance('static', Survey_Update_Method))
# ceshi = None

# print(type(a) == str, type(str))

# try:
    # check_type('string_list', a, Survey_Update_Method)
# check_type(
#     argname='wudi',
#     value=ceshi,
#     expected_type=str,
# )
# print("string_list conforms to string_list_class")
# except TypeError:
#     # print("string_list does not conform to string_list_class")
#     raise TypeError

# ceshi = {'5': {}}
# ceshi = {}

# # dict[dict[str, Any]]
# # dict[str, dict[str, Any]]
# check_type(
#     argname='wudi',
#     value=ceshi,
#     expected_type=dict[str, Any],
# )

# @typechecked
# class Ceshi:

#     @classmethod
#     def __ceshi(cls, a: int):
#         print('__ceshi')
    
#     @classmethod
#     def ceshi(cls, a: str):
#         cls.__ceshi(a)

# Ceshi.ceshi('6')
# def check():
#     check_argument_types()

# @typechecked
# def ceshi(a: str):
#     check()
#     # check_argument_types()
#     print('!!!', a)

# ceshi(5)

# import json

# # a = datetime.now(tz=timezone.utc)
# # json.dumps(a)
# import numpy as np
# a = {'5': 5}
# b = np.array(5)
# c1 = json.dumps(a, default=str)
# c2 = json.dumps(b, default=str)
# print(c1)
# print(c2)
# raise Exception('There has been an error in the system')


# @typechecked
# def handle_response(
#     func: Callable
# ) -> Callable:
#     print('daohandlele')
#     def wrapper(*args, **kwargs):
#         print('daopzheli')
#         return func(*args, **kwargs)
#         print('after')
#         # res = func(*args,**kwargs)
#         # # res = Serialization.make_data_serializable(res)
#         # print('???wrapperle')
#         # return jsonify(res)

#     return wrapper

# from functools import wraps
# def decorator_name(f):
#     # @wraps(f)
#     def decorated(*args, **kwargs):
#         if not can_run:
#             return "Function will not run"
#         return f(*args, **kwargs)
#     return decorated

# can_run = True
# @decorator_name
# def ceshi(a: str):
#     print(f'aaaaa: {a}')

# ceshi('52352')

# from flask.json import jsonify
# a = datetime.now(tz=timezone.utc)
# b = jsonify(a)
# @decorator_name
# def func():
#     print('44Function is running')
#     return("Function is running")
 
# can_run = True
# print(func())
# # Output: Function is running
 
# can_run = False
# print(func())
# # Output: Function will not run

# import json
# ceshi = {4,5,6}
# ceshi = list(ceshi)
# a = json.dumps(ceshi, default=str)
# print(a)
# b = json.loads(a)
# print(type(b))

# import datetime
# # from datetime import (
# #     datetime, 
# #     timedelta, 
# #     timezone
# # )
# a = datetime.datetime.now(tz=datetime.timezone.utc)
# print(type(a), type(datetime), type(datetime.timezone.utc.timestamp()))
# print(type(a) == datetime.datetime)

from typing import Type, List
from typeguard import typechecked, check_argument_types

# check_type(
#     argname='wudi',
#     value=['5'],
#     expected_type=List[str]
# )
# class Ceshi:
#     pass

# @typechecked
# class Ceshi2:

#     @classmethod
#     def get_instance(cls) -> Ceshi:
#         return Ceshi

# @typechecked
# class Ceshi3:

#     @classmethod
#     def get_instance(cls) -> Ceshi:
#         return Ceshi()

# Ceshi2.get_instance()
# Ceshi3.get_instance()

# print(type(Ceshi))
# print(type(Ceshi()), type(Ceshi()) == Ceshi,  type(Ceshi()) == Type[Ceshi])
# print(type[Ceshi], Type[Ceshi])
# print(type(Ceshi) == Ceshi)
# print(type(Ceshi) == Type[Ceshi])

# check_type(
#     argname='wudi',
#     value=Ceshi,
#     expected_type=type[Ceshi]
# )

# check_type(
#     argname='wudi',
#     value=Ceshi(),
#     expected_type=Ceshi
# )

# check_type(
#     argname='wudi',
#     value=Ceshi,
#     expected_type=Type[Ceshi]
# )

# a = ['a', 'b']
# b = ['a', 'b', 'c']
# c = ['a', 'c']

# print(set(a).issubset(b))
# print(set(a).issubset(c))

a = {'a': 5, 'b': 6, 'c': 7}
b = {'a': 5, 'b': 6, 'c': 7, 'd': 8}

print(type(a.keys()))
d = set(a.keys())
print(d, type(d))