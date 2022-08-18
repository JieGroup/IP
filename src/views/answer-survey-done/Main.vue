<template>
  <div class="p-5">
    <!-- <Preview> -->
      <AccordionGroup class="accordion-boxed">
        <AccordionItem>
            <Accordion>
              Thank you for your participation! Please use Survey Answer ID and
              Mturk ID to get your payment!
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
