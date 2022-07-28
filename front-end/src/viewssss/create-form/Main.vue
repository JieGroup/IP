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
            <br />
            <br />
            <IpFixForm :fix_form_data="fix_form_data"/>
            <IpDynamicForm  v-for="(item, index) in dynamic_form_array"
                            :key="item.unique_id" 
                            :dynamic_form_index="index"
                            :dynamic_form_data="item"
                            @parent_add_dynamic_form="add_dynamic_form" 
                            @parent_delete_dynamic_form="delete_dynamic_form"/>
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
          </Preview>
          <Source>
            <Highlight type="javascript">
              {{
                `
                    const formData = reactive({
                      name: "",
                      email: "",
                      password: "",
                      age: "",
                      url: "",
                      comment: ""
                    });
                    const rules = {
                      name: {
                        required,
                        minLength: minLength(2)
                      },
                      email: {
                        required,
                        email
                      },
                      password: {
                        required,
                        minLength: minLength(6)
                      },
                      age: {
                        required,
                        integer,
                        maxLength: maxLength(3)
                      },
                      url: {
                        url
                      },
                      comment: {
                        required,
                        minLength: minLength(10)
                      }
                    };
                    const validate = useVuelidate(rules, toRefs(formData));
                    const save = () => {
                      validate.value.$touch();
                      if (validate.value.$invalid) {
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
                      } else {
                        Toastify({
                          node: dom("#success-notification-content")
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
                    };
                  `
              }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Form Validation -->
    </div>
    <button @click="test">TEST</button>
    <button @click="test">TEST2 no async</button>
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
import dom from "@left4code/tw-starter/dist/js/dom";
import IpFixForm from "@/components/ip-fix-form/Main.vue";
import IpDynamicForm from "@/components/ip-dynamic-form/Main.vue";
import { axios } from "@/utils/axios";
import { linkTo, process_template_data } from "./index"
import { process_axios_response, process_axios_error, get_api_url } from "@/utils/axios_utils"

let request_error = reactive({})
request_error.adasdsa = 'asdfasdf'

const test = async () => {
  console.log('!!!!')
  try{
    let res = await axios.get('/api/testing_get_exception')
    console.log('$$$$', res)
  } catch (err) {
    let processed_err = process_axios_error(err)
    // console.log('asdasd', aa)
    // console.log('!@#!@#errrrr', err)
    // console.log(err.error_name)
    // let request_error = ref({'adasdsa': '12312'})
    request_error.error_name = processed_err.error_name
    request_error.error_msg = processed_err.error_msg
    request_error.error_status = processed_err.error_status

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
  console.log('??????')
}

const test2 = () => {
  console.log('!!!!')
  axios.get('/api/testing_get')
    .then((response) => {
      console.log('!!!!!!')
      console.log('$$zhende response', response);
    })
    .catch((error) => {
      console.log('&&&&&&')
      console.log('$$zhende response', error);
    });
  console.log('??????')
}

let fix_form_data = reactive({})
let unique_id = 0
let dynamic_form_array = reactive([{unique_id: unique_id}])

const add_dynamic_form = () => {
  console.log('jiajiajia')
  unique_id += 1
  dynamic_form_array.push({unique_id: unique_id})
  console.log('dynamic_form_array', dynamic_form_array, unique_id)
}

const delete_dynamic_form = (dynamic_form_index) => {
  console.log('shemeqingkuang-000', dynamic_form_array)
  console.log('wudi,duide', dynamic_form_index)
  
  if (dynamic_form_index !== 0){
    // array.splice(index, howmany)
    dynamic_form_array.splice(dynamic_form_index, 1)
  }
  console.log('shemeqingkuang', dynamic_form_array)
}

const is_fix_form_validate = (data_valid) => {
  // fix_form_data.validate is the value of 
  // the vuelidate we used
  const validate = fix_form_data.validate
  validate.$touch();
  console.log('fixxxxx', validate.$invalid, data_valid, validate)
  if (validate.$invalid === true) {
    data_valid = false
  }
  // data_invalid = validate.$invalid
  return data_valid
};

const is_dynamic_form_validate = (data_valid) => {
  console.log('dynamic_form_arrayaa', dynamic_form_array);
  dynamic_form_array.forEach((item, index) => {
    console.log('dynamic_form_arrayaabb', item, index);
    console.log('sdfasdf', item['validate'])
    console.log('sdfasdfsdfsa', item.validate)
    // item is the value of the vuelidate we used
    const validate = item.validate
    validate.$touch();
    console.log('dynamic!!!!!!', validate.$invalid, data_valid)
    if (validate.$invalid === true) {
      data_valid = false
    }
    // data_invalid = validate.$invalid
  });
  
  return data_valid
};

const notification = (data_valid) => {
  if (data_valid) {
    Toastify({
      node: dom("#success-notification-content")
        .clone()
        .removeClass("hidden")[0],
      duration: 3000,
      newWindow: true,
      close: true,
      gravity: "top",
      position: "right",
      stopOnFocus: true,
    }).showToast();
  } else {
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
  console.log('total@@@@@@', fix_data_valid, dynamic_data_valid)
  return fix_data_valid && dynamic_data_valid
}


const send_form = async (templateData) => {
  try {
    let response = await axios.post(get_api_url('create_survey_template'), templateData);
    console.log('response', response)
    console.log('asda', response.data)
    let processed_response = process_axios_response(response);
    console.log(`send_form response: ${processed_response}`)
    // Go to response page
    // linkTo()
  } catch (err) {
    console.log(`send_form err 0.5: ${err}`)
    let processed_err = process_axios_error(err)
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
}

const send_to_server = () => {
  let validation = is_form_valid()
  notification(validation)
  console.log('fix_form_data', fix_form_data)
  console.log('dynamic_form_array', dynamic_form_array)
  if (validation === true) {
    let templateData = process_template_data(
      fix_form_data,
      dynamic_form_array
    )
    console.log('templateData', templateData)
    send_form(templateData)
  }
}
</script>
