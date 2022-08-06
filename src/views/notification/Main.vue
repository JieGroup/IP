<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Notification</h2>
  </div>
  <div class="grid grid-cols-12 gap-6 mt-5">
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- BEGIN: Basic Notification -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Basic Notification</h2>
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
              <!-- BEGIN: Basic Non Sticky Notification Content -->
              <Notification
                refKey="basicNonStickyNotification"
                :options="{
                  duration: 3000,
                }"
                class="flex flex-col sm:flex-row"
              >
                <div class="font-medium">Yay! Updates Published!</div>
                <a
                  class="font-medium text-primary dark:text-slate-400 mt-1 sm:mt-0 sm:ml-40"
                  href=""
                  >Review Changes</a
                >
              </Notification>
              <!-- END: Basic Non Sticky Notification Content -->
              <!-- BEGIN: Basic Sticky Notification Content -->
              <Notification
                refKey="basicStickyNotification"
                class="flex flex-col sm:flex-row"
              >
                <div class="font-medium">Yay! Updates Published!</div>
                <a
                  class="font-medium text-primary dark:text-slate-400 mt-1 sm:mt-0 sm:ml-40"
                  href=""
                  >Review Changes</a
                >
              </Notification>
              <!-- END: Basic Sticky Notification Content -->
              <!-- BEGIN: Notification Toggle -->
              <button
                class="btn btn-primary mr-1"
                @click="basicNonStickyNotificationToggle"
              >
                Show Non Sticky Notification
              </button>
              <button
                class="btn btn-primary mt-2 sm:mt-0"
                @click="basicStickyNotificationToggle"
              >
                Show Sticky Notification
              </button>
              <!-- END: Notification Toggle -->
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Basic Non Sticky Notification Content -->
              <Notification
                refKey="basicNonStickyNotification"
                :options="{
                  duration: 3000,
                }"
                class="flex flex-col sm:flex-row"
              >
                <div class="font-medium">Yay! Updates Published!</div>
                <a
                  class="font-medium text-primary dark:text-slate-400 mt-1 sm:mt-0 sm:ml-40"
                  href=""
                  >Review Changes</a
                >
              </Notification>
              <!-- END: Basic Non Sticky Notification Content -->
              <!-- BEGIN: Basic Sticky Notification Content -->
              <Notification
                refKey="basicStickyNotification"
                class="flex flex-col sm:flex-row"
              >
                <div class="font-medium">Yay! Updates Published!</div>
                <a
                  class="font-medium text-primary dark:text-slate-400 mt-1 sm:mt-0 sm:ml-40"
                  href=""
                  >Review Changes</a
                >
              </Notification>
              <!-- END: Basic Sticky Notification Content -->
              <!-- BEGIN: Notification Toggle -->
              <button
                class="btn btn-primary mr-1"
                @click="basicNonStickyNotificationToggle"
              >
                Show Non Sticky Notification
              </button>
              <button
                class="btn btn-primary mt-2 sm:mt-0"
                @click="basicStickyNotificationToggle"
              >
                Show Sticky Notification
              </button>
              <!-- END: Notification Toggle -->
              ` }}
            </Highlight>
            <Highlight type="javascript" class="mt-5">
              {{
                `
                // Basic non sticky notification
                const basicNonStickyNotification = ref();
                provide("bind[basicNonStickyNotification]", (el) => {
                  // Binding
                  basicNonStickyNotification.value = el;
                });
                const basicNonStickyNotificationToggle = () => {
                  // Show notification
                  basicNonStickyNotification.value.showToast();
                };

                // Basic sticky notification
                const basicStickyNotification = ref();
                provide("bind[basicStickyNotification]", (el) => {
                  // Binding
                  basicStickyNotification.value = el;
                });
                const basicStickyNotificationToggle = () => {
                  // Show notification
                  basicStickyNotification.value.showToast();
                };
                `
              }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Basic Notification -->
      <!-- BEGIN: Success Notification -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Success Notification</h2>
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
              <!-- BEGIN: Notification Content -->
              <Notification refKey="successNotification" class="flex">
                <CheckCircleIcon class="text-success" />
                <div class="ml-4 mr-4">
                  <div class="font-medium">Message Saved!</div>
                  <div class="text-slate-500 mt-1">
                    The message will be sent in 5 minutes.
                  </div>
                </div>
              </Notification>
              <!-- END: Notification Content -->
              <!-- BEGIN: Notification Toggle -->
              <button
                class="btn btn-primary"
                @click="successNotificationToggle"
              >
                Show Notification
              </button>
              <!-- END: Notification Toggle -->
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Notification Content -->
              <Notification refKey="successNotification" class="flex">
                <CheckCircleIcon class="text-success" />
                <div class="ml-4 mr-4">
                  <div class="font-medium">Message Saved!</div>
                  <div class="text-slate-500 mt-1">
                    The message will be sent in 5 minutes.
                  </div>
                </div>
              </Notification>
              <!-- END: Notification Content -->
              <!-- BEGIN: Notification Toggle -->
              <button
                class="btn btn-primary"
                @click="successNotificationToggle"
              >
                Show Notification
              </button>
              <!-- END: Notification Toggle -->
              ` }}
            </Highlight>
            <Highlight type="javascript" class="mt-5">
              {{
                `
                // Success notification
                const successNotification = ref();
                provide("bind[successNotification]", (el) => {
                  // Binding
                  successNotification.value = el;
                });
                const successNotificationToggle = () => {
                  // Show notification
                  successNotification.value.showToast();
                };
                `
              }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Success Notification -->
      <!-- BEGIN: Notification With Actions -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Notification With Actions
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
            <div class="text-center">
              <!-- BEGIN: Notification Content -->
              <Notification refKey="notificationWithActions" class="flex">
                <HardDriveIcon />
                <div class="ml-4 mr-4">
                  <div class="font-medium">Storage Removed!</div>
                  <div class="text-slate-500 mt-1">
                    The server will restart in 30 seconds, don't make<br />
                    changes during the update process!
                  </div>
                  <div class="font-medium flex mt-1.5">
                    <a class="text-primary dark:text-slate-400" href=""
                      >Restart Now</a
                    >
                    <a class="text-slate-500 ml-3" href="">Cancel</a>
                  </div>
                </div>
              </Notification>
              <!-- END: Notification Content -->
              <!-- BEGIN: Notification Toggle -->
              <button
                class="btn btn-primary"
                @click="notificationWithActionsToggle"
              >
                Show Notification
              </button>
              <!-- END: Notification Toggle -->
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Notification Content -->
              <Notification refKey="notificationWithActions" class="flex">
                <HardDriveIcon />
                <div class="ml-4 mr-4">
                  <div class="font-medium">Storage Removed!</div>
                  <div class="text-slate-500 mt-1">
                    The server will restart in 30 seconds, don't make<br />
                    changes during the update process!
                  </div>
                  <div class="font-medium flex mt-1.5">
                    <a class="text-primary dark:text-slate-400" href=""
                      >Restart Now</a
                    >
                    <a class="text-slate-500 ml-3" href="">Cancel</a>
                  </div>
                </div>
              </Notification>
              <!-- END: Notification Content -->
              <!-- BEGIN: Notification Toggle -->
              <button
                class="btn btn-primary"
                @click="notificationWithActionsToggle"
              >
                Show Notification
              </button>
              <!-- END: Notification Toggle -->
              ` }}
            </Highlight>
            <Highlight type="javascript" class="mt-5">
              {{
                `
                // Notification with actions
                const notificationWithActions = ref();
                provide("bind[notificationWithActions]", (el) => {
                  // Binding
                  notificationWithActions.value = el;
                });
                const notificationWithActionsToggle = () => {
                  // Show notification
                  notificationWithActions.value.showToast();
                };
                `
              }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
    </div>
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- END: Notification With Actions -->
      <!-- BEGIN: Notification With Avatar -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Notification With Avatar
          </h2>
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
            <div class="text-center">
              <!-- BEGIN: Notification Content -->
              <Notification
                refKey="notificationWithAvatar"
                :options="{
                  close: false,
                }"
                class="flex"
              >
                <div
                  class="w-10 h-10 flex-none image-fit rounded-full overflow-hidden"
                >
                  <img
                    alt="Midone Tailwind HTML Admin Template"
                    :src="$f()[0].photos[0]"
                  />
                </div>
                <div class="ml-4 sm:mr-28">
                  <div class="font-medium">
                    {{ $f()[0].users[0].name }}
                  </div>
                  <div class="text-slate-500 mt-1">See you later! 😃😃😃</div>
                </div>
                <a
                  data-dismiss="notification"
                  class="absolute top-0 bottom-0 right-0 flex items-center px-6 border-l border-slate-200/60 dark:border-darkmode-400 font-medium text-primary dark:text-slate-400"
                  href="javascript:;"
                  >Reply</a
                >
              </Notification>
              <!-- END: Notification Content -->
              <!-- BEGIN: Notification Toggle -->
              <button
                class="btn btn-primary"
                @click="notificationWithAvatarToggle"
              >
                Show Notification
              </button>
              <!-- END: Notification Toggle -->
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Notification Content -->
              <Notification
                refKey="notificationWithAvatar"
                :options="{
                  close: false,
                }"
                class="flex"
              >
                <div
                  class="w-10 h-10 flex-none image-fit rounded-full overflow-hidden"
                >
                  <img
                    alt="Midone Tailwind HTML Admin Template"
                    :src="$f()[0].photos[0]"
                  />
                </div>
                <div class="ml-4 sm:mr-28">
                  <div class="font-medium">\{\{ $f()[0].users[0].name \}\}</div>
                  <div class="text-slate-500 mt-1">See you later! 😃😃😃</div>
                </div>
                <a
                  data-dismiss="notification"
                  class="absolute top-0 bottom-0 right-0 flex items-center px-6 border-l border-slate-200/60 dark:border-darkmode-400 font-medium text-primary dark:text-slate-400"
                  href="javascript:;"
                  >Reply</a
                >
              </Notification>
              <!-- END: Notification Content -->
              <!-- BEGIN: Notification Toggle -->
              <button
                class="btn btn-primary"
                @click="notificationWithAvatarToggle"
              >
                Show Notification
              </button>
              <!-- END: Notification Toggle -->
              ` }}
            </Highlight>
            <Highlight type="javascript" class="mt-5">
              {{
                `
                // Notification with avatar
                const notificationWithAvatar = ref();
                provide("bind[notificationWithAvatar]", (el) => {
                  // Binding
                  notificationWithAvatar.value = el;
                });
                const notificationWithAvatarToggle = () => {
                  // Show notification
                  notificationWithAvatar.value.showToast();
                };
                `
              }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Notification With Avatar -->
      <!-- BEGIN: Notification With Split Buttons -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Notification With Split Buttons
          </h2>
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
            <div class="text-center">
              <!-- BEGIN: Notification Content -->
              <Notification
                refKey="notificationWithSplitButtons"
                :options="{
                  close: false,
                }"
                class="flex"
              >
                <div class="sm:mr-40">
                  <div class="font-medium">Introducing new theme</div>
                  <div class="text-slate-500 mt-1">Release version 2.3.3</div>
                </div>
                <div
                  class="absolute top-0 bottom-0 right-0 flex flex-col border-l border-slate-200/60 dark:border-darkmode-400"
                >
                  <a
                    class="flex-1 flex items-center justify-center px-6 font-medium text-primary dark:text-slate-400 border-b border-slate-200/60 dark:border-darkmode-400"
                    href="javascript:;"
                    >View Details</a
                  >
                  <a
                    data-dismiss="notification"
                    class="flex-1 flex items-center justify-center px-6 font-medium text-slate-500"
                    href="javascript:;"
                    >Dismiss</a
                  >
                </div>
              </Notification>
              <!-- END: Notification Content -->
              <!-- BEGIN: Notification Toggle -->
              <button
                class="btn btn-primary"
                @click="notificationWithSplitButtonsToggle"
              >
                Show Notification
              </button>
              <!-- END: Notification Toggle -->
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Notification Content -->
              <Notification
                refKey="notificationWithSplitButtons"
                :options="{
                  close: false,
                }"
                class="flex"
              >
                <div class="sm:mr-40">
                  <div class="font-medium">Introducing new theme</div>
                  <div class="text-slate-500 mt-1">Release version 2.3.3</div>
                </div>
                <div
                  class="absolute top-0 bottom-0 right-0 flex flex-col border-l border-slate-200/60 dark:border-darkmode-400"
                >
                  <a
                    class="flex-1 flex items-center justify-center px-6 font-medium text-primary dark:text-slate-400 border-b border-slate-200/60 dark:border-darkmode-400"
                    href="javascript:;"
                    >View Details</a
                  >
                  <a
                    data-dismiss="notification"
                    class="flex-1 flex items-center justify-center px-6 font-medium text-slate-500"
                    href="javascript:;"
                    >Dismiss</a
                  >
                </div>
              </Notification>
              <!-- END: Notification Content -->
              <!-- BEGIN: Notification Toggle -->
              <button
                class="btn btn-primary"
                @click="notificationWithSplitButtonsToggle"
              >
                Show Notification
              </button>
              <!-- END: Notification Toggle -->
              ` }}
            </Highlight>
            <Highlight type="javascript" class="mt-5">
              {{
                `
                // Notification with split buttons
                const notificationWithSplitButtons = ref();
                provide("bind[notificationWithSplitButtons]", (el) => {
                  // Binding
                  notificationWithSplitButtons.value = el;
                });
                const notificationWithSplitButtonsToggle = () => {
                  // Show notification
                  notificationWithSplitButtons.value.showToast();
                };
                `
              }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Notification With Split Buttons -->
      <!-- BEGIN: Notification With Buttons Below -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Notification With Buttons Below
          </h2>
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
            <div class="text-center">
              <!-- BEGIN: Notification Content -->
              <Notification
                refKey="notificationWithButtonsBelow"
                :options="{
                  close: false,
                }"
                class="flex"
              >
                <FileTextIcon />
                <div class="ml-4 mr-5 sm:mr-20">
                  <div class="font-medium">
                    {{ $f()[0].users[0].name }}
                  </div>
                  <div class="text-slate-500 mt-1">Sent you new documents.</div>
                  <div class="mt-2.5">
                    <a class="btn btn-primary py-1 px-2 mr-2" href=""
                      >Preview</a
                    >
                    <a class="btn btn-outline-secondary py-1 px-2" href=""
                      >Download</a
                    >
                  </div>
                </div>
              </Notification>
              <!-- END: Notification Content -->
              <!-- BEGIN: Notification Toggle -->
              <button
                class="btn btn-primary"
                @click="notificationWithButtonsBelowToggle"
              >
                Show Notification
              </button>
              <!-- END: Notification Toggle -->
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Notification Content -->
              <Notification
                refKey="notificationWithButtonsBelow"
                :options="{
                  close: false,
                }"
                class="flex"
              >
                <FileTextIcon />
                <div class="ml-4 mr-5 sm:mr-20">
                  <div class="font-medium">\{\{ $f()[0].users[0].name \}\}</div>
                  <div class="text-slate-500 mt-1">Sent you new documents.</div>
                  <div class="mt-2.5">
                    <a class="btn btn-primary py-1 px-2 mr-2" href=""
                      >Preview</a
                    >
                    <a class="btn btn-outline-secondary py-1 px-2" href=""
                      >Download</a
                    >
                  </div>
                </div>
              </Notification>
              <!-- END: Notification Content -->
              <!-- BEGIN: Notification Toggle -->
              <button
                class="btn btn-primary"
                @click="notificationWithButtonsBelowToggle"
              >
                Show Notification
              </button>
              <!-- END: Notification Toggle -->
              ` }}
            </Highlight>
            <Highlight type="javascript" class="mt-5">
              {{
                `
                // Notification with buttons below
                const notificationWithButtonsBelow = ref();
                provide("bind[notificationWithButtonsBelow]", (el) => {
                  // Binding
                  notificationWithButtonsBelow.value = el;
                });
                const notificationWithButtonsBelowToggle = () => {
                  // Show notification
                  notificationWithButtonsBelow.value.showToast();
                };
                `
              }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Notification With Buttons Below -->
    </div>
  </div>
</template>

<script setup>
import { ref, provide } from "vue";

// Basic non sticky notification
const basicNonStickyNotification = ref();
provide("bind[basicNonStickyNotification]", (el) => {
  // Binding
  basicNonStickyNotification.value = el;
});
const basicNonStickyNotificationToggle = () => {
  // Show notification
  basicNonStickyNotification.value.showToast();
};

// Basic sticky notification
const basicStickyNotification = ref();
provide("bind[basicStickyNotification]", (el) => {
  // Binding
  basicStickyNotification.value = el;
});
const basicStickyNotificationToggle = () => {
  // Show notification
  basicStickyNotification.value.showToast();
};

// Success notification
const successNotification = ref();
provide("bind[successNotification]", (el) => {
  // Binding
  successNotification.value = el;
});
const successNotificationToggle = () => {
  // Show notification
  successNotification.value.showToast();
};

// Notification with actions
const notificationWithActions = ref();
provide("bind[notificationWithActions]", (el) => {
  // Binding
  notificationWithActions.value = el;
});
const notificationWithActionsToggle = () => {
  // Show notification
  notificationWithActions.value.showToast();
};

// Notification with avatar
const notificationWithAvatar = ref();
provide("bind[notificationWithAvatar]", (el) => {
  // Binding
  notificationWithAvatar.value = el;
});
const notificationWithAvatarToggle = () => {
  // Show notification
  notificationWithAvatar.value.showToast();
};

// Notification with split buttons
const notificationWithSplitButtons = ref();
provide("bind[notificationWithSplitButtons]", (el) => {
  // Binding
  notificationWithSplitButtons.value = el;
});
const notificationWithSplitButtonsToggle = () => {
  // Show notification
  notificationWithSplitButtons.value.showToast();
};

// Notification with buttons below
const notificationWithButtonsBelow = ref();
provide("bind[notificationWithButtonsBelow]", (el) => {
  // Binding
  notificationWithButtonsBelow.value = el;
});
const notificationWithButtonsBelowToggle = () => {
  // Show notification
  notificationWithButtonsBelow.value.showToast();
};
</script>
