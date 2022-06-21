from app._typing import Survey_Update_Method

from app.dp.update_topics.strategy.api import UpdateTopicsOperator

from typeguard import typechecked


@typechecked
def update_topics(
    survey_update_method: Survey_Update_Method,
    **kwargs
) -> list:

    update_topics_operator = UpdateTopicsOperator()
    update_topics_operator.set_update_method(
        set_update_method=survey_update_method
    )
    return update_topics_operator.update_topics(**kwargs)
