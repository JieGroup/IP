const process_FormData = (FormDataValidate) => {
    console.log('FormDataValidate', FormDataValidate, FormDataValidate.value)
    console.log('asdsa', FormDataValidate.value.survey_template_id)
    console.log('zzz', FormDataValidate.value.survey_template_id.$model)
    return {
        'survey_template_id': FormDataValidate.value.survey_template_id.$model
    }
}

export { process_FormData };