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
                            :key="index" 
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
                <div class="font-medium">Registration success!</div>
                <div class="text-slate-500 mt-1">
                  Please check your e-mail for further info!
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
                <div class="font-medium">Registration failed!</div>
                <div class="text-slate-500 mt-1">
                  Please check the fileld form.
                </div>
              </div>
            </div>
            <!-- END: Failed Notification Content -->
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

let fix_form_data = reactive({})
let dynamic_form_array = reactive([{}])

const add_dynamic_form = () => {
  console.log('jiajiajia')
  dynamic_form_array.push({})
  console.log('dynamic_form_array', dynamic_form_array)
}

const delete_dynamic_form = (dynamic_form_index) => {
  console.log('wudi,duide')
  if (dynamic_form_index !== 0){
    // array.splice(index, howmany)
    dynamic_form_array.splice(dynamic_form_index, 1)
  }
}

const is_fix_form_validate = (data_invalid) => {
  // fix_form_data.validate is the value of 
  // the vuelidate we used
  const validate = fix_form_data.validate
  validate.$touch();
  if (validate.$invalid === false) {
    data_invalid = false
  }
  return data_invalid
};

const is_dynamic_form_validate = (data_invalid) => {
  console.log('dynamic_form_arrayaa', dynamic_form_array);
  dynamic_form_array.forEach((item, index) => {
    console.log('dynamic_form_arrayaabb', item, index);
    console.log('sdfasdf', item['validate'])
    console.log('sdfasdfsdfsa', item.validate)
    // item is the value of the vuelidate we used
    const validate = item.validate
    validate.$touch();
    if (validate.$invalid === false) {
      data_invalid = false
    }
  });
  return data_invalid
};

const notification = (data_invalid) => {
  if (data_invalid) {
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
}

const send_to_server = () => {
  let fix_data_invalid = ref(true)
  let dynamic_data_invalid = ref(true)
  fix_data_invalid = is_fix_form_validate(fix_data_invalid)
  dynamic_data_invalid = is_dynamic_form_validate(dynamic_data_invalid)
  notification(dynamic_data_invalid || fix_data_invalid)
}
</script>
