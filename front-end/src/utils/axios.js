import axios from 'axios'
import Toastify from "toastify-js";
import router from '../router/index.js'
import { computed, toRefs } from "vue";
import { useAuthenticationStore } from "@/stores/authentication";
import { useRoute, useRouter } from "vue-router";
import { process_axios_response, is_url_belonging_voter_answering, update_token } from './axios_utils'
import { update } from 'lodash';

// default setting
axios.defaults.timeout = 50000  // 超时时间
axios.defaults.baseURL = 'http://127.0.0.1:5000'
// axios.defaults.baseURL = 'http://3.145.140.55'
// axios.defaults.baseURL = 'http://synspot-env.eba-mvtmbnb2.us-east-2.elasticbeanstalk.com/'


// console.log('useRouter', router);



const linkTo = (path, router) => {
  router.push({
      path: path,
  });
};

// Add a request interceptor to axios
axios.interceptors.request.use(config => {
  console.log('request config1', config)
  const authenticationStore = useAuthenticationStore();
  // If current request is sending to the voter answering part
  // we may need to add the voterToken
  if (is_url_belonging_voter_answering(config.url) === true) {
    const voterToken = authenticationStore.voterToken;
    config.headers.Authorization = `Bearer ${voterToken}`
  } else {
    // If current request is sending to the api that needs
    // to verify user identity, we need to add the userToken
    const userToken = authenticationStore.userToken;
    config.headers.Authorization = `Bearer ${userToken}`
  }
  console.log('request config2', config)
  return config
}, function (error) {
  // handle error
  return Promise.reject(error)
})

// Add a response interceptor to axios
axios.interceptors.response.use(response => {
  console.log('----- Debug Axios Response', response)
  let data = process_axios_response(response)
  update_token(data)
  return response
}, error => {
  // handle response error
  // there are 2 kinds of response error:
  // 1. error return by the back-end
  // 2. error throwed by the XMLHttpRequest
  console.log('----- Debug Axios Error', error)
  if ('response' in error && error.response !== undefined){
    if ('status' in error.response){
      console.log('error.response.status', error.response.status)
      switch  (error.response.status) {
        case 401:
          const authenticationStore = useAuthenticationStore();
          // clean Token && isauthenticated state
          authenticationStore.logoutAction()
          // go to login page
          console.log('useRouter222', router)
          if (router.currentRoute.path !== '/login') {
            // Vue.toasted.error('401: 认证已失效，请先登录', { icon: 'fingerprint' })
            router.replace({
              path: '/login',
              query: { redirect: router.currentRoute.path },
            })

            Toastify({
              text: "Please Login first",
              duration: 10000,
              // destination: "https://github.com/apvarun/toastify-js",
              newWindow: true,
              close: true,
              gravity: "top", // `top` or `bottom`
              position: "right", // `left`, `center` or `right`
              stopOnFocus: true, // Prevents dismissing of toast on hover
              style: {
                background: "linear-gradient(to right, #00b09b, #96c93d)",
              },
              onClick: function(){} // Callback after click
            }).showToast();
          }
          break
        case 404:
          // Vue.toasted.error('404: NOT FOUND', { icon: 'fingerprint' })
          router.back()
          break
        case 500:
          break
      }
    }
  }
  return Promise.reject(error)
})

// const install = (app) => {
//   app.config.globalProperties.$f = () => {
//     return axios;
//   };
// };

export { axios as axios }
