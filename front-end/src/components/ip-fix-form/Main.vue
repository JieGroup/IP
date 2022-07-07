<template>
    <div>
        <!-- BEGIN: Validation Form -->
        <form class="validate-form">
            <div class="input-form">
            <label
                for="validation-form-1"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Name
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, at least 2 characters</span
                >
            </label>
            <input
                id="validation-form-1"
                v-model.trim="validate.name.$model"
                type="text"
                name="name"
                class="form-control"
                :class="{ 'border-danger': validate.name.$error }"
                placeholder="John Legend"
            />
            <template v-if="validate.name.$error">
                <div
                v-for="(error, index) in validate.name.$errors"
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
                Email
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, email address format</span
                >
            </label>
            <input
                id="validation-form-2"
                v-model.trim="validate.email.$model"
                type="email"
                name="email"
                class="form-control"
                :class="{ 'border-danger': validate.email.$error }"
                placeholder="example@gmail.com"
            />
            <template v-if="validate.email.$error">
                <div
                v-for="(error, index) in validate.email.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template>
            </div>
            <div class="input-form mt-3">
            <label
                for="validation-form-3"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Password
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, at least 6 characters</span
                >
            </label>
            <input
                id="validation-form-3"
                v-model.trim="validate.password.$model"
                type="password"
                name="password" 
                class="form-control"
                :class="{ 'border-danger': validate.password.$error }"
                placeholder="secretc"
            />
            <template v-if="validate.password.$error">
                <div
                v-for="(error, index) in validate.password.$errors"
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
                Age
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, integer only & maximum 3 characters</span
                >
            </label>
            <input
                id="validation-form-4"
                v-model.trim="validate.age.$model"
                type="number"
                name="age"
                class="form-control"
                :class="{ 'border-danger': validate.age.$error }"
                placeholder="21"
            />
            <template v-if="validate.age.$error">
                <div
                v-for="(error, index) in validate.age.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template>
            </div>
            <div class="input-form mt-3">
            <label
                for="validation-form-5"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Profile URL
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Optional, URL format</span
                >
            </label>
            <input
                id="validation-form-5"
                v-model.trim="validate.url.$model"
                type="url"
                name="url"
                class="form-control"
                :class="{ 'border-danger': validate.url.$error }"
                placeholder="https://google.com"
            />
            <template v-if="validate.url.$error">
                <div
                v-for="(error, index) in validate.url.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template>
            </div>
            <div class="input-form mt-3">
            <label
                for="validation-form-6"
                class="form-label w-full flex flex-col sm:flex-row"
            >
                Comment
                <span class="sm:ml-auto mt-1 sm:mt-0 text-xs text-slate-500"
                >Required, at least 10 characters</span
                >
            </label>
            <textarea
                id="validation-form-6"
                v-model.trim="validate.comment.$model"
                class="form-control"
                :class="{ 'border-danger': validate.comment.$error }"
                name="comment"
                placeholder="Type your comments"
            ></textarea>
            <template v-if="validate.comment.$error">
                <div
                v-for="(error, index) in validate.comment.$errors"
                :key="index"
                class="text-danger mt-2"
                >
                {{ error.$message }}
                </div>
            </template>
            </div>
        </form>
        <!-- END: Validation Form -->
    </div>
</template>


<script setup>
import { reactive, toRefs } from "vue";
import {
  required,
  minLength,
  maxLength,
  email,
  url,
  integer,
} from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import Toastify from "toastify-js";
import dom from "@left4code/tw-starter/dist/js/dom";

// receive variable from parent
const props = defineProps({
  fix_form_data: {
    default: null,
  },
});

const emit = defineEmits([])

const formData = reactive({
  name: "",
  email: "",
  password: "secret",
  age: "",
  url: "",
  comment: "",
});

const rules = {
  name: {
    required,
    minLength: minLength(2),
  },
  email: {
    required,
    email,
  },
  password: {
    required,
    minLength: minLength(6),
  },
  age: {
    required,
    integer,
    maxLength: maxLength(3),
  },
  url: {
    url,
  },
  comment: {
    required,
    minLength: minLength(10),
  },
};

const validate = useVuelidate(rules, toRefs(formData));
props.fix_form_data.validate = validate;
</script>