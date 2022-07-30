<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Form Validation</h2>
  </div>

  <div class="grid grid-cols-12 gap-6 mt-5">
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- BEGIN: Form Validation -->
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
            <div class="input-form mt-3">
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
                  v-model.trim="FormDataValidate.survey_template_id.$model"
                  type="text"
                  name="survey_template_id"
                  class="form-control"
                  :class="{ 'border-danger': FormDataValidate.survey_template_id.$error }"
                  placeholder="The survey template id that you want to get voter answers."
              />
              <template v-if="FormDataValidate.survey_template_id.$error">
                  <div
                  v-for="(error, index) in FormDataValidate.survey_template_id.$errors"
                  :key="index"
                  class="text-danger mt-2"
                  >
                  {{ error.$message }}
                  </div>
              </template>
            </div>
            <!-- END: Start Answering Topics -->

            <div v-for="(option, index) in allSurveyAnswers" 
                      :key="index"
                      :value="index">{{ option }}</div>

            allSurveyAnswers: {{ allSurveyAnswers }}
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
              <div class="ml-4 mr-4" :model="request_error">
                <div class="font-medium">Network request error!</div>
                <div class="text-slate-500 mt-1" >
                  <!-- {{ request_error }}
                  error_name: {{ request_error['error_name'] }}
                  error_msg: {{ request_error.error_msg }}
                  error_status: {{ request_error.error_status }} -->
                  Please check your input!
                </div>
              </div>
            </div>
            <!-- END: Request Error Content -->

            <!-- BEGIN: Data Error Content -->
            <div
              id="data-error-content"
              class="toastify-content hidden flex"
            >
              <CheckCircleIcon class="text-danger" />
              <div class="ml-4 mr-4">
                <div class="font-medium">Survey Template ID is wrong</div>
                <div class="text-slate-500 mt-1" >
                  <!-- {{ request_error }}
                  error_name: {{ request_error['error_name'] }}
                  error_msg: {{ request_error.error_msg }}
                  error_status: {{ request_error.error_status }} -->
                  Please check your input!
                </div>
              </div>
            </div>
            <!-- END: Data Error Content -->

          </Preview>
        </div>
      </PreviewComponent>
      <!-- END: Form Validation -->
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
import { process_FormData } from "./index"
import { process_axios_response, process_axios_error, get_api_url } from "@/utils/axios_utils"

const router = useRouter();
let allSurveyAnswers = reactive([]);
let request_error = reactive({})
request_error.adasdsa = 'asdfasdf'

let FormData = reactive({
  survey_template_id: "",
});
const rules = {
  survey_template_id: {
    required,
    minLength: minLength(1),
  },
};
const FormDataValidate = reactive(useVuelidate(rules, toRefs(FormData)));

const send_to_server = async () => {
  // static categorical: 62e220016648301fab9ab211
  // static categorical_multiple: 62e2e89b6be732eba69f0b6a
  // static continuous: 62e220226648301fab9ab213
  // static categorical + continuous: 62e2204c6648301fab9ab215
  // uniform categorical: 62e220af6648301fab9ab217
  // uniform continuous: 62e220d76648301fab9ab219
  // uniform categorical + continuous: 62e2210d6648301fab9ab21b

  // send voter submit answer data to
  // corresponding back-end api
  let processed_FormData = process_FormData(
    FormDataValidate
  )
  try{
    let res = await axios.post(get_api_url('get_voter_answers_of_template'), processed_FormData)
    res = process_axios_response(res)
    console.log('voter_submit_answers_rrrese', res)

    if (res === null || res.length === 0){
      Toastify({
        node: dom("#data-error-content")
          .clone()
          .removeClass("hidden")[0],
        duration: 10000,
        newWindow: true,
        close: true,
        gravity: "top",
        position: "right",
        stopOnFocus: true,
      }).showToast();
    } else {
      allSurveyAnswers.push(...res)
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
</script>
