<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Buttons</h2>
  </div>
  <div class="intro-y grid grid-cols-12 gap-6 mt-5">
    <div class="col-span-12 lg:col-span-6">
      <!-- BEGIN: Basic Button -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Basic Buttons</h2>
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
            <button class="btn btn-primary w-24 mr-1 mb-2">Primary</button>
            <button class="btn btn-secondary w-24 mr-1 mb-2">Secondary</button>
            <button class="btn btn-success w-24 mr-1 mb-2">Success</button>
            <button class="btn btn-warning w-24 mr-1 mb-2">Warning</button>
            <button class="btn btn-pending w-24 mr-1 mb-2">Pending</button>
            <button class="btn btn-danger w-24 mr-1 mb-2">Danger</button>
            <button class="btn btn-dark w-24 mr-1 mb-2">Dark</button>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <button class="btn btn-primary w-24 mr-1 mb-2">Primary</button>
              <button class="btn btn-secondary w-24 mr-1 mb-2">
                Secondary
              </button>
              <button class="btn btn-success w-24 mr-1 mb-2">Success</button>
              <button class="btn btn-warning w-24 mr-1 mb-2">Warning</button>
              <button class="btn btn-pending w-24 mr-1 mb-2">Pending</button>
              <button class="btn btn-danger w-24 mr-1 mb-2">Danger</button>
              <button class="btn btn-dark w-24 mr-1 mb-2">Dark</button>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Basic Button -->
      <!-- BEGIN: Button Size -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Button Sizes</h2>
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
            <div>
              <button class="btn btn-sm btn-primary w-24 mr-1 mb-2">
                Small
              </button>
              <button class="btn btn-primary w-24 mr-1 mb-2">Medium</button>
              <button class="btn btn-lg btn-primary w-24 mr-1 mb-2">
                Large
              </button>
            </div>
            <div class="mt-5">
              <button class="btn btn-sm btn-secondary w-24 mr-1 mb-2">
                Small
              </button>
              <button class="btn btn-secondary w-24 mr-1 mb-2">Medium</button>
              <button class="btn btn-lg btn-secondary w-24 mr-1 mb-2">
                Large
              </button>
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div>
                <button class="btn btn-sm btn-primary w-24 mr-1 mb-2">
                  Small
                </button>
                <button class="btn btn-primary w-24 mr-1 mb-2">Medium</button>
                <button class="btn btn-lg btn-primary w-24 mr-1 mb-2">
                  Large
                </button>
              </div>
              <div class="mt-5">
                <button class="btn btn-sm btn-secondary w-24 mr-1 mb-2">
                  Small
                </button>
                <button class="btn btn-secondary w-24 mr-1 mb-2">Medium</button>
                <button class="btn btn-lg btn-secondary w-24 mr-1 mb-2">
                  Large
                </button>
              </div>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Button Size -->
      <!-- BEGIN: Button Link -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Working with Links</h2>
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
            <a href="" class="btn btn-primary w-24 inline-block mr-1 mb-2"
              >Link</a
            >
            <a href="" class="btn btn-secondary w-24 inline-block mr-1 mb-2"
              >Button</a
            >
            <a href="" class="btn btn-success w-24 inline-block mr-1 mb-2"
              >Input</a
            >
            <a href="" class="btn btn-warning w-24 inline-block mr-1 mb-2"
              >Submit</a
            >
            <a href="" class="btn btn-pending w-24 inline-block mr-1 mb-2"
              >Pending</a
            >
            <a href="" class="btn btn-danger w-24 inline-block mr-1 mb-2"
              >Reset</a
            >
            <a href="" class="btn btn-dark w-24 inline-block mr-1 mb-2"
              >Metal</a
            >
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <a href="" class="btn btn-primary w-24 inline-block mr-1 mb-2"
                >Link</a
              >
              <a href="" class="btn btn-secondary w-24 inline-block mr-1 mb-2"
                >Button</a
              >
              <a href="" class="btn btn-success w-24 inline-block mr-1 mb-2"
                >Input</a
              >
              <a href="" class="btn btn-warning w-24 inline-block mr-1 mb-2"
                >Submit</a
              >
              <a href="" class="btn btn-pending w-24 inline-block mr-1 mb-2"
                >Pending</a
              >
              <a href="" class="btn btn-danger w-24 inline-block mr-1 mb-2"
                >Reset</a
              >
              <a href="" class="btn btn-dark w-24 inline-block mr-1 mb-2"
                >Metal</a
              >
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Button Link -->
      <!-- BEGIN: Elevated Button -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Elevated Buttons</h2>
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
            <div>
              <button class="btn btn-elevated-primary w-24 mr-1 mb-2">
                Primary
              </button>
              <button class="btn btn-elevated-secondary w-24 mr-1 mb-2">
                Secondary
              </button>
              <button class="btn btn-elevated-success w-24 mr-1 mb-2">
                Success
              </button>
              <button class="btn btn-elevated-warning w-24 mr-1 mb-2">
                Warning
              </button>
              <button class="btn btn-elevated-pending w-24 mr-1 mb-2">
                Pending
              </button>
              <button class="btn btn-elevated-danger w-24 mr-1 mb-2">
                Danger
              </button>
              <button class="btn btn-elevated-dark w-24 mr-1 mb-2">Dark</button>
            </div>
            <div class="mt-5">
              <button class="btn btn-elevated-rounded-primary w-24 mr-1 mb-2">
                Primary
              </button>
              <button class="btn btn-elevated-rounded-secondary w-24 mr-1 mb-2">
                Secondary
              </button>
              <button class="btn btn-elevated-rounded-success w-24 mr-1 mb-2">
                Success
              </button>
              <button class="btn btn-elevated-rounded-warning w-24 mr-1 mb-2">
                Warning
              </button>
              <button class="btn btn-elevated-rounded-pending w-24 mr-1 mb-2">
                Pending
              </button>
              <button class="btn btn-elevated-rounded-danger w-24 mr-1 mb-2">
                Danger
              </button>
              <button class="btn btn-elevated-rounded-dark w-24 mr-1 mb-2">
                Dark
              </button>
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div>
                <button class="btn btn-elevated-primary w-24 mr-1 mb-2">
                  Primary
                </button>
                <button class="btn btn-elevated-secondary w-24 mr-1 mb-2">
                  Secondary
                </button>
                <button class="btn btn-elevated-success w-24 mr-1 mb-2">
                  Success
                </button>
                <button class="btn btn-elevated-warning w-24 mr-1 mb-2">
                  Warning
                </button>
                <button class="btn btn-elevated-pending w-24 mr-1 mb-2">
                  Pending
                </button>
                <button class="btn btn-elevated-danger w-24 mr-1 mb-2">
                  Danger
                </button>
                <button class="btn btn-elevated-dark w-24 mr-1 mb-2">
                  Dark
                </button>
              </div>
              <div class="mt-5">
                <button class="btn btn-elevated-rounded-primary w-24 mr-1 mb-2">
                  Primary
                </button>
                <button
                  class="btn btn-elevated-rounded-secondary w-24 mr-1 mb-2"
                >
                  Secondary
                </button>
                <button class="btn btn-elevated-rounded-success w-24 mr-1 mb-2">
                  Success
                </button>
                <button class="btn btn-elevated-rounded-warning w-24 mr-1 mb-2">
                  Warning
                </button>
                <button class="btn btn-elevated-rounded-pending w-24 mr-1 mb-2">
                  Pending
                </button>
                <button class="btn btn-elevated-rounded-danger w-24 mr-1 mb-2">
                  Danger
                </button>
                <button class="btn btn-elevated-rounded-dark w-24 mr-1 mb-2">
                  Dark
                </button>
              </div>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Elevated Button -->
      <!-- BEGIN: Social Media Button -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Social Media Buttons</h2>
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
            <div class="flex flex-wrap">
              <button class="btn btn-facebook w-32 mr-2 mb-2">
                <FacebookIcon class="w-4 h-4 mr-2" /> Facebook
              </button>
              <button class="btn btn-twitter w-32 mr-2 mb-2">
                <TwitterIcon class="w-4 h-4 mr-2" /> Twitter
              </button>
              <button class="btn btn-instagram w-32 mr-2 mb-2">
                <InstagramIcon class="w-4 h-4 mr-2" /> Instagram
              </button>
              <button class="btn btn-linkedin w-32 mr-2 mb-2">
                <LinkedinIcon class="w-4 h-4 mr-2" /> Linkedin
              </button>
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <button class="btn btn-facebook w-32 mr-2 mb-2">
                <FacebookIcon class="w-4 h-4 mr-2" /> Facebook
              </button>
              <button class="btn btn-twitter w-32 mr-2 mb-2">
                <TwitterIcon class="w-4 h-4 mr-2" /> Twitter
              </button>
              <button class="btn btn-instagram w-32 mr-2 mb-2">
                <InstagramIcon class="w-4 h-4 mr-2" /> Instagram
              </button>
              <button class="btn btn-linkedin w-32 mr-2 mb-2">
                <LinkedinIcon class="w-4 h-4 mr-2" /> Linkedin
              </button>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Social Media Button -->
    </div>
    <div class="col-span-12 lg:col-span-6">
      <!-- BEGIN: Outline Button -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Outline Buttons</h2>
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
            <button class="btn btn-outline-primary w-24 inline-block mr-1 mb-2">
              Primary
            </button>
            <button
              class="btn btn-outline-secondary w-24 inline-block mr-1 mb-2"
            >
              Secondary
            </button>
            <button class="btn btn-outline-success w-24 inline-block mr-1 mb-2">
              Success
            </button>
            <button class="btn btn-outline-warning w-24 inline-block mr-1 mb-2">
              Warning
            </button>
            <button class="btn btn-outline-pending w-24 inline-block mr-1 mb-2">
              Pending
            </button>
            <button class="btn btn-outline-danger w-24 inline-block mr-1 mb-2">
              Danger
            </button>
            <button class="btn btn-outline-dark w-24 inline-block mr-1 mb-2">
              Dark
            </button>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <button
                class="btn btn-outline-primary w-24 inline-block mr-1 mb-2"
              >
                Primary
              </button>
              <button
                class="btn btn-outline-secondary w-24 inline-block mr-1 mb-2"
              >
                Secondary
              </button>
              <button
                class="btn btn-outline-success w-24 inline-block mr-1 mb-2"
              >
                Success
              </button>
              <button
                class="btn btn-outline-warning w-24 inline-block mr-1 mb-2"
              >
                Warning
              </button>
              <button
                class="btn btn-outline-pending w-24 inline-block mr-1 mb-2"
              >
                Pending
              </button>
              <button
                class="btn btn-outline-danger w-24 inline-block mr-1 mb-2"
              >
                Danger
              </button>
              <button class="btn btn-outline-dark w-24 inline-block mr-1 mb-2">
                Dark
              </button>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Outline Button -->
      <!-- BEGIN: Loading Button -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Loading State Buttons</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-7"
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
            <button class="btn btn-primary mr-1 mb-2">
              Saving
              <LoadingIcon icon="oval" color="white" class="w-4 h-4 ml-2" />
            </button>
            <button class="btn btn-success mr-1 mb-2">
              Adding
              <LoadingIcon
                icon="spinning-circles"
                color="white"
                class="w-4 h-4 ml-2"
              />
            </button>
            <button class="btn btn-warning mr-1 mb-2">
              Loading
              <LoadingIcon
                icon="three-dots"
                color="1a202c"
                class="w-4 h-4 ml-2"
              />
            </button>
            <button class="btn btn-danger mr-1 mb-2">
              Deleting
              <LoadingIcon icon="puff" color="white" class="w-4 h-4 ml-2" />
            </button>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <button class="btn btn-primary mr-1 mb-2">
                Saving
                <LoadingIcon icon="oval" color="white" class="w-4 h-4 ml-2" />
              </button>
              <button class="btn btn-success mr-1 mb-2">
                Adding
                <LoadingIcon
                  icon="spinning-circles"
                  color="white"
                  class="w-4 h-4 ml-2"
                />
              </button>
              <button class="btn btn-warning mr-1 mb-2">
                Loading
                <LoadingIcon
                  icon="three-dots"
                  color="1a202c"
                  class="w-4 h-4 ml-2"
                />
              </button>
              <button class="btn btn-danger mr-1 mb-2">
                Deleting
                <LoadingIcon icon="puff" color="white" class="w-4 h-4 ml-2" />
              </button>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Loading Button -->
      <!-- BEGIN: Rounded Button -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Rounded Buttons</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-8"
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
            <button class="btn btn-rounded-primary w-24 mr-1 mb-2">
              Primary
            </button>
            <button class="btn btn-rounded-secondary w-24 mr-1 mb-2">
              Secondary
            </button>
            <button class="btn btn-rounded-success w-24 mr-1 mb-2">
              Success
            </button>
            <button class="btn btn-rounded-warning w-24 mr-1 mb-2">
              Warning
            </button>
            <button class="btn btn-rounded-pending w-24 mr-1 mb-2">
              Pending
            </button>
            <button class="btn btn-rounded-danger w-24 mr-1 mb-2">
              Danger
            </button>
            <button class="btn btn-rounded-dark w-24 mr-1 mb-2">Dark</button>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <button class="btn btn-rounded-primary w-24 mr-1 mb-2">
                Primary
              </button>
              <button class="btn btn-rounded-secondary w-24 mr-1 mb-2">
                Secondary
              </button>
              <button class="btn btn-rounded-success w-24 mr-1 mb-2">
                Success
              </button>
              <button class="btn btn-rounded-warning w-24 mr-1 mb-2">
                Warning
              </button>
              <button class="btn btn-rounded-pending w-24 mr-1 mb-2">
                Pending
              </button>
              <button class="btn btn-rounded-danger w-24 mr-1 mb-2">
                Danger
              </button>
              <button class="btn btn-rounded-dark w-24 mr-1 mb-2">Dark</button>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Rounded Button -->
      <!-- BEGIN: Soft Color Button -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Soft Color Buttons</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-9"
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
            <button class="btn btn-rounded btn-primary-soft w-24 mr-1 mb-2">
              Primary
            </button>
            <button class="btn btn-rounded btn-secondary-soft w-24 mr-1 mb-2">
              Secondary
            </button>
            <button class="btn btn-rounded btn-success-soft w-24 mr-1 mb-2">
              Success
            </button>
            <button class="btn btn-rounded btn-warning-soft w-24 mr-1 mb-2">
              Warning
            </button>
            <button class="btn btn-rounded btn-pending-soft w-24 mr-1 mb-2">
              Pending
            </button>
            <button class="btn btn-rounded btn-danger-soft w-24 mr-1 mb-2">
              Danger
            </button>
            <button class="btn btn-rounded btn-dark-soft w-24 mr-1 mb-2">
              Dark
            </button>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <button class="btn btn-rounded btn-primary-soft w-24 mr-1 mb-2">
                Primary
              </button>
              <button class="btn btn-rounded btn-secondary-soft w-24 mr-1 mb-2">
                Secondary
              </button>
              <button class="btn btn-rounded btn-success-soft w-24 mr-1 mb-2">
                Success
              </button>
              <button class="btn btn-rounded btn-warning-soft w-24 mr-1 mb-2">
                Warning
              </button>
              <button class="btn btn-rounded btn-pending-soft w-24 mr-1 mb-2">
                Pending
              </button>
              <button class="btn btn-rounded btn-danger-soft w-24 mr-1 mb-2">
                Danger
              </button>
              <button class="btn btn-rounded btn-dark-soft w-24 mr-1 mb-2">
                Dark
              </button>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Soft Color Button -->
      <!-- BEGIN: Icon Button -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Icon Buttons</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-10"
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
            <div class="flex flex-wrap">
              <button class="btn btn-primary w-32 mr-2 mb-2">
                <ActivityIcon class="w-4 h-4 mr-2" /> Activity
              </button>
              <button class="btn btn-secondary w-32 mr-2 mb-2">
                <HardDriveIcon class="w-4 h-4 mr-2" /> Hard Drive
              </button>
              <button class="btn btn-success w-32 mr-2 mb-2">
                <CalendarIcon class="w-4 h-4 mr-2" /> Calendar
              </button>
              <button class="btn btn-warning w-32 mr-2 mb-2">
                <Share2Icon class="w-4 h-4 mr-2" /> Share
              </button>
              <button class="btn btn-pending w-32 mr-2 mb-2">
                <DownloadIcon class="w-4 h-4 mr-2" /> Pending
              </button>
              <button class="btn btn-danger w-32 mr-2 mb-2">
                <TrashIcon class="w-4 h-4 mr-2" /> Trash
              </button>
              <button class="btn btn-dark w-32 mr-2 mb-2">
                <ImageIcon class="w-4 h-4 mr-2" /> Image
              </button>
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <button class="btn btn-primary w-32 mr-2 mb-2">
                <ActivityIcon class="w-4 h-4 mr-2" /> Activity
              </button>
              <button class="btn btn-secondary w-32 mr-2 mb-2">
                <HardDriveIcon class="w-4 h-4 mr-2" /> Hard Drive
              </button>
              <button class="btn btn-success w-32 mr-2 mb-2">
                <CalendarIcon class="w-4 h-4 mr-2" /> Calendar
              </button>
              <button class="btn btn-warning w-32 mr-2 mb-2">
                <Share2Icon class="w-4 h-4 mr-2" /> Share
              </button>
              <button class="btn btn-pending w-32 mr-2 mb-2">
                <DownloadIcon class="w-4 h-4 mr-2" /> Pending
              </button>
              <button class="btn btn-danger w-32 mr-2 mb-2">
                <TrashIcon class="w-4 h-4 mr-2" /> Trash
              </button>
              <button class="btn btn-dark w-32 mr-2 mb-2">
                <ImageIcon class="w-4 h-4 mr-2" /> Image
              </button>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Icon Button -->
      <!-- BEGIN: Icon Only Button -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Icon Only Buttons</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-11"
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
            <button class="btn btn-primary mr-1 mb-2">
              <ActivityIcon class="w-5 h-5" />
            </button>
            <button class="btn btn-secondary mr-1 mb-2">
              <HardDriveIcon class="w-5 h-5" />
            </button>
            <button class="btn btn-success mr-1 mb-2">
              <CalendarIcon class="w-5 h-5" />
            </button>
            <button class="btn btn-warning mr-1 mb-2">
              <Share2Icon class="w-5 h-5" />
            </button>
            <button class="btn btn-pending mr-1 mb-2">
              <DownloadIcon class="w-5 h-5" />
            </button>
            <button class="btn btn-danger mr-1 mb-2">
              <TrashIcon class="w-5 h-5" />
            </button>
            <button class="btn btn-dark mr-1 mb-2">
              <ImageIcon class="w-5 h-5" />
            </button>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <button class="btn btn-primary mr-1 mb-2">
                <ActivityIcon class="w-5 h-5" />
              </button>
              <button class="btn btn-secondary mr-1 mb-2">
                <HardDriveIcon class="w-5 h-5" />
              </button>
              <button class="btn btn-success mr-1 mb-2">
                <CalendarIcon class="w-5 h-5" />
              </button>
              <button class="btn btn-warning mr-1 mb-2">
                <Share2Icon class="w-5 h-5" />
              </button>
              <button class="btn btn-pending mr-1 mb-2">
                <DownloadIcon class="w-5 h-5" />
              </button>
              <button class="btn btn-danger mr-1 mb-2">
                <TrashIcon class="w-5 h-5" />
              </button>
              <button class="btn btn-dark mr-1 mb-2">
                <ImageIcon class="w-5 h-5" />
              </button>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Icon Only Button -->
    </div>
  </div>
</template>
