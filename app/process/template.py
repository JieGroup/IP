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

from app.utils.dtypes.api import (
    is_var_in_literal
)

from app._typing import Survey_Update_Method

from typing import (
    Any,
    Union
)


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
        if max_rounds < 1:
            return False
        return True

    @classmethod
    def __is_survey_topics_valid(
        cls, 
        survey_update_method: Survey_Update_Method,
        time_period: int,
        number_of_copies: int,
        max_rounds: int,
        survey_topics: dict[dict[str, Any]]
    ) -> dict:
        '''
        Check if all parameters are valid

        Parameters
        ----------
        number_of_copies : int

        Returns
        -------
        dict
            If the parameters pass all tests, error_message would be an empty dict.
            Otherwise, it would contain error message
        '''
        error_message = {}

        # Check if survey_update_method is in defined category
        if not is_var_in_literal(
            var=survey_update_method,
            expected_type=Survey_Update_Method
        ):
            error_message['survey_update_method'] = 'Please provide a valid survey topics update method'

        # Check if the time_period is within 2 months
        if not Time.is_time_period_valid(time_period):
            error_message['time_period'] = 'Please provide a time period between 1 and 60 days'

        # Check if the number of copies is within maximum number
        # of copies
        if not cls.__is_number_of_copies_valid(number_of_copies):
            error_message['number_of_copies'] = 'Please provide a number of copies between 1 and 500'
        
        # Check if the max_rounds is within range
        if not cls.__is_max_rounds_valid(max_rounds):
            error_message['max_rounds'] = 'Please provide a number of max_rounds between 1 and 3'

        # TODO: Check Survey_topics. Not urgent
        return error_message

    @classmethod
    def create_survey_template(
        cls, 
        survey_update_method: Survey_Update_Method,
        time_period: int,
        number_of_copies: int,
        max_rounds: int,
        survey_topics: dict[str, Any]
    ) -> str:
        '''
        Check survey template information uploaded by creator and store
            the survey template information in db.

        Parameters
        ----------
        survey_update_method : Survey_Update_Method
            Defines how we update topic new ranges. 'static' means the voter would only answer
            the all topics once. 'uniform' means the topics would be dynamically generated and voter
            may need to answer each topic more than one time.
        time_period : int
            Defines how long we should keep the survey template in database
        number_of_copies : int
            Defines the max number of survey to issue
        max_rounds : int
            Defines how many times the topic can be regenerated
        survey_topics : dict
            The detailed information of each topic

        Returns
        -------
        str
            Return an unique survey_template_id that creator can obtain the information 
            about the survey template
        '''
        # Check the survey topics uploaded by user
        validation_res = cls.__is_survey_topics_valid(
            survey_update_method=survey_update_method,
            time_period=time_period,
            number_of_copies=number_of_copies,
            max_rounds=max_rounds,
            survey_topics=survey_topics
        )
        # If validation_res != {}, it means we have error message.
        # We need to return error message
        if validation_res:
            return bad_request(validation_res)

        # Store the new template
        survey_template_id = get_unique_id()
        expiration_time = Time.get_expiration_utc_time(time_period)
        create_document(
            database_type='survey_template',
            survey_template_id=survey_template_id,
            survey_update_method=survey_update_method,
            expiration_time=expiration_time,
            number_of_copies=number_of_copies,
            max_rounds=max_rounds,
            survey_topics=survey_topics
        )

        return survey_template_id