from typing import Final

class Constant:

    TOKEN_EXPIRATION_PERIOD: Final[int] = 5000
    UPDATE_TOKEN_INTERVAL: Final[int] = 900

    # time period to store the survey template
    TIME_PERIOD_UPPER_LIMIT: Final[float] = 5.62e6
    TIME_PERIOD_LOWER_LIMIT: Final[float] = 2.592e5

    # max number of answers for a survey template
    MAX_NUMBER_OF_COPIES: Final[int] = 500

    # max rounds of a topic can be re-answered
    MAX_ROUNDS: Final[int] = 3
    



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

    # ordered from less private to more private, according to the original survey excel
#     TOPICS = (
#         'gender',
#         'race',
#         'age', 
#         'education',
#         'zip',
#         'hours_web',
#         'politics',
#         'sexual_orientation',
#         'spouse_age',
#         'social_class',
#         'no_houses',
#         'health',
#         'salary',
#         'cash',
#         'stock',
#         'sex'
#         )
    TOPICS = (     
        'age', 
        'salary',
        )

    ALPH_GENDER = ('Male', 'Female', 'Transgender', 'Gender neutral', 'Others')

    ALPH_RACE = ('White', 'Black or African American', 'American Indian or Alaska Native', 'Asian',
            'Native Hawaiian and Pacific Islander', 'others')

    NUM_AGE = (18, 80) # inclusive

    ALPH_EDUCATION = ('Less than high school', 'High school', 'Bachelor\'s degree',
            'Master\'s degree', 'Doctoral or professional degree')
            
    NUM_ZIP=(2, 99)

    NUM_HOURS_WEB = (1, 6)

    ALPH_PHLITICS = ('Conservatism', 'Socialism', 'Social Liberalism', 'Classical liberalism', 'Others')

    ALPH_SEXUAL_ORIENTATION = ('Heterosexuality', 'Bisexuality', 'Homosexuality', 'Asexuality', 'Others')

    NUMS_SPOUSE_AGE = (18, 80) #(0, 100) 

    ALPH_SOCIAL_CLASS = ('Upper (elite)', 'Upper middle', 'Lower middle', 'Working', 'Poor')

    # alph_no_houses = ('None', '1', '2', 'More than 2')
    NUM_NO_HOUSES = (0, 5)

    NUM_HEALTH = (1, 10)

    NUM_SALARY = (0, 200)

    NUM_CASH = (0, 300)

    NUM_STOCK = (0, 300)

    NUM_SEX = (0, 100)
