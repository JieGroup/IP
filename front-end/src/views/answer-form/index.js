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
  // console.log('answerFormData', answerFormData, answerFormData.value)
  // console.log(typeof answerFormData)
  let tempData = {};
  for (let key of answerFormData) {
    let answer_type = surveyTopics[key].answer_type
    if (answer_type === 'continuous') {
      let chosedIndex = answerFormData[key].validate.continuous_range.$model
      if (surveyUpdateMethod === 'static') {
        tempData[key] = {}
        tempData[key]['min'] = surveyTopics[key]['choices_list'][chosedIndex]['min']
        tempData[key]['max'] = surveyTopics[key]['choices_list'][chosedIndex]['max']
      } else {
        tempData[key] = surveyTopics[key]['choices_list'][chosedIndex]
      }
    } else if (answer_type === 'categorical') {
      let chosedIndex = answerFormData[key].validate.categorical_range.$model
      tempData[key] = surveyTopics[key]['choices_list'][chosedIndex]
    }
    
    // at current time, uniform update does not need to change
    // only continuous option in static update needs modification
    
  }
  console.log('ttttempData', tempData)
  return JSON.parse(JSON.stringify(tempData))
}

export { linkTo, process_startFormData, process_answerFormData };