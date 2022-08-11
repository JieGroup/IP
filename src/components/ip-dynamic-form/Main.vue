<template>
    
    <!-- <div
      class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
    >
    </div> -->
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
            Question {{ dynamic_form_index+1 }}
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
            placeholder="What to ask from respondents, e.g., 'What is your age?'"
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

        <div class="input-form mt-3">
        <label
            for="validation-form-1"
            class="form-label w-full flex flex-col sm:flex-row"
        >
            Topic of this question
            <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
            >Required, at least 1 character</span
            >
        </label>
        <input
            id="validation-form-1"
            v-model.trim="validate.topic_name.$model"
            type="text"
            name="topic_name"
            class="form-control"
            :class="{ 'border-danger': validate.topic_name.$error }"
            placeholder="A keyword of this question, e.g., salary"
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
        

        <div class="mt-3">
        <label>Collected data type</label>
        <div class="mt-2">
            <TomSelect v-model="validate.answer_type.$model" :options="{
                        placeholder: 'Select a data type to collect',
                        }" class="w-full">
              <optgroup label="Collected data type">
                  <option value="categorical">Categorical</option>
                  <option value="continuous">Continuous</option>
              </optgroup>
            </TomSelect>
        </div>
        </div>

        <div v-if="validate.answer_type.$model === 'categorical'" class="input-form mt-3">
        <CategoricalAnsOpt v-for="(item, index) in categorical_answer_options"
                          :key="item.unique_id" 
                          :categorical_answer_option_index="index"
                          :categorical_answer_option_data="item"
                          @parent_delete_categorical_answer_option="delete_categorical_answer_option"/>
        <br />
        <div class="input-form">
          <!-- <br> -->
          <input class="form-check-input" type="checkbox" id="disabledFieldsetCheck" disabled>
          <label class="form-check-label" for="disabledFieldsetCheck" @click="add_categorical_answer_option">
            <!-- <u class="block mt-1">add new option</u> -->
            <u>Add new option</u>
            <!-- <u class="block mt-1">This line of text will render as underlined</u> -->
          </label>
        </div>
        </div>

        <div v-if="validate.answer_type.$model === 'continuous'" class="input-form mt-3">
          <ContinuousAnsOpt :continuous_answer_option_data="continuous_answer_options"/>
        </div>

        <div class="input-form mt-3">
        <label
            for="validation-form-4"
            class="form-label w-full flex flex-col sm:flex-row"
        >
            Unit
            <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
            >Required, at least 1 character</span
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
          <u>Create another question</u>
        </button>
        

        <br />
        <button type='button' @click="delete_dynamic_form" class="btn btn-danger mt-5">
          <TrashIcon class="w-5 h-5" />
          <u>Remove the above question</u>
        </button>

        <br />
        <button type='button' @click="duplicate_dynamic_form" class="btn btn-danger mt-5">
          <PlusIcon class="w-5 h-5" />
          <u>Duplicate the above question</u>
        </button>
      <div
        class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-400/60 dark:border-darkmode-800"
      >
      </div>  
      <!-- </form> -->
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
import CategoricalAnsOpt from "@/components/categorical-ans-opt/Main.vue";
import ContinuousAnsOpt from "@/components/continuous-ans-opt/Main.vue";

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
let categorical_answer_options = reactive([
  {
    unique_id: 0,
  },
  {
    unique_id: 1,
  },
  {
    unique_id: 2,  
  }
])
let unique_id = categorical_answer_options.length
let continuous_answer_options = reactive([{}])

const emits = defineEmits([
  'parent_add_dynamic_form', 
  'parent_delete_dynamic_form',
  'parent_duplicate_dynamic_form'
])

const add_dynamic_form = () => {
  emits('parent_add_dynamic_form')
  console.log('zizujian add')
}

const delete_dynamic_form = () => {
  console.log('indexxxx', props.dynamic_form_index)
  emits('parent_delete_dynamic_form', props.dynamic_form_index)
}

const duplicate_dynamic_form = () => {
  console.log('duplicate')
  emits('parent_duplicate_dynamic_form', props.dynamic_form_index)
}

const add_categorical_answer_option = () => {
  categorical_answer_options.push({unique_id: unique_id})
  unique_id += 1
}

const delete_categorical_answer_option = (categorical_answer_options_index) => {
  console.log('zizujian', categorical_answer_options_index)
  if (categorical_answer_options_index !== 0){
    // array.splice(index, howmany)
    categorical_answer_options.splice(categorical_answer_options_index, 1)
  }
}

const formData = reactive({
  topic_name: "",
  topic_question: "",
  answer_type: "categorical",
  categorical_answer_options: categorical_answer_options,
  continuous_answer_options: continuous_answer_options,
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
    required: requiredIf(() => formData.answer_type === 'categorical')
  },
  continuous_answer_options: {
    required: requiredIf(() => formData.answer_type === 'continuous')
  },
  unit: {
    required,
    minLength: minLength(1),
  },
};

// const validate = reactive(useVuelidate(rules, toRefs(formData)));
const validate = useVuelidate(rules, toRefs(formData));
props.dynamic_form_data.validate = validate;
// dynamic_form_data.value = validate
console.log('validate', validate)
console.log('dynamic----', props.dynamic_form_data.validate)
console.log('vaaaa', validate.value)
console.log('dynamic', props.dynamic_form_data.validate)
// console.log('dynamicaaaa', props.dynamic_form_data.value)
</script>