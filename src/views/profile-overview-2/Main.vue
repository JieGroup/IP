<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Profile Layout</h2>
  </div>
  <TabGroup>
    <!-- BEGIN: Profile Info -->
    <div class="intro-y box px-5 pt-5 mt-5">
      <div
        class="flex flex-col lg:flex-row border-b border-slate-200/60 dark:border-darkmode-400 pb-5 -mx-5"
      >
        <div
          class="flex flex-1 px-5 items-center justify-center lg:justify-start"
        >
          <div
            class="w-20 h-20 sm:w-24 sm:h-24 flex-none lg:w-32 lg:h-32 image-fit relative"
          >
            <img
              alt="Midone Tailwind HTML Admin Template"
              class="rounded-full"
              :src="$f()[0].photos[0]"
            />
          </div>
          <div class="ml-5">
            <div
              class="w-24 sm:w-40 truncate sm:whitespace-normal font-medium text-lg"
            >
              {{ $f()[0].users[0].name }}
            </div>
            <div class="text-slate-500">{{ $f()[0].jobs[0] }}</div>
          </div>
        </div>
        <div
          class="mt-6 lg:mt-0 flex-1 px-5 border-l border-r border-slate-200/60 dark:border-darkmode-400 border-t lg:border-t-0 pt-5 lg:pt-0"
        >
          <div class="font-medium text-center lg:text-left lg:mt-3">
            Contact Details
          </div>
          <div
            class="flex flex-col justify-center items-center lg:items-start mt-4"
          >
            <div class="truncate sm:whitespace-normal flex items-center">
              <MailIcon class="w-4 h-4 mr-2" />
              {{ $f()[0].users[0].email }}
            </div>
            <div class="truncate sm:whitespace-normal flex items-center mt-3">
              <InstagramIcon class="w-4 h-4 mr-2" /> Instagram
              {{ $f()[0].users[0].name }}
            </div>
            <div class="truncate sm:whitespace-normal flex items-center mt-3">
              <TwitterIcon class="w-4 h-4 mr-2" /> Twitter
              {{ $f()[0].users[0].name }}
            </div>
          </div>
        </div>
        <div
          class="mt-6 lg:mt-0 flex-1 flex items-center justify-center px-5 border-t lg:border-0 border-slate-200/60 dark:border-darkmode-400 pt-5 lg:pt-0"
        >
          <div class="text-center rounded-md w-20 py-3">
            <div class="font-medium text-primary text-xl">201</div>
            <div class="text-slate-500">Orders</div>
          </div>
          <div class="text-center rounded-md w-20 py-3">
            <div class="font-medium text-primary text-xl">1k</div>
            <div class="text-slate-500">Purchases</div>
          </div>
          <div class="text-center rounded-md w-20 py-3">
            <div class="font-medium text-primary text-xl">492</div>
            <div class="text-slate-500">Reviews</div>
          </div>
        </div>
      </div>
      <TabList
        class="nav-link-tabs flex-col sm:flex-row justify-center lg:justify-start text-center"
      >
        <Tab :fullWidth="false" class="py-4 flex items-center cursor-pointer">
          <UserIcon class="w-4 h-4 mr-2" /> Profile
        </Tab>
        <Tab :fullWidth="false" class="py-4 flex items-center cursor-pointer">
          <ShieldIcon class="w-4 h-4 mr-2" /> Account
        </Tab>
        <Tab :fullWidth="false" class="py-4 flex items-center cursor-pointer">
          <LockIcon class="w-4 h-4 mr-2" /> Change Password
        </Tab>
        <Tab :fullWidth="false" class="py-4 flex items-center cursor-pointer">
          <SettingsIcon class="w-4 h-4 mr-2" /> Settings
        </Tab>
      </TabList>
    </div>
    <!-- END: Profile Info -->
    <TabPanels class="mt-5">
      <TabPanel>
        <div class="grid grid-cols-12 gap-6">
          <!-- BEGIN: Latest Uploads -->
          <div class="intro-y box col-span-12 lg:col-span-6">
            <div
              class="flex items-center px-5 py-5 sm:py-3 border-b border-slate-200/60 dark:border-darkmode-400"
            >
              <h2 class="font-medium text-base mr-auto">Latest Uploads</h2>
              <Dropdown class="ml-auto sm:hidden">
                <DropdownToggle
                  tag="a"
                  class="w-5 h-5 block"
                  href="javascript:;"
                >
                  <MoreHorizontalIcon class="w-5 h-5 text-slate-500" />
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>All Files</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <button class="btn btn-outline-secondary hidden sm:flex">
                All Files
              </button>
            </div>
            <div class="p-5">
              <div class="flex items-center">
                <div class="file">
                  <a href="" class="w-12 file__icon file__icon--directory"></a>
                </div>
                <div class="ml-4">
                  <a class="font-medium" href="">Documentation</a>
                  <div class="text-slate-500 text-xs mt-0.5">40 KB</div>
                </div>
                <Dropdown class="ml-auto">
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
                        <UsersIcon class="w-4 h-4 mr-2" /> Share File
                      </DropdownItem>
                      <DropdownItem>
                        <TrashIcon class="w-4 h-4 mr-2" /> Delete
                      </DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
              </div>
              <div class="flex items-center mt-5">
                <div class="file">
                  <a href="" class="w-12 file__icon file__icon--file">
                    <div class="file__icon__file-name text-xs">MP3</div>
                  </a>
                </div>
                <div class="ml-4">
                  <a class="font-medium" href="">Celine Dion - Ashes</a>
                  <div class="text-slate-500 text-xs mt-0.5">40 KB</div>
                </div>
                <Dropdown class="ml-auto">
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
                        <UsersIcon class="w-4 h-4 mr-2" /> Share File
                      </DropdownItem>
                      <DropdownItem>
                        <TrashIcon class="w-4 h-4 mr-2" /> Delete
                      </DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
              </div>
              <div class="flex items-center mt-5">
                <div class="file">
                  <a
                    href=""
                    class="w-12 file__icon file__icon--empty-directory"
                  ></a>
                </div>
                <div class="ml-4">
                  <a class="font-medium" href="">Resources</a>
                  <div class="text-slate-500 text-xs mt-0.5">0 KB</div>
                </div>
                <Dropdown class="ml-auto">
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
                        <UsersIcon class="w-4 h-4 mr-2" /> Share File
                      </DropdownItem>
                      <DropdownItem>
                        <TrashIcon class="w-4 h-4 mr-2" /> Delete
                      </DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
              </div>
            </div>
          </div>
          <!-- END: Latest Uploads -->
          <!-- BEGIN: Work In Progress -->
          <TabGroup class="intro-y box col-span-12 lg:col-span-6">
            <div
              class="flex items-center px-5 py-5 sm:py-0 border-b border-slate-200/60 dark:border-darkmode-400"
            >
              <h2 class="font-medium text-base mr-auto">Work In Progress</h2>
              <Dropdown class="ml-auto sm:hidden">
                <DropdownToggle
                  tag="a"
                  class="w-5 h-5 block"
                  href="javascript:;"
                >
                  <MoreHorizontalIcon class="w-5 h-5 text-slate-500" />
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent tag="div">
                    <TabList class="block">
                      <Tab
                        :fullWidth="false"
                        class="dropdown-item cursor-pointer"
                        >New</Tab
                      >
                      <Tab
                        :fullWidth="false"
                        class="dropdown-item cursor-pointer"
                        >Last Week</Tab
                      >
                    </TabList>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <TabList class="nav-link-tabs w-auto ml-auto hidden sm:flex">
                <Tab :fullWidth="false" class="py-5 cursor-pointer">New</Tab>
                <Tab :fullWidth="false" class="py-5 cursor-pointer"
                  >Last Week</Tab
                >
              </TabList>
            </div>
            <div class="p-5">
              <TabPanels>
                <TabPanel>
                  <div>
                    <div class="flex">
                      <div class="mr-auto">Pending Tasks</div>
                      <div>20%</div>
                    </div>
                    <div class="progress h-1 mt-2">
                      <div
                        class="progress-bar w-1/2 bg-primary"
                        role="progressbar"
                        aria-valuenow="0"
                        aria-valuemin="0"
                        aria-valuemax="100"
                      ></div>
                    </div>
                  </div>
                  <div class="mt-5">
                    <div class="flex">
                      <div class="mr-auto">Completed Tasks</div>
                      <div>2 / 20</div>
                    </div>
                    <div class="progress h-1 mt-2">
                      <div
                        class="progress-bar w-1/4 bg-primary"
                        role="progressbar"
                        aria-valuenow="0"
                        aria-valuemin="0"
                        aria-valuemax="100"
                      ></div>
                    </div>
                  </div>
                  <div class="mt-5">
                    <div class="flex">
                      <div class="mr-auto">Tasks In Progress</div>
                      <div>42</div>
                    </div>
                    <div class="progress h-1 mt-2">
                      <div
                        class="progress-bar w-3/4 bg-primary"
                        role="progressbar"
                        aria-valuenow="0"
                        aria-valuemin="0"
                        aria-valuemax="100"
                      ></div>
                    </div>
                  </div>
                  <a href="" class="btn btn-secondary block w-40 mx-auto mt-5"
                    >View More Details</a
                  >
                </TabPanel>
              </TabPanels>
            </div>
          </TabGroup>
          <!-- END: Work In Progress -->
          <!-- BEGIN: Daily Sales -->
          <div class="intro-y box col-span-12 lg:col-span-6">
            <div
              class="flex items-center px-5 py-5 sm:py-3 border-b border-slate-200/60 dark:border-darkmode-400"
            >
              <h2 class="font-medium text-base mr-auto">Daily Sales</h2>
              <Dropdown class="ml-auto sm:hidden">
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
                      <FileIcon class="w-4 h-4 mr-2" /> Download Excel
                    </DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <button class="btn btn-outline-secondary hidden sm:flex">
                <FileIcon class="w-4 h-4 mr-2" /> Download Excel
              </button>
            </div>
            <div class="p-5">
              <div class="relative flex items-center">
                <div class="w-12 h-12 flex-none image-fit">
                  <img
                    alt="Midone Tailwind HTML Admin Template"
                    class="rounded-full"
                    :src="$f()[0].photos[0]"
                  />
                </div>
                <div class="ml-4 mr-auto">
                  <a href="" class="font-medium">{{ $f()[0].users[0].name }}</a>
                  <div class="text-slate-500 mr-5 sm:mr-5">
                    Bootstrap 4 HTML Admin Template
                  </div>
                </div>
                <div class="font-medium text-slate-600 dark:text-slate-500">
                  +$19
                </div>
              </div>
              <div class="relative flex items-center mt-5">
                <div class="w-12 h-12 flex-none image-fit">
                  <img
                    alt="Midone Tailwind HTML Admin Template"
                    class="rounded-full"
                    :src="$f()[1].photos[0]"
                  />
                </div>
                <div class="ml-4 mr-auto">
                  <a href="" class="font-medium">{{ $f()[1].users[0].name }}</a>
                  <div class="text-slate-500 mr-5 sm:mr-5">
                    Tailwind HTML Admin Template
                  </div>
                </div>
                <div class="font-medium text-slate-600 dark:text-slate-500">
                  +$25
                </div>
              </div>
              <div class="relative flex items-center mt-5">
                <div class="w-12 h-12 flex-none image-fit">
                  <img
                    alt="Midone Tailwind HTML Admin Template"
                    class="rounded-full"
                    :src="$f()[2].photos[0]"
                  />
                </div>
                <div class="ml-4 mr-auto">
                  <a href="" class="font-medium">{{ $f()[2].users[0].name }}</a>
                  <div class="text-slate-500 mr-5 sm:mr-5">
                    Vuejs HTML Admin Template
                  </div>
                </div>
                <div class="font-medium text-slate-600 dark:text-slate-500">
                  +$21
                </div>
              </div>
            </div>
          </div>
          <!-- END: Daily Sales -->
          <!-- BEGIN: Latest Tasks -->
          <TabGroup class="intro-y box col-span-12 lg:col-span-6">
            <div
              class="flex items-center px-5 py-5 sm:py-0 border-b border-slate-200/60 dark:border-darkmode-400"
            >
              <h2 class="font-medium text-base mr-auto">Latest Tasks</h2>
              <Dropdown class="ml-auto sm:hidden">
                <DropdownToggle
                  tag="a"
                  class="w-5 h-5 block"
                  href="javascript:;"
                >
                  <MoreHorizontalIcon class="w-5 h-5 text-slate-500" />
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent tag="div">
                    <TabList class="block">
                      <Tab
                        :fullWidth="false"
                        class="dropdown-item cursor-pointer"
                        >New</Tab
                      >
                      <Tab
                        :fullWidth="false"
                        class="dropdown-item cursor-pointer"
                        >Last Week</Tab
                      >
                    </TabList>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <TabList class="nav-link-tabs w-auto ml-auto hidden sm:flex">
                <Tab :fullWidth="false" class="py-5 cursor-pointer">New</Tab>
                <Tab :fullWidth="false" class="py-5 cursor-pointer"
                  >Last Week</Tab
                >
              </TabList>
            </div>
            <div class="p-5">
              <TabPanels>
                <TabPanel>
                  <div class="flex items-center">
                    <div
                      class="border-l-2 border-primary dark:border-primary pl-4"
                    >
                      <a href="" class="font-medium">Create New Campaign</a>
                      <div class="text-slate-500">10:00 AM</div>
                    </div>
                    <div class="form-check form-switch ml-auto">
                      <input class="form-check-input" type="checkbox" />
                    </div>
                  </div>
                  <div class="flex items-center mt-5">
                    <div
                      class="border-l-2 border-primary dark:border-primary pl-4"
                    >
                      <a href="" class="font-medium">Meeting With Client</a>
                      <div class="text-slate-500">02:00 PM</div>
                    </div>
                    <div class="form-check form-switch ml-auto">
                      <input class="form-check-input" type="checkbox" />
                    </div>
                  </div>
                  <div class="flex items-center mt-5">
                    <div
                      class="border-l-2 border-primary dark:border-primary pl-4"
                    >
                      <a href="" class="font-medium">Create New Repository</a>
                      <div class="text-slate-500">04:00 PM</div>
                    </div>
                    <div class="form-check form-switch ml-auto">
                      <input class="form-check-input" type="checkbox" />
                    </div>
                  </div>
                </TabPanel>
              </TabPanels>
            </div>
          </TabGroup>
          <!-- END: Latest Tasks -->
          <!-- BEGIN: New Products -->
          <div class="intro-y box col-span-12">
            <div
              class="flex items-center px-5 py-3 border-b border-slate-200/60 dark:border-darkmode-400"
            >
              <h2 class="font-medium text-base mr-auto">New Products</h2>
              <button
                class="tiny-slider-navigator btn btn-outline-secondary px-2 mr-2"
                @click="prevNewProducts"
              >
                <ChevronLeftIcon class="w-4 h-4" />
              </button>
              <button
                class="tiny-slider-navigator btn btn-outline-secondary px-2"
                @click="nextNewProducts"
              >
                <ChevronRightIcon class="w-4 h-4" />
              </button>
            </div>
            <div id="new-products" class="tiny-slider py-5">
              <TinySlider ref-key="newProductsRef">
                <div
                  v-for="(faker, fakerKey) in $_.take($f(), 5)"
                  :key="fakerKey"
                  class="px-5"
                >
                  <div class="flex flex-col lg:flex-row items-center pb-5">
                    <div
                      class="flex flex-col sm:flex-row items-center pr-5 lg:border-r border-slate-200/60 dark:border-darkmode-400"
                    >
                      <div class="sm:mr-5">
                        <div class="w-20 h-20 image-fit">
                          <img
                            alt="Midone Tailwind HTML Admin Template"
                            class="rounded-full"
                            :src="faker.images[0]"
                          />
                        </div>
                      </div>
                      <div
                        class="mr-auto text-center sm:text-left mt-3 sm:mt-0"
                      >
                        <a href="" class="font-medium text-lg">{{
                          faker.products[0].name
                        }}</a>
                        <div class="text-slate-500 mt-1 sm:mt-0">
                          {{ faker.news[0].shortContent }}
                        </div>
                      </div>
                    </div>
                    <div
                      class="w-full lg:w-auto mt-6 lg:mt-0 pt-4 lg:pt-0 flex-1 flex items-center justify-center px-5 border-t lg:border-t-0 border-slate-200/60 dark:border-darkmode-400"
                    >
                      <div class="text-center rounded-md w-20 py-3">
                        <div class="font-medium text-primary text-xl">
                          {{ faker.totals[0] }}
                        </div>
                        <div class="text-slate-500">Orders</div>
                      </div>
                      <div class="text-center rounded-md w-20 py-3">
                        <div class="font-medium text-primary text-xl">
                          {{ faker.totals[1] }}k
                        </div>
                        <div class="text-slate-500">Purchases</div>
                      </div>
                      <div class="text-center rounded-md w-20 py-3">
                        <div class="font-medium text-primary text-xl">
                          {{ faker.totals[0] }}
                        </div>
                        <div class="text-slate-500">Reviews</div>
                      </div>
                    </div>
                  </div>
                  <div
                    class="flex flex-col sm:flex-row items-center border-t border-slate-200/60 dark:border-darkmode-400 pt-5"
                  >
                    <div
                      class="w-full sm:w-auto flex justify-center sm:justify-start items-center border-b sm:border-b-0 border-slate-200/60 dark:border-darkmode-400 pb-5 sm:pb-0"
                    >
                      <div
                        class="px-3 py-2 text-primary bg-primary/10 dark:bg-darkmode-400 dark:text-slate-300 rounded font-medium mr-3"
                      >
                        {{ faker.dates[0] }}
                      </div>
                      <div class="text-slate-500">Date of Release</div>
                    </div>
                    <div class="flex sm:ml-auto mt-5 sm:mt-0">
                      <button class="btn btn-secondary w-20 ml-auto">
                        Preview
                      </button>
                      <button class="btn btn-secondary w-20 ml-2">
                        Details
                      </button>
                    </div>
                  </div>
                </div>
              </TinySlider>
            </div>
          </div>
          <!-- END: New Products -->
          <!-- BEGIN: New Authors -->
          <div class="intro-y box col-span-12">
            <div
              class="flex items-center px-5 py-3 border-b border-slate-200/60 dark:border-darkmode-400"
            >
              <h2 class="font-medium text-base mr-auto">New Authors</h2>
              <button
                class="tiny-slider-navigator btn btn-outline-secondary px-2 mr-2"
                @click="prevNewAuthors"
              >
                <ChevronLeftIcon class="w-4 h-4" />
              </button>
              <button
                class="tiny-slider-navigator btn btn-outline-secondary px-2"
                @click="nextNewAuthors"
              >
                <ChevronRightIcon class="w-4 h-4" />
              </button>
            </div>
            <div id="new-authors" class="tiny-slider py-5">
              <TinySlider ref-key="newAuthorsRef">
                <div
                  v-for="(faker, fakerKey) in $_.take($f(), 5)"
                  :key="fakerKey"
                  class="px-5"
                >
                  <div class="flex flex-col lg:flex-row items-center pb-5">
                    <div
                      class="flex-1 flex flex-col sm:flex-row items-center pr-5 lg:border-r border-slate-200/60 dark:border-darkmode-400"
                    >
                      <div class="sm:mr-5">
                        <div class="w-20 h-20 image-fit">
                          <img
                            alt="Midone Tailwind HTML Admin Template"
                            class="rounded-full"
                            :src="faker.photos[0]"
                          />
                        </div>
                      </div>
                      <div
                        class="mr-auto text-center sm:text-left mt-3 sm:mt-0"
                      >
                        <a href="" class="font-medium text-lg">{{
                          faker.users[0].name
                        }}</a>
                        <div class="text-slate-500 mt-1 sm:mt-0">
                          {{ faker.jobs[0] }}
                        </div>
                      </div>
                    </div>
                    <div
                      class="w-full lg:w-auto mt-6 lg:mt-0 pt-4 lg:pt-0 flex-1 flex flex-col justify-center items-center lg:items-start px-5 border-t lg:border-t-0 border-slate-200/60 dark:border-darkmode-400"
                    >
                      <div class="flex items-center">
                        <a
                          href=""
                          class="w-8 h-8 rounded-full flex items-center justify-center border mr-2 text-slate-400"
                        >
                          <FacebookIcon class="w-3 h-3 fill-current" />
                        </a>
                        {{ faker.users[0].email }}
                      </div>
                      <div class="flex items-center mt-2">
                        <a
                          href=""
                          class="w-8 h-8 rounded-full flex items-center justify-center border mr-2 text-slate-400"
                        >
                          <TwitterIcon class="w-3 h-3 fill-current" />
                        </a>
                        {{ faker.users[0].name }}
                      </div>
                    </div>
                  </div>
                  <div
                    class="flex flex-col sm:flex-row items-center border-t border-slate-200/60 dark:border-darkmode-400 pt-5"
                  >
                    <div
                      class="w-full sm:w-auto flex justify-center sm:justify-start items-center border-b sm:border-b-0 border-slate-200/60 dark:border-darkmode-400 pb-5 sm:pb-0"
                    >
                      <div
                        class="px-3 py-2 text-primary bg-primary/10 dark:bg-darkmode-400 dark:text-slate-300 rounded font-medium mr-3"
                      >
                        {{ faker.dates[0] }}
                      </div>
                      <div class="text-slate-500">Joined Date</div>
                    </div>
                    <div class="flex sm:ml-auto mt-5 sm:mt-0">
                      <button class="btn btn-secondary w-20 ml-auto">
                        Message
                      </button>
                      <button class="btn btn-secondary w-20 ml-2">
                        Profile
                      </button>
                    </div>
                  </div>
                </div>
              </TinySlider>
            </div>
          </div>
          <!-- END: New Authors -->
        </div>
      </TabPanel>
    </TabPanels>
  </TabGroup>
</template>

<script setup>
import { ref, provide } from "vue";

const newProductsRef = ref();
const newAuthorsRef = ref();

provide("bind[newProductsRef]", (el) => {
  newProductsRef.value = el;
});

provide("bind[newAuthorsRef]", (el) => {
  newAuthorsRef.value = el;
});

const prevNewProducts = () => {
  const el = newProductsRef.value;
  el.tns.goTo("prev");
};
const nextNewProducts = () => {
  const el = newProductsRef.value;
  el.tns.goTo("next");
};
const prevNewAuthors = () => {
  const el = newAuthorsRef.value;
  el.tns.goTo("prev");
};
const nextNewAuthors = () => {
  const el = newAuthorsRef.value;
  el.tns.goTo("next");
};
</script>
