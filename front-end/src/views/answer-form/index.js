const linkTo = (name, router, params) => {
  router.push({
    name: name,
    params: params
  });
};

const startFormDataKeys = new Set([
  'survey_template_id',
  'mturk_id'
])

const process_startFormData = (startFormDataValidate) => {
  console.log('validate', startFormDataValidate)
  let tempData = {}
  let startFormDataValidateValue = startFormDataValidate.value
  for (let key of startFormDataKeys) {
    console.log('valida_key', key, startFormDataValidateValue[key])
    console.log("???", startFormDataValidateValue[key].$model)
    tempData[key] = startFormDataValidateValue[key].$model
  }
  console.log('!@#!@', tempData)
  return JSON.parse(JSON.stringify(tempData))
}



// answerFormData
// {
//   survey_answer_id: unique id of current answer
//   survey_new_answers: {
//       topic_name_1: {
//           categorical_range: {
//               'inclusion': ['a', 'b', 'c'] (list of options or str)
//           },
//       },
//       ...
//       topic_name_n: {
//           continuous_range: {
//               'min': min_value,
//               'max': max_value
//           },   
//       }
//   }
// }

const process_answerFormData = (surveyTopics, surveyAnswerID, surveyUpdateMethod, answerFormData) => {
  console.log('process_answerFormData', surveyTopics, surveyAnswerID, surveyUpdateMethod)
  console.log('answerFormData', answerFormData, answerFormData.categorical_1)
  console.log(typeof answerFormData)
  let tempData = {
    survey_answer_id: surveyAnswerID,
    survey_new_answers: {}
  };
  for (let key in surveyTopics) {
    console.log('keyyyy', key)
    let newSubAns = {}
    let answer_type = surveyTopics[key].answer_type
    console.log('answerFormData[key]', answerFormData[key])
    console.log('surveyTopics[key]', surveyTopics[key])
    answerFormData.$touch();
    if (answer_type === 'continuous') {
      if (surveyUpdateMethod === 'static') {
        // input specific value, no choices
        newSubAns = {
          'continuous_range': {
            'min': null,
            'max': null
          }
        }
        newSubAns['continuous_range']['min'] = answerFormData[key].continuous_range.$model
        newSubAns['continuous_range']['max'] = answerFormData[key].continuous_range.$model
      } else {
        let chosedIndex = answerFormData[key].continuous_range.$model
        newSubAns['continuous_range'] = surveyTopics[key]['choices_list'][chosedIndex]
      }
    } else if (answer_type === 'categorical') {
      // at current time, uniform update does not need to change
      // only continuous option in static update needs modification
      let chosedIndex = answerFormData[key].categorical_range.$model
      console.log('BB', chosedIndex)
      newSubAns['categorical_range'] = surveyTopics[key]['choices_list'][chosedIndex]
    }
    tempData['survey_new_answers'][key] = newSubAns
  }
  console.log('ttttempData', tempData)
  return JSON.parse(JSON.stringify(tempData))
}

export { linkTo, process_startFormData, process_answerFormData };