from __future__ import annotations

from app.process.utils import get_unique_id

from app.database.api import (
    search_document,
    create_document,
    update_document
)

from app.utils.api import (
    Time,
    Constant
)

from typeguard import typechecked

from app._typing import (
    Survey_Update_Method,
    Survey_Topics,
    Survey_Prev_Answers,
    Survey_New_Answers
)

from flask import g

from typing import (
    Any,
    Union
)


@typechecked
class SurveyTemplate:
    '''
    Handle the creating template process. Mainly focus on the validation
    of the uploaded parameters

    Attributes
    ----------
    None

    Methods
    -------
    create_survey_template
    '''

    @classmethod
    def __is_number_of_copies_valid(
        cls, number_of_copies: int
    ) -> bool:
        '''
        Check if number_of_copies is in predefined range

        Parameters
        ----------
        number_of_copies : int

        Returns
        -------
        bool
        '''
        if number_of_copies > Constant.MAX_NUMBER_OF_COPIES:
            return False
        if number_of_copies < 1:
            return False
        return True

    @classmethod
    def __is_max_rounds_valid(
        cls, max_rounds: int
    ) -> bool:
        '''
        Check if max_rounds is in predefined range

        Parameters
        ----------
        max_rounds : int

        Returns
        -------
        bool
        '''
        if max_rounds > Constant.MAX_ROUNDS:
            return False
        if max_rounds < Constant.MIN_ROUNDS:
            return False
        return True

    @classmethod
    def __check_survey_topics(
        cls, 
        time_period: int,
        number_of_copies: int,
        max_rounds: int,
        survey_topics: Survey_Topics
    ) -> None:
        '''
        Check if all parameters are valid

        Parameters
        ----------
        time_period : int
        number_of_copies : int
        max_rounds : int
        survey_topics : Survey_Topics

        Returns
        -------
        None
        '''
        # Check if the time_period is within 2 months
        if not Time.is_time_period_valid(time_period):
            raise ValueError('Please provide a time period between 1 and 60 days')

        # Check if the number of copies is within maximum number
        # of copies
        if not cls.__is_number_of_copies_valid(number_of_copies):
            raise ValueError('Please provide a number of copies between 1 and 500')
        
        # Check if the max_rounds is within range
        if not cls.__is_max_rounds_valid(max_rounds):
            raise ValueError('Please provide a number of max_rounds between 1 and 3')

        # TODO: Check Survey_topics. Not urgent
        return


    @classmethod
    def create_survey_template(
        cls, 
        survey_template_name: str,
        survey_update_method: Survey_Update_Method,
        time_period: str,
        number_of_copies: int,
        max_rounds: int,
        survey_topics: Survey_Topics
    ) -> dict:
        '''
        Check survey template information uploaded by creator and store
            the survey template information in db.

        Parameters
        ----------
        survey_update_method : Survey_Update_Method
            Defines how we update topic new ranges. 'static' means the voter would only answer
            the all topics once. 'uniform' means the topics would be dynamically generated and voter
            may need to answer each topic more than one time.
        time_period : str
            Defines how long we should keep the survey template in database
        number_of_copies : int
            Defines the max number of survey to issue
        max_rounds : int
            Defines how many times the topic can be regenerated
        survey_topics : dict
            The detailed information of each topic

        Returns
        -------
        dict
            Return an unique survey_template_id that creator can obtain the information 
            about the survey template
        '''
        # Change time_period from str(number of day) to int(seconds)
        print('0.7')
        temp_time_period = time_period
        time_period = Time.change_time_period_to_sec(time_period=time_period)
        print('1')
        # Check the survey topics uploaded by user
        cls.__check_survey_topics(
            time_period=time_period,
            number_of_copies=number_of_copies,
            max_rounds=max_rounds,
            survey_topics=survey_topics
        )
        print('2')
        # Store the new template
        survey_template_id = get_unique_id()
        print('zheli')
        creation_time = Time.get_current_utc_time()
        expiration_time = Time.get_expiration_utc_time(time_period)
        print('zheli2')
        create_document(
            database_type='survey_template',
            survey_template_id=survey_template_id,
            survey_template_name=survey_template_name,
            survey_update_method=survey_update_method,
            creation_time=creation_time,
            expiration_time=expiration_time,
            time_period=temp_time_period,
            number_of_copies=number_of_copies,
            max_rounds=max_rounds,
            participated_voters=[],
            survey_topics=survey_topics
        )

        user_id = g.current_user['user_id']
        # record the survey template created by current user
        # delete searching process when user wants to check
        # its history
        update_document(
            database_type='user',
            user_id=user_id,
            survey_template_id=survey_template_id,
            survey_template_name=survey_template_name,
            creation_time=creation_time,
            expiration_time=expiration_time,
        )

        print('zheli3')
        return {
            'survey_template_id': survey_template_id
        }