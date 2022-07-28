<template>
    <div
      class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
    >
    </div>
    <br />
    <!-- <br /> -->
    <div>
      <!-- BEGIN: Static Answer Form -->
      <form class="validate-form">
        <!-- BEGIN: Continuous Topic Options -->
        <div v-if="subSurveyTopicValue.answer_type === 'continuous'" class="input-form mt-3">
        <label
          for="validation-form-1"
          class="form-label w-full flex flex-col sm:flex-row"
        >
          Q: {{ subSurveyTopicValue.topic_question }}
          <br />
          Unit: {{ subSurveyTopicValue.unit }}
          <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
          >Range: {{ continuousMinValue }} - {{ continuousMaxValue }}</span
          >
        </label>
        <input
          id="validation-form-1"
          v-model.trim="validate.continuous_range.$model"
          type="number"
          name="continuous_range"
          class="form-control"
          :class="{ 'border-danger': validate.continuous_range.$error }"
          placeholder="Please type in your answer between the min value and max value"
        />
        {{ validate.continuous_range.$model }}
        {{ validate.continuous_range.$error }}
        <template v-if="validate.continuous_range.$error">
          <div
          v-for="(error, index) in validate.continuous_range.$errors"
          :key="index"
          class="text-danger mt-2"
          >
          {{ error.$message }}
          </div>
        </template>
        </div>
        <!-- END: Continuous Topic Options -->

        <!-- BEGIN: Categorical Topic Options -->
        <div v-if="subSurveyTopicValue.answer_type === 'categorical'" class="mt-3">
        <label
            for="validation-form-2"
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
                      :value="index">{{ option.inclusion }}</option>
            </optgroup>
            
          </TomSelect>
        </div>
        </div>
        zhe zhe{{validate.categorical_range.$model}}
        <!-- END: Categorical Topic Options -->
      <br />
      </form>
      <!-- END: Static Answer Form -->
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

const continuousMinValue = computed(() => {
  if (props.subSurveyTopicValue.answer_type === 'continuous'){
      return props.subSurveyTopicValue.choices_list[0].min
  } else {
      return ""
  }
});
const continuousMaxValue = computed(() => {
  if (props.subSurveyTopicValue.answer_type === 'continuous'){
      return props.subSurveyTopicValue.choices_list[0].max
  } else {
      return ""
  }
});
const categoricalChoicesList = computed(() => {
  if (props.subSurveyTopicValue.answer_type === 'categorical'){
      return props.subSurveyTopicValue.choices_list
  } else {
      return []
  }
});

console.log('props.subSurveyTopicValue-ans-opt', props.subSurveyTopicValue)

const formData = reactive({
  continuous_range: "",
  categorical_range: '?????'
})
const rules = {
  // Answer can be null at current time.
  // If the answer is continuous, it must fall in min-max if not null
  // If the answer is categorical, no requirements.
  // console.log('shenme', continuousMinValue.value, continuousMaxValue.value),
  continuous_range: {
    required: requiredIf(() => props.subSurveyTopicValue.answer_type === 'continuous'),
    minValue: minValue(continuousMinValue.value),
    maxValue: maxValue(continuousMaxValue.value)
  },
  categorical_range: {
    required: requiredIf(() => props.subSurveyTopicValue.answer_type === 'continuous')
  },
};
const validate = reactive(useVuelidate(rules, toRefs(formData)));
props.answerFormData[props.subSurveyTopicKey] = validate;
</script>