<template>
    <div>
        <!-- BEGIN: Validation Form -->
        <form class="validate-form">
            surveyTemplateFixData: {{ surveyTemplateFixData }}

            ceshi max rounds {{ surveyTemplateFixData.max_rounds }}

            <div class="input-form mt-3">
            <label
                for="validation-form-2"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Survey update method
            </label>
            <input
                id="validation-form-2"
                v-model.trim="surveyTemplateFixData.survey_update_method"
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
                Number of copies
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
                Expiration time
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
import { reactive, toRefs, onBeforeMount } from "vue";
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

// receive variable from parent
const props = defineProps({
  surveyTemplateFixData: {
    default: null,
  },
});

console.log('template-fix-form', props.surveyTemplateFixData)
// let surveyTemplateFixData = reactive({})

// onBeforeMount(() => {
//     for (let key in props.surveyTemplateFixData) {
//         surveyTemplateFixData[key] = props.surveyTemplateFixData[key]
//     }
//     console.log('template-fix-form-2', surveyTemplateFixData)
// })
// surveyTemplateFixData = {...props.surveyTemplateFixData}
// const emit = defineEmits([])

// const formData = reactive({
//   survey_update_method: "static",
//   max_rounds: 1,
//   number_of_copies: "",
//   time_period: "3"
// });

// const rules = {
//   survey_update_method: {
//     required
//   },
//   max_rounds: {
//     required: requiredIf(() => formData.survey_update_method === 'uniform'),
//     integer,
//     maxValue: maxValue(5),
//     minValue: minValue(1)
//   },
//   number_of_copies: {
//     required,
//     integer,
//     maxValue: maxValue(500),
//     minValue: minValue(0)
//   },
//   time_period: {
//     required,
//   },
// };

// const validate = useVuelidate(rules, toRefs(formData));
// props.fix_form_data.validate = validate;
</script>