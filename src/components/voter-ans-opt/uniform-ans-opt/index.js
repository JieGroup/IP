const reform_choices = (choicesList, answerType) => {
    // reform choices to user frienly choices
    let tempData = [];
    if (answerType === 'continuous') {
      tempData.push(`${choicesList[0]['min']}-${choicesList[0]['max']}`)
      tempData.push(`${choicesList[1]['min']}-${choicesList[1]['max']}`)
      tempData.push('Not wish to answer')
    } else if (answerType === 'categorical') {
      tempData.push(choicesList[0]['inclusion'])
      tempData.push('Not in aboving options')
      tempData.push('Not wish to answer')
    }
    
    console.log('ttttempData', tempData)
    return JSON.parse(JSON.stringify(tempData))
  }
  
  export { reform_choices };