<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Change Password</h2>
  </div>
  <div class="grid grid-cols-12 gap-6">
    <!-- BEGIN: Profile Menu -->
    <div
      class="col-span-12 lg:col-span-4 2xl:col-span-3 flex lg:block flex-col-reverse"
    >
      <div class="intro-y box mt-5">
        <div class="relative flex items-center p-5">
          <div class="w-12 h-12 image-fit">
            <img
              alt="Midone Tailwind HTML Admin Template"
              class="rounded-full"
              :src="$f()[0].photos[0]"
            />
          </div>
          <div class="ml-4 mr-auto">
            <div class="font-medium text-base">
              {{ $f()[0].users[0].name }}
            </div>
            <div class="text-slate-500">{{ $f()[0].jobs[0] }}</div>
          </div>
          <Dropdown>
            <DropdownToggle tag="a" class="w-5 h-5 block" href="javascript:;">
              <MoreHorizontalIcon class="w-5 h-5 text-slate-500" />
            </DropdownToggle>
            <DropdownMenu class="w-56">
              <DropdownContent>
                <DropdownHeader> Export Options</DropdownHeader>
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
    </div>
    <!-- END: Profile Menu -->
    <div class="col-span-12 lg:col-span-8 2xl:col-span-9">
      <!-- BEGIN: Change Password -->
      <div class="intro-y box lg:mt-5">
        <div
          class="flex items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Change Password</h2>
        </div>
        <div class="p-5">
          <div>
            <label for="change-password-form-1" class="form-label"
              >Old Password</label
            >
            <input
              id="change-password-form-1"
              type="password"
              class="form-control"
              placeholder="Input text"
            />
          </div>
          <div class="mt-3">
            <label for="change-password-form-2" class="form-label"
              >New Password</label
            >
            <input
              id="change-password-form-2"
              type="password"
              class="form-control"
              placeholder="Input text"
            />
          </div>
          <div class="mt-3">
            <label for="change-password-form-3" class="form-label"
              >Confirm New Password</label
            >
            <input
              id="change-password-form-3"
              type="password"
              class="form-control"
              placeholder="Input text"
            />
          </div>
          <button type="button" class="btn btn-primary mt-4">
            Change Password
          </button>
        </div>
      </div>
      <!-- END: Change Password -->
    </div>
  </div>
</template>
