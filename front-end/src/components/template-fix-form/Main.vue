<template>
    <div>
        <!-- BEGIN: Validation Form -->
        <form class="validate-form">
            surveyTemplateFixData: {{ surveyTemplateFixData }}
            <!-- <div class="input-form">
            <label
                for="validation-form-1"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Survey Update Method
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, at least 2 characters</span
                >
            </label>
            <input
                id="validation-form-1"
                v-model.trim="validate.name.$model"
                type="text"
                name="name"
                class="form-control"
                :class="{ 'border-danger': validate.name.$error }"
                placeholder="John Legend"
            />
            <template v-if="validate.name.$error">
                <div
                v-for="(error, index) in validate.name.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template>
            </div> -->
            max rounds {{ surveyTemplateFixData.max_rounds }}
            <div class="input-form mt-3">
            <label
                for="validation-form-2"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Max rounds
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, integer only & maximum 5 rounds</span
                >
            </label>
            <input
                id="validation-form-2"
                v-model.trim="surveyTemplateFixData.max_rounds"
                type="number"
                name="max_rounds"
                class="form-control"
            />
            <!-- <template v-if="validate.max_rounds.$error">
                <div
                v-for="(error, index) in validate.max_rounds.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template> -->
            </div>

            <div v-if="surveyTemplateFixData.survey_update_method === 'uniform'" class="input-form mt-3">
            <label
                for="validation-form-2"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Max rounds
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, integer only & maximum 5 rounds</span
                >
            </label>
            <input
                id="validation-form-2"
                v-model.trim="surveyTemplateFixData.max_rounds"
                type="number"
                name="max_rounds"
                class="form-control"
                placeholder="The number of times the voter can answer the topic. E.g.1"
            />
            <!-- <template v-if="validate.max_rounds.$error">
                <div
                v-for="(error, index) in validate.max_rounds.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template> -->
            </div>

            <div class="input-form mt-3">
            <label
                for="validation-form-3"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Number of copies
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, integer only & maximum 500 copies</span
                >
            </label>
            <input
                id="validation-form-3"
                v-model.trim="surveyTemplateFixData.number_of_copies"
                type="number"
                name="number_of_copies"
                class="form-control"
                placeholder="The maximum number of surveys issued. E.g. 200"
            />
            <!-- <template v-if="validate.number_of_copies.$error">
                <div
                v-for="(error, index) in validate.number_of_copies.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template> -->
            </div>

            <div class="input-form mt-3">
            <label
                for="validation-form-3"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Number of copies
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, integer only & maximum 500 copies</span
                >
            </label>
            <input
                id="validation-form-3"
                v-model.trim="surveyTemplateFixData.time_period"
                type="number"
                name="time_period"
                class="form-control"
                placeholder="survey expiration time"
            />
            <!-- <template v-if="validate.number_of_copies.$error">
                <div
                v-for="(error, index) in validate.number_of_copies.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template> -->
            </div>

            <!-- <div class="mt-3">
            <label>Expiration time</label>
            <div class="mt-2">
                <TomSelect v-model="validate.time_period.$model" :options="{
                            placeholder: 'Select survey expiration time',
                            }" class="w-full">
                <optgroup label="Expiration Time">
                    <option value='3'>3 days</option>
                    <option value='7'>7 days</option>
                    <option value='15'>15 days</option>
                    <option value='30'>30 days</option>
                    <option value='60'>60 days</option>
                </optgroup>
                </TomSelect>
            </div>
            </div> -->

            <!-- <div class="input-form mt-3">
            <label
                for="validation-form-4"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Expiration Time
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, at least 6 characters</span
                >
            </label>
            <input
                id="validation-form-4"
                v-model.trim="validate.password.$model"
                type="password"
                name="password" 
                class="form-control"
                :class="{ 'border-danger': validate.password.$error }"
                placeholder="secretc"
            />
            <template v-if="validate.password.$error">
                <div
                v-for="(error, index) in validate.password.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template>
            </div> -->

            <!-- <div class="input-form mt-3">
            <label
                for="validation-form-5"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Profile URL
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Optional, URL format</span
                >
            </label>
            <input
                id="validation-form-5"
                v-model.trim="validate.url.$model"
                type="url"
                name="url"
                class="form-control"
                :class="{ 'border-danger': validate.url.$error }"
                placeholder="https://google.com"
            />
            <template v-if="validate.url.$error">
                <div
                v-for="(error, index) in validate.url.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template>
            </div> -->

            <!-- <div class="input-form mt-3">
            <label
                for="validation-form-6"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Comment
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, at least 10 characters</span
                >
            </label>
            <textarea
                id="validation-form-6"
                v-model.trim="validate.comment.$model"
                class="form-control"
                :class="{ 'border-danger': validate.comment.$error }"
                name="comment"
                placeholder="Type your comments"
            ></textarea>
            <template v-if="validate.comment.$error">
                <div
                v-for="(error, index) in validate.comment.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template>
            </div> -->

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
let surveyTemplateFixData = reactive({})

onBeforeMount(() => {
    for (let key in props.surveyTemplateFixData) {
        surveyTemplateFixData[key] = props.surveyTemplateFixData[key]
    }
    console.log('template-fix-form-2', surveyTemplateFixData)
})
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