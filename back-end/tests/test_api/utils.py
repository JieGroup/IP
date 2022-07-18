import copy

from app._typing import Survey_Topics

def get_api_url(root: str) -> str:
    return f'/api/{root}'

def select_first_option(
    updated_survey_topics: Survey_Topics
) -> None:
    '''
    select the first option
    '''
    selected_option = copy.deepcopy(updated_survey_topics)
    
    for key, val in updated_survey_topics.items():
        answer_type = val['answer_type']
        selected_option[key][f'{answer_type}_range'] = copy.deepcopy(
            val['choices_list'][0]
        )
        del selected_option[key]['choices_list']
        
    return selected_option

def stop_first_topic(
    selected_option: Survey_Topics
) -> tuple[dict, str]:
    '''
    select the first option
    '''
    first_key = next(iter(selected_option))

    answer_type = selected_option[first_key]['answer_type']
    selected_option[first_key][f'{answer_type}_range'] = {
        'stop': 'stop'
    }
    return selected_option, first_key