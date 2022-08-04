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
                Survey Template Name
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
                Survey Template ID
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

            <div class="input-form mt-3">
            <label
                for="validation-form-1"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Survey update method
            </label>
            <input
                id="validation-form-1"
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

</script>