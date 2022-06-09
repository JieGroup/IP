from __future__ import annotations

import collections

from app import pyMongo
from app.database.database.utils import (
    if_file_size_exceed_limit
)

from app.dp.update_topics.update_method.base import BaseUpdateMethod

from app.dp.update_topics.update_method.abstract_method import AbstractUpdateMethod

from app._typing import Survey_Update_Method

from typing import (
    Union,
    Any
)


class StaticUpdate(AbstractUpdateMethod, BaseUpdateMethod):

    @classmethod
    def generate_topic_new_range(
        cls,
    ) -> None:
        return None


    @classmethod
    def update_topics(
        cls,
        max_rounds_of_survey: int,
        survey_topics: dict[dict[str, Any]],
        survey_answer_document: dict[str, Union[str, Any]],
        survey_new_answers: dict[dict[str, Any]]
    ) -> None:

        return super().update_topics_base_flow(
            max_rounds_of_survey=max_rounds_of_survey,
            survey_topics=survey_topics,
            survey_answer_document=survey_answer_document,
            survey_new_answers=survey_new_answers,
            update_method_recall=cls.generate_topic_new_range
        )

            