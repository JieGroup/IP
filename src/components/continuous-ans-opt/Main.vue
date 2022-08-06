<template>
    <div class="input-form">
    <label
        for="validation-form-31"
        class="form-label w-full flex flex-col sm:flex-row"
    >
      Answer minimum
      <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
      >Required, at least 1 number</span
      >
    </label>
    <input
        id="validation-form-31"
        v-model.trim="validate.continuous_answer_min.$model"
        type='number'
        name="continuous_answer_min"
        class="form-control"
        :class="{ 'border-danger': validate.continuous_answer_min.$error }"
        placeholder="Type your minimum range. E.g. 0"
    />
    <template v-if="validate.continuous_answer_min.$error">
        <div
        v-for="(error, index) in validate.continuous_answer_min.$errors"
        :key="index"
        class="text-danger mt-2"
        >
        {{ error.$message }}
        </div>
    </template>
    </div>

    <br />
    <div class="input-form">
    <label
        for="validation-form-32"
        class="form-label w-full flex flex-col sm:flex-row"
    >
        Answer maximum
        <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
        >Required, at least 1 number</span
        >
    </label>
    <input
        id="validation-form-32"
        v-model.trim="validate.continuous_answer_max.$model"
        type='number'
        name="continuous_answer_max"
        class="form-control"
        :class="{ 'border-danger': validate.continuous_answer_max.$error }"
        placeholder="Type your maximum range. E.g. 10000"
    />
    <template v-if="validate.continuous_answer_max.$error">
        <div
        v-for="(error, index) in validate.continuous_answer_max.$errors"
        :key="index"
        class="text-danger mt-2"
        >
        {{ error.$message }}
        </div>
    </template>
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
  requiredIf,
  minValue,
  maxValue,
  helpers
} from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import Toastify from "toastify-js";
import dom from "@left4code/tw-starter/dist/js/dom";

// receive variable from parent
const props = defineProps({
  continuous_answer_option_data: {
    default: null,
  },
});


const emits = defineEmits([])

const error_msg = reactive("")
const form_data = reactive({
  continuous_answer_min: "",
  continuous_answer_max: "",
});


const min_smaller_than_max = () => form_data.continuous_answer_min < form_data.continuous_answer_max

console.log('maxxx', form_data.continuous_answer_max)
const rules = {
  continuous_answer_min: {
    required,
    min_smaller_than_max: helpers.withMessage(`Min value must be smaller than the max value`, min_smaller_than_max)
    // maxValue: maxValue(form_data.continuous_answer_max),
  },
  continuous_answer_max: {
    required
  },
};

// const validate = reactive(useVuelidate(rules, toRefs(form_data)));
const validate = useVuelidate(rules, toRefs(form_data));
props.continuous_answer_option_data.validate = validate;
</script>