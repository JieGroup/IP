<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Form Validation</h2>
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
              <!-- <button @click="submit_ceshi_answer" type="button" class="btn btn-primary mt-3">
              submit_ceshi_answer
              </button> -->
              <br />
              <br />

              <!-- BEGIN: Start Answering Topics -->
              <div v-if="isStartAnswer === true" class="input-form mt-3">
              WOW: {{ isStartAnswer }} {{ isStartAnswer.value }}
              <label
                  for="validation-form-2"
                  class="form-label w-full flex flex-col sm:flex-row"
              >
                  Survey Template ID
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
                  placeholder="The survey template id that you need to answer."
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
              </div>

              <br />

              <div class="input-form mt-3">
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
              <!-- END: Start Answering Topics -->

              <!-- BEGIN: Voter Submit Answers -->
              <div v-if="isStartAnswer === false" class="input-form mt-3">
                isStartAnswer shi false
                <div v-if="formTemplateData.surveyUpdateMethod === 'static'" class="input-form mt-3">
                  <StaticOpt  v-for="(item, key) in formTemplateData.surveyTopics"
                              :key="key"
                              :subSurveyTopicKey="key"
                              :subSurveyTopicValue="item"
                              :answerFormData="answerFormData"/>
                </div>

                <div v-if="formTemplateData.surveyUpdateMethod === 'uniform'" class="input-form mt-3">
                  <UniformOpt  v-for="(item, key) in formTemplateData.surveyTopics"
                              :key="key"
                              :subSurveyTopicKey="key"
                              :subSurveyTopicValue="item"
                              :answerFormData="answerFormData"/>
                </div>
              </div>
              <!-- BEGIN: Voter Submit Answers -->

              <button type='button' @click='test_error'>
                test_error
              </button>
              zhe!! {{ request_error }}
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
              <!-- END: Request Error Content -->
              <!-- BEGIN: Request Error Content -->
              <div
                id="request-error-content"
                class="toastify-content hidden flex"
              >
                <CheckCircleIcon class="text-danger" />
                <div class="ml-4 mr-4">
                  <div class="font-medium">Network request error!</div>
                  <div class="text-slate-500 mt-1">
                    <!-- {{ request_error }}
                    error_name: {{ request_error['error_name'] }}
                    error_msg: {{ request_error.error_msg }}
                    error_status: {{ request_error.error_status }} -->
                    <!-- <div> -->
                    Please check your input and send again
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
      <button @click='tiaozhuan'>wowowow
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
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
const voterAnswer = voterAnswerStore();
const storedSurveyTopics = computed(() => voterAnswer.surveyTopics);
const storedSurveyAnswerID = computed(() => voterAnswer.surveyAnswerID);
const storedSurveyUpdateMethod = computed(() => voterAnswer.surveyUpdateMethod);

//判断voterToken
const authenticationStore = useAuthenticationStore();
// const voterToken = computed(() => authenticationStore.voterToken);

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
console.log('~~~~~', startFormDataValidate)

const tiaozhuan = () => {
  console.log('!!!!ceshi', startFormDataValidate)
  startFormDataValidate.value.$touch()
  // startFormDataValidate.$touch()

}

const test_error = () => {
  request_error.value = 'ceshishishi'
  console.log('request_error', request_error)
  // Object.assign(request_error, 'ceshideyo')
  // Object.assign(request_error.error, 'ceshideyo')
  Toastify({
    text: 'shaaaa',
    node: dom("#request-error-content")
      .clone()
      .removeClass("hidden")[0],
    duration: 10000,
    newWindow: true,
    close: true,
    gravity: "top",
    position: "right",
    stopOnFocus: true,
  }).showToast();

  Toastify({

    // <div class="ml-4 mr-4">
    //             <div class="font-medium">Network request error!</div>
    //             <div class="text-slate-500 mt-1" >

    text: "ceshi0",
    className: 'toastify-content hidden flex',
    className: 'ml-4 mr-4',
    duration: 3000,
    // gravity: "bottom", // `top` or `bottom`
    // position: 'center', // `left`, `center` or `right`
    // backgroundColor: "linear-gradient(to right, red, orange)",
    newWindow: true,
    close: true,
    gravity: "top",
    position: "right",
    stopOnFocus: true,
  }).showToast();

  Toastify({
    text: "ceshi1",
    duration: 3000,
    // destination: "https://github.com/apvarun/toastify-js",
    newWindow: true,
    close: true,
    gravity: "top", // `top` or `bottom`
    position: "left", // `left`, `center` or `right`
    stopOnFocus: true, // Prevents dismissing of toast on hover
    style: {
      background: "linear-gradient(to right, #00b09b, #96c93d)",
    },
    onClick: function(){} // Callback after click
  }).showToast();

  Toastify({
  text: "ceshi2",
  className: "info",
  style: {
    background: "linear-gradient(to right, #00b09b, #96c93d)",
  }
}).showToast();
}

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
  authenticationStore.setVoterToken(null)
}

// ref, computed 取值要加.value

const submit_ceshi_answer = () => {
  send_voter_submit_answers()
}

const send_to_server = () => {
  console.log('formTemplateData send_to_server', formTemplateData)
  console.log('topics and token value', storedSurveyTopics.value)
  if (Object.keys(formTemplateData).length > 0){
    send_voter_submit_answers()
  } else {
    send_voter_start_answering()
  }
}

const store_cur_template_info = (templateData) => {
  // change data in storage
  console.log('~~~~~~store_cur_template_info', templateData)
  voterAnswer.setsurveyTopics(templateData.updated_survey_topics);
  voterAnswer.setsurveyAnswerID(templateData.survey_answer_id);
  voterAnswer.setsurveyUpdateMethod(templateData.survey_update_method);

  // change variables in current page
  formTemplateData.surveyTopics = templateData.updated_survey_topics;
  formTemplateData.surveyAnswerID = templateData.survey_answer_id;
  formTemplateData.surveyUpdateMethod = templateData.survey_update_method;

  console.log('change data in storage', formTemplateData)
}

const send_voter_start_answering = async () => {
  // static categorical: 62e220016648301fab9ab211
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
      position: "right",
      stopOnFocus: true,
    }).showToast();
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
  let answer_id = formTemplateData.surveyAnswerID
  try{
    let res = await axios.post(get_api_url('voter_submit_answers'), processed_answerFormData)
    res = process_axios_response(res)
    console.log('voter_submit_answers_rrrese', res, formTemplateData)

    Toastify({
      node: dom("#request-success-content")
        .clone()
        .removeClass("hidden")[0],
      duration: 10000,
      newWindow: true,
      close: true,
      gravity: "top",
      position: "right",
      stopOnFocus: true,
    }).showToast();
    
    // Finish all rounds of survey
    if (Object.keys(res.updated_survey_topics).length === 0) {
      back_to_start_answering()
      let params = {
        surveyAnswerID: answer_id
      }
      linkTo('side-menu-answer-form-done', router, params)
    } else {
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
      position: "right",
      stopOnFocus: true,
    }).showToast();
  } 
}

const load_prev_template_info = () => {
  console.log('##### load_prev_template_info', voterAnswer.surveyTopics)
  // console.log('##### json parse', JSON.parse(voterAnswer.surveyTopics))
  for (let key in voterAnswer.surveyTopics) {
    console.log('dasdsad', key)
  }
  console.log('storedSurveyTopics.value', storedSurveyTopics.value)
  formTemplateData.surveyTopics = storedSurveyTopics.value;
  formTemplateData.surveyAnswerID = storedSurveyAnswerID.value;
  formTemplateData.surveyUpdateMethod = storedSurveyUpdateMethod.value;
  
}

onMounted(() => {
  // Indicates the voter is answering the survey topics
  // The voter might refresh the page
  console.log('storage', storedSurveyTopics, storedSurveyAnswerID, storedSurveyUpdateMethod)
  // if (storedSurveyTopics.value !== null){
  //   console.log('jinlai')
  //   // isStartAnswer = false
  //   // Object.assign(isStartAnswer, false)
  //   isStartAnswer.value = false
  //   console.log('isStartAnswer', isStartAnswer)
  //   // load_prev_template_info()
  // } else {
  //   // New answer to a survey template
  //   // pass
  // }
});


// let fix_form_data = reactive({})
// let unique_id = 0
// let dynamic_form_array = reactive([{unique_id: unique_id}])

// const add_dynamic_form = () => {
//   console.log('jiajiajia')
//   unique_id += 1
//   dynamic_form_array.push({unique_id: unique_id})
//   console.log('dynamic_form_array', dynamic_form_array, unique_id)
// }

// const delete_dynamic_form = (dynamic_form_index) => {
//   console.log('shemeqingkuang-000', dynamic_form_array)
//   console.log('wudi,duide', dynamic_form_index)
  
//   if (dynamic_form_index !== 0){
//     // array.splice(index, howmany)
//     dynamic_form_array.splice(dynamic_form_index, 1)
//   }
//   console.log('shemeqingkuang', dynamic_form_array)
// }

// const is_fix_form_validate = (data_valid) => {
//   // fix_form_data.validate is the value of 
//   // the vuelidate we used
//   const validate = fix_form_data.validate
//   validate.$touch();
//   console.log('fixxxxx', validate.$invalid, data_valid, validate)
//   if (validate.$invalid === true) {
//     data_valid = false
//   }
//   // data_invalid = validate.$invalid
//   return data_valid
// };

// const is_dynamic_form_validate = (data_valid) => {
//   console.log('dynamic_form_arrayaa', dynamic_form_array);
//   dynamic_form_array.forEach((item, index) => {
//     console.log('dynamic_form_arrayaabb', item, index);
//     console.log('sdfasdf', item['validate'])
//     console.log('sdfasdfsdfsa', item.validate)
//     // item is the value of the vuelidate we used
//     const validate = item.validate
//     validate.$touch();
//     console.log('dynamic!!!!!!', validate.$invalid, data_valid)
//     if (validate.$invalid === true) {
//       data_valid = false
//     }
//     // data_invalid = validate.$invalid
//   });
  
//   return data_valid
// };

// const notification = (data_valid) => {
//   if (data_valid) {
//     Toastify({
//       node: dom("#success-notification-content")
//         .clone()
//         .removeClass("hidden")[0],
//       duration: 3000,
//       newWindow: true,
//       close: true,
//       gravity: "top",
//       position: "right",
//       stopOnFocus: true,
//     }).showToast();
//   } else {
//     Toastify({
//       node: dom("#failed-notification-content")
//         .clone()
//         .removeClass("hidden")[0],
//       duration: 3000,
//       newWindow: true,
//       close: true,
//       gravity: "top",
//       position: "right",
//       stopOnFocus: true,
//     }).showToast();
//   }
// }

// const is_form_valid = () => {
//   let fix_data_valid = true
//   let dynamic_data_valid = true
//   fix_data_valid = is_fix_form_validate(fix_data_valid)
//   dynamic_data_valid = is_dynamic_form_validate(dynamic_data_valid)
//   console.log('total@@@@@@', fix_data_valid, dynamic_data_valid)
//   return fix_data_valid && dynamic_data_valid
// }


// const send_to_server = () => {
//   let validation = is_form_valid()
//   notification(validation)
//   console.log('fix_form_data', fix_form_data)
//   console.log('dynamic_form_array', dynamic_form_array)
//   if (validation === true) {
//     let templateData = process_template_data(
//       fix_form_data,
//       dynamic_form_array
//     )
//     console.log('templateData', templateData)
//     send_form(templateData)
//   }
// }
</script>
