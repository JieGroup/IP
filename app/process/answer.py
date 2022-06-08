from __future__ import annotations

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

from app.error import SurveyAnswerError


class VoterAnswerSurvey:

    '''
    Helper class for voter answering survey
    '''

    @classmethod
    def start_answering(
        cls, 
        survey_template_id: str,
        mturk_id: str,
    ) -> None:

        survey_template_document = SurveyTemplate.get_survey_template(
            survey_template_id=survey_template_id
        )

        # TODO: check if survey_template_document is None
        # if is None, return Error message
        
        # TODO: check if number of copies exceed limit

        newObjectId = ObjectId()
        survey_answer_id=str(newObjectId)
        create_document(
            database_type='survey_answer',
            survey_answer_id=survey_answer_id,
            survey_template_id=survey_template_id,
            mturk_id=mturk_id,
        )

        return survey_answer_id
    
    @classmethod
    def update_survey_topics(
        cls,
        survey_answer_id: str,
        survey_new_answers: dict[dict[str, Any]],
        start_time,
        end_time
    ) -> None:

        '''
            调取相关的document, 调取update_topics
        '''

        survey_answer_document = search_document(
            database_type='survey_answer',
            survey_answer_id=survey_answer_id
        )

        # TODO: check if survey_answer_id in database

        survey_template_id = survey_answer_document['survey_template_id']
        survey_template_document = SurveyTemplate.get_survey_template(
            survey_template_id=survey_template_id
        )

        # TODO: 不知道要不要再check一些东西

        survey_update_method = survey_template_document['survey_update_method']
        survey_topics = survey_template_document['survey_topics']
        max_rounds_of_survey = survey_template_document['max_rounds_of_survey']

        survey_prev_answers = survey_answer_document['survey_answers']
        cur_rounds_num = get_cur_rounds_num(
            survey_prev_answers=survey_prev_answers
        )

        if ValidateAnswer.if_survey_answer_valid(
            cur_rounds_num=cur_rounds_num,
            survey_topics=survey_topics,
            survey_prev_answers=survey_prev_answers,
            survey_new_answers=survey_new_answers
        ) == SurveyAnswerError:
            return SurveyAnswerError

        # TODO: store processed_survey_answers

        updated_survey_topics = update_topics(
            survey_update_method_type=survey_update_method,
            max_rounds_of_survey=max_rounds_of_survey,
            survey_topics=survey_topics,
            survey_prev_answers=survey_prev_answers,
            survey_new_answers=survey_new_answers
        )
        
        return updated_survey_topics