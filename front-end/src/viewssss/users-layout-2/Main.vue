<template>
  <h2 class="intro-y text-lg font-medium mt-10">Users Layout</h2>
  <div class="grid grid-cols-12 gap-6 mt-5">
    <div
      class="intro-y col-span-12 flex flex-wrap sm:flex-nowrap items-center mt-2"
    >
      <button class="btn btn-primary shadow-md mr-2">Add New User</button>
      <Dropdown>
        <DropdownToggle class="btn px-2 box">
          <span class="w-5 h-5 flex items-center justify-center">
            <PlusIcon class="w-4 h-4" />
          </span>
        </DropdownToggle>
        <DropdownMenu class="w-40">
          <DropdownContent>
            <DropdownItem>
              <UsersIcon class="w-4 h-4 mr-2" /> Add Group
            </DropdownItem>
            <DropdownItem>
              <MessageCircleIcon class="w-4 h-4 mr-2" /> Send Message
            </DropdownItem>
          </DropdownContent>
        </DropdownMenu>
      </Dropdown>
      <div class="hidden md:block mx-auto text-slate-500">
        Showing 1 to 10 of 150 entries
      </div>
      <div class="w-full sm:w-auto mt-3 sm:mt-0 sm:ml-auto md:ml-0">
        <div class="w-56 relative text-slate-500">
          <input
            type="text"
            class="form-control w-56 box pr-10"
            placeholder="Search..."
          />
          <SearchIcon class="w-4 h-4 absolute my-auto inset-y-0 mr-3 right-0" />
        </div>
      </div>
    </div>
    <!-- BEGIN: Users Layout -->
    <div
      v-for="(faker, fakerKey) in $f()"
      :key="fakerKey"
      class="intro-y col-span-12 md:col-span-6"
    >
      <div class="box">
        <div class="flex flex-col lg:flex-row items-center p-5">
          <div class="w-24 h-24 lg:w-12 lg:h-12 image-fit lg:mr-1">
            <img
              alt="Midone Tailwind HTML Admin Template"
              class="rounded-full"
              :src="faker.photos[0]"
            />
          </div>
          <div class="lg:ml-2 lg:mr-auto text-center lg:text-left mt-3 lg:mt-0">
            <a href="" class="font-medium">{{ faker.users[0].name }}</a>
            <div class="text-slate-500 text-xs mt-0.5">
              {{ faker.jobs[0] }}
            </div>
          </div>
          <div class="flex mt-4 lg:mt-0">
            <button class="btn btn-primary py-1 px-2 mr-2">Message</button>
            <button class="btn btn-outline-secondary py-1 px-2">Profile</button>
          </div>
        </div>
      </div>
    </div>
    <!-- BEGIN: Users Layout -->
    <!-- END: Pagination -->
    <div
      class="intro-y col-span-12 flex flex-wrap sm:flex-row sm:flex-nowrap items-center"
    >
      <nav class="w-full sm:w-auto sm:mr-auto">
        <ul class="pagination">
          <li class="page-item">
            <a class="page-link" href="#">
              <ChevronsLeftIcon class="w-4 h-4" />
            </a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">
              <ChevronLeftIcon class="w-4 h-4" />
            </a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">...</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">1</a>
          </li>
          <li class="page-item active">
            <a class="page-link" href="#">2</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">3</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">...</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">
              <ChevronRightIcon class="w-4 h-4" />
            </a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">
              <ChevronsRightIcon class="w-4 h-4" />
            </a>
          </li>
        </ul>
      </nav>
      <select class="w-20 form-select box mt-3 sm:mt-0">
        <option>10</option>
        <option>25</option>
        <option>35</option>
        <option>50</option>
      </select>
    </div>
    <!-- END: Pagination -->
  </div>
</template>
