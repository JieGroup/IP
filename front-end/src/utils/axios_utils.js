import { useAuthenticationStore } from "@/stores/authentication";

const process_axios_response = (response) => {
    console.log('???')
    let data = response.data
    console.log('data', data)
    return data
}

const process_axios_error = (error) => {
    console.log('error', error)
    // const error_name = error.response.data.error_name
    // const error_msg = error.response.data.error_msg
    // const error_status = error.response.status
    // return {
    //     error_name,
    //     error_msg,
    //     error_status
    // }
}

// const install = (app) => {
//   app.config.globalProperties.$f = () => {
//       return process_axios_error;
//   };
// };

const get_api_url = (root) => '/api/' + root

const get_auth_url = (root) => '/auth/' + root

const is_url_belonging_voter_answering = (url) => {
    if (url.indexOf('voter_submit_answer') >= 0) {
        return true;
    }
    return false;
}

const update_token = (data) => {
    const authenticationStore = useAuthenticationStore();
    if ('userToken' in data) {
        authenticationStore.setUserToken(data.userToken)
    }
    if ('voterToken' in data) {
        authenticationStore.setVoterToken(data.voterToken)
    }
}

export { 
    process_axios_response,
    process_axios_error, 
    get_api_url,
    get_auth_url,
    is_url_belonging_voter_answering,
    update_token
}