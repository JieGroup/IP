<template>
    <div class="input-form">
    <label
        :for="input_id"
        class="form-label w-full flex flex-col sm:flex-row"
    >
        <!-- Topic name -->
        <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
        >Required, at least 1 character</span
        >
    </label>

    <!-- <div class="form-check mt-2">
        <input id="checkbox-switch-1" class="form-check-input" type="checkbox" value="" />
        <label class="form-check-label" for="checkbox-switch-1">Chris Evans</label>
    </div> -->

    <div class="form-check mt-2">
      <!-- <input id="checkbox-switch-1" class="form-check-input" type="checkbox" value="" /> -->
      <!-- <fieldset disabled>
      <input id="customCheckDisabled" for="disabledFieldsetCheck" class="form-check-input" type="checkbox" value="" />
      </fieldset> -->
      <input class="form-check-input" type="checkbox" id="disabledFieldsetCheck" disabled>
      <label class="form-check-label" for="disabledFieldsetCheck">
        
      </label>
      <!-- <li>
      </li> -->
      <!-- <input class="form-check-input" type="checkbox" id="disabledFieldsetCheck" disabled>
      <label class="form-check-label" for="disabledFieldsetCheck">
        Can't check this
      </label> -->
      <input
        :id="input_id"
        v-model.trim="validate.specific_option.$model"
        type="text"
        name="specific_option"
        class="form-control"
        :class="{ 'border-danger': validate.specific_option.$error }"
        :placeholder="placeholder"
      />
      <template v-if="validate.specific_option.$error">
        <div
        v-for="(error, index) in validate.specific_option.$errors"
        :key="index"
        class="text-danger mt-2"
        >
        {{ error.$message }}
        </div>
      </template>
      <!-- <input id="checkbox-switch-1" class="form-check-input" type="checkbox" value="" /> -->
      <!-- <label class="form-check-label" for="checkbox-switch-1">Chris Evans</label> -->
      <div class="input-group-append">
        <button type='button' @click="delete_categorical_answer_option" class="btn btn-outline-secondary">
          <XIcon class="w-5 h-5" />
        </button>
      </div>
      <!-- <button type='button' class="btn btn-secondary mr-1 mb-2">
        <CircleIcon class="w-5 h-5" />
      </button> -->
      
    </div>

    <!-- <div class="form-check mt-2">
    <button type='button' class="btn btn-secondary mr-1 mb-2">
      <CircleIcon class="w-5 h-5" />
    </button>
    <input
        id="input_id"
        v-model.trim="validate.specific_option.$model"
        type="text"
        name="specific_option"
        class="form-control"
        :class="{ 'border-danger': validate.specific_option.$error }"
        placeholder="placeholder"
    />
    <template v-if="validate.specific_option.$error">
        <div
        v-for="(error, index) in validate.specific_option.$errors"
        :key="index"
        class="text-danger mt-2"
        >
        {{ error.$message }}
        </div>
    </template>
    </div> -->
    <!-- <button type='button' @click="add_dynamic_form" class="btn btn-success mt-5">
          <PlusIcon class="w-5 h-5" />
    </button>
    <button type='button' @click="delete_dynamic_form" class="btn btn-danger mt-5">
      <TrashIcon class="w-5 h-5" />
    </button> -->
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
  categorical_answer_option_index: {
    type: [Number],
    default: null,
  },
  categorical_answer_option_data: {
    default: null,
  },
});

const input_id = `validation-form ${props.categorical_answer_option_index+100}`
const placeholder = `Option ${props.categorical_answer_option_index+1}`

const emits = defineEmits([
  'parent_delete_categorical_answer_option'
])

const delete_categorical_answer_option = () => {
  console.log('zizizujian')
  emits('parent_delete_categorical_answer_option', props.categorical_answer_option_index)
}

const form_data = reactive({
  specific_option: "",
});

const rules = {
  specific_option: {
    required,
    minLength: minLength(1),
  },
};

// const validate = reactive(useVuelidate(rules, toRefs(form_data)));
const validate = useVuelidate(rules, toRefs(form_data));
props.categorical_answer_option_data.validate = validate;
</script>