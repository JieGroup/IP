from app._typing import Survey_Update_Method

from app.dp.update_topics.strategy.api import UpdateTopicsOperator

from typeguard import typechecked

from typing import (
    Union,
    Any
)

@typechecked
def update_topics(
    **kwargs
) -> Union[None, dict[str, dict[str, Any]]]:
    survey_update_method = kwargs['survey_update_method']
    update_topics_operator = UpdateTopicsOperator()
    update_topics_operator.set_update_method(
        update_method_type=survey_update_method
    )
    res = update_topics_operator.update_survey_topics(**kwargs)
    print('ceshi: 6666')
    return res