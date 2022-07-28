<template>
  <h2 class="intro-y text-lg font-medium mt-10">Product List</h2>
  <div class="grid grid-cols-12 gap-6 mt-5">
    <div
      class="intro-y col-span-12 flex flex-wrap sm:flex-nowrap items-center mt-2"
    >
      <button class="btn btn-primary shadow-md mr-2">Add New Product</button>
      <Dropdown>
        <DropdownToggle class="btn px-2 box">
          <span class="w-5 h-5 flex items-center justify-center">
            <PlusIcon class="w-4 h-4" />
          </span>
        </DropdownToggle>
        <DropdownMenu class="w-40">
          <DropdownContent>
            <DropdownItem>
              <PrinterIcon class="w-4 h-4 mr-2" /> Print
            </DropdownItem>
            <DropdownItem>
              <FileTextIcon class="w-4 h-4 mr-2" /> Export to Excel
            </DropdownItem>
            <DropdownItem>
              <FileTextIcon class="w-4 h-4 mr-2" /> Export to PDF
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
    <!-- BEGIN: Data List -->
    <div class="intro-y col-span-12 overflow-auto lg:overflow-visible">
      <table class="table table-report -mt-2">
        <thead>
          <tr>
            <th class="whitespace-nowrap">IMAGES</th>
            <th class="whitespace-nowrap">PRODUCT NAME</th>
            <th class="text-center whitespace-nowrap">STOCK</th>
            <th class="text-center whitespace-nowrap">PRICE</th>
            <th class="text-center whitespace-nowrap">STATUS</th>
            <th class="text-center whitespace-nowrap">ACTIONS</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(faker, fakerKey) in $_.take($f(), 9)"
            :key="fakerKey"
            class="intro-x"
          >
            <td class="w-40">
              <div class="flex">
                <div class="w-10 h-10 image-fit zoom-in">
                  <Tippy
                    tag="img"
                    alt="Midone Tailwind HTML Admin Template"
                    class="rounded-full"
                    :src="faker.images[0]"
                    :content="`Uploaded at ${faker.dates[0]}`"
                  />
                </div>
                <div class="w-10 h-10 image-fit zoom-in -ml-5">
                  <Tippy
                    tag="img"
                    alt="Midone Tailwind HTML Admin Template"
                    class="rounded-full"
                    :src="faker.images[1]"
                    :content="`Uploaded at ${faker.dates[1]}`"
                  />
                </div>
                <div class="w-10 h-10 image-fit zoom-in -ml-5">
                  <Tippy
                    tag="img"
                    alt="Midone Tailwind HTML Admin Template"
                    class="rounded-full"
                    :src="faker.images[2]"
                    :content="`Uploaded at ${faker.dates[2]}`"
                  />
                </div>
              </div>
            </td>
            <td>
              <a href="" class="font-medium whitespace-nowrap">{{
                faker.products[0].name
              }}</a>
              <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">
                {{ faker.products[0].category }}
              </div>
            </td>
            <td class="text-center">{{ faker.stocks[0] }}</td>
            <td class="text-center">${{ faker.totals[0] }}</td>
            <td class="w-40">
              <div
                class="flex items-center justify-center"
                :class="{
                  'text-success': faker.trueFalse[0],
                  'text-danger': !faker.trueFalse[0],
                }"
              >
                <CheckSquareIcon class="w-4 h-4 mr-2" />
                {{ faker.trueFalse[0] ? "Active" : "Inactive" }}
              </div>
            </td>
            <td class="table-report__action w-56">
              <div class="flex justify-center items-center">
                <a class="flex items-center mr-3" href="javascript:;">
                  <CheckSquareIcon class="w-4 h-4 mr-1" /> Edit
                </a>
                <a
                  class="flex items-center text-danger"
                  href="javascript:;"
                  @click="deleteConfirmationModal = true"
                >
                  <Trash2Icon class="w-4 h-4 mr-1" /> Delete
                </a>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- END: Data List -->
    <!-- BEGIN: Pagination -->
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
  <!-- BEGIN: Delete Confirmation Modal -->
  <Modal
    :show="deleteConfirmationModal"
    @hidden="deleteConfirmationModal = false"
  >
    <ModalBody class="p-0">
      <div class="p-5 text-center">
        <XCircleIcon class="w-16 h-16 text-danger mx-auto mt-3" />
        <div class="text-3xl mt-5">Are you sure?</div>
        <div class="text-slate-500 mt-2">
          Do you really want to delete these records? <br />This process cannot
          be undone.
        </div>
      </div>
      <div class="px-5 pb-8 text-center">
        <button
          type="button"
          @click="deleteConfirmationModal = false"
          class="btn btn-outline-secondary w-24 mr-1"
        >
          Cancel
        </button>
        <button type="button" class="btn btn-danger w-24">Delete</button>
      </div>
    </ModalBody>
  </Modal>
  <!-- END: Delete Confirmation Modal -->
</template>

<script setup>
import { ref } from "vue";

const deleteConfirmationModal = ref(false);
</script>
