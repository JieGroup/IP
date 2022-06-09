from __future__ import annotations
from app import database

from bson import ObjectId

from app.utils.api import obtain_unique_id

from typing import Any

from app.database.api import (
    search_document,
    create_document,
    update_document
)

from app.dp.update_topics.api import update_topics

from app.dp.update_topics.validate.api import ValidateAnswer

from app.process.utils import get_cur_rounds_num

from app.utils.api import Time

from app.utils.constant import Constant

from app._typing import Survey_Update_Method

from app.process.template import SurveyTemplate

from typing import Union

from app.error import DBDocumentNotFound


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
    def start_answering(
        cls, 
        survey_template_id: str,
        mturk_id: str,
    ) -> dict[str, Any]:

        '''
        Check the information uploaded by Voter and
        check the constrains of the survey template 
        prescribed by creator

        Parameters
        ----------
        survey_template_id : str
            An unique string corresponding to a survey template.
        mturk_id : str
            An unique id that Amazon delivers to Voter.

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
            raise DBDocumentNotFound
        
        # TODO: check if number of copies exceed limit, not urgent

        # create survey_answer document
        newObjectId = ObjectId()
        survey_answer_id=str(newObjectId)
        create_document(
            database_type='survey_answer',
            survey_answer_id=survey_answer_id,
            survey_template_id=survey_template_id,
            mturk_id=mturk_id,
        )

        return {
            'survey_answer_id': survey_answer_id,
            'survey_topics': survey_template_document['survey_topics']
        }
    
    @classmethod
    def update_survey_topics(
        cls,
        survey_answer_id: str,
        survey_new_answers: dict[dict[str, Any]]
    ) -> Union[None, dict[str, dict[str, Any]]]:

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
        dict
        '''

        # check if survey_answer_id in database
        survey_answer_document = search_document(
            database_type='survey_answer',
            survey_answer_id=survey_answer_id
        )
        if survey_answer_document is None:
            raise DBDocumentNotFound

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

        # Validate the new answers
        ValidateAnswer.validate_survey_answers(
            cur_rounds_num=cur_rounds_num,
            survey_topics=survey_topics,
            survey_prev_answers=survey_prev_answers,
            survey_new_answers=survey_new_answers
        )

        # Store new answers
        update_document(
            database_type='survey_answer',
            cur_rounds_num=cur_rounds_num,
            survey_answer_id=survey_answer_id,
            survey_new_answers=survey_new_answers
        )

        # Get dynamic topic
        updated_survey_topics = update_topics(
            survey_update_method=survey_update_method,
            cur_rounds_num=cur_rounds_num,
            max_rounds=max_rounds,
            survey_topics=survey_topics,
            survey_prev_answers=survey_prev_answers,
            survey_new_answers=survey_new_answers
        )
        
        return updated_survey_topics