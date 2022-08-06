<template>
    <div class="input-form">
    <label
        for="validation-form-31"
        class="form-label w-full flex flex-col sm:flex-row"
    >
      Answer minimum
    </label>
    <input
        id="validation-form-31"
        v-model.trim="continuous_answer_option_data.min"
        type='number'
        name="continuous_answer_min"
        class="form-control"
        readonly="readonly"
    />
    </div>

    <br />
    <div class="input-form">
    <label
        for="validation-form-32"
        class="form-label w-full flex flex-col sm:flex-row"
    >
        Answer maximum
    </label>
    <input
        id="validation-form-32"
        v-model.trim="continuous_answer_option_data.max"
        type='number'
        name="continuous_answer_max"
        class="form-control"
        readonly="readonly"
    />
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
  maxValue
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
</script>