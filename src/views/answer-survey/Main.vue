<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Answer Survey</h2>
  </div>

  <div class="grid grid-cols-12 gap-6 mt-5">
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- BEGIN: Form Validation -->
      <form class="validate-form">
        <!-- <PreviewComponent class="intro-y box" v-slot="{ toggle }"> -->
        <PreviewComponent class="intro-y box">
          <!-- <div
            class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
          > -->
            <!-- <h2 class="font-medium text-base mr-auto">Implementation</h2>
            <div
              class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
            >
              <label class="form-check-label ml-0" for="show-example-1"
                >Show example code</label
              >
              <input
                @click="toggle"
                class="form-check-input mr-0 ml-3"
                type="checkbox"
              />
            </div> -->
          <!-- </div> -->

          <div class="p-5">
            <Preview>
              <!-- BEGIN: Validation Form -->
              <button @click="send_to_server" type="button" class="btn btn-primary mt-3">
              Send
              </button>
              {{ }}
              <button @click="back_to_start_answering" type="button" class="btn btn-primary mt-3">
              Back
              </button>
              
              <!-- <br />
              <br /> -->

              <!-- BEGIN: Start Answering Topics -->
              <div v-if="isStartAnswer === true" class="input-form mt-3">
              <!-- WOW: {{ isStartAnswer }} {{ isStartAnswer.value }} -->
              <label
                  for="validation-form-2"
                  class="form-label w-full flex flex-col sm:flex-row"
              >
                  Survey ID
                  <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                  >Required</span
                  >
              </label>
              <input
                  id="validation-form-2"
                  v-model.trim="startFormDataValidate.survey_template_id.$model"
                  type="text"
                  name="survey_template_id"
                  class="form-control"
                  :class="{ 'border-danger': startFormDataValidate.survey_template_id.$error }"
                  placeholder="The survey id that you need to answer."
              />
              <template v-if="startFormDataValidate.survey_template_id.$error">
                  <div
                  v-for="(error, index) in startFormDataValidate.survey_template_id.$errors"
                  :key="index"
                  class="text-danger mt-2"
                  >
                  {{ error.$message }}
                  </div>
              </template>
              <br />
              <br />
              <label
                  for="validation-form-2"
                  class="form-label w-full flex flex-col sm:flex-row"
              >
                  Mturk ID
                  <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                  >Required</span
                  >
              </label>
              <input
                  id="validation-form-2"
                  v-model.trim="startFormDataValidate.mturk_id.$model"
                  type="text"
                  name="mturk_id"
                  class="form-control"
                  :class="{ 'border-danger': startFormDataValidate.mturk_id.$error }"
                  placeholder="Your Mturk ID."
              />
              <template v-if="startFormDataValidate.mturk_id.$error">
                  <div
                  v-for="(error, index) in startFormDataValidate.mturk_id.$errors"
                  :key="index"
                  class="text-danger mt-2"
                  >
                  {{ error.$message }}
                  </div>
              </template>
              </div>

              

              <!-- <div class="input-form mt-3">
              
              </div> -->
              <!-- END: Start Answering Topics -->

              <!-- BEGIN: Voter Submit Answers -->
              <!-- formTemplateData{{ formTemplateData }} -->
              <div v-if="isStartAnswer === false" class="input-form mt-3">
                <div v-if="formTemplateData.surveyUpdateMethod === 'static'" class="input-form mt-3">
                  <StaticOpt  v-for="(item, key, index) in formTemplateData.surveyTopics"
                              :key="unique_key_num+index"
                              :subSurveyTopicKey="key"
                              :subSurveyTopicValue="item"
                              :answerFormData="answerFormData"/>
                </div>

                <div v-if="formTemplateData.surveyUpdateMethod === 'uniform'" class="input-form mt-3">
                  <UniformOpt  v-for="(item, key, index) in formTemplateData.surveyTopics"
                              :key="unique_key_num+index"
                              :subSurveyTopicKey="key"
                              :subSurveyTopicValue="item"
                              :answerFormData="answerFormData"/>
                </div>
              </div>
              <!-- BEGIN: Voter Submit Answers -->

              <!-- <button @click="ceshierror">
                ceshierror
              </button> -->
              <!-- BEGIN: Request Success Content -->
              <div
                id="request-success-content"
                class="toastify-content hidden flex"
              >
                <CheckCircleIcon class="text-success" />
                <div class="ml-4 mr-4">
                  <div class="font-medium">Send request successfully!</div>
                  <div class="text-slate-500 mt-1">
                    Please wait for the response
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
                  <div class="text-slate-500 mt-1">
                    <!-- {{ request_error }}
                    error_name: {{ request_error['error_name'] }}
                    error_msg: {{ request_error.error_msg }}
                    error_status: {{ request_error.error_status }} -->
                    <!-- <div> -->
                    The error may caused by the following reasons:
                    <br/>
                      1. Incorrect or incomplete input form
                      <br/>
                      2. The number of respondents has been reached
                    <!-- </div> -->
                  </div>
                </div>
              </div>
              <!-- END: Request Error Content -->
            </Preview>
          </div>
        </PreviewComponent>
      </form>
      <!-- END: Form Validation -->
    </div>
  </div>
</template>

<script setup>
import { ref, isReactive } from "vue";
import { reactive, toRefs, computed, onMounted } from "vue";
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
import Toastify from "toastify-js";
import { useRoute, useRouter } from "vue-router";
import dom from "@left4code/tw-starter/dist/js/dom";
import { axios } from "@/utils/axios";
import { linkTo, process_startFormData, process_answerFormData } from "./index"
import { process_axios_response, process_axios_error, get_api_url } from "@/utils/axios_utils"
import { useAuthenticationStore } from '@/stores/authentication'
import { voterAnswerStore } from '@/stores/voter-answer'
import StaticOpt from '@/components/voter-ans-opt/static-ans-opt/Main.vue';
import UniformOpt from '@/components/voter-ans-opt/uniform-ans-opt/Main.vue'

const router = useRouter();
const route = useRoute();
// let request_error = reactive({
//   error: 'adadsd'
// })
let request_error = ref(false)

let isStartAnswer = ref(true);
// let unique_id = 0
// voter's answers
let answerFormData = reactive({})
// data returned by the back-end
let formTemplateData = reactive({})

//判断answer store
const storedVoterAnswer = voterAnswerStore();

//判断voterToken
const authenticationStore = useAuthenticationStore();
// const voterToken = computed(() => authenticationStore.voterToken);

let unique_key_num = ref(100000);

let startFormData = reactive({
  survey_template_id: "",
  mturk_id: "",
});
const rules = {
  survey_template_id: {
    required,
    minLength: minLength(1),
  },
  mturk_id: {
    required,
    minLength: minLength(1),
  },
};
// const startFormDataValidate = reactive(useVuelidate(rules, toRefs(startFormData)));
const startFormDataValidate = useVuelidate(rules, toRefs(startFormData));

const back_to_start_answering = () => {
  // go back to start_answering
  // clean related variables
  for (let key in formTemplateData) {
    delete formTemplateData[key]
  }
  for (let key in answerFormData) {
    delete answerFormData[key]
  }
  isStartAnswer.value = true
  authenticationStore.deleteVoterToken();
  storedVoterAnswer.deletesurveyTopics()
  storedVoterAnswer.deletesurveyAnswerID();
  storedVoterAnswer.deletesurveyUpdateMethod();
}

// ref, computed 取值要加.value

const send_to_server = () => {
  console.log('formTemplateData send_to_server', formTemplateData)
  // console.log('topics and token value', storedSurveyTopics.value)
  if (Object.keys(formTemplateData).length > 0){
    send_voter_submit_answers()
  } else {
    send_voter_start_answering()
  }
}

const load_prev_template_info = () => {
  console.log('##### load_prev_template_info', storedVoterAnswer)
  // console.log('##### json parse', JSON.parse(voterAnswer.surveyTopics))
  // for (let key in storedVoterAnswer.surveyTopics) {
  //   console.log('dasdsad', key)
  // }
  console.log('storedSurveyTopics.value', storedVoterAnswer.surveyTopics, JSON.parse(storedVoterAnswer.surveyTopics))
  formTemplateData.surveyTopics = JSON.parse(storedVoterAnswer.surveyTopics);
  formTemplateData.surveyAnswerID = storedVoterAnswer.surveyAnswerID;
  formTemplateData.surveyUpdateMethod = storedVoterAnswer.surveyUpdateMethod;
}

const store_cur_template_info = (templateDataFromBackEnd) => {
  // change data in storage
  console.log('~~~~~~store_cur_template_info', templateDataFromBackEnd)
  // object needs to be json stringify
  storedVoterAnswer.setsurveyTopics(JSON.stringify(templateDataFromBackEnd.updated_survey_topics));
  storedVoterAnswer.setsurveyAnswerID(templateDataFromBackEnd.survey_answer_id);
  storedVoterAnswer.setsurveyUpdateMethod(templateDataFromBackEnd.survey_update_method);

  // change variables in current page
  formTemplateData.surveyTopics = templateDataFromBackEnd.updated_survey_topics;
  formTemplateData.surveyAnswerID = templateDataFromBackEnd.survey_answer_id;
  formTemplateData.surveyUpdateMethod = templateDataFromBackEnd.survey_update_method;

  console.log('change data in storage', formTemplateData, isReactive(formTemplateData))
}

const send_voter_start_answering = async () => {
  // static categorical: 62eb182d048f31af26c30f05
  // static categorical_multiple: 62e2e89b6be732eba69f0b6a
  // static continuous: 62e220226648301fab9ab213
  // static categorical + continuous: 62e2204c6648301fab9ab215
  // uniform categorical: 62e220af6648301fab9ab217
  // uniform continuous: 62e220d76648301fab9ab219
  // uniform categorical + continuous: 62e2210d6648301fab9ab21b

  // send voter start answering data to
  // corresponding back-end api
  console.log('!!!!', startFormDataValidate)

  startFormDataValidate.value.$touch();
  let startFormData = process_startFormData(
    startFormDataValidate
  )
  if (startFormDataValidate.value.$invalid) {
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
      let res = await axios.post(get_api_url('voter_start_answering'), startFormData);
      console.log('bucuowu')
      res = process_axios_response(res);
      // update indicator and variables
      isStartAnswer.value = false
      store_cur_template_info(res)
      console.log('$$$$', res)
      console.log('formTemplateData', formTemplateData)
    } catch (err) {
      console.log('sttt', err)
      let processed_err = process_axios_error(err)
      console.log('----- Debugdone', processed_err)
      // request_error.error_name = processed_err.error_name
      // request_error.error_msg = processed_err.error_msg
      // request_error.error_status = processed_err.error_status
      console.log('fuzhi', request_error)
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

const send_voter_submit_answers = async () => {
  // send voter submit answer data to
  // corresponding back-end api
  let processed_answerFormData = process_answerFormData(
    formTemplateData.surveyTopics,
    formTemplateData.surveyAnswerID,
    formTemplateData.surveyUpdateMethod,
    answerFormData
  )
  if (processed_answerFormData === false) {
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
    let answer_id = formTemplateData.surveyAnswerID
    try{
      let res = await axios.post(get_api_url('voter_submit_answers'), processed_answerFormData)
      res = process_axios_response(res)
      console.log('voter_submit_answers_rrrese', res, formTemplateData)
      unique_key_num.value = unique_key_num.value + 100000;
      const dom_ele = dom("#request-success-content").clone().removeClass("hidden")[0]
      dom_ele.children[1].querySelector(".font-medium").innerHTML = 'Submitted successfully!'

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
      
      // Finish all rounds of survey
      if (Object.keys(res.updated_survey_topics).length === 0) {
        back_to_start_answering()
        let params = {
          surveyAnswerID: answer_id
        }
        linkTo('side-menu-answer-survey-done', router, params)
      } else {
        console.log('update survey answer')
        store_cur_template_info(res)
      }
    } catch (err) {
      let processed_err = process_axios_error(err)
      // request_error.error_name = processed_err.error_name
      // request_error.error_msg = processed_err.error_msg
      // request_error.error_status = processed_err.error_status

      console.log('fuzhi', request_error)
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



onMounted(() => {
  // Indicates the voter is answering the survey topics
  // The voter might refresh the page

  console.log('storage', storedVoterAnswer.surveyTopics, storedVoterAnswer.surveyAnswerID, storedVoterAnswer.surveyUpdateMethod)
  console.log(JSON.parse(JSON.stringify(storedVoterAnswer.surveyTopics)))
  console.log('storage_json_parse', storedVoterAnswer.surveyTopics, typeof storedVoterAnswer.surveyTopics === 'string')
  console.log('!@#!@#!', router.query, route.query)
  // if (storedVoterAnswer.surveyTopics === null && isStartAnswer.value === true){
  //   //
  if (route.query !== null && 'surveyTemplateID' in route.query){
    startFormData.survey_template_id = route.query.surveyTemplateID
  }
  // } else {
  // let a = JSON.parse(null)
  // let b = JSON.parse('')
  // console.log('123123', a, b)
  try {
    JSON.parse(storedVoterAnswer.surveyTopics)
  } catch (error) {
    console.log('------DEBUG JSON.parse error', error)
    back_to_start_answering()
  }
  // }
  if (JSON.parse(storedVoterAnswer.surveyTopics) !== null || isStartAnswer.value === false){
    console.log('jinlai')
    isStartAnswer.value = false
    console.log('isStartAnswer', isStartAnswer)
    load_prev_template_info()
  } else {
    // New answer to a survey template
    // pass
  }
});
</script>
