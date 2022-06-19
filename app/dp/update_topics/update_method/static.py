from __future__ import annotations

from app.dp.update_topics.update_method.base import BaseUpdateMethod

from app.dp.update_topics.update_method.abstract_method import AbstractUpdateMethod

from typeguard import typechecked

from app._typing import Survey_Update_Method

from typing import (
    Union,
    Any
)


@typechecked
class StaticUpdate(AbstractUpdateMethod, BaseUpdateMethod):

    @classmethod
    def generate_topic_new_range(
        cls,
    ) -> None:
        return None


    @classmethod
    def update_topics(
        cls,
        max_rounds: int,
        survey_topics: dict[dict[str, Any]],
        survey_answer_document: dict[str, Union[str, Any]],
        survey_new_answers: dict[dict[str, Any]]
    ) -> None:

        return super().update_topics_base_flow(
            max_rounds=max_rounds,
            survey_topics=survey_topics,
            survey_answer_document=survey_answer_document,
            survey_new_answers=survey_new_answers,
            update_method_recall=cls.generate_topic_new_range
        )

            