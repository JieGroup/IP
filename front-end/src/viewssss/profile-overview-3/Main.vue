<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Profile Layout</h2>
  </div>
  <div class="grid grid-cols-12 gap-6 mt-5">
    <!-- BEGIN: Profile Menu -->
    <div
      class="col-span-12 lg:col-span-4 2xl:col-span-3 flex lg:block flex-col-reverse"
    >
      <div class="intro-y box mt-5 lg:mt-0">
        <div class="relative flex items-center p-5">
          <div class="w-12 h-12 image-fit">
            <img
              alt="Midone Tailwind HTML Admin Template"
              class="rounded-full"
              :src="$f()[0].photos[0]"
            />
          </div>
          <div class="ml-4 mr-auto">
            <div class="font-medium text-base">{{ $f()[0].users[0].name }}</div>
            <div class="text-slate-500">{{ $f()[0].jobs[0] }}</div>
          </div>
          <Dropdown>
            <DropdownToggle tag="a" class="w-5 h-5 block" href="javascript:;">
              <MoreHorizontalIcon class="w-5 h-5 text-slate-500" />
            </DropdownToggle>
            <DropdownMenu class="w-56">
              <DropdownContent>
                <DropdownHeader>Export Options</DropdownHeader>
                <DropdownDivider />
                <DropdownItem>
                  <ActivityIcon class="w-4 h-4 mr-2" />
                  English
                </DropdownItem>
                <DropdownItem>
                  <BoxIcon class="w-4 h-4 mr-2" />
                  Indonesia
                  <div
                    class="text-xs text-white px-1 rounded-full bg-danger ml-auto"
                  >
                    10
                  </div>
                </DropdownItem>
                <DropdownItem>
                  <LayoutIcon class="w-4 h-4 mr-2" />
                  English
                </DropdownItem>
                <DropdownItem>
                  <SidebarIcon class="w-4 h-4 mr-2" />
                  Indonesia
                </DropdownItem>
                <DropdownDivider />
                <DropdownFooter>
                  <button type="button" class="btn btn-primary py-1 px-2">
                    Settings
                  </button>
                  <button
                    type="button"
                    class="btn btn-secondary py-1 px-2 ml-auto"
                  >
                    View Profile
                  </button>
                </DropdownFooter>
              </DropdownContent>
            </DropdownMenu>
          </Dropdown>
        </div>
        <div class="p-5 border-t border-slate-200/60 dark:border-darkmode-400">
          <a class="flex items-center text-primary font-medium" href="">
            <ActivityIcon class="w-4 h-4 mr-2" /> Personal Information
          </a>
          <a class="flex items-center mt-5" href="">
            <BoxIcon class="w-4 h-4 mr-2" /> Account Settings
          </a>
          <a class="flex items-center mt-5" href="">
            <LockIcon class="w-4 h-4 mr-2" /> Change Password
          </a>
          <a class="flex items-center mt-5" href="">
            <SettingsIcon class="w-4 h-4 mr-2" /> User Settings
          </a>
        </div>
        <div class="p-5 border-t border-slate-200/60 dark:border-darkmode-400">
          <a class="flex items-center" href="">
            <ActivityIcon class="w-4 h-4 mr-2" /> Email Settings
          </a>
          <a class="flex items-center mt-5" href="">
            <BoxIcon class="w-4 h-4 mr-2" /> Saved Credit Cards
          </a>
          <a class="flex items-center mt-5" href="">
            <LockIcon class="w-4 h-4 mr-2" /> Social Networks
          </a>
          <a class="flex items-center mt-5" href="">
            <SettingsIcon class="w-4 h-4 mr-2" /> Tax Information
          </a>
        </div>
        <div
          class="p-5 border-t border-slate-200/60 dark:border-darkmode-400 flex"
        >
          <button type="button" class="btn btn-primary py-1 px-2">
            New Group
          </button>
          <button
            type="button"
            class="btn btn-outline-secondary py-1 px-2 ml-auto"
          >
            New Quick Link
          </button>
        </div>
      </div>
      <div class="intro-y box p-5 bg-primary text-white mt-5">
        <div class="flex items-center">
          <div class="font-medium text-lg">Important Update</div>
          <div
            class="text-xs bg-white dark:bg-primary dark:text-white text-slate-700 px-1 rounded-md ml-auto"
          >
            New
          </div>
        </div>
        <div class="mt-4">
          Lorem Ipsum is simply dummy text of the printing and typesetting
          industry. Lorem Ipsum has been the industry's standard dummy text ever
          since the 1500s.
        </div>
        <div class="font-medium flex mt-5">
          <button
            type="button"
            class="btn py-1 px-2 border-white text-white dark:text-slate-300 dark:bg-darkmode-400 dark:border-darkmode-400"
          >
            Take Action
          </button>
          <button
            type="button"
            class="btn py-1 px-2 border-transparent text-white dark:border-transparent ml-auto"
          >
            Dismiss
          </button>
        </div>
      </div>
    </div>
    <!-- END: Profile Menu -->
    <div class="col-span-12 lg:col-span-8 2xl:col-span-9">
      <div class="grid grid-cols-12 gap-6">
        <!-- BEGIN: Daily Sales -->
        <div class="intro-y box col-span-12 2xl:col-span-6">
          <div
            class="flex items-center px-5 py-5 sm:py-3 border-b border-slate-200/60 dark:border-darkmode-400"
          >
            <h2 class="font-medium text-base mr-auto">Daily Sales</h2>
            <Dropdown class="ml-auto sm:hidden">
              <DropdownToggle tag="a" class="w-5 h-5 block" href="javascript:;">
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
        <!-- BEGIN: Announcement -->
        <div class="intro-y box col-span-12 2xl:col-span-6">
          <div
            class="flex items-center px-5 py-3 border-b border-slate-200/60 dark:border-darkmode-400"
          >
            <h2 class="font-medium text-base mr-auto">Announcement</h2>
            <button
              class="tiny-slider-navigator btn btn-outline-secondary px-2 mr-2"
              @click="prevAnnouncement"
            >
              <ChevronLeftIcon class="w-4 h-4" />
            </button>
            <button
              class="tiny-slider-navigator btn btn-outline-secondary px-2"
              @click="nextAnnouncement"
            >
              <ChevronRightIcon class="w-4 h-4" />
            </button>
          </div>
          <TinySlider ref-key="announcementRef" class="py-5">
            <div class="px-5">
              <div class="font-medium text-lg">Midone Admin Template</div>
              <div class="text-slate-600 dark:text-slate-500 mt-2">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever. <br /><br />
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry since the 1500s.
              </div>
              <div class="flex items-center mt-5">
                <div
                  class="px-3 py-2 text-primary bg-primary/10 dark:bg-darkmode-400 dark:text-slate-300 rounded font-medium"
                >
                  02 June 2021
                </div>
                <button class="btn btn-secondary ml-auto">View Details</button>
              </div>
            </div>
            <div class="px-5">
              <div class="font-medium text-lg">Midone Admin Template</div>
              <div class="text-slate-600 dark:text-slate-500 mt-2">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever. <br /><br />
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry since the 1500s.
              </div>
              <div class="flex items-center mt-5">
                <div
                  class="px-3 py-2 text-primary bg-primary/10 dark:bg-darkmode-400 dark:text-slate-300 rounded font-medium"
                >
                  02 June 2021
                </div>
                <button class="btn btn-secondary ml-auto">View Details</button>
              </div>
            </div>
            <div class="px-5">
              <div class="font-medium text-lg">Midone Admin Template</div>
              <div class="text-slate-600 dark:text-slate-500 mt-2">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever. <br /><br />
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry since the 1500s.
              </div>
              <div class="flex items-center mt-5">
                <div
                  class="px-3 py-2 text-primary bg-primary/10 dark:bg-darkmode-400 dark:text-slate-300 rounded font-medium"
                >
                  02 June 2021
                </div>
                <button class="btn btn-secondary ml-auto">View Details</button>
              </div>
            </div>
          </TinySlider>
        </div>
        <!-- END: Announcement -->
        <!-- BEGIN: Projects -->
        <div class="intro-y box col-span-12 2xl:col-span-6">
          <div
            class="flex items-center px-5 py-3 border-b border-slate-200/60 dark:border-darkmode-400"
          >
            <h2 class="font-medium text-base mr-auto">Projects</h2>
            <button
              class="tiny-slider-navigator btn btn-outline-secondary px-2 mr-2"
              @click="prevNewProjects"
            >
              <ChevronLeftIcon class="w-4 h-4" />
            </button>
            <button
              class="tiny-slider-navigator btn btn-outline-secondary px-2"
              @click="nextNewProjects"
            >
              <ChevronRightIcon class="w-4 h-4" />
            </button>
          </div>
          <TinySlider ref-key="newProjectsRef" class="py-5">
            <div class="px-5">
              <div class="font-medium text-lg">Midone Admin Template</div>
              <div class="text-slate-600 dark:text-slate-500 mt-2">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever since the 1500s.
              </div>
              <div class="mt-5">
                <div class="flex text-slate-500">
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
            </div>
            <div class="px-5">
              <div class="font-medium text-lg">Midone Admin Template</div>
              <div class="text-slate-600 dark:text-slate-500 mt-2">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever since the 1500s.
              </div>
              <div class="mt-5">
                <div class="flex text-slate-500">
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
            </div>
            <div class="px-5">
              <div class="font-medium text-lg">Midone Admin Template</div>
              <div class="text-slate-600 dark:text-slate-500 mt-2">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy
                text ever since the 1500s.
              </div>
              <div class="mt-5">
                <div class="flex text-slate-500">
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
            </div>
          </TinySlider>
        </div>
        <!-- END: Projects -->
        <!-- BEGIN: Today Schedules -->
        <div class="intro-y box col-span-12 2xl:col-span-6">
          <div
            class="flex items-center px-5 py-3 border-b border-slate-200/60 dark:border-darkmode-400"
          >
            <h2 class="font-medium text-base mr-auto">Today Schedules</h2>
            <button
              class="tiny-slider-navigator btn btn-outline-secondary px-2 mr-2"
              @click="prevTodaySchedules"
            >
              <ChevronLeftIcon class="w-4 h-4" />
            </button>
            <button
              class="tiny-slider-navigator btn btn-outline-secondary px-2"
              @click="nextTodaySchedules"
            >
              <ChevronRightIcon class="w-4 h-4" />
            </button>
          </div>
          <TinySlider ref-key="todaySchedulesRef" class="py-5">
            <div class="px-5 text-center sm:text-left">
              <div class="font-medium text-lg">
                Developing rest API with Laravel 7
              </div>
              <div class="text-slate-600 dark:text-slate-500 mt-2">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry
              </div>
              <div class="mt-2">11:15AM - 12:30PM</div>
              <div class="flex flex-col sm:flex-row items-center mt-5">
                <div class="flex items-center text-slate-500">
                  <MapPinIcon class="hidden sm:block w-4 h-4 mr-2" />
                  1396 Pooh Bear Lane, New Market
                </div>
                <button
                  class="btn btn-secondary py-1 px-2 sm:ml-auto mt-3 sm:mt-0sm:ml-auto mt-3 sm:mt-0"
                >
                  View On Map
                </button>
              </div>
            </div>
            <div class="px-5 text-center sm:text-left">
              <div class="font-medium text-lg">
                Developing rest API with Laravel 7
              </div>
              <div class="text-slate-600 dark:text-slate-500 mt-2">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry
              </div>
              <div class="mt-2">11:15AM - 12:30PM</div>
              <div class="flex flex-col sm:flex-row items-center mt-5">
                <div class="flex items-center text-slate-500">
                  <MapPinIcon class="hidden sm:block w-4 h-4 mr-2" />
                  1396 Pooh Bear Lane, New Market
                </div>
                <button
                  class="btn btn-secondary py-1 px-2 sm:ml-auto mt-3 sm:mt-0sm:ml-auto mt-3 sm:mt-0"
                >
                  View On Map
                </button>
              </div>
            </div>
            <div class="px-5 text-center sm:text-left">
              <div class="font-medium text-lg">
                Developing rest API with Laravel 7
              </div>
              <div class="text-slate-600 dark:text-slate-500 mt-2">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry
              </div>
              <div class="mt-2">11:15AM - 12:30PM</div>
              <div class="flex flex-col sm:flex-row items-center mt-5">
                <div class="flex items-center text-slate-500">
                  <MapPinIcon class="hidden sm:block w-4 h-4 mr-2" />
                  1396 Pooh Bear Lane, New Market
                </div>
                <button
                  class="btn btn-secondary py-1 px-2 sm:ml-auto mt-3 sm:mt-0sm:ml-auto mt-3 sm:mt-0"
                >
                  View On Map
                </button>
              </div>
            </div>
          </TinySlider>
        </div>
        <!-- END: Today Schedules -->
        <!-- BEGIN: Top Products -->
        <TabGroup class="intro-y box col-span-12 2xl:col-span-6">
          <div
            class="flex items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
          >
            <h2 class="font-medium text-base mr-auto">Top Products</h2>
            <Dropdown class="ml-auto">
              <DropdownToggle tag="a" class="w-5 h-5 block" href="javascript:;">
                <MoreHorizontalIcon class="w-5 h-5 text-slate-500" />
              </DropdownToggle>
              <DropdownMenu class="w-40">
                <DropdownContent>
                  <DropdownItem>
                    <Edit2Icon class="w-4 h-4 mr-2" /> New Chat
                  </DropdownItem>
                  <DropdownItem>
                    <TrashIcon class="w-4 h-4 mr-2" /> Delete
                  </DropdownItem>
                </DropdownContent>
              </DropdownMenu>
            </Dropdown>
          </div>
          <div class="p-5">
            <TabList class="nav-boxed-tabs justify-center flex-col sm:flex-row">
              <Tab
                :fullWidth="false"
                class="text-center w-full sm:w-20 mb-2 sm:mb-0 sm:mx-2 py-2 px-0 cursor-pointer"
              >
                <BoxIcon class="block w-6 h-6 mb-2 mx-auto" /> Laravel
              </Tab>
              <Tab
                :fullWidth="false"
                class="text-center w-full sm:w-20 mb-2 sm:mb-0 sm:mx-2 py-2 px-0 cursor-pointer"
              >
                <InboxIcon class="block w-6 h-6 mb-2 mx-auto" />
                Symfony
              </Tab>
              <Tab
                :fullWidth="false"
                class="text-center w-full sm:w-20 mb-2 sm:mb-0 sm:mx-2 py-2 px-0 cursor-pointer"
              >
                <ActivityIcon class="block w-6 h-6 mb-2 mx-auto" />
                Bootstrap
              </Tab>
            </TabList>
            <TabPanels class="mt-8">
              <TabPanel>
                <div class="flex flex-col sm:flex-row items-center">
                  <div class="mr-auto">
                    <a href="" class="font-medium">Wordpress Template</a>
                    <div class="text-slate-500 mt-1">HTML, PHP, Mysql</div>
                  </div>
                  <div class="w-full sm:w-auto flex items-center mt-3 sm:mt-0">
                    <div class="bg-success/20 text-success rounded px-2 mr-5">
                      +20%
                    </div>
                    <div class="progress h-1 mt-2 sm:w-40">
                      <div
                        class="progress-bar w-1/2 bg-primary"
                        role="progressbar"
                        aria-valuenow="0"
                        aria-valuemin="0"
                        aria-valuemax="100"
                      ></div>
                    </div>
                  </div>
                </div>
                <div class="flex flex-col sm:flex-row items-center mt-5">
                  <div class="mr-auto">
                    <a href="" class="font-medium">Laravel Template</a>
                    <div class="text-slate-500 mt-1">PHP, Mysql</div>
                  </div>
                  <div class="w-full sm:w-auto flex items-center mt-3 sm:mt-0">
                    <div class="bg-success/20 text-success rounded px-2 mr-5">
                      +55%
                    </div>
                    <div class="progress h-1 mt-2 sm:w-40">
                      <div
                        class="progress-bar w-2/3 bg-primary"
                        role="progressbar"
                        aria-valuenow="0"
                        aria-valuemin="0"
                        aria-valuemax="100"
                      ></div>
                    </div>
                  </div>
                </div>
                <div class="flex flex-col sm:flex-row items-center mt-5">
                  <div class="mr-auto">
                    <a href="" class="font-medium">Tailwind HTML Template</a>
                    <div class="text-slate-500 mt-1">HTML, CSS, JS</div>
                  </div>
                  <div class="w-full sm:w-auto flex items-center mt-3 sm:mt-0">
                    <div class="bg-success/20 text-success rounded px-2 mr-5">
                      +40%
                    </div>
                    <div class="progress h-1 mt-2 sm:w-40">
                      <div
                        class="progress-bar w-3/4 bg-primary"
                        role="progressbar"
                        aria-valuenow="0"
                        aria-valuemin="0"
                        aria-valuemax="100"
                      ></div>
                    </div>
                  </div>
                </div>
              </TabPanel>
            </TabPanels>
          </div>
        </TabGroup>
        <!-- END: Top Products -->
        <!-- BEGIN: Work In Progress -->
        <TabGroup class="intro-y box col-span-12 2xl:col-span-6">
          <div
            class="flex items-center px-5 py-5 sm:py-0 border-b border-slate-200/60 dark:border-darkmode-400"
          >
            <h2 class="font-medium text-base mr-auto">Work In Progress</h2>
            <Dropdown class="ml-auto sm:hidden">
              <DropdownToggle tag="a" class="w-5 h-5 block" href="javascript:;">
                <MoreHorizontalIcon class="w-5 h-5 text-slate-500" />
              </DropdownToggle>
              <DropdownMenu class="w-40">
                <DropdownContent tag="div">
                  <TabList class="block">
                    <Tab :fullWidth="false" class="dropdown-item cursor-pointer"
                      >New</Tab
                    >
                    <Tab :fullWidth="false" class="dropdown-item cursor-pointer"
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
                <div class="mt-5">
                  <div class="flex">
                    <div class="mr-auto">Tasks In Review</div>
                    <div>70%</div>
                  </div>
                  <div class="progress h-1 mt-2">
                    <div
                      class="progress-bar w-4/5 bg-primary"
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
        <!-- BEGIN: Latest Tasks -->
        <TabGroup class="intro-y box col-span-12 2xl:col-span-6">
          <div
            class="flex items-center px-5 py-5 sm:py-0 border-b border-slate-200/60 dark:border-darkmode-400"
          >
            <h2 class="font-medium text-base mr-auto">Latest Tasks</h2>
            <Dropdown class="ml-auto sm:hidden">
              <DropdownToggle tag="a" class="w-5 h-5 block" href="javascript:;">
                <MoreHorizontalIcon class="w-5 h-5 text-slate-500" />
              </DropdownToggle>
              <DropdownMenu class="w-40">
                <DropdownContent tag="div">
                  <TabList class="block">
                    <Tab :fullWidth="false" class="dropdown-item cursor-pointer"
                      >New</Tab
                    >
                    <Tab :fullWidth="false" class="dropdown-item cursor-pointer"
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
                <div class="flex items-center mt-5">
                  <div
                    class="border-l-2 border-primary dark:border-primary pl-4"
                  >
                    <a href="" class="font-medium">Meeting With Client</a>
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
                    <a href="" class="font-medium">Create New Repository</a>
                    <div class="text-slate-500">11:00 PM</div>
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
        <!-- BEGIN: General Statistics -->
        <div class="intro-y box col-span-12 2xl:col-span-6">
          <div
            class="flex items-center px-5 py-5 sm:py-3 border-b border-slate-200/60 dark:border-darkmode-400"
          >
            <h2 class="font-medium text-base mr-auto">General Statistics</h2>
            <Dropdown class="ml-auto">
              <DropdownToggle
                tag="a"
                class="w-5 h-5 block sm:hidden"
                href="javascript:;"
              >
                <MoreHorizontalIcon class="w-5 h-5 text-slate-500" />
              </DropdownToggle>
              <DropdownToggle
                class="btn btn-outline-secondary font-normal hidden sm:flex"
              >
                Export <ChevronDownIcon class="w-4 h-4 ml-2" />
              </DropdownToggle>
              <DropdownMenu class="w-40">
                <DropdownContent>
                  <DropdownHeader>Export Tools</DropdownHeader>
                  <DropdownDivider />
                  <DropdownItem>
                    <PrinterIcon class="w-4 h-4 mr-2" />
                    Print
                  </DropdownItem>
                  <DropdownItem>
                    <ExternalLinkIcon class="w-4 h-4 mr-2" />
                    Excel
                  </DropdownItem>
                  <DropdownItem>
                    <FileTextIcon class="w-4 h-4 mr-2" />
                    CSV
                  </DropdownItem>
                  <DropdownItem>
                    <ArchiveIcon class="w-4 h-4 mr-2" />
                    PDF
                  </DropdownItem>
                </DropdownContent>
              </DropdownMenu>
            </Dropdown>
          </div>
          <div class="p-5">
            <div class="flex flex-col sm:flex-row items-center">
              <div class="flex flex-wrap sm:flex-nowrap mr-auto">
                <div class="flex items-center mr-5 mb-1 sm:mb-0">
                  <div class="w-2 h-2 bg-pending rounded-full mr-3"></div>
                  <span>Author Sales</span>
                </div>
                <div class="flex items-center mr-5 mb-1 sm:mb-0">
                  <div class="w-2 h-2 bg-primary rounded-full mr-3"></div>
                  <span>Product Profit</span>
                </div>
              </div>
              <Dropdown class="mt-3 sm:mt-0 mr-auto sm:mr-0">
                <DropdownToggle class="btn btn-outline-secondary font-normal">
                  Filter by Month
                  <ChevronDownIcon class="w-4 h-4 ml-2" />
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent class="overflow-y-auto h-32">
                    <DropdownItem>January</DropdownItem>
                    <DropdownItem>February</DropdownItem>
                    <DropdownItem>March</DropdownItem>
                    <DropdownItem>June</DropdownItem>
                    <DropdownItem>July</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
            </div>
            <div class="report-chart mt-8">
              <ReportLineChart :height="212" />
            </div>
          </div>
        </div>
        <!-- END: General Statistics -->
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, provide } from "vue";
import ReportLineChart from "@/components/report-line-chart/Main.vue";

const announcementRef = ref();
const newProjectsRef = ref();
const todaySchedulesRef = ref();

provide("bind[announcementRef]", (el) => {
  announcementRef.value = el;
});

provide("bind[newProjectsRef]", (el) => {
  newProjectsRef.value = el;
});

provide("bind[todaySchedulesRef]", (el) => {
  todaySchedulesRef.value = el;
});

const prevAnnouncement = () => {
  const el = announcementRef.value;
  el.tns.goTo("prev");
};
const nextAnnouncement = () => {
  const el = announcementRef.value;
  el.tns.goTo("next");
};
const prevNewProjects = () => {
  const el = newProjectsRef.value;
  el.tns.goTo("prev");
};
const nextNewProjects = () => {
  const el = newProjectsRef.value;
  el.tns.goTo("next");
};
const prevTodaySchedules = () => {
  const el = todaySchedulesRef.value;
  el.tns.goTo("prev");
};
const nextTodaySchedules = () => {
  const el = todaySchedulesRef.value;
  el.tns.goTo("next");
};
</script>
