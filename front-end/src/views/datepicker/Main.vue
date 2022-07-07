<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Datepicker</h2>
  </div>
  <div class="intro-y grid grid-cols-12 gap-6 mt-5">
    <div class="col-span-12 lg:col-span-6">
      <!-- BEGIN: Basic Datepicker -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Basic Date Picker</h2>
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
            <Litepicker
              v-model="date"
              :options="{
                autoApply: false,
                showWeekNumbers: true,
                dropdowns: {
                  minYear: 1990,
                  maxYear: null,
                  months: true,
                  years: true,
                },
              }"
              class="form-control w-56 block mx-auto"
            />
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Litepicker
                v-model="date"
                :options="{
                  autoApply: false,
                  showWeekNumbers: true,
                  dropdowns: {
                    minYear: 1990,
                    maxYear: null,
                    months: true,
                    years: true,
                  },
                }"
                class="form-control w-56 block mx-auto"
              />
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Basic Datepicker -->
      <!-- BEGIN: Input Group -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Input Group</h2>
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
            <div class="relative w-56 mx-auto">
              <div
                class="absolute rounded-l w-10 h-full flex items-center justify-center bg-slate-100 border text-slate-500 dark:bg-darkmode-700 dark:border-darkmode-800 dark:text-slate-400"
              >
                <CalendarIcon class="w-4 h-4" />
              </div>
              <Litepicker
                v-model="date"
                :options="{
                  autoApply: false,
                  showWeekNumbers: true,
                  dropdowns: {
                    minYear: 1990,
                    maxYear: null,
                    months: true,
                    years: true,
                  },
                }"
                class="form-control pl-12"
              />
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div class="relative w-56 mx-auto">
                <div
                  class="absolute rounded-l w-10 h-full flex items-center justify-center bg-slate-100 border text-slate-500 dark:bg-darkmode-700 dark:border-darkmode-800 dark:text-slate-400"
                >
                  <CalendarIcon class="w-4 h-4" />
                </div>
                <Litepicker
                  v-model="date"
                  :options="{
                    autoApply: false,
                    showWeekNumbers: true,
                    dropdowns: {
                      minYear: 1990,
                      maxYear: null,
                      months: true,
                      years: true,
                    },
                  }"
                  class="form-control pl-12"
                />
              </div>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Input Group -->
    </div>
    <div class="col-span-12 lg:col-span-6">
      <!-- BEGIN: Daterange Picker -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Date Range Picker</h2>
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
            <Litepicker
              v-model="daterange"
              :options="{
                autoApply: false,
                singleMode: false,
                numberOfColumns: 2,
                numberOfMonths: 2,
                showWeekNumbers: true,
                dropdowns: {
                  minYear: 1990,
                  maxYear: null,
                  months: true,
                  years: true,
                },
              }"
              class="form-control w-56 block mx-auto"
            />
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Litepicker
                v-model="daterange"
                :options="{
                  autoApply: false,
                  singleMode: false,
                  numberOfColumns: 2,
                  numberOfMonths: 2,
                  showWeekNumbers: true,
                  dropdowns: {
                    minYear: 1990,
                    maxYear: null,
                    months: true,
                    years: true,
                  },
                }"
                class="form-control w-56 block mx-auto"
              />
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Daterange Picker -->
      <!-- BEGIN: Modal Datepicker -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Modal Date Picker</h2>
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
            <!-- BEGIN: Show Modal Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                @click="datepickerModalPreview = true"
                class="btn btn-primary"
                >Show Modal</a
              >
            </div>
            <!-- END: Show Modal Toggle -->
            <!-- BEGIN: Modal Content -->
            <Modal
              :show="datepickerModalPreview"
              @hidden="datepickerModalPreview = false"
            >
              <!-- BEGIN: Modal Header -->
              <ModalHeader>
                <h2 class="font-medium text-base mr-auto">Filter by Date</h2>
                <button class="btn btn-outline-secondary hidden sm:flex">
                  <FileIcon class="w-4 h-4 mr-2" /> Download Docs
                </button>
                <Dropdown class="sm:hidden">
                  <DropdownToggle
                    tag="a"
                    class="w-5 h-5 block"
                    href="javascript:;"
                  >
                    <MoreHorizontalIcon class="w-5 h-5 text-slate-500" />
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>
                        <FileIcon class="w-4 h-4 mr-2" />
                        Download Docs
                      </DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
              </ModalHeader>
              <!-- END: Modal Header -->
              <!-- BEGIN: Modal Body -->
              <ModalBody class="grid grid-cols-12 gap-4 gap-y-3">
                <div class="col-span-12 sm:col-span-6">
                  <label for="modal-datepicker-1" class="form-label"
                    >From</label
                  >
                  <Litepicker
                    id="modal-datepicker-1"
                    v-model="date"
                    :options="{
                      autoApply: false,
                      showWeekNumbers: true,
                      dropdowns: {
                        minYear: 1990,
                        maxYear: null,
                        months: true,
                        years: true,
                      },
                    }"
                    class="form-control"
                  />
                </div>
                <div class="col-span-12 sm:col-span-6">
                  <label for="modal-datepicker-2" class="form-label">To</label>
                  <Litepicker
                    id="modal-datepicker-2"
                    v-model="date"
                    :options="{
                      autoApply: false,
                      showWeekNumbers: true,
                      dropdowns: {
                        minYear: 1990,
                        maxYear: null,
                        months: true,
                        years: true,
                      },
                    }"
                    class="form-control"
                  />
                </div>
              </ModalBody>
              <!-- END: Modal Body -->
              <!-- BEGIN: Modal Footer -->
              <ModalFooter class="text-right">
                <button
                  type="button"
                  @click="datepickerModalPreview = false"
                  class="btn btn-outline-secondary w-20 mr-1"
                >
                  Cancel
                </button>
                <button type="button" class="btn btn-primary w-20">
                  Submit
                </button>
              </ModalFooter>
              <!-- END: Modal Footer -->
            </Modal>
            <!-- END: Modal Content -->
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Show Modal Toggle -->
              <div class="text-center">
                <a
                  href="javascript:;"
                  @click="datepickerModalPreview = true"
                  class="btn btn-primary"
                  >Show Modal</a
                >
              </div>
              <!-- END: Show Modal Toggle -->
              <!-- BEGIN: Modal Content -->
              <Modal
                :show="datepickerModalPreview"
                @hidden="datepickerModalPreview = false"
              >
                <!-- BEGIN: Modal Header -->
                <ModalHeader>
                  <h2 class="font-medium text-base mr-auto">Filter by Date</h2>
                  <button class="btn btn-outline-secondary hidden sm:flex">
                    <FileIcon class="w-4 h-4 mr-2" /> Download Docs
                  </button>
                  <Dropdown class="sm:hidden">
                    <DropdownToggle
                      tag="a"
                      class="w-5 h-5 block"
                      href="javascript:;"
                    >
                      <MoreHorizontalIcon class="w-5 h-5 text-slate-500" />
                    </DropdownToggle>
                    <DropdownMenu class="w-40">
                      <DropdownContent>
                        <DropdownItem>
                          <FileIcon class="w-4 h-4 mr-2" />
                          Download Docs
                        </DropdownItem>
                      </DropdownContent>
                    </DropdownMenu>
                  </Dropdown>
                </ModalHeader>
                <!-- END: Modal Header -->
                <!-- BEGIN: Modal Body -->
                <ModalBody class="grid grid-cols-12 gap-4 gap-y-3">
                  <div class="col-span-12 sm:col-span-6">
                    <label for="modal-datepicker-1" class="form-label"
                      >From</label
                    >
                    <Litepicker
                      id="modal-datepicker-1"
                      v-model="date"
                      :options="{
                        autoApply: false,
                        showWeekNumbers: true,
                        dropdowns: {
                          minYear: 1990,
                          maxYear: null,
                          months: true,
                          years: true,
                        },
                      }"
                      class="form-control"
                    />
                  </div>
                  <div class="col-span-12 sm:col-span-6">
                    <label for="modal-datepicker-2" class="form-label"
                      >To</label
                    >
                    <Litepicker
                      id="modal-datepicker-2"
                      v-model="date"
                      :options="{
                        autoApply: false,
                        showWeekNumbers: true,
                        dropdowns: {
                          minYear: 1990,
                          maxYear: null,
                          months: true,
                          years: true,
                        },
                      }"
                      class="form-control"
                    />
                  </div>
                </ModalBody>
                <!-- END: Modal Body -->
                <!-- BEGIN: Modal Footer -->
                <ModalFooter class="text-right">
                  <button
                    type="button"
                    @click="datepickerModalPreview = false"
                    class="btn btn-outline-secondary w-20 mr-1"
                  >
                    Cancel
                  </button>
                  <button type="button" class="btn btn-primary w-20">
                    Submit
                  </button>
                </ModalFooter>
                <!-- END: Modal Footer -->
              </Modal>
              <!-- END: Modal Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Modal Datepicker -->
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const date = ref("");
const daterange = ref("");
const datepickerModalPreview = ref(false);
</script>
