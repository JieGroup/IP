<template>
  <div class="p-5">
    <!-- <Preview> -->
      <AccordionGroup class="accordion-boxed">
        <AccordionItem>
            <Accordion>
              Thank you! Please use 
              your Participation ID (used to fill the survey) and the following Completion Code
              to get your reward (if any) from the survey creator.
            </Accordion>
            <AccordionPanel class="text-slate-600 dark:text-slate-500 leading-relaxed">
                Survey Answer ID: {{ surveyAnswerID }}
            </AccordionPanel>
        </AccordionItem>
      </AccordionGroup>
    <!-- </Preview> -->
  </div>
  
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from 'vue-router'

const router = useRouter()
let params = router.currentRoute.value.params

let surveyAnswerID = ref('')
surveyAnswerID.value = params.surveyAnswerID
console.log('testsss', params)
</script>
