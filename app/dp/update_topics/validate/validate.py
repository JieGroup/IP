from __future__ import annotations

from typing import (
    final,
    Any,
    Callable,
    Union
)

from app.dp.update_topics.validate.utils import (
    ValidateCategoricalAnswer,
    ValidateContinuousAnswer,
)

from app.error import SurveyAnswerError


class ValidateAnswer:

    @classmethod
    def if_cur_rounds_num_equals_one(
        cls, cur_rounds_num: int
    ) -> bool:

        return cur_rounds_num == 1

    @classmethod
    def get_prev_answer(
        cls, 
        cur_rounds_num: int,
        topic_name: str,
        topic_info: dict[str, Any],
        # survey_topics: dict[dict[str, Any]],
        survey_prev_answers: Union[None, dict[str, dict[str, Any]]],
    ) -> bool:

        '''
            If cur_rounds_num is one, we need to get range from survey 
            template document.
            If cur_rounds_num is greater than one, we need to get range
            from last round survey answer.
            Current round's answer always is the subset of the last round's
            answer
        '''

        if cls.if_cur_rounds_num_equals_one(
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
        survey_topics: dict[dict[str, Any]],
        survey_prev_answers: Union[None, dict[str, dict[str, Any]]],
        survey_new_answers: dict[dict[str, Any]],
    ) -> None:

        '''
            Check if the survey answers uploaded by the voter
            are valid
        '''
        
        for topic_name, topic_info in survey_topics.items():

            # Check if topic_name is in survey_new_answers
            if topic_name not in survey_new_answers:
                return SurveyAnswerError

            prev_answer = cls.get_prev_answer(
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
                    cur_rounds_num=cur_rounds_num,
                    topic_name=topic_name,
                    topic_info=topic_info,
                    prev_answer=prev_answer,
                    cur_topic_ans=cur_topic_ans
                )
            elif answer_type == 'continuous':
                ValidateContinuousAnswer.validate_continuous_answer(
                    cur_rounds_num=cur_rounds_num,
                    topic_name=topic_name,
                    topic_info=topic_info,
                    prev_answer=prev_answer,
                    cur_topic_ans=cur_topic_ans
                )
        return
