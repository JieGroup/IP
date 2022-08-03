from __future__ import annotations
from app import database

from bson import ObjectId

from typing import Any
from app.authentication.token_auth import get_voterToken

from app.database.api import (
    delete_document,
    search_document,
    create_document,
    update_document
)

from app.dp.update_topics.api import update_topics

from app.dp.update_topics.validate.api import ValidateAnswer

from app.process.utils import get_cur_rounds_num

from app.utils.api import (
    Time,
    Constant
)

from app._typing import Survey_Update_Method

from app.process.template import SurveyTemplate

from app.error import DBDocumentNotFound

from typing import Union

from app.process.api import get_unique_id

from typeguard import typechecked

from app._typing import (
    MTurkID,
    Survey_New_Answers,
    Survey_Topics
)


@typechecked
class VoterAnswerSurvey:
    '''
    Helper class for voter answering survey process.
    Mainly Check the parameters uploaded by Voter and
    check the constrains of the survey template prescribed by creator

    Attributes
    ----------
    None

    Methods
    -------
    start_answering
    update_survey_topics
    '''
    @classmethod
    def __is_within_the_number_of_copies_issued(
        cls,
        number_of_copies: int,
        participated_voters: list[str]
    ) -> bool:
        '''
        Check if the number of answers is within 
        the number of copies issued

        Parameters
        ----------
        number_of_copies : int
            The number of copies to issued
        participated_voters : list[str]
            Record all participated_voters

        Returns
        -------
        bool
        '''
        if len(participated_voters) < number_of_copies:
            return True
        return False

    @classmethod
    def __has_voter_answered_survey_template(
        cls,
        mturk_id: str,
        participated_voters: list[str]
    ) -> bool:
        '''
        Check if the voter has answered this
        survey template

        Parameters
        ----------
        mturk_id : str
            unique id
        participated_voters : list[str]
            Record all participated_voters

        Returns
        -------
        bool
        '''
        if mturk_id in set(participated_voters):
            return True
        return False
    
    @classmethod
    def __is_voter_a_new_voter(
        cls,
        mturk_id: str,
    ) -> bool:
        '''
        Check if the voter is a new voter

        Parameters
        ----------
        mturk_id : str
            unique id

        Returns
        -------
        bool
        '''
        voter_document = search_document(
            database_type='voter',
            mturk_id=mturk_id,
            check_response=False
        )
        if voter_document == None:
            return True
        return False


    @classmethod
    def start_answering(
        cls, 
        survey_template_id: str,
        mturk_id: MTurkID,
    ) -> dict[str, Any]:
        '''
        Check the information uploaded by Voter and
        check the constrains of the survey template 
        prescribed by creator

        Parameters
        ----------
        voterToken : str
            Token to verify voter
        survey_answer_id : str
            unique string to distinguish answer
        survey_topics : Survey_Topics
            Union[None, dict[str, dict[str, Any]]]

        Returns
        -------
        dict
        '''
        # check if survey_template_document is None
        # if is None, raise SurveyTemplateNotFound error
        survey_template_document = search_document(
            database_type='survey_template',
            survey_template_id=survey_template_id
        )
        if survey_template_document is None:
            raise DBDocumentNotFound(
                'cannot find corresponding survey template document'
            )
        
        # check if number of copies exceed limit
        if not cls.__is_within_the_number_of_copies_issued(
            number_of_copies=survey_template_document['number_of_copies'],
            participated_voters=survey_template_document['participated_voters']
        ):
            raise ValueError(
                'Reach the limit of number of copies'
            )
        
        # check if current voter is a new voter
        # if the voter is a new voter, create
        # corresponding documents
        if cls.__is_voter_a_new_voter(
            mturk_id=mturk_id
        ):
            create_document(
                database_type='voter',
                mturk_id=mturk_id,
                participated_survey_template_ids={}
            )

        # create survey_answer document
        survey_answer_id = get_unique_id()
        create_document(
            database_type='survey_answer',
            survey_answer_id=survey_answer_id,
            survey_template_id=survey_template_id,
            mturk_id=mturk_id,
        )

        # update voter participated_survey_template_ids
        update_document(
            database_type='voter',
            mturk_id=mturk_id,
            survey_template_id=survey_template_id,
            survey_answer_id=survey_answer_id
        )

        # update participated_voters of current template
        update_document(
            database_type='survey_template',
            survey_template_id=survey_template_id,
            mturk_id=mturk_id
        )

        survey_update_method = survey_template_document['survey_update_method']
        survey_topics = survey_template_document['survey_topics']
        # get choices list from survey template topics 
        updated_survey_topics = update_topics(
            survey_update_method=survey_update_method,
            cur_rounds_num=0,
            max_rounds=1,
            survey_topics=survey_topics,
            survey_prev_answers={},
            survey_new_answers=survey_topics
        )
        print('99999')

        get_voterToken(
            survey_template_id=survey_template_id,
            mturk_id=mturk_id
        )

        return {
            'survey_answer_id': survey_answer_id,
            'survey_update_method': survey_update_method,
            'updated_survey_topics': updated_survey_topics
        }
    
    @classmethod
    def update_survey_topics(
        cls,
        survey_answer_id: str,
        survey_new_answers: Survey_New_Answers,
    ) -> dict[str, Union[str, dict, dict[str, dict[str, Any]]]]:
        '''
        Check the information uploaded by Voter and
        check the constrains of the survey template 
        prescribed by creator

        Parameters
        ----------
        survey_answer_id : str
            An unique string corresponding to an answer of a survey template.
        survey_new_answers : dict[dict[str, Any]]
            New answers

        Returns
        -------
        None or dict
            If the voter has finished all rounds of survey, return None.
            Otherwise return new topics
        '''
        # check if survey_answer_id in database
        print('2')
        survey_answer_document = search_document(
            database_type='survey_answer',
            survey_answer_id=survey_answer_id
        )
        if survey_answer_document is None:
            raise DBDocumentNotFound('cannot find the db document')
        print('3')
        # Get the info prescribed by creator
        survey_template_id = survey_answer_document['survey_template_id']
        survey_template_document = search_document(
            database_type='survey_template',
            survey_template_id=survey_template_id
        )
        survey_update_method = survey_template_document['survey_update_method']
        survey_topics = survey_template_document['survey_topics']
        max_rounds = survey_template_document['max_rounds']

        # Get the number of current round
        survey_prev_answers = survey_answer_document['survey_answers']
        cur_rounds_num = get_cur_rounds_num(
            survey_prev_answers=survey_prev_answers
        )
        print('4')
        # Validate the new answers
        ValidateAnswer.validate_survey_answers(
            cur_rounds_num=cur_rounds_num,
            survey_topics=survey_topics,
            survey_prev_answers=survey_prev_answers,
            survey_new_answers=survey_new_answers
        )
        print('5')
        # Store new answers
        update_document(
            database_type='survey_answer',
            cur_rounds_num=cur_rounds_num,
            survey_answer_id=survey_answer_id,
            survey_new_answers=survey_new_answers
        )
        print('6')
        # Get dynamic topics
        updated_survey_topics = update_topics(
            survey_update_method=survey_update_method,
            cur_rounds_num=cur_rounds_num,
            max_rounds=max_rounds,
            survey_topics=survey_topics,
            survey_prev_answers=survey_prev_answers,
            survey_new_answers=survey_new_answers
        )

        return {
            'survey_answer_id': survey_answer_id,
            'survey_update_method': survey_update_method,
            'updated_survey_topics': updated_survey_topics
        }