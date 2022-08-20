<template>
  <div class="p-5">
    <!-- <Preview> -->
      <AccordionGroup class="accordion-boxed">
        <AccordionItem>
            <Accordion>
              {{ msg }}
            </Accordion>
            <!-- <AccordionPanel class="text-slate-600 dark:text-slate-500 leading-relaxed">
                {{ msg }}
            </AccordionPanel> -->
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

let msg = ref('')
msg.value = params.msg
console.log('testsss', params)
</script>
