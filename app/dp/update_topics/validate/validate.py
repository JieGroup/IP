from __future__ import annotations

from typing import (
    final,
    Any,
    Callable,
    Union
)

from .validate_continuous import ValidateContinuousAnswer

from .validate_categorical import ValidateCategoricalAnswer

from typeguard import typechecked

from app.error import SurveyAnswerError

from app._typing import (
    Survey_Topics,
    Survey_Prev_Answers,
    Survey_New_Answers
)


@typechecked
class ValidateAnswer:
    '''
    Validate if range of new answers uploaded by 
    voter are within the previous range.

    Attributes
    ----------
    None

    Methods
    -------
    validate_survey_answers
    '''

    @classmethod
    def __is_cur_rounds_num_equals_one(
        cls, cur_rounds_num: int
    ) -> bool:
        '''
        check if cur_rounds_num equals to 1

        Parameters
        ----------
        cur_rounds_num : int

        Returns
        -------
        bool
        '''
        return cur_rounds_num == 1

    @classmethod
    def __get_range_criteria(
        cls, 
        cur_rounds_num: int,
        topic_name: str,
        topic_info: dict[str, Any],
        survey_prev_answers: Survey_Prev_Answers,
    ) -> dict[str, Any]:
        '''
        Get range criteria from previous answer or survey template info.

        If cur_rounds_num is one, we need to get range from survey 
        template document.
        If cur_rounds_num is greater than one, we need to get range
        from last round survey answer.
        
        Parameters
        ----------
        cur_rounds_num : int
        topic_name : str
        topic_info : dict[str, Any]
        survey_prev_answers : Union[None, dict[str, dict[str, Any]]]

        Returns
        -------
        dict[str, Any]

        Notes
        -----
        Current round's answer always is the subset of the last round's
        answer
        '''
        if cls.__is_cur_rounds_num_equals_one(
            cur_rounds_num=cur_rounds_num
        ):
            return topic_info
        else:
            rounds_key = f'rounds_{cur_rounds_num-1}'
            return survey_prev_answers[rounds_key][topic_name]

    @classmethod
    def validate_survey_answers(
        cls,
        cur_rounds_num: int,
        survey_topics: Survey_Topics,
        survey_prev_answers: Survey_Prev_Answers,
        survey_new_answers: Survey_New_Answers,
    ) -> None:
        '''
        Validate survey_new_answers. Mainly check if the survey_new_answers
        are within the range of survey_prev_answers.
        
        Parameters
        ----------
        cur_rounds_num : int
        survey_topics : Survey_Topics
        survey_prev_answers : Survey_Prev_Answers
        survey_new_answers : Survey_New_Answers

        Returns
        -------
        None

        Notes
        -----
        Current round's answer always is the subset of the last round's
        answer
        '''
        # check if the survey_new_answers contains the extra key that
        # is not in pre-defined survey template
        if not set(survey_new_answers.keys()).issubset(set(survey_topics.keys())):
            raise SurveyAnswerError(
                f'New answer contains extra key'
            )

        for topic_name, topic_info in survey_topics.items():

            # Check if topic_name is in survey_new_answers
            if topic_name not in survey_new_answers:
                continue

            range_criteria = cls.__get_range_criteria(
                cur_rounds_num=cur_rounds_num,
                topic_name=topic_name,
                topic_info=topic_info,
                survey_prev_answers=survey_prev_answers,
            )

            answer_type = topic_info['answer_type']
            cur_topic_ans = survey_new_answers[topic_name][f"{answer_type}_range"]
            # Check if current survey_answer is valid
            if answer_type == 'categorical':
                ValidateCategoricalAnswer.validate_categorical_answer(
                    topic_name=topic_name,
                    range_criteria=range_criteria,
                    cur_topic_ans=cur_topic_ans
                )
            elif answer_type == 'continuous':
                ValidateContinuousAnswer.validate_continuous_answer(
                    topic_name=topic_name,
                    range_criteria=range_criteria,
                    cur_topic_ans=cur_topic_ans
                )
            else:
                raise ValueError('answer_type is wrong')
        return
