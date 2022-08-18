<template>
    <div
      class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
    >
    </div>
    <br />
    <!-- <br /> -->
    <div>
      <!-- BEGIN: Validation Form -->
      <!-- <form class="validate-form"> -->
        
        <div class="input-form mt-3">
        <label
          for="validation-form-2"
          class="form-label w-full flex flex-col sm:flex-row"
        >
          Topic question
        </label>
        <input
          id="validation-form-2"
          v-model.trim="surveyTemplateDynamicDataValue.topic_question"
          type="text"
          name="topic_question"
          class="form-control"
          readonly="readonly"
        />
        </div>

        <div class="input-form mt-3">
        <label
          for="validation-form-1"
          class="form-label w-full flex flex-col sm:flex-row"
        >
          Topic of this question
        </label>
        <input
          id="validation-form-1"
          v-model.trim="surveyTemplateDynamicDataKey"
          type="text"
          name="topic name"
          class="form-control"
          readonly="readonly"
        />
        </div>

        <div class="input-form mt-3">
        <label
          for="validation-form-3"
          class="form-label w-full flex flex-col sm:flex-row"
        >
          Collected data type
        </label>
        <input
          id="validation-form-3"
          v-model.trim="surveyTemplateDynamicDataValue.answer_type"
          type="text"
          name="topic_question"
          class="form-control"
          readonly="readonly"
        />
        </div>

        <div v-if="surveyTemplateDynamicDataValue.answer_type === 'categorical'" class="input-form mt-3">
        <!-- <TemplateCategoricalAnsOpt :categorical_answer_option_data="surveyTemplateDynamicDataValue.categorical_range"/> -->

        <TemplateCategoricalAnsOpt v-for="(item, index) in surveyTemplateDynamicDataValue.categorical_range.inclusion"
                                  :key="index" 
                                  :categorical_answer_option_data="item"/>

        </div>

        <div v-if="surveyTemplateDynamicDataValue.answer_type === 'continuous'" class="input-form mt-3">
          <TemplateContinuousAnsOpt :continuous_answer_option_data="surveyTemplateDynamicDataValue.continuous_range"/>
        </div>

        <div class="input-form mt-3">
          <label
            for="validation-form-4"
            class="form-label w-full flex flex-col sm:flex-row"
          >
            Unit
          </label>
          <input
            id="validation-form-4"
            v-model.trim="surveyTemplateDynamicDataValue.unit"
            type="text"
            name="unit"
            class="form-control"
            readonly="readonly"
          />
        </div>

      <br />
      <!-- END: Validation Form -->
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
import TemplateCategoricalAnsOpt from "@/components/template-categorical-ans-opt/Main.vue";
import TemplateContinuousAnsOpt from "@/components/template-continuous-ans-opt/Main.vue";


const props = defineProps({
  surveyTemplateDynamicDataKey: {
    default: null,
  },
  surveyTemplateDynamicDataValue: {
    default: null
  }
});

console.log('template-dynamic-form', props.surveyTemplateDynamicDataKey, props.surveyTemplateDynamicDataValue)

</script>