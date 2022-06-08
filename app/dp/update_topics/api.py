from app._typing import Survey_Update_Method

from app.dp.update_topics.strategy.api import UpdateTopicsOperator

def update_topics(
    survey_update_method_type: Survey_Update_Method,
    **kwargs
) -> None:

    update_topics_operator = UpdateTopicsOperator()
    update_topics_operator.set_update_method(
        set_update_method=survey_update_method_type
    )
    return update_topics_operator.update_topics(**kwargs)
