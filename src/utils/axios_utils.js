import { useAuthenticationStore } from "@/stores/authentication";
import { useWebStore } from "@/stores/web-info"



const process_axios_response = (response) => {
    console.log('???')
    let data = response.data
    console.log('data', data)
    return data
}

const process_axios_error = (error) => {
  console.log('----- Debug process_axios_error', error)
  // there are 2 kinds of response error:
  // 1. error return by the back-end
  // 2. error throwed by the XMLHttpRequest
  if ('response' in error && error.response !== undefined){
    // 1. error return by the back-end
    if ('data' in error.response) {
      const error_name = error.response.data.error_name
      const error_msg = error.response.data.error_msg
      const error_status = error.response.status
      return {
        error_name,
        error_msg,
        error_status
      }
    } else {
      const error_name = error.response.name
      const error_msg = error.response.message
      const error_status = error.response.status
      return {
        error_name,
        error_msg,
        error_status
      }
    }
  }
  return error    
}

// const install = (app) => {
//   app.config.globalProperties.$f = () => {
//       return process_axios_error;
//   };
// };

const get_api_url = (root) => '/api/' + root

const get_auth_url = (root) => '/auth/' + root

const is_url_belonging_voter_answering = (url) => {
  // check if current url needs voterToken
  if (url.indexOf('voter_submit_answers') >= 0) {
      return true;
  }
  return false;
}

const update_token = (data) => {
  const authenticationStore = useAuthenticationStore();
  console.log('update_token')
  if ('userToken' in data) {
    console.log('update_userToken')
    authenticationStore.setUserToken(data.userToken)
  }
  if ('voterToken' in data) {
    console.log('update_voterToken')
    authenticationStore.setVoterToken(data.voterToken)
  }
}

const get_survey_share_link = (surveyTemplateID) => {

  const webStore = useWebStore();

  return `${webStore.websiteURL}/answer-survey/?surveyTemplateID=${surveyTemplateID}`
}

export { 
    process_axios_response,
    process_axios_error, 
    get_api_url,
    get_auth_url,
    is_url_belonging_voter_answering,
    update_token,
    get_survey_share_link
}