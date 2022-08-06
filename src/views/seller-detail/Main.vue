<template>
  <div class="intro-y flex flex-col sm:flex-row items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Seller Details</h2>
    <div class="w-full sm:w-auto flex mt-4 sm:mt-0">
      <button class="btn btn-primary shadow-md mr-2">Print</button>
      <Dropdown class="ml-auto sm:ml-0">
        <DropdownToggle class="btn px-2 box">
          <span class="w-5 h-5 flex items-center justify-center">
            <PlusIcon class="w-4 h-4" />
          </span>
        </DropdownToggle>
        <DropdownMenu class="w-40">
          <DropdownContent>
            <DropdownItem>
              <FileIcon class="w-4 h-4 mr-2" /> Export Word
            </DropdownItem>
            <DropdownItem>
              <FileIcon class="w-4 h-4 mr-2" /> Export PDF
            </DropdownItem>
          </DropdownContent>
        </DropdownMenu>
      </Dropdown>
    </div>
  </div>
  <!-- BEGIN: Seller Details -->
  <div class="intro-y grid grid-cols-11 gap-5 mt-5">
    <div class="col-span-12 lg:col-span-4 2xl:col-span-3">
      <div class="box p-5 rounded-md">
        <div
          class="flex items-center border-b border-slate-200/60 dark:border-darkmode-400 pb-5 mb-5"
        >
          <div class="font-medium text-base truncate">User Details</div>
          <a href="" class="flex items-center ml-auto text-primary">
            <EditIcon class="w-4 h-4 mr-2" /> More Details
          </a>
        </div>
        <div class="flex items-center">
          <ClipboardIcon class="w-4 h-4 text-slate-500 mr-2" />
          Unique ID:
          <a href="" class="underline decoration-dotted ml-1"
            >SLR-20220217-2053411933</a
          >
        </div>
        <div class="flex items-center mt-3">
          <UserIcon class="w-4 h-4 text-slate-500 mr-2" /> Name:
          <a href="" class="underline decoration-dotted ml-1">{{
            $f()[0].users[0].name
          }}</a>
        </div>
        <div class="flex items-center mt-3">
          <CalendarIcon class="w-4 h-4 text-slate-500 mr-2" />
          Phone Number: +71828273732
        </div>
        <div class="flex items-center mt-3">
          <MapPinIcon class="w-4 h-4 text-slate-500 mr-2" />
          Address: 260 W. Storm Street New York, NY 10025.
        </div>
        <div
          class="flex items-center border-t border-slate-200/60 dark:border-darkmode-400 pt-5 mt-5 font-medium"
        >
          <button
            type="button"
            class="btn btn-outline-secondary w-full py-1 px-2"
          >
            Message User
          </button>
        </div>
      </div>
      <div class="box p-5 rounded-md mt-5">
        <div
          class="flex items-center border-b border-slate-200/60 dark:border-darkmode-400 pb-5 mb-5"
        >
          <div class="font-medium text-base truncate">Store Details</div>
          <a href="" class="flex items-center ml-auto text-primary">
            <EditIcon class="w-4 h-4 mr-2" /> More Details
          </a>
        </div>
        <div class="flex items-center">
          <ClipboardIcon class="w-4 h-4 text-slate-500 mr-2" />
          Unique ID:
          <a href="" class="underline decoration-dotted ml-1"
            >STR-2053411933-20220217</a
          >
        </div>
        <div class="flex items-center mt-3">
          <ShoppingBagIcon class="w-4 h-4 text-slate-500 mr-2" />
          Name:
          <a href="" class="underline decoration-dotted ml-1">Themeforest</a>
        </div>
        <div class="flex items-center mt-3">
          <CalendarIcon class="w-4 h-4 text-slate-500 mr-2" />
          Phone Number: +71828273732
        </div>
        <div class="flex items-center mt-3">
          <MapPinIcon class="w-4 h-4 text-slate-500 mr-2" />
          Address: 260 W. Storm Street New York, NY 10025.
        </div>
        <div class="flex items-center mt-3">
          <CalendarIcon class="w-4 h-4 text-slate-500 mr-2" />
          Status:
          <span class="bg-success/20 text-success rounded px-2 ml-1"
            >Active</span
          >
        </div>
        <div
          class="flex items-center border-t border-slate-200/60 dark:border-darkmode-400 pt-5 mt-5 font-medium"
        >
          <button
            type="button"
            class="btn btn-outline-secondary w-full py-1 px-2"
          >
            Change Status
          </button>
        </div>
      </div>
      <div class="box p-5 rounded-md mt-5">
        <div
          class="flex items-center border-b border-slate-200/60 dark:border-darkmode-400 pb-5 mb-5"
        >
          <div class="font-medium text-base truncate">Transaction Reports</div>
          <a href="" class="flex items-center ml-auto text-primary">
            <EditIcon class="w-4 h-4 mr-2" /> More Details
          </a>
        </div>
        <div class="flex items-center mt-3">
          <ClipboardIcon class="w-4 h-4 text-slate-500 mr-2" />
          Avg. Daily Transactions:
          <div class="ml-auto">$1,500.00</div>
        </div>
        <div class="flex items-center mt-3">
          <ClipboardIcon class="w-4 h-4 text-slate-500 mr-2" />
          Avg. Monthly Transactions:
          <div class="ml-auto">$42,500.00</div>
        </div>
        <div class="flex items-center mt-3">
          <ClipboardIcon class="w-4 h-4 text-slate-500 mr-2" />
          Avg. Annually Transactions:
          <div class="ml-auto">$1,012,500.00</div>
        </div>
        <div class="flex items-center mt-3">
          <StarIcon class="w-4 h-4 text-slate-500 mr-2" /> Average Rating:
          <div class="ml-auto">4.9+</div>
        </div>
        <div class="flex items-center mt-3">
          <AlbumIcon class="w-4 h-4 text-slate-500 mr-2" /> Total Products:
          <div class="ml-auto">7,120</div>
        </div>
        <div class="flex items-center mt-3">
          <ArchiveIcon class="w-4 h-4 text-slate-500 mr-2" />
          Total Transactions:
          <div class="ml-auto">1.512.001</div>
        </div>
        <div class="flex items-center mt-3">
          <MonitorIcon class="w-4 h-4 text-slate-500 mr-2" />
          Active Disputes:
          <div class="ml-auto">1</div>
        </div>
      </div>
    </div>
    <div class="col-span-12 lg:col-span-7 2xl:col-span-8">
      <div class="grid grid-cols-12 gap-5">
        <div
          v-for="(faker, fakerKey) in $_.take($f(), 9)"
          :key="fakerKey"
          class="intro-y col-span-12 sm:col-span-6 2xl:col-span-4"
        >
          <div class="box">
            <div class="p-5">
              <div
                class="h-40 2xl:h-56 image-fit rounded-md overflow-hidden before:block before:absolute before:w-full before:h-full before:top-0 before:left-0 before:z-10 before:bg-gradient-to-t before:from-black before:to-black/10"
              >
                <img
                  alt="Midone - HTML Admin Template"
                  class="rounded-md"
                  :src="faker.images[0]"
                />
                <template v-if="faker.trueFalse[0]">
                  <span
                    class="absolute top-0 bg-pending/80 text-white text-xs m-5 px-2 py-1 rounded z-10"
                    >Featured</span
                  >
                </template>
                <div class="absolute bottom-0 text-white px-5 pb-6 z-10">
                  <a href="" class="block font-medium text-base">{{
                    faker.products[0].name
                  }}</a>
                  <span class="text-white/90 text-xs mt-3">{{
                    faker.products[0].category
                  }}</span>
                </div>
              </div>
              <div class="text-slate-600 dark:text-slate-500 mt-5">
                <div class="flex items-center">
                  <LinkIcon class="w-4 h-4 mr-2" /> Price: ${{
                    faker.totals[0]
                  }}
                </div>
                <div class="flex items-center mt-2">
                  <LayersIcon class="w-4 h-4 mr-2" /> Remaining Stock:
                  {{ faker.stocks[0] }}
                </div>
                <div class="flex items-center mt-2">
                  <CheckSquareIcon class="w-4 h-4 mr-2" />
                  Status: {{ faker.trueFalse[0] ? "Active" : "Inactive" }}
                </div>
              </div>
            </div>
            <div
              class="flex justify-center lg:justify-end items-center p-5 border-t border-slate-200/60 dark:border-darkmode-400"
            >
              <a
                class="flex items-center text-primary mr-auto"
                href="javascript:;"
              >
                <EyeIcon class="w-4 h-4 mr-1" /> Preview
              </a>
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
          </div>
        </div>
      </div>
      <!-- BEGIN: Pagination -->
      <div
        class="intro-y col-span-11 flex flex-wrap sm:flex-row sm:flex-nowrap items-center mt-6"
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
  </div>
  <!-- END: Seller Details -->
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
