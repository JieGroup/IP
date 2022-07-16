const linkTo = (path, router) => {
  router.push({
      path: path,
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
      unit: None
    },
    topic_name_2: {
      answer_type: 'continuous',
      continuous_range: {
        'min': min_value,
        'max': max_value    
      } 
      unit: k       
    }
    ...
    topic_name_n: {
      answer_type: 'continuous',
      continuous_range: {
        'min': min_value,
        'max': max_value
      },
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
  console.log('vvvvv', validate, validate['time_period'].$model)

  for(let key of fix_form_data_keys) {
    console.log('valida_key', key, validate[key])
    console.log("???", validate[key].$model)
    template_data[key] = validate[key].$model
  }
  console.log('!@#!@', template_data)
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
    console.log('single_dynamic_data value', validate[key])
    let value = validate[key].$model
    if (key === 'categorical_answer_options') {
      if (answer_type === 'categorical'){
        let categorical_answer_options = [];
        value.forEach((item, index) => {
          console.log('22222', item.validate.specific_option.$model)
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
      console.log('!!!before', template_data, value.$model)
      template_data[key] = value
      console.log('template_data', template_data)
    }
  }
  console.log('~~~~~', template_data)
  let b = JSON.parse(JSON.stringify(template_data))
  console.log('bbbbb', b)
  // let a = structuredClone(template_data)
  // console.log()
  
  return JSON.parse(JSON.stringify(template_data))
}

const process_dynamic_form_data = (dynamic_form_array) => {
  let template_data = {}
  dynamic_form_array.forEach((item, index) => {
    if (!'validate' in item) {
      throw 'validate is not in dynamic form data!';
    }
    if (!'topic_name' in item.validate) {
      throw 'topic_name is not in dynamic form data!';
    }
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



export { linkTo, process_template_data };