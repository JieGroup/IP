<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Dropzone</h2>
  </div>
  <div class="grid grid-cols-12 gap-6 mt-5">
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- BEGIN: Single File Upload -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Single File Upload</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-1"
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
            <Dropzone
              ref-key="dropzoneSingleRef"
              :options="{
                url: 'https://httpbin.org/post',
                thumbnailWidth: 150,
                maxFilesize: 0.5,
                maxFiles: 1,
                headers: { 'My-Awesome-Header': 'header value' },
              }"
              class="dropzone"
            >
              <div class="text-lg font-medium">
                Drop files here or click to upload.
              </div>
              <div class="text-gray-600">
                This is just a demo dropzone. Selected files are
                <span class="font-medium">not</span> actually uploaded.
              </div>
            </Dropzone>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Dropzone
                ref-key="dropzoneSingleRef"
                :options="{
                  url: 'https://httpbin.org/post',
                  thumbnailWidth: 150,
                  maxFilesize: 0.5,
                  maxFiles: 1,
                  headers: { 'My-Awesome-Header': 'header value' },
                }"
                class="dropzone"
              >
                <div class="text-lg font-medium">
                  Drop files here or click to upload.
                </div>
                <div class="text-gray-600">
                  This is just a demo dropzone. Selected files are
                  <span class="font-medium">not</span> actually uploaded.
                </div>
              </Dropzone>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Single File Upload -->
      <!-- BEGIN: Multiple File Upload -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Multiple File Upload</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-2"
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
            <Dropzone
              ref-key="dropzoneMultipleRef"
              :options="{
                url: 'https://httpbin.org/post',
                thumbnailWidth: 150,
                maxFilesize: 0.5,
                headers: { 'My-Awesome-Header': 'header value' },
              }"
              class="dropzone"
            >
              <div class="text-lg font-medium">
                Drop files here or click to upload.
              </div>
              <div class="text-gray-600">
                This is just a demo dropzone. Selected files are
                <span class="font-medium">not</span> actually uploaded.
              </div>
            </Dropzone>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Dropzone
                ref-key="dropzoneMultipleRef"
                :options="{
                  url: 'https://httpbin.org/post',
                  thumbnailWidth: 150,
                  maxFilesize: 0.5,
                  headers: { 'My-Awesome-Header': 'header value' },
                }"
                class="dropzone"
              >
                <div class="text-lg font-medium">
                  Drop files here or click to upload.
                </div>
                <div class="text-gray-600">
                  This is just a demo dropzone. Selected files are
                  <span class="font-medium">not</span> actually uploaded.
                </div>
              </Dropzone>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Multiple File Upload -->
    </div>
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- BEGIN: File Type Validation -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">File Type Validation</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-3"
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
            <Dropzone
              ref-key="dropzoneValidationRef"
              :options="{
                url: 'https://httpbin.org/post',
                thumbnailWidth: 150,
                maxFilesize: 0.5,
                acceptedFiles: 'image/jpeg|image/png|image/jpg',
                headers: { 'My-Awesome-Header': 'header value' },
              }"
              class="dropzone"
            >
              <div class="text-lg font-medium">
                Drop files here or click to upload.
              </div>
              <div class="text-gray-600">
                This is just a demo dropzone. Selected files are
                <span class="font-medium">not</span> actually uploaded.
              </div>
            </Dropzone>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Dropzone
                ref-key="dropzoneValidationRef"
                :options="{
                  url: 'https://httpbin.org/post',
                  thumbnailWidth: 150,
                  maxFilesize: 0.5,
                  acceptedFiles: 'image/jpeg|image/png|image/jpg',
                  headers: { 'My-Awesome-Header': 'header value' },
                }"
                class="dropzone"
              >
                <div class="text-lg font-medium">
                  Drop files here or click to upload.
                </div>
                <div class="text-gray-600">
                  This is just a demo dropzone. Selected files are
                  <span class="font-medium">not</span> actually uploaded.
                </div>
              </Dropzone>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: File Type Validation -->
    </div>
  </div>
</template>

<script setup>
import { ref, provide, onMounted } from "vue";

const dropzoneSingleRef = ref();
const dropzoneMultipleRef = ref();
const dropzoneValidationRef = ref();

provide("bind[dropzoneSingleRef]", (el) => {
  dropzoneSingleRef.value = el;
});

provide("bind[dropzoneMultipleRef]", (el) => {
  dropzoneMultipleRef.value = el;
});

provide("bind[dropzoneValidationRef]", (el) => {
  dropzoneValidationRef.value = el;
});

onMounted(() => {
  const elDropzoneSingleRef = dropzoneSingleRef.value;
  elDropzoneSingleRef.dropzone.on("success", () => {
    alert("Added file.");
  });
  elDropzoneSingleRef.dropzone.on("error", () => {
    alert("No more files please!");
  });

  const elDropzoneMultipleRef = dropzoneMultipleRef.value;
  elDropzoneMultipleRef.dropzone.on("success", () => {
    alert("Added file.");
  });
  elDropzoneMultipleRef.dropzone.on("error", () => {
    alert("No more files please!");
  });

  const elDropzoneValidationRef = dropzoneValidationRef.value;
  elDropzoneValidationRef.dropzone.on("success", () => {
    alert("Added file.");
  });
  elDropzoneValidationRef.dropzone.on("error", () => {
    alert("No more files please!");
  });
});
</script>
