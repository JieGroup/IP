from typing import Final

class Constant:

    EMAIL_PATTERN = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    TOKEN_EXPIRATION_PERIOD: Final[int] = 5000
    UPDATE_TOKEN_INTERVAL: Final[int] = 900

    # time period to store the survey template
    # maximum is 60 days
    TIME_PERIOD_UPPER_LIMIT: Final[int] = 5200000
    # minimum is 3 days
    TIME_PERIOD_LOWER_LIMIT: Final[int] = 259200

    # max number of answers for a survey template
    MAX_NUMBER_OF_COPIES: Final[int] = 500
    
    # min rounds of a topic can be answered
    MIN_ROUNDS: Final[int] = 1
    # max rounds of a topic can be answered
    MAX_ROUNDS: Final[int] = 3
    
    CATEGORICAL_RANGE_KEY: Final[str] = 'categorical_range'
    CONTINUOUS_RANGE_KEY: Final[str] = 'continuous_range'


    SURVEY_TEMPLATE_ID = 'CESHICESHICESHI'

    # define fixed TYPE of entry to either random, dynamic, or static survey
    RAN = '1mACBzA4ktv9fEEPfcXh8RB6' # http://0.0.0.0:8000/1mACBzA4ktv9fEEPfcXh8RB6
    DYN = 'ZrovHUMI0wZE8DdPNI6WElY3' # http://0.0.0.0:8000/ZrovHUMI0wZE8DdPNI6WElY3
    STA = 'ypnWYpfb5dLEQ6xWfiALTVqH' # http://0.0.0.0:8000/ypnWYpfb5dLEQ6xWfiALTVqH

    # to publish: 
    # http://3.141.9.233:8000/1mACBzA4ktv9fEEPfcXh8RB6 
    # http://3.141.9.233:8000/ZrovHUMI0wZE8DdPNI6WElY3
    # http://3.141.9.233:8000/ypnWYpfb5dLEQ6xWfiALTVqH

    # MAXREP = 3  # max num of repetitions per question
    MAXREP = 1  # max num of repetitions per question
    MAXSHOW = 5  # max num of question shown in a page
    SURVEY_WAY = ('dynamic', 'static')  # survey way to use


    # DEFAULT_CATEGORICAL_OPTIONS = {
    #     'gender': {
    #         'range': [
    #             'Male', 
    #             'Female', 
    #             'Transgender', 
    #             'Gender neutral', 
    #             'Others'
    #         ],
    #         'unit': None
    #     },
    #     'race': {
    #         'range': [
    #             'White', 
    #             'Black or African American', 
    #             'American Indian or Alaska Native', 
    #             'Asian',
    #             'Native Hawaiian and Pacific Islander', 
    #             'others'
    #         ],
    #         'unit': None
 
    #     },
    #     'education': {
    #         'range':{
    #             'Less than high school', 
    #             'High school', 
    #             "Bachelor's degree",
    #             "Master's degree", 
    #             'Doctoral or professional degree'
    #         },
    #         'unit': {
    #             None
    #         }
    #     },
    #     'politics': {
    #         'range':{
    #             'Conservatism', 
    #             'Socialism', 
    #             'Social Liberalism', 
    #             'Classical liberalism', 
    #             'Others'
    #         },
    #         'unit':{
    #             None
    #         }
            
    #     },
    #     'sexual_orientation': {
    #         'range':{
    #             'Heterosexuality', 
    #             'Bisexuality', 
    #             'Homosexuality', 
    #             'Asexuality', 
    #             'Others'
    #         },
    #         'unit':{
    #             None
    #         }
    #     },
    #     'social_class': {
    #         'range':{
    #             'Upper (elite)', 
    #             'Upper middle', 
    #             'Lower middle', 
    #             'Working', 
    #             'Poor'
    #         },
    #         'unit':{
    #             None
    #         }
    #     }
    # }

    # DEFAULT_CONTINUOUS_OPTIONS = {
    #     'age': {
    #         'range':{
    #             [18, 80]
    #         },
    #         'unit':{
    #             None
    #         }
    #     },
    #     'zip': {
    #         'range':{
    #             [2, 99]
    #         },
    #         'unit':{
    #             ' (first two digits)'
    #         }
    #     },
    #     'hours_web': {
    #         'range':{
    #             [1, 6]
    #         },
    #         'unit':{
    #             ' hours per day'
    #         }
    #     },
    #     'spouse_age': {
    #         'range':{
    #             [18, 80]
    #         },
    #         'unit':{
    #             None
    #         }
    #     },
    #     'num_houses': {
    #         'range':{
    #             [0, 5]
    #         },
    #         'unit':{
    #             None
    #         }
    #     },
    #     'health': {
    #         'range':{
    #             [1, 10]
    #         },
    #         'unit':{
    #             ' at scale 1-10'
    #         }
    #     },
    #     'salary': {
    #         'range':{
    #             [0, 150]
    #         },
    #         'unit':{
    #             ' k (before tax)'
    #         }
    #     },
    #     'cash': {
    #         'range':{
    #             [0, 300]
    #         },
    #         'unit':{
    #             ' k (before tax)'
    #         }
    #     },
    #     'stock': {
    #         'range':{
    #             [0, 300]
    #         },
    #         'unit':{
    #             ' k'
    #         }
    #     },
    #     'sex': {
    #         'range':{
    #             [0, 100]
    #         },
    #         'unit':{
    #             ' times per month'
    #         }
    #     },
    # }

    # DEFAULT_TEMPLATE = None

    # @classmethod
    # def generate_default_template(cls):
    #     if cls.DEFAULT_TEMPLATE is None:
    #         for key, val in cls.DEFAULT_CATEGORICAL_OPTIONS.items():
    #             cls.DEFAULT_TEMPLATE[key] = {
    #                 'answer_type': 'categorical',
    #                 'categorical_range': {
    #                     'inclusion': val['range']
    #                 },
    #                 'unit': val['unit']
    #             }
            
    #         for key, val in cls.DEFAULT_CONTINUOUS_OPTIONS.items():
    #             cls.DEFAULT_TEMPLATE[key] = {
    #                 'answer_type': 'continuous',
    #                 'continuous_range': {
    #                     'min': val['range'][0],
    #                     'max': val['range'][1] 
    #                 },
    #                 'unit': val['unit']
    #             }
    #     return cls.DEFAULT_TEMPLATE