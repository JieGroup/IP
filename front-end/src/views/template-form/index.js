import Toastify from "toastify-js";
import dom from "@left4code/tw-starter/dist/js/dom";

const linkTo = (name, router, params) => {
  router.push({
    name: name,
    params: params
  });
};

/*
Form of the data that transfer to back-end
{
  survey_update_method: 'uniform' / 'static' / etc,
  expiration_time: the time that the survey template and the survey answer would be destroyed
  number_of_copies: max number of copies issued,
  max_rounds: max_rounds_of_updating_survey_topics
  survey_topics: {
    topic_name_1: {
      answer_type: ’categorical‘,
      categorical_range: {
        'inclusion': {'a', 'b', 'c'} (set of options)
      },
      topic_question: what is your gender?
      unit: None
    },
    topic_name_2: {
      answer_type: 'continuous',
      continuous_range: {
        'min': min_value,
        'max': max_value    
      },
      topic_question: what is your age? 
      unit: k       
    }
    ...
    topic_name_n: {
      answer_type: 'continuous',
      continuous_range: {
        'min': min_value,
        'max': max_value
      },
      topic_question: ...,
      unit: ...       
    }
  }
}
*/

const fix_form_data_keys = new Set([
  'survey_update_method',
  'time_period',
  'number_of_copies',
  'max_rounds'
])

const dynamic_form_data_keys = new Set([
  'topic_name',
  'topic_question',
  'answer_type',
  'categorical_answer_options',
  'continuous_answer_options',
  'unit',
])

const process_fix_form_data = (fix_form_data, template_data) => {
  const validate = fix_form_data.validate
  console.log(`validate_fix_form_data: ${validate}`)
  for (let key of fix_form_data_keys) {
    template_data[key] = validate[key].$model
  }
  return JSON.parse(JSON.stringify(template_data))
}

const parse_single_dynamic_data = (valueDict) => {
  let template_data = {}
  const validate = valueDict.validate
  const answer_type = validate['answer_type'].$model
  for(let key of dynamic_form_data_keys) {
    if (key === 'topic_name') {
      continue;
    }
    let value = validate[key].$model
    if (key === 'categorical_answer_options') {
      if (answer_type === 'categorical'){
        let categorical_answer_options = [];
        value.forEach((item, index) => {
          categorical_answer_options.push(item.validate.specific_option.$model)
        })
        template_data['categorical_range'] = {}
        template_data['categorical_range']['inclusion'] = categorical_answer_options
      }
    } else if (key === 'continuous_answer_options') {
      if (answer_type === 'continuous'){
        template_data['continuous_range'] = {}
        template_data['continuous_range']['min'] = value.validate.continuous_answer_min.$model
        template_data['continuous_range']['max'] = value.validate.continuous_answer_max.$model
      }
    } else {
      template_data[key] = value
    }
  }
  
  return JSON.parse(JSON.stringify(template_data))
}

const process_dynamic_form_data = (dynamic_form_array) => {
  let template_data = {}
  dynamic_form_array.forEach((item, index) => {
    console.log(`process_dynamic_form_data: ${dynamic_form_array}`)
    template_data[item.validate.topic_name.$model] = parse_single_dynamic_data(item)
  })
  return JSON.parse(JSON.stringify(template_data))
}

const process_template_data = (fix_form_data, dynamic_form_array) => {
  let template_data = {}
  process_fix_form_data(fix_form_data, template_data)
  // reform the user defined topics
  template_data.survey_topics = process_dynamic_form_data(dynamic_form_array)
  return template_data
}

const is_fix_form_data_valid = (fix_form_data) => null

const is_dynamic_form_data_valid = (dynamic_form_array) => {
  let template_data = {}
  let err_msg = null;
  dynamic_form_array.forEach((item, index) => {
    try {
      if (!'validate' in item) {
        throw 'validate is not in dynamic form data!';
      }
      if (!'topic_name' in item.validate) {
        throw 'topic_name is not in dynamic form data!';
      }
      if (item.validate.topic_name.$model in template_data) {
        throw 'topic_name must be unique'
      }
    } catch (err) {
      err_msg = err
    }
    template_data[item.validate.topic_name.$model] = 1
  })
  return err_msg
}

const is_data_valid = (fix_form_data, dynamic_form_array) => {
  let err_msg = is_fix_form_data_valid(fix_form_data)
  if (err_msg !== null) {
    return err_msg
  }
  err_msg = is_dynamic_form_data_valid(dynamic_form_array)
  console.log('is_data_valid', err_msg)
  return err_msg
}

export { linkTo, process_template_data, is_data_valid };