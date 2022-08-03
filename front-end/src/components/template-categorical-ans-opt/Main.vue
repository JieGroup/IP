<template>
    <div class="input-form">
      <label
          for="template-categorical-ans-opt"
          class="form-label w-full flex flex-col sm:flex-row"
      >
          <!-- Topic name -->
          <!-- <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
          >Required, at least 1 character</span
          > -->
      </label>

      <div class="form-check mt-2">
        <input class="form-check-input" type="checkbox" id="disabledFieldsetCheck" disabled>
        <label class="form-check-label" for="disabledFieldsetCheck">
          
        </label>
        <input
          id="template-categorical-ans-opt"
          v-model.trim="categorical_answer_option_data"
          type="text"
          name="categorical_answer_option_data"
          class="form-control"
          readonly="readonly"
        />
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
  requiredIf
} from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import Toastify from "toastify-js";
import dom from "@left4code/tw-starter/dist/js/dom";

// receive variable from parent
const props = defineProps({
  categorical_answer_option_data: {
    default: null,
  },
});
</script>