<template>
    <div
      class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
    >
    </div>
    <br />
    <!-- <br /> -->
    <div>
      <!-- BEGIN: Uniform Answer Form -->
      <form class="validate-form">
        <!-- BEGIN: Continuous Topic Options -->
        <div v-if="subSurveyTopicValue.answer_type === 'continuous'" class="input-form">
        <label
            for="validation-form-1"
            class="form-label w-full flex flex-col sm:flex-row"
        >
            Q: {{ subSurveyTopicValue.topic_question }}
            <br />
            Unit: {{ subSurveyTopicValue.unit }}
        </label>
        <div class="mt-2">
          <TomSelect v-model="validate.continuous_range.$model" :options="{
                      placeholder: 'Select answer',
                      }" class="w-full">
            <optgroup label="Answer">
              <option v-for="(option, index) in continuousChoicesList" 
                      :key="option"
                      :value="index">{{ option }}</option>
            </optgroup>
          </TomSelect>
        </div>
        <!-- END: Continuous Topic Options -->

        <!-- BEGIN: Categorical Topic Options -->
        <div v-if="subSurveyTopicValue.answer_type === 'categorical'" class="mt-3">
        <label
            for="validation-form-1"
            class="form-label w-full flex flex-col sm:flex-row"
        >
            Q: {{ subSurveyTopicValue.topic_question }}
            <br />
            Unit: {{ subSurveyTopicValue.unit }}
        </label>
        <div class="mt-2">
          <TomSelect v-model="validate.categorical_range.$model" :options="{
                      placeholder: 'Select answer',
                      }" class="w-full">
            <optgroup label="Answer">
              <option v-for="(option, index) in categoricalChoicesList" 
                      :key="index"
                      :value="index">{{ option }}</option>
            </optgroup>
          </TomSelect>
        </div>
        </div>
        <!-- END: Categorical Topic Options -->
      <br />
      </form>
      <!-- END: Uniform Answer Form -->
    </div>
</template>


<script setup>
import { ref } from "vue";
import { reactive, toRefs, computed } from "vue";
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
import { reform_choices } from './index'

// receive variable from parent
const props = defineProps({
  subSurveyTopicKey: {
    default: null,
  },
  subSurveyTopicValue: {
    default: null,
  },
  answerFormData: {
    default: null,
  }
});

const continuousChoicesList = computed(() => {
  if (props.subSurveyTopicValue.answer_type === 'continuous'){
      return reform_choices(props.subSurveyTopicValue.choices_list, 'continuous')
  } else {
      return []
  }
});
const categoricalChoicesList = computed(() => {
  if (props.subSurveyTopicValue.answer_type === 'categorical'){
      return reform_choices(props.subSurveyTopicValue.choices_list, 'categorical')
  } else {
      return []
  }
});

const formData = reactive({
  continuous_range: "",
  categorical_range: ""
})
const rules = {
  // Answer can be null at current time.
  // If the answer is continuous, it must fall in min-max if not null
  // If the answer is categorical, no requirements.
  continuous_range: {
    required: requiredIf(() => props.subSurveyTopicValue.answer_type === 'continuous')
  },
  categorical_range: {
    required: requiredIf(() => props.subSurveyTopicValue.answer_type === 'categorical')
  },
};
const validate = reactive(useVuelidate(rules, toRefs(formData)));
props.answerFormData[props.subSurveyTopicKey] = validate;
</script>