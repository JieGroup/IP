<template>
    <div
      class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
    >
    </div>
    <br />
    <!-- <br /> -->
    <div>
      <!-- BEGIN: Validation Form -->
      <form class="validate-form">

        <div class="input-form">
        <label
            for="validation-form-1"
            class="form-label w-full flex flex-col sm:flex-row"
        >
            Topic Name
            <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
            >Required, at least 1 characters</span
            >
        </label>
        <input
            id="validation-form-1"
            v-model.trim="validate.topic_name.$model"
            type="text"
            name="topic_name"
            class="form-control"
            :class="{ 'border-danger': validate.topic_name.$error }"
            placeholder="Type your topic name. E.g. age"
        />

        <template v-if="validate.topic_name.$error">
            <div
            v-for="(error, index) in validate.topic_name.$errors"
            :key="index"
            class="text-danger mt-2"
            >
            {{ error.$message }}
            </div>
        </template>
        </div>

        <div class="input-form mt-3">
        <label
            for="validation-form-2"
            class="form-label w-full flex flex-col sm:flex-row"
        >
            Topic Question
            <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
            >Required, at least 5 characters</span
            >
        </label>
        <input
            id="validation-form-2"
            v-model.trim="validate.topic_question.$model"
            type="text"
            name="topic_question"
            class="form-control"
            :class="{ 'border-danger': validate.topic_question.$error }"
            placeholder="Question about this topic. E.g. what is your age?"
        />
        <template v-if="validate.topic_question.$error">
            <div
            v-for="(error, index) in validate.topic_question.$errors"
            :key="index"
            class="text-danger mt-2"
            >
            {{ error.$message }}
            </div>
        </template>
        </div>

        <div class="mt-3">
        <label>Answer Type</label>
        <div class="mt-2">
            <TomSelect v-model="validate.answer_type.$model" :options="{
                        placeholder: 'Select answer type',
                        }" class="w-full">
              <optgroup label="Answer Type">
                  <option value="categorical">Categorical</option>
                  <option value="continuous">Continuous</option>
              </optgroup>
            </TomSelect>
        </div>
        </div>

        <div v-if="validate.answer_type.$model === 'categorical'" class="input-form mt-3">
        <label
            for="validation-form-3"
            class="form-label w-full flex flex-col sm:flex-row"
        >
            Categorical Answer Options
            <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
            >Required, at least 1 option</span
            >
        </label>
        <input
            id="validation-form-3"
            v-model.trim="validate.categorical_answer_options.$model"
            type='text'
            name="categorical_answer_options"
            class="form-control"
            :class="{ 'border-danger': validate.categorical_answer_options.$error }"
            placeholder="Type your options. E.g. Student, Nurse, etc."
        />
        <template v-if="validate.categorical_answer_options.$error">
            <div
            v-for="(error, index) in validate.categorical_answer_options.$errors"
            :key="index"
            class="text-danger mt-2"
            >
            {{ error.$message }}
            </div>
        </template>
        </div>

        <div v-if="validate.answer_type.$model === 'continuous'" class="input-form mt-3">
        <label
            for="validation-form-31"
            class="form-label w-full flex flex-col sm:flex-row"
        >
            Continuous Answer Minimum
            <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
            >Required, at least 1 number</span
            >
        </label>
        <input
            id="validation-form-31"
            v-model.trim="validate.continuous_answer_min.$model"
            type='text'
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

        <div v-if="validate.answer_type.$model === 'continuous'" class="input-form mt-3">
        <label
            for="validation-form-32"
            class="form-label w-full flex flex-col sm:flex-row"
        >
            Continuous Answer Maximum
            <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
            >Required, at least 1 number</span
            >
        </label>
        <input
            id="validation-form-32"
            v-model.trim="validate.continuous_answer_max.$model"
            type='text'
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

        <div class="input-form mt-3">
        <label
            for="validation-form-4"
            class="form-label w-full flex flex-col sm:flex-row"
        >
            Unit
            <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
            >Required, at least 1 characters</span
            >
        </label>
        <input
            id="validation-form-4"
            v-model.trim="validate.unit.$model"
            type='text'
            name="unit"
            class="form-control"
            :class="{ 'border-danger': validate.unit.$error }"
            placeholder="Type your unit. E.g. m/s"
        />
        <template v-if="validate.unit.$error">
            <div
            v-for="(error, index) in validate.unit.$errors"
            :key="index"
            class="text-danger mt-2"
            >
            {{ error.$message }}
            </div>
        </template>
        </div>

        <!-- <button type="submit" class="btn btn-primary mt-5">
        Submit
        </button> -->
        <!-- <button @click="add_dynamic_form" class="btn btn-success mr-1 mb-2"> -->
        <button type='button' @click="add_dynamic_form" class="btn btn-success mt-5">
          <PlusIcon class="w-5 h-5" />
        </button>
        <button type='button' @click="delete_dynamic_form" class="btn btn-danger mt-5">
          <TrashIcon class="w-5 h-5" />
        </button>
      </form>
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
import { defineEmits } from 'vue'

// receive variable from parent
const props = defineProps({
  dynamic_form_index: {
    type: [Number],
    default: null,
  },
  dynamic_form_data: {
    default: null,
  },
});

// const { dynamic_form_index, dynamic_form_data } = toRefs(props);

const emits = defineEmits([
  'parent_add_dynamic_form', 
  'parent_delete_dynamic_form'
])

const add_dynamic_form = () => {
  emits('parent_add_dynamic_form')
  console.log('zizujian add')
}

const delete_dynamic_form = () => {
  console.log('indexxxx', props.dynamic_form_index)
  emits('parent_delete_dynamic_form', props.dynamic_form_index)
}

const form_data = reactive({
  topic_name: "",
  topic_question: "",
  answer_type: "categorical",
  categorical_answer_options: "",
  continuous_answer_min: null,
  continuous_answer_max: null,
  unit: "",
});

const rules = {
  topic_name: {
    required,
    minLength: minLength(1),
  },
  topic_question: {
    required,
    minLength: minLength(5),
  },
  answer_type: {
    required
  },
  categorical_answer_options: {
    required: requiredIf(() => form_data.answer_type === 'categorical')
  },
  continuous_answer_min: {
    required: requiredIf(() => form_data.answer_type === 'continuous')
  },
  continuous_answer_max: {
    required: requiredIf(() => form_data.answer_type === 'continuous')
  },
  unit: {
    required,
    minLength: minLength(1),
  },
};

const validate = useVuelidate(rules, toRefs(form_data));
props.dynamic_form_data.validate = validate;
// dynamic_form_data.value = validate
console.log('validate', validate)
console.log('dynamic----', props.dynamic_form_data.validate)
console.log('vaaaa', validate.value)
console.log('dynamic', props.dynamic_form_data.validate)
// console.log('dynamicaaaa', props.dynamic_form_data.value)
</script>