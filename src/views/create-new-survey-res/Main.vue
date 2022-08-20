<template>
  <div class="p-5">
    <!-- <Preview> -->
      <AccordionGroup class="accordion-boxed">
        <AccordionItem>
            <Accordion>
              Please use the following link to deliver the survey:
            </Accordion>
            <AccordionPanel class="text-slate-600 dark:text-slate-500 leading-relaxed">
              {{ get_survey_share_link(surveyTemplateID) }}
              <br />
              <!-- <div @click="copy_survey_link(surveyTemplateID)" class="flex items-center">
                <Share2Icon  class="w-5 h-5"/>
                <u>Copy Link</u>
              </div> -->
              <button type='button' @click="copy_survey_link(surveyTemplateID)" class="btn btn-primary-soft mt-5">
                <Share2Icon class="w-5 h-5" />
                <u>Copy Link</u>
              </button>
            </AccordionPanel>
        </AccordionItem>
        <AccordionItem>
            <Accordion>
              Your Survey ID: {{ surveyTemplateID }}
            </Accordion>
            <AccordionPanel class="text-slate-600 dark:text-slate-500 leading-relaxed">
                {{ surveyTemplateID }}
            </AccordionPanel>
        </AccordionItem>
        
        <!-- <AccordionItem>
            <Accordion>
                Understanding IP Addresses, Subnets, and CIDR Notation
            </Accordion>
            <AccordionPanel class="text-slate-600 dark:text-slate-500 leading-relaxed">
                Lorem Ipsum is simply dummy text of the printing and
                typesetting industry. Lorem Ipsum has been the industry's
                standard dummy text ever since the 1500s, when an unknown
                printer took a galley of type and scrambled it to make a
                type specimen book. It has survived not only five centuries,
                but also the leap into electronic typesetting, remaining
                essentially unchanged.
            </AccordionPanel>
        </AccordionItem>
        <AccordionItem>
            <Accordion>
                How To Troubleshoot Common HTTP Error Codes
            </Accordion>
            <AccordionPanel class="text-slate-600 dark:text-slate-500 leading-relaxed">
                Lorem Ipsum is simply dummy text of the printing and
                typesetting industry. Lorem Ipsum has been the industry's
                standard dummy text ever since the 1500s, when an unknown
                printer took a galley of type and scrambled it to make a
                type specimen book. It has survived not only five centuries,
                but also the leap into electronic typesetting, remaining
                essentially unchanged.
            </AccordionPanel>
        </AccordionItem>
        <AccordionItem>
            <Accordion>
                An Introduction to Securing your Linux VPS
            </Accordion>
            <AccordionPanel class="text-slate-600 dark:text-slate-500 leading-relaxed">
                Lorem Ipsum is simply dummy text of the printing and
                typesetting industry. Lorem Ipsum has been the industry's
                standard dummy text ever since the 1500s, when an unknown
                printer took a galley of type and scrambled it to make a
                type specimen book. It has survived not only five centuries,
                but also the leap into electronic typesetting, remaining
                essentially unchanged.
            </AccordionPanel>
        </AccordionItem> -->
      </AccordionGroup>
      <!-- BEGIN: Copy Success Content -->
      <div
          id="success-notification-content"
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
      <!-- END: Copy Success Content -->
      <!-- BEGIN: Copy Error Content -->
      <div
          id="request-error-content"
          class="toastify-content hidden flex"
      >
          <CheckCircleIcon class="text-danger" />
          <div class="ml-4 mr-4">
          <div class="font-medium">Copy error!</div>
          <div class="text-slate-500 mt-1">
              <!-- {{ request_error }}
              error_name: {{ request_error['error_name'] }}
              error_msg: {{ request_error.error_msg }}
              error_status: {{ request_error.error_status }} -->
              <!-- <div> -->
              Please copy the survey link again
              <!-- </div> -->
          </div>
          </div>
      </div>
      <!-- END: Copy Error Content -->
    <!-- </Preview> -->
  </div>
  
</template>

<script setup>
import { ref } from "vue";
import useClipboard from "vue-clipboard3";
import Toastify from "toastify-js";
// import { reactive, toRefs } from "vue";
// import {
//   required,
//   minLength,
//   maxLength,
//   email,
//   url,
//   integer,
// } from "@vuelidate/validators";
// import { useVuelidate } from "@vuelidate/core";
// import Toastify from "toastify-js";
// import dom from "@left4code/tw-starter/dist/js/dom";
// import IpFixForm from "@/components/ip-fix-form/Main.vue";
// import IpDynamicForm from "@/components/ip-dynamic-form/Main.vue";
// import { axios } from "@/utils/axios";
// import { linkTo, process_template_data, is_data_valid } from "./index"
// import { process_axios_response, process_axios_error, get_api_url } from "@/utils/axios_utils"
import { useRouter } from 'vue-router'
import { get_survey_share_link } from "@/utils/axios_utils"
// receive variable from parent
// const props = defineProps({
//   test: {
//     default: null,
//   },
// });
const router = useRouter();

let params = router.currentRoute.value.params

let surveyTemplateID = ref('')
surveyTemplateID.value = params.surveyTemplateID
console.log('testsss', params)

const { toClipboard } = useClipboard();
const copy_survey_link = async (surveyTemplateID) => {
  let survey_link = get_survey_share_link(surveyTemplateID)
  try {
    await toClipboard(survey_link);  //实现复制
    const dom_ele = dom("#success-notification-content").clone().removeClass("hidden")[0]
    dom_ele.children[1].querySelector(".font-medium").innerHTML = 'Thank you!'
    dom_ele.children[1].querySelector(".text-slate-500.mt-1").innerHTML = `Survey link successfully copied`

    Toastify({
      node: dom_ele,
      duration: 10000,
      newWindow: true,
      close: true,
      gravity: "top",
      position: "center",
      stopOnFocus: true,
    }).showToast();
    console.log(`Success, ${surveyTemplateID}`);

  } catch (e) {
    const dom_ele = dom("#request-error-content").clone().removeClass("hidden")[0]
    dom_ele.children[1].querySelector(".font-medium").innerHTML = 'Sorry'
    dom_ele.children[1].querySelector(".text-slate-500.mt-1").innerHTML = `Please copy one more time`

    Toastify({
      node: dom_ele,
      duration: 10000,
      newWindow: true,
      close: true,
      gravity: "top",
      position: "center",
      stopOnFocus: true,
    }).showToast();
    console.error(e);
  }
}
</script>
