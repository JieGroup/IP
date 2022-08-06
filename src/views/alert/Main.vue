<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Alert</h2>
  </div>
  <div class="intro-y grid grid-cols-12 gap-6 mt-5">
    <div class="col-span-12 lg:col-span-6">
      <!-- BEGIN: Basic Alert -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Basic Alerts</h2>
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
            <Alert class="alert-primary mb-2"> Awesome simple alert </Alert>
            <Alert class="alert-secondary mb-2"> Awesome simple alert </Alert>
            <Alert class="alert-success mb-2"> Awesome simple alert </Alert>
            <Alert class="alert-warning mb-2"> Awesome simple alert </Alert>
            <Alert class="alert-pending mb-2"> Awesome simple alert </Alert>
            <Alert class="alert-danger mb-2"> Awesome simple alert </Alert>
            <Alert class="alert-dark mb-2"> Awesome simple alert </Alert>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Alert class="alert-primary mb-2"> Awesome simple alert </Alert>
              <Alert class="alert-secondary mb-2"> Awesome simple alert </Alert>
              <Alert class="alert-success mb-2"> Awesome simple alert </Alert>
              <Alert class="alert-warning mb-2"> Awesome simple alert </Alert>
              <Alert class="alert-pending mb-2"> Awesome simple alert </Alert>
              <Alert class="alert-danger mb-2"> Awesome simple alert </Alert>
              <Alert class="alert-dark mb-2"> Awesome simple alert </Alert>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Basic Alert -->
      <!-- BEGIN: Icon's Alert -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Icon Alerts</h2>
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
            <Alert class="alert-primary flex items-center mb-2">
              <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
            <Alert class="alert-secondary flex items-center mb-2">
              <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
            <Alert class="alert-success flex items-center mb-2">
              <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
            <Alert class="alert-warning flex items-center mb-2">
              <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
            <Alert class="alert-pending flex items-center mb-2">
              <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
            <Alert class="alert-danger flex items-center mb-2">
              <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
            <Alert class="alert-dark flex items-center mb-2">
              <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Alert class="alert-primary flex items-center mb-2">
                <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              </Alert>
              <Alert class="alert-secondary flex items-center mb-2">
                <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
              </Alert>
              <Alert class="alert-success flex items-center mb-2">
                <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
              </Alert>
              <Alert class="alert-warning flex items-center mb-2">
                <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              </Alert>
              <Alert class="alert-pending flex items-center mb-2">
                <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
              </Alert>
              <Alert class="alert-danger flex items-center mb-2">
                <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
              </Alert>
              <Alert class="alert-dark flex items-center mb-2">
                <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
              </Alert>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Icon's Alert -->
      <!-- BEGIN: Additional Content Alert -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Additional Content Alerts
          </h2>
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
            <Alert class="alert-primary mb-2">
              <div class="flex items-center">
                <div class="font-medium text-lg">
                  Awesome alert with additional info
                </div>
                <div
                  class="text-xs bg-white px-1 rounded-md text-slate-700 ml-auto"
                >
                  New
                </div>
              </div>
              <div class="mt-3">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever since the 1500s.
              </div>
            </Alert>
            <Alert class="alert-secondary mb-2">
              <div class="flex items-center">
                <div class="font-medium text-lg">
                  Awesome alert with additional info
                </div>
                <div
                  class="text-xs bg-slate-500 px-1 rounded-md text-white ml-auto"
                >
                  New
                </div>
              </div>
              <div class="mt-3">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever since the 1500s.
              </div>
            </Alert>
            <Alert class="alert-success mb-2">
              <div class="flex items-center">
                <div class="font-medium text-lg">
                  Awesome alert with additional info
                </div>
                <div
                  class="text-xs bg-white px-1 rounded-md text-slate-700 ml-auto"
                >
                  New
                </div>
              </div>
              <div class="mt-3">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever since the 1500s.
              </div>
            </Alert>
            <Alert class="alert-warning mb-2">
              <div class="flex items-center">
                <div class="font-medium text-lg">
                  Awesome alert with additional info
                </div>
                <div
                  class="text-xs bg-white px-1 rounded-md text-slate-700 ml-auto"
                >
                  New
                </div>
              </div>
              <div class="mt-3">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever since the 1500s.
              </div>
            </Alert>
            <Alert class="alert-pending mb-2">
              <div class="flex items-center">
                <div class="font-medium text-lg">
                  Awesome alert with additional info
                </div>
                <div
                  class="text-xs bg-white px-1 rounded-md text-slate-700 ml-auto"
                >
                  New
                </div>
              </div>
              <div class="mt-3">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever since the 1500s.
              </div>
            </Alert>
            <Alert class="alert-danger mb-2">
              <div class="flex items-center">
                <div class="font-medium text-lg">
                  Awesome alert with additional info
                </div>
                <div
                  class="text-xs bg-white px-1 rounded-md text-slate-700 ml-auto"
                >
                  New
                </div>
              </div>
              <div class="mt-3">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever since the 1500s.
              </div>
            </Alert>
            <Alert class="alert-dark mb-2">
              <div class="flex items-center">
                <div class="font-medium text-lg">
                  Awesome alert with additional info
                </div>
                <div
                  class="text-xs bg-slate-500 px-1 rounded-md text-white ml-auto"
                >
                  New
                </div>
              </div>
              <div class="mt-3">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever since the 1500s.
              </div>
            </Alert>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Alert class="alert-primary mb-2">
                <div class="flex items-center">
                  <div class="font-medium text-lg">
                    Awesome alert with additional info
                  </div>
                  <div
                    class="text-xs bg-white px-1 rounded-md text-slate-700 ml-auto"
                  >
                    New
                  </div>
                </div>
                <div class="mt-3">
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s.
                </div>
              </Alert>
              <Alert class="alert-secondary mb-2">
                <div class="flex items-center">
                  <div class="font-medium text-lg">
                    Awesome alert with additional info
                  </div>
                  <div
                    class="text-xs bg-slate-500 px-1 rounded-md text-white ml-auto"
                  >
                    New
                  </div>
                </div>
                <div class="mt-3">
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s.
                </div>
              </Alert>
              <Alert class="alert-success mb-2">
                <div class="flex items-center">
                  <div class="font-medium text-lg">
                    Awesome alert with additional info
                  </div>
                  <div
                    class="text-xs bg-white px-1 rounded-md text-slate-700 ml-auto"
                  >
                    New
                  </div>
                </div>
                <div class="mt-3">
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s.
                </div>
              </Alert>
              <Alert class="alert-warning mb-2">
                <div class="flex items-center">
                  <div class="font-medium text-lg">
                    Awesome alert with additional info
                  </div>
                  <div
                    class="text-xs bg-white px-1 rounded-md text-slate-700 ml-auto"
                  >
                    New
                  </div>
                </div>
                <div class="mt-3">
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s.
                </div>
              </Alert>
              <Alert class="alert-pending mb-2">
                <div class="flex items-center">
                  <div class="font-medium text-lg">
                    Awesome alert with additional info
                  </div>
                  <div
                    class="text-xs bg-white px-1 rounded-md text-slate-700 ml-auto"
                  >
                    New
                  </div>
                </div>
                <div class="mt-3">
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s.
                </div>
              </Alert>
              <Alert class="alert-danger mb-2">
                <div class="flex items-center">
                  <div class="font-medium text-lg">
                    Awesome alert with additional info
                  </div>
                  <div
                    class="text-xs bg-white px-1 rounded-md text-slate-700 ml-auto"
                  >
                    New
                  </div>
                </div>
                <div class="mt-3">
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s.
                </div>
              </Alert>
              <Alert class="alert-dark mb-2">
                <div class="flex items-center">
                  <div class="font-medium text-lg">
                    Awesome alert with additional info
                  </div>
                  <div
                    class="text-xs bg-slate-500 px-1 rounded-md text-white ml-auto"
                  >
                    New
                  </div>
                </div>
                <div class="mt-3">
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s.
                </div>
              </Alert>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Additional Content Alert -->
      <!-- BEGIN: Icon & Dismiss Alert -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Icon & Dismiss Alerts</h2>
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
            <Alert
              class="alert-primary flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close text-white"
                aria-label="Close"
                @click="dismiss"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
            <Alert
              class="alert-secondary flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close"
                aria-label="Close"
                @click="dismiss"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
            <Alert
              class="alert-success flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close"
                aria-label="Close"
                @click="dismiss"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
            <Alert
              class="alert-warning flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close"
                aria-label="Close"
                @click="dismiss"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
            <Alert
              class="alert-pending flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close"
                aria-label="Close"
                @click="dismiss"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
            <Alert
              class="alert-danger flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close text-white"
                aria-label="Close"
                @click="dismiss"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
            <Alert
              class="alert-dark flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close text-white"
                aria-label="Close"
                @click="dismiss"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Alert
                class="alert-primary flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
                <button
                  type="button"
                  class="btn-close text-white"
                  aria-label="Close"
                  @click="dismiss"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              <Alert
                class="alert-secondary flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
                <button
                  type="button"
                  class="btn-close"
                  aria-label="Close"
                  @click="dismiss"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              <Alert
                class="alert-success flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
                <button
                  type="button"
                  class="btn-close"
                  aria-label="Close"
                  @click="dismiss"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              <Alert
                class="alert-warning flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
                <button
                  type="button"
                  class="btn-close"
                  aria-label="Close"
                  @click="dismiss"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              <Alert
                class="alert-pending flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
                <button
                  type="button"
                  class="btn-close"
                  aria-label="Close"
                  @click="dismiss"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              <Alert
                class="alert-danger flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
                <button
                  type="button"
                  class="btn-close text-white"
                  aria-label="Close"
                  @click="dismiss"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              <Alert
                class="alert-dark flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
                <button
                  type="button"
                  class="btn-close text-white"
                  aria-label="Close"
                  @click="dismiss"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Icon & Dismiss Alert -->
      <!-- BEGIN: Outline Alert -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Outline Alerts</h2>
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
            <Alert
              class="alert-outline-primary flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close"
                @click="dismiss"
                aria-label="Close"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
            <Alert
              class="alert-outline-secondary flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close"
                @click="dismiss"
                aria-label="Close"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
            <Alert
              class="alert-outline-success flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close"
                @click="dismiss"
                aria-label="Close"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
            <Alert
              class="alert-outline-warning flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close"
                @click="dismiss"
                aria-label="Close"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
            <Alert
              class="alert-outline-pending flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close"
                @click="dismiss"
                aria-label="Close"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
            <Alert
              class="alert-outline-danger flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close"
                @click="dismiss"
                aria-label="Close"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
            <Alert
              class="alert-outline-dark flex items-center mb-2"
              v-slot="{ dismiss }"
            >
              <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              <button
                type="button"
                class="btn-close"
                @click="dismiss"
                aria-label="Close"
              >
                <XIcon class="w-4 h-4" />
              </button>
            </Alert>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Alert
                class="alert-outline-primary flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
                <button
                  type="button"
                  class="btn-close"
                  @click="dismiss"
                  aria-label="Close"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              <Alert
                class="alert-outline-secondary flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
                <button
                  type="button"
                  class="btn-close"
                  @click="dismiss"
                  aria-label="Close"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              <Alert
                class="alert-outline-success flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
                <button
                  type="button"
                  class="btn-close"
                  @click="dismiss"
                  aria-label="Close"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              <Alert
                class="alert-outline-warning flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
                <button
                  type="button"
                  class="btn-close"
                  @click="dismiss"
                  aria-label="Close"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              <Alert
                class="alert-outline-pending flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
                <button
                  type="button"
                  class="btn-close"
                  @click="dismiss"
                  aria-label="Close"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              <Alert
                class="alert-outline-danger flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
                <button
                  type="button"
                  class="btn-close"
                  @click="dismiss"
                  aria-label="Close"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              <Alert
                class="alert-outline-dark flex items-center mb-2"
                v-slot="{ dismiss }"
              >
                <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
                <button
                  type="button"
                  class="btn-close"
                  @click="dismiss"
                  aria-label="Close"
                >
                  <XIcon class="w-4 h-4" />
                </button>
              </Alert>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Outline Alert -->
      <!-- BEGIN: Soft Color Alert -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Soft Color Alerts</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-6"
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
            <Alert class="alert-primary-soft flex items-center mb-2">
              <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
            <Alert class="alert-secondary-soft flex items-center mb-2">
              <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
            <Alert class="alert-success-soft flex items-center mb-2">
              <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
            <Alert class="alert-warning-soft flex items-center mb-2">
              <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
            <Alert class="alert-pending-soft flex items-center mb-2">
              <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
            <Alert class="alert-danger-soft flex items-center mb-2">
              <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
            <Alert class="alert-dark-soft flex items-center mb-2">
              <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
            </Alert>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Alert class="alert-primary-soft flex items-center mb-2">
                <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              </Alert>
              <Alert class="alert-secondary-soft flex items-center mb-2">
                <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
              </Alert>
              <Alert class="alert-success-soft flex items-center mb-2">
                <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
              </Alert>
              <Alert class="alert-warning-soft flex items-center mb-2">
                <AlertCircleIcon class="w-6 h-6 mr-2" /> Awesome alert with icon
              </Alert>
              <Alert class="alert-pending-soft flex items-center mb-2">
                <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
              </Alert>
              <Alert class="alert-danger-soft flex items-center mb-2">
                <AlertOctagonIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
              </Alert>
              <Alert class="alert-dark-soft flex items-center mb-2">
                <AlertTriangleIcon class="w-6 h-6 mr-2" /> Awesome alert with
                icon
              </Alert>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Soft Color Alert -->
    </div>
    <div class="col-span-12 lg:col-span-6">
      <!-- BEGIN: Component Reference -->
      <div class="intro-y box">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Component Reference</h2>
        </div>
        <div class="p-5">
          <div>
            Alert are built using the
            <span class="text-red-500">`Alert`</span> components.
          </div>
        </div>
      </div>
      <!-- END: Component Reference -->
      <!-- BEGIN: Component API -->
      <div class="intro-y box mt-5">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Component API</h2>
        </div>
        <div class="p-5">
          <div class="text-base font-medium">Alert</div>
          <div class="mt-2">The main Alert component.</div>
          <table class="table mt-5">
            <thead>
              <tr>
                <th class="whitespace-nowrap w-24">Prop</th>
                <th class="whitespace-nowrap">Values</th>
                <th class="whitespace-nowrap">Default</th>
                <th class="whitespace-nowrap">Description</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="align-top text-red-500">`show`</td>
                <td class="align-top">`true`, `false`</td>
                <td class="align-top">`false`</td>
                <td class="align-top">
                  <div class="font-medium mb-1">`Boolean`</div>
                  Whether the Alert is open or not.
                </td>
              </tr>
            </tbody>
          </table>
          <table class="table mt-5">
            <thead>
              <tr>
                <th class="whitespace-nowrap w-24">Event</th>
                <th class="whitespace-nowrap">Description</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="align-top text-red-500">`show`</td>
                <td class="align-top">
                  This event fires immediately when the
                  <span class="text-red-500">show</span> instance method is
                  called.
                </td>
              </tr>
              <tr>
                <td class="align-top text-red-500">`shown`</td>
                <td class="align-top">
                  This event is fired when the alert has been made visible to
                  the user (will wait for CSS transitions to complete)
                </td>
              </tr>
              <tr>
                <td class="align-top text-red-500">`hide`</td>
                <td class="align-top">
                  This event is fired immediately when the
                  <span class="text-red-500">hide</span> instance method has
                  been called.
                </td>
              </tr>
              <tr>
                <td class="align-top text-red-500">`hidden`</td>
                <td class="align-top">
                  This event is fired when the alert has finished being hidden
                  from the user (will wait for CSS transitions to complete).
                </td>
              </tr>
            </tbody>
          </table>
          <table class="table mt-5">
            <thead>
              <tr>
                <th class="whitespace-nowrap w-24">Slot Prop</th>
                <th class="whitespace-nowrap">Description</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="align-top text-red-500">`dismiss`</td>
                <td class="align-top">Manually hides an alert.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <!-- END: Component API -->
    </div>
  </div>
</template>
