<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">FAQ</h2>
  </div>
  <div class="grid grid-cols-12 gap-6">
    <!-- BEGIN: FAQ Menu -->
    <div class="intro-y col-span-12 lg:col-span-4 xl:col-span-3">
      <div class="box mt-5">
        <div class="px-4 pb-3 pt-5">

          <a
            v-if="faq_indicator === 'about'"
            class="flex rounded-lg items-center px-4 py-2 bg-primary text-white font-medium"

            @click='to_about'
          >
            <ActivityIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">About This Free Tool</div>
          </a>
          <a
            v-else
            class="flex items-center px-4 py-2 mt-1"
            @click='to_about'
          >
            <ActivityIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">About This Free Tool</div>
          </a>

          <a v-if="faq_indicator === 'contact_us'" 
             class="flex rounded-lg items-center px-4 py-2 bg-primary text-white font-medium"
             @click='to_contact_us'>
            <BoxIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">About Us</div>
          </a>
          <a v-else 
             class="flex items-center px-4 py-2 mt-1" 
             @click='to_contact_us'>
            <BoxIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">About Us</div>
          </a>

          <a v-if="faq_indicator === 'terms_and_conditions'" 
             class="flex rounded-lg items-center px-4 py-2 bg-primary text-white font-medium"
             @click='to_terms_and_conditions'>
            <BoxIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Terms and Conditions</div>
          </a>
          <a v-else 
             class="flex items-center px-4 py-2 mt-1" 
             @click='to_terms_and_conditions'>
            <BoxIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Terms and Conditions</div>
          </a>

          <a v-if="faq_indicator === 'privacy_policy'" 
             class="flex rounded-lg items-center px-4 py-2 bg-primary text-white font-medium"
             @click='to_privacy_policy'>
            <LockIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Privacy Policy</div>
          </a>
          <a v-else 
             class="flex items-center px-4 py-2 mt-1" 
             @click='to_privacy_policy'>
            <LockIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Privacy Policy</div>
          </a>

          <!-- <a class="flex items-center px-4 py-2 mt-1" href="">
            <SettingsIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Multi Application License</div>
          </a> -->
        </div>
        <!-- <div
          class="px-4 py-3 border-t border-slate-200/60 dark:border-darkmode-400"
        >
          <a class="flex items-center px-4 py-2" href="">
            <ActivityIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Trem of Use</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <BoxIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Author Fees</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <LockIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Product Review</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <SettingsIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Privacy Policy</div>
          </a>
        </div> -->
        <!-- <div
          class="px-4 pt-3 pb-5 border-t border-slate-200/60 dark:border-darkmode-400"
        >
          <a class="flex items-center px-4 py-2" href="">
            <ActivityIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">About Our Products</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <BoxIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Related License</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <LockIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Single Application License</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <SettingsIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Multi Application License</div>
          </a>
        </div> -->
      </div>
    </div>
    <!-- END: FAQ Menu -->
    <!-- BEGIN: FAQ Content -->
    <div class="intro-y col-span-12 lg:col-span-8 xl:col-span-9">
      <div v-if="faq_indicator === 'about'" class="intro-y box lg:mt-5">
        <div
          class="flex items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">About This Free Tool</h2>
        </div>
        <AccordionGroup class="accordion-boxed p-5">

          <AccordionItem>
            <Accordion>
              Why use it
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              This survey tool is being developed as a research product that
              aims to provide a data-private, collection-efficient, and 
              inference-accurate way of surveying.
            </AccordionPanel>
          </AccordionItem>

          <AccordionItem>
            <Accordion>
              How does our engine work
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Underpinning this survey tool are novel ways of creating surveys and collecting data
              based on advanced AI algorithms.

              Any user (you) can easily create a survey by naming the desired topics and their value 
              ranges.
              
              Then, our engine will automatically create respondent-specific surveys, which can 
              adaptively enhance respondents' privacy and optimize collection efficiency.
            </AccordionPanel>
          </AccordionItem>

          <AccordionItem>
            <Accordion>
              How to create a survey
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              NOTE: the whole process is completely anonymous and free
              <br/>
              1. Register and log in
              <br/>
              2. Click 'Create New Survey' (Hint: choose "Private" mode to enhance privacy)
              <br/>
              3. Create a survey of (privacy-sensitive) questions
            </AccordionPanel>
          </AccordionItem>

          <AccordionItem>
            <Accordion> How to monitor and download survey results </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              NOTE: the whole process is completely anonymous and free
              <br/>
              1. Login to your account
              <br/>
              2. Click 'My Surveys' to monitor collection and download data
              <br/>
              All your surveys will be displayed in chronological order.
              By clicking 'Download' of a survey, you can download all its current responses.
              By clicking 'View Details' of a survey, you can view the parameters used to create it.
            </AccordionPanel>
          </AccordionItem>

          <AccordionItem>
            <Accordion> How to participate in a survey </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              If you are invited to participate in an existing survey:
              <br/>
              1. Type your participation ID (e.g., MTurk ID, student ID) following the survey link
              <br/>
              2. Keep answering the survey until it shows 'Thank you'
              <br/>
              3. Use the provided completion code to get rewards (if any) from the survey creator
            </AccordionPanel>
          </AccordionItem>
        </AccordionGroup>
      </div>
      <!-- END: FAQ Content -->
      <!-- START: Terms and Conditions Content -->
      <!-- faq_indicator {{ faq_indicator }} -->
      <div v-if="faq_indicator === 'terms_and_conditions'" class="intro-y box mt-5">
        <div
          class="flex items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Terms and Conditions
          </h2>
        </div>
        <AccordionGroup class="accordion-boxed p-5">
          <AccordionItem>
            <Accordion>
              OpenSSL Essentials: Working with SSL Certificates, Private Keys
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion>
              Understanding IP Addresses, Subnets, and CIDR Notation
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion> How To Troubleshoot Common HTTP Error Codes </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion> An Introduction to Securing your Linux VPS </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
        </AccordionGroup>
      </div>
      <!-- END: Terms and Conditions Content -->
      <!-- START: Privacy Policy -->
      <div v-if="faq_indicator === 'privacy_policy'" class="intro-y box mt-5">
        <div
          class="flex items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Privacy Policy
          </h2>
        </div>
        <AccordionGroup class="accordion-boxed p-5">
          <AccordionItem>
            <Accordion>
              OpenSSL Essentials: Working with SSL Certificates, Private Keys
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion>
              Understanding IP Addresses, Subnets, and CIDR Notation
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion> How To Troubleshoot Common HTTP Error Codes </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion> An Introduction to Securing your Linux VPS </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
        </AccordionGroup>
      </div>
      <!-- END: Privacy Policy -->

      <!-- START: Contact Us -->
      <div v-if="faq_indicator === 'contact_us'" class="intro-y box mt-5">
        <div
          class="flex items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            About Us
          </h2>
        </div>
        <AccordionGroup class="accordion-boxed p-5">
          <AccordionItem>
            <Accordion>
              Contact
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              We are a group of researchers based in Minnesota, US, who are actively maintaining this survey tool.
              If you have any technical questions or suggestions (e.g., new functions, domain customizations), 
              please feel free to contact us at IntervalPrivacy@gmail.com
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion>
              Data analysis support
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              The downloadable data are in json format. Please also contact us if you need technical support to 
              process them or use them for subsequent data analysis.
              Meanwhile, we are working to launch sample scripts to illustrate 
              how to post-process data for advanced analysis.
            </AccordionPanel>
          </AccordionItem>
        </AccordionGroup>
      </div>
      <!-- END: Contact Us -->
    </div>
    <!-- END: FAQ Content -->
  </div>
</template>

<script setup>
import { reactive, toRefs, ref } from "vue";
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
import { computed, onMounted } from "vue";
import Toastify from "toastify-js";
import { useRoute, useRouter } from "vue-router";
import DarkModeSwitcher from "@/components/dark-mode-switcher/Main.vue";
import dom from "@left4code/tw-starter/dist/js/dom";
import { useInfoStore } from "@/stores/user-info"
import { useAuthenticationStore } from "@/stores/authentication"
import { process_axios_error, get_auth_url, get_api_url } from "@/utils/axios_utils"
import { axios } from "@/utils/axios";
// import { axios } from "@/utils/axios";

const router = useRouter();

let faq_indicator = ref('about')

const to_about = () => {
  faq_indicator.value = 'about'
}

const to_terms_and_conditions = () => {
  faq_indicator.value = 'terms_and_conditions'
  console.log('faq', faq_indicator)
}

const to_privacy_policy = () => {
  faq_indicator.value = 'privacy_policy'
}

const to_contact_us = () => {
  faq_indicator.value = 'contact_us'
}

let params = router.currentRoute.value.params

onMounted(() => {
  console.log('layout-params', params)
  if ('faq_indicator' in params){
    faq_indicator.value = params.faq_indicator
  }
});
</script>