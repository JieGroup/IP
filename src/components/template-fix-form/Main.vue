<template>
    <div>
        <!-- BEGIN: Validation Form -->
        <form class="validate-form">
            <!-- surveyTemplateFixData: {{ surveyTemplateFixData }} -->

            <!-- ceshi max rounds {{ surveyTemplateFixData.max_rounds }} -->

            <div class="input-form mt-3">
            <label
                for="validation-form-0"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Title
            </label>
            <input
                id="validation-form-0"
                v-model.trim="surveyTemplateFixData.survey_template_name"
                type="text"
                name="survey_template_name"
                class="form-control"
                readonly="readonly"
            />
            </div>

            <div class="input-form mt-3">
            <label
                for="validation-form-0-5"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Survey ID
            </label>
            <input
                id="validation-form-0-5"
                v-model.trim="surveyTemplateFixData.survey_template_id"
                type="text"
                name="survey_template_id"
                class="form-control"
                readonly="readonly"
            />
            </div>
            <!-- {{ get_survey_share_link(surveyTemplateFixData.survey_template_id) }} -->
            <div class="input-form mt-3">
            <label
                for="validation-form-0-6"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Survey Link
            </label>
            <input
                id="validation-form-0-6"
                v-model.trim="surveyLink"
                type="text"
                name="survey_link"
                class="form-control"
                readonly="readonly"
            />
            </div>

            <div v-if="surveyTemplateFixData.survey_update_method === 'static'" class="input-form mt-3">
            <label
                for="validation-form-1"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Mode
            </label>
            <input
                id="validation-form-1"
                value="Non-private"
                type="text"
                name="survey_update_method"
                class="form-control"
                readonly="readonly"
            />
            </div>
            <div v-else class="input-form mt-3">
            <label
                for="validation-form-1"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Mode
            </label>
            <input
                id="validation-form-1"
                value="Private"
                type="text"
                name="survey_update_method"
                class="form-control"
                readonly="readonly"
            />
            </div>


            <div class="input-form mt-3">
            <label
                for="validation-form-2"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Max rounds
            </label>
            <input
                id="validation-form-2"
                v-model.trim="surveyTemplateFixData.max_rounds"
                type="number"
                name="max_rounds"
                class="form-control"
                readonly="readonly"
            />
            </div>
            
            <div class="input-form mt-3">
            <label
                for="validation-form-3"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Number of respondents
            </label>
            <input
                id="validation-form-3"
                v-model.trim="surveyTemplateFixData.number_of_copies"
                type="number"
                name="number_of_copies"
                class="form-control"
                readonly="readonly"
            />
            </div>

            <div class="input-form mt-3">
            <label
                for="validation-form-4"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Expiration
            </label>
            <input
                id="validation-form-4"
                v-model.trim="surveyTemplateFixData.time_period"
                type="text"
                name="time_period"
                class="form-control"
                readonly="readonly"
            />
            </div>

        </form>
        <!-- END: Validation Form -->
    </div>
</template>


<script setup>
import { reactive, toRefs, onMounted, ref, toRaw, onBeforeMount } from "vue";

import {
  required,
  minLength,
  maxLength,
  email,
  url,
  integer,
  requiredIf,
  minValue,
  maxValue
} from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import Toastify from "toastify-js";
import dom from "@left4code/tw-starter/dist/js/dom";
import { get_survey_share_link } from "@/utils/axios_utils"

// receive variable from parent
const props = defineProps({
  surveyTemplateFixData: {
    default: null,
  },
  surveyTemplateID: {
    default: ''
  }
});

console.log('%%%%%%%%%%fix form', props.surveyTemplateFixData, props.surveyTemplateID)
const surveyLink = ref(get_survey_share_link(props.surveyTemplateFixData.survey_template_id))
// console.log('jjjjjjjjjjjjjj1')
// const change_survey_update_method_to_user_friendly_text = () => {
//     console.log('Obj', props.surveyTemplateFixData)
//     const rawObject = JSON.parse(JSON.stringify(props.surveyTemplateFixData))
//     console.log('rawObj', rawObject, rawObject[0])
//     console.log('jjjj1.5', props.surveyTemplateFixData, rawObject.survey_update_method)
//     if (props.surveyTemplateFixData.survey_update_method === 'static'){
//         return 'Non-private'
//     }
//     else if (props.surveyTemplateFixData.survey_update_method === 'uniform'){
//         return 'Private'
//     }
// }

// console.log('jjjjjjjjjjjjjj2', change_survey_update_method_to_user_friendly_text())
// const mode = ref(change_survey_update_method_to_user_friendly_text())

// onMounted(() => {
//   console.log('jjjjjjjjjjjjjj3', change_survey_update_method_to_user_friendly_text())
//   const mode = ref(change_survey_update_method_to_user_friendly_text())
// });

// props.surveyTemplateFixData.forEach((item, index) => {
//     console.log('1231231', item, index)
// });

const arr = reactive([])


// const a = 5;
// const ceshi = JSON.parse(JSON.stringify(props.surveyTemplateFixData))

// const ceshi2 = toRaw(props.surveyTemplateFixData)
// console.log('~~~~~~~~~~~~~chuanyige', props.surveyTemplateID)
// console.log('xianzaiceshi', toRaw(props.surveyTemplateFixData), ceshi2.survey_template_id)
// console.log('--------------------template-fix-form', props.surveyTemplateFixData, props.surveyTemplateFixData['survey_template_id'])
// // onBeforeMount
// let surveyLink = ref(get_survey_share_link(props.surveyTemplateFixData.survey_template_id))
// console.log('surveyLink', surveyLink)
// onBeforeMount(() => {
//     let surveyLink = ref(get_survey_share_link(props.surveyTemplateFixData.survey_template_id))
// })


</script>