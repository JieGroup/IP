<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Survey Template</h2>
  </div>
  <div class="grid grid-cols-12 gap-6 mt-5">
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- BEGIN: Form Validation -->
      <!-- <PreviewComponent class="intro-y box" v-slot="{ toggle }"> -->
      <PreviewComponent class="intro-y box">

        <div class="p-5">
          <Preview>
            <!-- BEGIN: Validation Form -->
            <!-- <button @click="send_to_server" type="button" class="btn btn-primary mt-3">
            Send
            </button> -->
            <br />
            <br />
            <TemplateIpFixForm :surveyTemplateFixData="surveyTemplateData"/>
            <!-- surveyTemplateData.survey_topics {{ surveyTemplateData.survey_topics }} -->
            <TemplateIpDynamicForm  v-for="(value, key, index) in surveyTemplateData.survey_topics"
                                    :key="index"
                                    :surveyTemplateDynamicDataKey="key" 
                                    :surveyTemplateDynamicDataValue="value"/>
            <!-- dynamic_form_array -->
            <!-- {{ dynamic_form_array }} -->
            <!-- <IpDynamicForm @add_dynamic_form="add_dynamic_form" 
                           @delete_dynamic_form="delete_dynamic_form"/> -->
            <!-- END: Validation Form -->

            <!-- BEGIN: Success Notification Content -->
            <div
              id="success-notification-content"
              class="toastify-content hidden flex"
            >
              <CheckCircleIcon class="text-success" />
              <div class="ml-4 mr-4">
                <div class="font-medium">Create form success!</div>
                <div class="text-slate-500 mt-1">
                  Please check your history for further info!
                </div>
              </div>
            </div>
            <!-- END: Success Notification Content -->
            <!-- BEGIN: Failed Notification Content -->
            <div
              id="failed-notification-content"
              class="toastify-content hidden flex"
            >
              <XCircleIcon class="text-danger" />
              <div class="ml-4 mr-4">
                <div class="font-medium">Create form failed!</div>
                <div class="text-slate-500 mt-1">
                  Please check the fileld form.
                </div>
              </div>
            </div>
            <!-- END: Failed Notification Content -->

            <!-- BEGIN: Failed Notification Content -->
            <div
              id="duplicate-topic-name"
              class="toastify-content hidden flex"
            >
              <XCircleIcon class="text-danger" />
              <div class="ml-4 mr-4">
                <div class="font-medium">Create form failed!</div>
                <div class="text-slate-500 mt-1">
                  Duplicate topic of this question
                </div>
              </div>
            </div>
            <!-- END: Failed Notification Content -->

            <!-- BEGIN: Request Error Content -->
            <div
              id="request-error-content"
              class="toastify-content hidden flex"
            >
              <CheckCircleIcon class="text-danger" />
              <div class="ml-4 mr-4">
                <div class="font-medium">Network request error!</div>
                <div class="text-slate-500 mt-1" >
                  <!-- {{ requestError }}
                  error_name: {{ requestError['error_name'] }}
                  error_msg: {{ requestError.error_msg }}
                  error_status: {{ requestError.error_status }} -->
                  Please check your input!
                </div>
              </div>
            </div>
            <!-- END: Request Error Content -->
          </Preview>
        </div>
      </PreviewComponent>
      <!-- END: Form Validation -->
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { reactive, toRefs, onBeforeMount } from "vue";
import {
  required,
  minLength,
  maxLength,
  email,
  url,
  integer,
} from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import Toastify from "toastify-js";
import { useRoute, useRouter } from "vue-router";
import dom from "@left4code/tw-starter/dist/js/dom";
import TemplateIpFixForm from "@/components/template-fix-form/Main.vue";
import TemplateIpDynamicForm from "@/components/template-dynamic-form/Main.vue";
import { axios } from "@/utils/axios";
import { linkTo, process_template_data, is_data_valid } from "./index"
import { process_axios_response, process_axios_error, get_api_url } from "@/utils/axios_utils"


/*
This page gets the survey template data from
back-end, then calls TemplateIpFixForm and
TemplateIpDynamicForm to show the data
in form format
*/

const router = useRouter();

let fix_form_data = reactive({})
let unique_id = 0
let dynamic_form_array = reactive([{unique_id: unique_id}])

let surveyTemplateData = reactive({
  // survey_template_name: "",
  // survey_template_id: '',
  // survey_update_method: '',
  // creation_time: '',
  // expiration_time: '',
  // time_period: '',
  // number_of_copies: '',
  // max_rounds: "",
  // survey_topics: ""
})


const get_survey_template = async (surveyTemplateIDData) => {
  try {
    let response = await axios.post(get_api_url('get_survey_template'), surveyTemplateIDData);
    // console.log('response', response)
    // console.log('asda', response.data)
    let processed_response = process_axios_response(response);
    let survey_template_document = processed_response.survey_template_document
    // console.log(`get_survey_template: ${processed_response}`)

    // let Data = {
    //   survey_template_name: 'survey_template_name',
    //   survey_template_id: 'survey_template_id',
    //   survey_update_method: 'survey_update_method',
    //   creation_time: 'creation_time',
    //   expiration_time: 'expiration_time',
    //   time_period: 'time_period',
    //   number_of_copies: 400,
    //   max_rounds: 3,
    //   survey_topics: {
    //     topic_name_1: {
    //       answer_type: 'categorical',
    //       categorical_range: {
    //           inclusion: ['a', 'b', 'c']
    //       },
    //       topic_question: 'topic_q',
    //       unit: 'km'
    //     },
    //     topic_name_2: {
    //       answer_type: 'continuous',
    //       continuous_range: {
    //         'min': 1,
    //         'max': 4    
    //       },
    //       topic_question: 'topic_q2',
    //       unit: 'kg'       
    //     }
    //   }
    // }
    // surveyTemplateData = Data
    // surveyTemplateData = toRefs(surveyTemplateData)
    for (let key in survey_template_document) {
      surveyTemplateData[key] = survey_template_document[key]
    }
    // surveyTemplateData = {...Data}
    console.log('template-form', surveyTemplateData)
    // Toastify({
    //   node: dom("#success-notification-content")
    //     .clone()
    //     .removeClass("hidden")[0],
    //   duration: 10000,
    //   newWindow: true,
    //   close: true,
    //   gravity: "top",
    //   position: "center",
    //   stopOnFocus: true,
    // }).showToast();
  } catch (err) {
    console.log(`send_form err 0.5: ${err}`)
    let processed_err = process_axios_error(err)
    // requestError.error = processed_err
    console.log(`send_form err: ${processed_err}`)

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
onBeforeMount(() => {
  let params = router.currentRoute.value.params
  console.log('12123', params)
  let surveyTemplateID = params.surveyTemplateID
  
  let surveyTemplateIDData = {
    'survey_template_id': surveyTemplateID
  }
  get_survey_template(surveyTemplateIDData)
  
  

})

</script>
