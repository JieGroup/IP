<template>
    <div>
        <!-- BEGIN: Validation Form -->
        <form class="validate-form">

            <div class="input-form mt-3">
            <label
                for="validation-form-0"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Title
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, at least 1 character</span
                >
            </label>
            <input
                id="validation-form-0"
                v-model.trim="validate.survey_template_name.$model"
                type="text"
                name="survey_template_name"
                class="form-control"
                :class="{ 'border-danger': validate.survey_template_name.$error }"
                placeholder="Survey title shown to the respondents, e.g., 'Salary Survey'"
            />
            <template v-if="validate.survey_template_name.$error">
                <div
                v-for="(error, index) in validate.survey_template_name.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template>
            </div>

            <div class="mt-3">
            <label>Mode</label>
            <div class="mt-2">
                <TomSelect v-model="validate.survey_update_method.$model" :options="{
                            placeholder: 'Select the mode of generating questions',
                            }" class="w-full">
                <optgroup label="mode">
                    <option value="static">Non-private</option>
                    <option value="uniform">Private</option>
                </optgroup>
                </TomSelect>
            </div>
            </div>

            <div v-if="validate.survey_update_method.$model === 'uniform'" class="input-form mt-3">
            <label
                for="validation-form-2"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Max rounds
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, integer only & maximum 3 rounds</span
                >
            </label>
            <input
                id="validation-form-2"
                v-model.trim="validate.max_rounds.$model"
                type="number"
                name="max_rounds"
                class="form-control"
                :class="{ 'border-danger': validate.max_rounds.$error }"
                placeholder="How many times a question may be repeated, e.g., 3"
            />
            <template v-if="validate.max_rounds.$error">
                <div
                v-for="(error, index) in validate.max_rounds.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template>
            </div>

            <div class="input-form mt-3">
            <label
                for="validation-form-3"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Number of respondents
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, integer only & maximum 500</span
                >
            </label>
            <input
                id="validation-form-3"
                v-model.trim="validate.number_of_copies.$model"
                type="number"
                name="number_of_copies"
                class="form-control"
                :class="{ 'border-danger': validate.number_of_copies.$error }"
                placeholder="The maximum number of respondents, e.g., 300"
            />
            <template v-if="validate.number_of_copies.$error">
                <div
                v-for="(error, index) in validate.number_of_copies.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template>
            </div>

            <div class="mt-3">
            <label>Expiration</label>
            <div class="mt-2">
                <TomSelect v-model="validate.time_period.$model" :options="{
                            placeholder: 'How long will this survey be open to respondents',
                            }" class="w-full">
                <optgroup label="Expiration">
                    <option value='3'>3 days</option>
                    <option value='7'>7 days</option>
                    <option value='15'>15 days</option>
                    <option value='30'>30 days</option>
                    <option value='60'>60 days</option>
                </optgroup>
                </TomSelect>
            </div>
            </div>
            <br />
            Please create question(s) below. 
        </form>
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-400/60 dark:border-darkmode-800"
        >
        </div>
        <!-- END: Validation Form -->
    </div>
</template>


<script setup>
import { reactive, toRefs } from "vue";
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
  fix_form_data: {
    default: null,
  },
});

const emit = defineEmits([])

const formData = reactive({
  survey_template_name: "",
  survey_update_method: "uniform",
  max_rounds: 1,
  number_of_copies: "",
  time_period: "3"
});

const rules = {
  survey_template_name: {
    required
  },  
  survey_update_method: {
    required
  },
  max_rounds: {
    required: requiredIf(() => formData.survey_update_method === 'uniform'),
    integer,
    maxValue: maxValue(3),
    minValue: minValue(1)
  },
  number_of_copies: {
    required,
    integer,
    maxValue: maxValue(500),
    minValue: minValue(0)
  },
  time_period: {
    required,
  },
};

const validate = useVuelidate(rules, toRefs(formData));
props.fix_form_data.validate = validate;
</script>