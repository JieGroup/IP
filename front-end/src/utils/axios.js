import axios from 'axios'
import Toastify from "toastify-js";
import { computed, toRefs } from "vue";
import { useAuthenticationStore } from "@/stores/authentication";
import { useRoute, useRouter } from "vue-router";

// default setting
axios.defaults.timeout = 50000  // 超时时间
axios.defaults.baseURL = 'http://127.0.0.1:5000'
// axios.defaults.baseURL = 'http://3.145.140.55'
// axios.defaults.baseURL = 'http://synspot-env.eba-mvtmbnb2.us-east-2.elasticbeanstalk.com/'

const router = useRouter();

const linkTo = (path, router) => {
  router.push({
      path: path,
  });
};

// Add a request interceptor to axios
axios.interceptors.request.use(config => {
  console.log('request config1')
  // add token to request
  const authenticationStore = useAuthenticationStore();
  const userToken = computed(() => authenticationStore.userToken);
  if (userToken !== null) {
    config.headers.Authorization = `Bearer ${userToken}`
  }
  console.log('request config2')
  return config
}, function (error) {
  // handle error
  return Promise.reject(error)
})

// Add a response interceptor to axios
axios.interceptors.response.use(response => {
  console.log('response config2', response)
  return response
  // return Promise.resolve(response)
}, error => {
  // handle response error
  console.log('Error_https', error)
  if ('response' in error && error.response !== undefined){
    if ('status' in error.response){
      // console.log('error', error.response.data.error)
      // console.log('error_name', error.response.data.error_name)
      switch  (error.response.status) {
        case 401:
          // 清除 Token 及 已认证 等状态
          store.logoutAction()
          // 跳转到登录页
          if (router.currentRoute.path !== '/login') {
            Vue.toasted.error('401: 认证已失效，请先登录', { icon: 'fingerprint' })
            router.replace({
              path: '/login',
              query: { redirect: router.currentRoute.path },
            })
          }
          break
        case 404:
          Vue.toasted.error('404: NOT FOUND', { icon: 'fingerprint' })
          router.back()
          break
        case 500:
          return Promise.reject(error)
          
          // return error
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
