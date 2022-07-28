<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Tooltip</h2>
  </div>
  <div class="grid grid-cols-12 gap-6 mt-5">
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- BEGIN: Basic Tooltip -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Basic Tooltip</h2>
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
            <div class="text-center">
              <Tippy
                tag="a"
                href="javascript:;"
                class="tooltip btn btn-primary"
                content="This is awesome tooltip example!"
                >Show Tooltip</Tippy
              >
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div class="text-center">
                <Tippy
                  tag="a"
                  href="javascript:;"
                  class="tooltip btn btn-primary"
                  content="This is awesome tooltip example!"
                  >Show Tooltip</Tippy
                >
              </div>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Basic Tooltip -->
      <!-- BEGIN: On CLick Tooltip -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">On Click Tooltip</h2>
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
            <div class="text-center">
              <Tippy
                tag="a"
                href="javascript:;"
                class="tooltip btn btn-primary"
                content="This is awesome tooltip example!"
                :options="{
                  trigger: 'click',
                }"
                >Show Tooltip</Tippy
              >
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div class="text-center">
                <Tippy
                  tag="a"
                  href="javascript:;"
                  class="tooltip btn btn-primary"
                  content="This is awesome tooltip example!"
                  :options="{
                    trigger: 'click',
                  }"
                  >Show Tooltip</Tippy
                >
              </div>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: On CLick Tooltip -->
      <!-- BEGIN: Light Tooltip -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Light Tooltip</h2>
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
            <div class="text-center">
              <Tippy
                tag="a"
                href="javascript:;"
                class="tooltip btn btn-primary"
                content="This is awesome tooltip example!"
                :options="{
                  theme: 'light',
                }"
                >Show Tooltip</Tippy
              >
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div class="text-center">
                <Tippy
                  tag="a"
                  href="javascript:;"
                  class="tooltip btn btn-primary"
                  content="This is awesome tooltip example!"
                  :options="{
                    theme: 'light',
                  }"
                  >Show Tooltip</Tippy
                >
              </div>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Light Tooltip -->
    </div>
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- BEGIN: Custom Content Tooltip -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Custom Tooltip Content</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-4"
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
            <!-- BEGIN: Custom Tooltip Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                name="custom-tooltip-content"
                class="tooltip btn btn-primary"
                >Show Tooltip</a
              >
            </div>
            <!-- END: Custom Tooltip Toggle -->
            <!-- BEGIN: Custom Tooltip Content -->
            <div class="tooltip-content">
              <TippyContent to="custom-tooltip-content">
                <div
                  id="custom-content-tooltip"
                  class="relative flex items-center py-1"
                >
                  <div class="w-12 h-12 image-fit">
                    <img
                      alt="Midone Tailwind HTML Admin Template"
                      class="rounded-full"
                      :src="$f()[0].photos[0]"
                    />
                  </div>
                  <div class="ml-4 mr-auto">
                    <div
                      class="font-medium dark:text-slate-200 leading-relaxed"
                    >
                      {{ $f()[0].users[0].name }}
                    </div>
                    <div class="text-slate-500 dark:text-slate-400">
                      Bootstrap 4 HTML Admin Template
                    </div>
                  </div>
                </div>
              </TippyContent>
            </div>
            <!-- END: Custom Tooltip Content -->
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Custom Tooltip Toggle -->
              <div class="text-center">
                <a
                  href="javascript:;"
                  name="custom-tooltip-content"
                  class="tooltip btn btn-primary"
                  >Show Tooltip</a
                >
              </div>
              <!-- END: Custom Tooltip Toggle -->
              <!-- BEGIN: Custom Tooltip Content -->
              <div class="tooltip-content">
                <TippyContent to="custom-tooltip-content">
                  <div
                    id="custom-content-tooltip"
                    class="relative flex items-center py-1"
                  >
                    <div class="w-12 h-12 image-fit">
                      <img
                        alt="Midone Tailwind HTML Admin Template"
                        class="rounded-full"
                        :src="$f()[0].photos[0]"
                      />
                    </div>
                    <div class="ml-4 mr-auto">
                      <div
                        class="font-medium dark:text-slate-200 leading-relaxed"
                      >
                        \{\{ $f()[0].users[0].name \}\}
                      </div>
                      <div class="text-slate-500 dark:text-slate-400">
                        Bootstrap 4 HTML Admin Template
                      </div>
                    </div>
                  </div>
                </TippyContent>
              </div>
              <!-- END: Custom Tooltip Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Custom Content Tooltip -->
      <!-- BEGIN: Chart Tooltip -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Chart Tooltip</h2>
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
            <!-- BEGIN: Custom Tooltip Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                name="chart-tooltip"
                class="tooltip btn btn-primary"
                >Show Tooltip</a
              >
            </div>
            <!-- END: Custom Tooltip Toggle -->
            <!-- BEGIN: Custom Tooltip Content -->
            <div class="tooltip-content">
              <TippyContent to="chart-tooltip" class="py-1">
                <div class="font-medium dark:text-slate-200">Net Worth</div>
                <div class="flex items-center mt-2 sm:mt-0">
                  <div
                    class="mr-2 w-20 flex dark:text-slate-500 dark:text-slate-400"
                  >
                    USP:
                    <span class="ml-auto font-medium text-success">+23%</span>
                  </div>
                  <div class="w-24 sm:w-32 lg:w-56">
                    <SimpleLineChart1 :height="30" />
                  </div>
                </div>
              </TippyContent>
            </div>
            <!-- END: Custom Tooltip Content -->
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Custom Tooltip Toggle -->
              <div class="text-center">
                <a
                  href="javascript:;"
                  name="chart-tooltip"
                  class="tooltip btn btn-primary"
                  >Show Tooltip</a
                >
              </div>
              <!-- END: Custom Tooltip Toggle -->
              <!-- BEGIN: Custom Tooltip Content -->
              <div class="tooltip-content">
                <TippyContent to="chart-tooltip" class="py-1">
                  <div class="font-medium dark:text-slate-200">Net Worth</div>
                  <div class="flex items-center mt-2 sm:mt-0">
                    <div
                      class="mr-2 w-20 flex dark:text-slate-500 dark:text-slate-400"
                    >
                      USP:
                      <span class="ml-auto font-medium text-success">+23%</span>
                    </div>
                    <div class="w-24 sm:w-32 lg:w-56">
                      <SimpleLineChart1 :height="30" />
                    </div>
                  </div>
                </TippyContent>
              </div>
              <!-- END: Custom Tooltip Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Chart Tooltip -->
    </div>
  </div>
</template>

<script setup>
import SimpleLineChart1 from "@/components/simple-line-chart-1/Main.vue";
</script>
