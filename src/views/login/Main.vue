<template>
  <div>
    <DarkModeSwitcher />
    <div class="container sm:px-10">
      <div class="block xl:grid grid-cols-2 gap-4">
        <!-- BEGIN: Login Info -->
        <div class="hidden xl:flex flex-col min-h-screen">


          <!-- <router-link
            :to="{ name: 'side-menu-dashboard-overview-4' }"
            tag="a"
            class="intro-x flex items-center pl-5 pt-4"
          >
            <img
              alt="Midone Tailwind HTML Admin Template"
              class="w-6"
              src="@/assets/images/logo.svg"
            />
            <span class="hidden xl:block text-white text-lg ml-3"> Interval Privacy </span>
          </router-link> -->



          <router-link
            :to="{ name: 'side-menu-faq-layout-3' }"
            tag="a"
            class="intro-x flex items-center pl-5 pt-4"
          >
            <img
              alt="Midone Tailwind HTML Admin Template"
              class="w-6"
              src="@/assets/images/logo.svg"
            />
            <span class="text-white text-lg ml-3"> Interval Privacy </span>
          </router-link>


          <div class="my-auto">
            <img
              alt="Midone Tailwind HTML Admin Template"
              class="-intro-x w-1/2 -mt-16"
              src="@/assets/images/illustration.svg"
            />
            <div
              class="-intro-x text-white font-medium text-4xl leading-tight mt-10"
            >
              A few more clicks to <br />
              sign in to your account.
            </div>
            <div
              class="-intro-x mt-5 text-lg text-white text-opacity-70 dark:text-slate-400"
            >
              Create survey with Interval Privacy to protect user privacy
            </div>
          </div>
        </div>
        <!-- END: Login Info -->
        <!-- BEGIN: Login Form -->
        <div class="h-screen xl:h-auto flex py-5 xl:py-0 my-10 xl:my-0">
          <div
            class="my-auto mx-auto xl:ml-20 bg-white dark:bg-darkmode-600 xl:bg-transparent px-5 sm:px-8 py-8 xl:p-0 rounded-md shadow-md xl:shadow-none w-full sm:w-3/4 lg:w-2/4 xl:w-auto"
          >
            <h2
              class="intro-x font-bold text-2xl xl:text-3xl text-center xl:text-left"
            >
              Sign In
            </h2>
            <div class="intro-x mt-2 text-slate-400 xl:hidden text-center">
              A few more clicks to sign in to your account. Create survey with Interval Privacy to protect user privacy
            </div>
            <div class="intro-x mt-8">
              <input
                id="login-form-1"
                v-model.trim="validate.username.$model"
                type="text"
                name="username"
                class="intro-x login__input form-control py-3 px-4 block"
                :class="{ 'border-danger': validate.username.$error }"
                placeholder="username"
              />
              <template v-if="validate.username.$error">
                <div
                v-for="(error, index) in validate.username.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
              </template>

              <input
                id="login-form-2"
                v-model.trim="validate.password.$model"
                type="text"
                name="password"
                class="intro-x login__input form-control py-3 px-4 block mt-4"
                :class="{ 'border-danger': validate.password.$error }"
                placeholder="password"
              />
              <template v-if="validate.password.$error">
                <div
                v-for="(error, index) in validate.password.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
              </template>
            </div>
            <div
              class="intro-x flex text-slate-600 dark:text-slate-500 text-xs sm:text-sm mt-4"
            >
              <div class="flex items-center mr-auto">
                <input
                  id="remember-me"
                  type="checkbox"
                  class="form-check-input border mr-2"
                  value='yes'
                  v-model="remember_me"
                />
                <label class="cursor-pointer select-none" for="remember-me"
                  >Remember me</label
                >
                <!-- {{ remember_me }} -->
              </div>
              <a href="javascript:;" @click="to_reset_pwd_page">Forgot Password?</a>
            </div>
            <div class="intro-x mt-5 xl:mt-8 text-center xl:text-left">
              <button
                @click="login"
                class="btn btn-primary py-3 px-4 w-full xl:w-32 xl:mr-3 align-top"
              >
                Login
              </button>
              <button
                class="btn btn-outline-secondary py-3 px-4 w-full xl:w-32 mt-3 xl:mt-0 align-top"
                @click="to_register_page"
              >
                Register
              </button>
            </div>
            <div
              class="intro-x mt-10 xl:mt-24 text-slate-600 dark:text-slate-500 text-center xl:text-left"
            >
              By signing up, you agree to our
              <a 
                @click="to_terms_and_conditions"
                class="text-primary dark:text-slate-200" 
                href="javascript:;"
                >Terms and Conditions</a
              >
              &
              <a 
                @click="to_privacy_policy"
                class="text-primary dark:text-slate-200" 
                href="javascript:;"
                >Privacy Policy</a
              >
            </div>
          </div>
        </div>
        <!-- END: Login Form -->
        <!-- BEGIN: Request Success Content -->
        <div
          id="request-success-content"
          class="toastify-content hidden flex"
        >
          <CheckCircleIcon class="text-success" />
          <div class="ml-4 mr-4">
            <div class="font-medium">Login successfully!</div>
            <div class="text-slate-500 mt-1">
              Welcome!
            </div>
          </div>
        </div>
        <!-- END: Request Success Content -->
        <!-- BEGIN: Request Error Content -->
          <div
            id="request-error-content"
            class="toastify-content hidden flex"
          >
            <CheckCircleIcon class="text-danger" />
            <div class="ml-4 mr-4">
              <div class="font-medium">Request error!</div>
              <div class="text-slate-500 mt-1" >
                Please check your input!
              </div>
            </div>
          </div>
        <!-- END: Request Error Content -->
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, toRefs, ref } from "vue";
import {
  required,
  minLength,
  maxLength,
  email,
  url,
  integer,
  requiredIf
} from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import { computed, onMounted } from "vue";
import Toastify from "toastify-js";
import { useRoute, useRouter } from "vue-router";
import DarkModeSwitcher from "@/components/dark-mode-switcher/Main.vue";
import dom from "@left4code/tw-starter/dist/js/dom";
import { useInfoStore } from "@/stores/user-info"
import { useAuthenticationStore } from "@/stores/authentication"
import { process_axios_error, get_auth_url, get_api_url } from "@/utils/axios_utils"
import { axios } from "@/utils/axios";
// import { axios } from "@/utils/axios";
import { linkTo } from "./index"

const router = useRouter();

const infoStore = useInfoStore()
// const username = computed(() => infoStore.username);
// const password = computed(() => infoStore.password);

const authenticationStore = useAuthenticationStore()

const remember_me = ref(false)

const formData = reactive({
  username: '',
  password: '',
});

const rules = {
  username: {
    required,
    minLength: minLength(1),
  },
  password: {
    required,
    minLength: minLength(1),
  },
};
// const validate = reactive(useVuelidate(rules, toRefs(formData)));
const validate = useVuelidate(rules, toRefs(formData));

const store_user_info = (username, password, remember) => {
  infoStore.setRemember(remember)
  infoStore.setUsername(username)
  infoStore.setPassword(password)
}

const load_user_info = () => {
  console.log('????', infoStore.remember, infoStore.remember === true, typeof infoStore.remember)
  if (infoStore.remember === 'true') {
    console.log('@@@@')
    formData.username = infoStore.username
    formData.password = infoStore.password
  }
  remember_me.value = infoStore.remember
} 

const login = async () => {
  let login_data = {
    'username': formData.username,
    'password': formData.password
  }
  console.log('login_data', login_data, validate.value.$invalid)
  let username = formData.username
  let password = formData.password
  store_user_info(username, password, remember_me.value)
  if (validate.value.$invalid) {
    Toastify({
      node: dom("#request-error-content")
        .clone()
        .removeClass("hidden")[0],
      duration: 10000,
      newWindow: true,
      close: true,
      gravity: "top",
      position: "center",
      stopOnFocus: true,
    }).showToast();
  } else {
    try{
      
      let response = await axios.post(get_auth_url('get_userToken'), login_data)
      authenticationStore.loginAction(response.data.userToken)
      Toastify({
        node: dom("#request-success-content")
          .clone()
          .removeClass("hidden")[0],
        duration: 10000,
        newWindow: true,
        close: true,
        gravity: "top",
        position: "center",
        stopOnFocus: true,
      }).showToast();
      linkTo('side-menu-create-new-survey', router, {})
    } catch (err) {
      let processed_err = process_axios_error(err)
      console.log(`login processed err: ${processed_err}`)

      Toastify({
        node: dom("#request-error-content")
          .clone()
          .removeClass("hidden")[0],
        duration: 10000,
        newWindow: true,
        close: true,
        gravity: "top",
        position: "center",
        stopOnFocus: true,
      }).showToast();
    }
  }
}

const to_register_page = () => {
  linkTo('register', router, {})
}

const to_reset_pwd_page = () => {
  linkTo('resetPwd', router, {})
}

const to_terms_and_conditions = () => {
  let params = {
    'faq_indicator': 'terms_and_conditions'
  }
  linkTo('side-menu-faq-layout-3', router, params)
}

const to_privacy_policy = () => {
  let params = {
    'faq_indicator': 'privacy_policy'
  }
  linkTo('side-menu-faq-layout-3', router, params)
}

onMounted(() => {
  load_user_info()
  dom("body").removeClass("main").removeClass("error-page").addClass("login");
});
</script>
