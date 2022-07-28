<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Slider</h2>
  </div>
  <div class="grid grid-cols-12 gap-6 mt-5">
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- BEGIN: Single Item -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Single Item</h2>
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
            <div class="mx-6">
              <TinySlider
                :options="{
                  controls: true,
                }"
              >
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      1
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      2
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      3
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      4
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      5
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      6
                    </h3>
                  </div>
                </div>
              </TinySlider>
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div class="mx-6">
                <TinySlider
                  :options="{
                    controls: true,
                  }"
                >
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        1
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        2
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        3
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        4
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        5
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        6
                      </h3>
                    </div>
                  </div>
                </TinySlider>
              </div>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Single Item -->
      <!-- BEGIN: Multiple Item -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Multiple Item</h2>
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
            <div class="mx-6">
              <TinySlider
                :options="{
                  autoplay: false,
                  controls: true,
                  items: 1,
                  responsive: {
                    600: {
                      items: 3,
                    },
                    480: {
                      items: 2,
                    },
                  },
                }"
              >
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      1
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      2
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      3
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      4
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      5
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      6
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      7
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      8
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      9
                    </h3>
                  </div>
                </div>
              </TinySlider>
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div class="mx-6">
                <TinySlider
                  :options="{
                    autoplay: false,
                    controls: true,
                    items: 1,
                    responsive: {
                      600: {
                        items: 3,
                      },
                      480: {
                        items: 2,
                      },
                    },
                  }"
                >
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        1
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        2
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        3
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        4
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        5
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        6
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        7
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        8
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        9
                      </h3>
                    </div>
                  </div>
                </TinySlider>
              </div>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Multiple Item -->
      <!-- BEGIN: Responsive Display -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Responsive Display</h2>
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
            <div class="mx-6 pb-8">
              <TinySlider
                :options="{
                  autoplay: false,
                  controls: true,
                  items: 1,
                  nav: true,
                  responsive: {
                    600: {
                      items: 3,
                    },
                    480: {
                      items: 2,
                    },
                  },
                }"
              >
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      1
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      2
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      3
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      4
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      5
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      6
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      7
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      8
                    </h3>
                  </div>
                </div>
              </TinySlider>
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div class="mx-6 pb-8">
                <TinySlider
                  :options="{
                    autoplay: false,
                    controls: true,
                    items: 1,
                    nav: true,
                    responsive: {
                      600: {
                        items: 3,
                      },
                      480: {
                        items: 2,
                      },
                    },
                  }"
                >
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        1
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        2
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        3
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        4
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        5
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        6
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        7
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        8
                      </h3>
                    </div>
                  </div>
                </TinySlider>
              </div>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Responsive Display -->
    </div>
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- BEGIN: Center Mode -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Center Mode</h2>
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
            <div class="mx-6">
              <TinySlider
                :options="{
                  autoplay: false,
                  controls: true,
                  center: true,
                  items: 1,
                  responsive: {
                    600: {
                      items: 2,
                    },
                  },
                }"
              >
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      1
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      2
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      3
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      4
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      5
                    </h3>
                  </div>
                </div>
                <div class="h-32 px-2">
                  <div
                    class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                  >
                    <h3
                      class="h-full font-medium flex items-center justify-center text-2xl"
                    >
                      6
                    </h3>
                  </div>
                </div>
              </TinySlider>
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div class="mx-6">
                <TinySlider
                  :options="{
                    autoplay: false,
                    controls: true,
                    center: true,
                    items: 1,
                    responsive: {
                      600: {
                        items: 2,
                      },
                    },
                  }"
                >
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        1
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        2
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        3
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        4
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        5
                      </h3>
                    </div>
                  </div>
                  <div class="h-32 px-2">
                    <div
                      class="h-full bg-slate-100 dark:bg-darkmode-400 rounded-md"
                    >
                      <h3
                        class="h-full font-medium flex items-center justify-center text-2xl"
                      >
                        6
                      </h3>
                    </div>
                  </div>
                </TinySlider>
              </div>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Center Mode -->
      <!-- BEGIN: Fade Animation -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Fade Animation</h2>
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
            <div class="mx-6 pb-8">
              <TinySlider
                :options="{
                  mode: 'gallery',
                  controls: true,
                  nav: true,
                  speed: 500,
                }"
              >
                <div class="h-64 px-2">
                  <div class="h-full image-fit rounded-md overflow-hidden">
                    <img
                      alt="Midone Tailwind HTML Admin Template"
                      :src="$f()[0].images[0]"
                    />
                  </div>
                </div>
                <div class="h-64 px-2">
                  <div class="h-full image-fit rounded-md overflow-hidden">
                    <img
                      alt="Midone Tailwind HTML Admin Template"
                      :src="$f()[1].images[1]"
                    />
                  </div>
                </div>
                <div class="h-64 px-2">
                  <div class="h-full image-fit rounded-md overflow-hidden">
                    <img
                      alt="Midone Tailwind HTML Admin Template"
                      :src="$f()[2].images[2]"
                    />
                  </div>
                </div>
              </TinySlider>
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div class="mx-6 pb-8">
                <TinySlider
                  :options="{
                    mode: 'gallery',
                    controls: true,
                    nav: true,
                    speed: 500,
                  }"
                >
                  <div class="h-64 px-2">
                    <div class="h-full image-fit rounded-md overflow-hidden">
                      <img
                        alt="Midone Tailwind HTML Admin Template"
                        :src="$f()[0].images[0]"
                      />
                    </div>
                  </div>
                  <div class="h-64 px-2">
                    <div class="h-full image-fit rounded-md overflow-hidden">
                      <img
                        alt="Midone Tailwind HTML Admin Template"
                        :src="$f()[1].images[1]"
                      />
                    </div>
                  </div>
                  <div class="h-64 px-2">
                    <div class="h-full image-fit rounded-md overflow-hidden">
                      <img
                        alt="Midone Tailwind HTML Admin Template"
                        :src="$f()[2].images[2]"
                      />
                    </div>
                  </div>
                </TinySlider>
              </div>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Fade Animation -->
    </div>
  </div>
</template>
