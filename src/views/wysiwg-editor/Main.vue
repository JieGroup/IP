<template>
  <div class="flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">CKEditor</h2>
  </div>
  <div class="grid grid-cols-12 gap-6 mt-5">
    <!-- BEGIN: Classic Editor -->
    <div class="col-span-12">
      <PreviewComponent class="box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Classic Editor</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-5"
              >Show example code</label
            >
            <input
              @click="toggle"
              class="form-check-input mr-0 ml-3"
              type="checkbox"
            />
          </div>
        </div>
        <div class="p-5">
          <Preview>
            <ClassicEditor v-model="editorData" />
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <ClassicEditor v-model="editorData" />
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
    </div>
    <!-- END: Classic Editor -->
  </div>
  <div></div>
</template>

<script setup>
import { ref } from "vue";

const editorData = ref("<p>Content of the editor.</p>");
</script>
