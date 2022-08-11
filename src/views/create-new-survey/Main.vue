<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Create New Survey</h2>
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
            <!-- <button @click="send_to_server" type="button" class="btn btn-primary mt-3">
            Create
            </button> -->
            <!-- <br />
            <br /> -->
            <IpFixForm :fix_form_data="fix_form_data"/>
            <IpDynamicForm  v-for="(item, index) in dynamic_form_array"
                            :key="item.unique_id" 
                            :dynamic_form_index="index"
                            :dynamic_form_data="item"
                            @parent_add_dynamic_form="add_dynamic_form" 
                            @parent_delete_dynamic_form="delete_dynamic_form"
                            @parent_duplicate_dynamic_form="duplicate_dynamic_form"/>
            <!-- dynamic_form_array -->
            <!-- {{ dynamic_form_array }} -->
            <!-- <IpDynamicForm @add_dynamic_form="add_dynamic_form" 
                           @delete_dynamic_form="delete_dynamic_form"/> -->
            <!-- END: Validation Form -->

            <!-- BEGIN: Success Notification Content -->
            <button @click="send_to_server" type="button" class="btn btn-primary mt-3">
            Create
            </button>
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
                <div class="font-medium">Network request error!: {{ requestError.error }}</div>
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
import { reactive, toRefs } from "vue";
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
import IpFixForm from "@/components/ip-fix-form/Main.vue";
import IpDynamicForm from "@/components/ip-dynamic-form/Main.vue";
import { axios } from "@/utils/axios";
import { linkTo, process_template_data, is_data_valid } from "./index"
import { process_axios_response, process_axios_error, get_api_url } from "@/utils/axios_utils"
import _ from "lodash";

const router = useRouter();

let requestError = reactive({
  error: ''
})
let formError = reactive({
  error: ''
})

let fix_form_data = reactive({})
let unique_id = 0
let dynamic_form_array = reactive([{unique_id: unique_id}])

const add_dynamic_form = () => {
  unique_id += 1
  dynamic_form_array.push({unique_id: unique_id})
  console.log(`add_dynamic_form - dynamic_form_array, ${dynamic_form_array}`)
}

const delete_dynamic_form = (dynamic_form_index) => {  
  if (dynamic_form_index !== 0){
    // array.splice(index, howmany)
    dynamic_form_array.splice(dynamic_form_index, 1)
  }
  console.log(`delete_dynamic_form - dynamic_form_array, ${dynamic_form_array}`)
}

const duplicate_dynamic_form = (dynamic_form_index) => {
  // let duplicate_ele = JSON.parse(JSON.stringify(dynamic_form_array[dynamic_form_index]));
  let duplicate_ele = _.cloneDeep(dynamic_form_array[dynamic_form_index])
  unique_id += 1
  duplicate_ele.unique_id = unique_id
  console.log('duplicate_ele', duplicate_ele, dynamic_form_array[dynamic_form_index])
  console.log('whole', dynamic_form_array)
  // 索引位置，要删除元素的数量，元素
  dynamic_form_array.splice(dynamic_form_index+1, 0, duplicate_ele)
  console.log('after_duplicate_ele', dynamic_form_array)
}

const is_fix_form_validate = (data_valid) => {
  // fix_form_data.validate is the value of 
  // the vuelidate we used
  const validate = fix_form_data.validate
  console.log('butonton', validate)
  validate.$touch();
  if (validate.$invalid === true) {
    data_valid = false
  }
  console.log(`is_fix_form_validate ${data_valid}`)
  return data_valid
};

const is_dynamic_form_validate = (data_valid) => {
  dynamic_form_array.forEach((item, index) => {
    // item is the value of the vuelidate we used
    const validate = item.validate
    validate.$touch();
    if (validate.$invalid === true) {
      data_valid = false
    }
    // data_invalid = validate.$invalid
  });
  console.log(`is_dynamic_form_validate ${data_valid}`)
  return data_valid
};

const notification = (data_valid) => {
  if (data_valid) {
    // pass
  } else {
    formError.error = 'Form error'
    Toastify({
      node: dom("#failed-notification-content")
        .clone()
        .removeClass("hidden")[0],
      duration: 3000,
      newWindow: true,
      close: true,
      gravity: "top",
      position: "right",
      stopOnFocus: true,
    }).showToast();
  }
}

const is_form_valid = () => {
  let fix_data_valid = true
  let dynamic_data_valid = true
  fix_data_valid = is_fix_form_validate(fix_data_valid)
  dynamic_data_valid = is_dynamic_form_validate(dynamic_data_valid)
  return fix_data_valid && dynamic_data_valid
}

const tiaozhuan = () => {
  
  let params = {
    'surveyTemplateID': 'zzzzz'
  }
  linkTo('side-menu-create-new-survey-res', router, params)
}

const send_form = async (templateData) => {
  let surveyTemplateID = ''
  try {
    let response = await axios.post(get_api_url('create_survey_template'), templateData);
    console.log('response', response)
    console.log('asda', response.data)
    let processed_response = process_axios_response(response);
    console.log(`send_form response: ${processed_response}`)
    surveyTemplateID = processed_response.survey_template_id
    Toastify({
      node: dom("#success-notification-content")
        .clone()
        .removeClass("hidden")[0],
      duration: 10000,
      newWindow: true,
      close: true,
      gravity: "top",
      position: "right",
      stopOnFocus: true,
    }).showToast();
  } catch (err) {
    console.log(`send_form err 0.5: ${err}`)
    let processed_err = process_axios_error(err)
    requestError.error = processed_err
    console.log(`send_form err: ${processed_err}`)

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

  // Go to response page
  let params = {
    'surveyTemplateID': surveyTemplateID
  }
  linkTo('side-menu-create-new-survey-res', router, params)
}

const send_to_server = () => {
  let validation = is_form_valid()
  notification(validation)
  console.log('!!fix_form_data', fix_form_data)
  console.log('!!dynamic_form_array', dynamic_form_array)
  if (validation === true) {
    let err_msg = is_data_valid(
      fix_form_data,
      dynamic_form_array
    )
    console.log('err_msg', err_msg)
    if (err_msg !== null) {
      formError.error = err_msg
      console.log('formError', formError)
      Toastify({
        node: dom("#failed-notification-content")
          .clone()
          .removeClass("hidden")[0],
        duration: 6000,
        newWindow: true,
        close: true,
        gravity: "top",
        position: "right",
        stopOnFocus: true,
      }).showToast();
      return null
    }
    console.log('zenmezaizhe')
    let templateData = process_template_data(
      fix_form_data,
      dynamic_form_array
    )
    console.log('!!templateData', templateData)
    send_form(templateData)
  }
}
</script>
