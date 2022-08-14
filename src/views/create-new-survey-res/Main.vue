<template>
  <div class="p-5">
    <!-- <Preview> -->
      <AccordionGroup class="accordion-boxed">
        <AccordionItem>
            <Accordion>
              Please use the following link to deliver the survey:
            </Accordion>
            <AccordionPanel class="text-slate-600 dark:text-slate-500 leading-relaxed">
                https://grand-liger-cad265.netlify.app/answer-survey/?surveyTemplateID={{ surveyTemplateID }}
            </AccordionPanel>
        </AccordionItem>
        <AccordionItem>
            <Accordion>
              Your Survey Template ID: {{ surveyTemplateID }}
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
    <!-- </Preview> -->
  </div>
  
</template>

<script setup>
import { ref } from "vue";
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
import {useRouter} from 'vue-router'
// receive variable from parent
// const props = defineProps({
//   test: {
//     default: null,
//   },
// });
const router = useRouter()
let params = router.currentRoute.value.params

let surveyTemplateID = ref('')
surveyTemplateID.value = params.surveyTemplateID
console.log('testsss', params)
</script>
