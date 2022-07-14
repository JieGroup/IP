
const process_axios_error = (error) => {
    const error_name = error.response.data.error_name
    const error_msg = error.response.data.error_msg
    const error_status = error.response.status
    return {
        error_name,
        error_msg,
        error_status
    }
}

// const install = (app) => {
//   app.config.globalProperties.$f = () => {
//       return process_axios_error;
//   };
// };

const get_api_url = (root) => '/api/' + root

const get_auth_url = (root) => '/auth/' + root

export { 
    process_axios_error, 
    get_api_url,
    get_auth_url 
}