<template>
  <div class="intro-y flex flex-col sm:flex-row items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Point of Sale</h2>
    <div class="w-full sm:w-auto flex mt-4 sm:mt-0">
      <a
        href="javascript:;"
        @click="newOrderModal = true"
        class="btn btn-primary shadow-md mr-2"
        >New Order</a
      >
      <Dropdown class="pos-dropdown ml-auto sm:ml-0">
        <DropdownToggle class="btn px-2 box">
          <span class="w-5 h-5 flex items-center justify-center">
            <ChevronDownIcon class="w-4 h-4" />
          </span>
        </DropdownToggle>
        <DropdownMenu class="pos-dropdown__dropdown-menu">
          <DropdownContent>
            <DropdownItem>
              <ActivityIcon class="w-4 h-4 mr-2" />
              <span class="truncate"
                >INV-0206020 - {{ $f()[3].users[0].name }}</span
              >
            </DropdownItem>
            <DropdownItem>
              <ActivityIcon class="w-4 h-4 mr-2" />
              <span class="truncate"
                >INV-0206022 - {{ $f()[4].users[0].name }}</span
              >
            </DropdownItem>
            <DropdownItem>
              <ActivityIcon class="w-4 h-4 mr-2" />
              <span class="truncate"
                >INV-0206021 - {{ $f()[5].users[0].name }}</span
              >
            </DropdownItem>
          </DropdownContent>
        </DropdownMenu>
      </Dropdown>
    </div>
  </div>
  <div class="intro-y grid grid-cols-12 gap-5 mt-5">
    <!-- BEGIN: Item List -->
    <div class="intro-y col-span-12 lg:col-span-8">
      <div class="lg:flex intro-y">
        <div class="relative">
          <input
            type="text"
            class="form-control py-3 px-4 w-full lg:w-64 box pr-10"
            placeholder="Search item..."
          />
          <SearchIcon
            class="w-4 h-4 absolute my-auto inset-y-0 mr-3 right-0 text-slate-500"
          />
        </div>
        <select
          class="form-select py-3 px-4 box w-full lg:w-auto mt-3 lg:mt-0 ml-auto"
        >
          <option>Sort By</option>
          <option>A to Z</option>
          <option>Z to A</option>
          <option>Lowest Price</option>
          <option>Highest Price</option>
        </select>
      </div>
      <div class="grid grid-cols-12 gap-5 mt-5">
        <div
          class="col-span-12 sm:col-span-4 2xl:col-span-3 box p-5 cursor-pointer zoom-in"
        >
          <div class="font-medium text-base">Soup</div>
          <div class="text-slate-500">5 Items</div>
        </div>
        <div
          class="col-span-12 sm:col-span-4 2xl:col-span-3 box bg-primary p-5 cursor-pointer zoom-in"
        >
          <div class="font-medium text-base text-white">Pancake & Toast</div>
          <div class="text-white text-opacity-80 dark:text-slate-500">
            8 Items
          </div>
        </div>
        <div
          class="col-span-12 sm:col-span-4 2xl:col-span-3 box p-5 cursor-pointer zoom-in"
        >
          <div class="font-medium text-base">Pasta</div>
          <div class="text-slate-500">4 Items</div>
        </div>
        <div
          class="col-span-12 sm:col-span-4 2xl:col-span-3 box p-5 cursor-pointer zoom-in"
        >
          <div class="font-medium text-base">Waffle</div>
          <div class="text-slate-500">3 Items</div>
        </div>
        <div
          class="col-span-12 sm:col-span-4 2xl:col-span-3 box p-5 cursor-pointer zoom-in"
        >
          <div class="font-medium text-base">Snacks</div>
          <div class="text-slate-500">8 Items</div>
        </div>
        <div
          class="col-span-12 sm:col-span-4 2xl:col-span-3 box p-5 cursor-pointer zoom-in"
        >
          <div class="font-medium text-base">Deserts</div>
          <div class="text-slate-500">8 Items</div>
        </div>
        <div
          class="col-span-12 sm:col-span-4 2xl:col-span-3 box p-5 cursor-pointer zoom-in"
        >
          <div class="font-medium text-base">Beverage</div>
          <div class="text-slate-500">9 Items</div>
        </div>
      </div>
      <div class="grid grid-cols-12 gap-5 mt-5 pt-5 border-t">
        <a
          v-for="(faker, fakerKey) in $_.take($f(), 8)"
          :key="fakerKey"
          href="javascript:;"
          @click="addItemModal = true"
          class="intro-y block col-span-12 sm:col-span-4 2xl:col-span-3"
        >
          <div class="box rounded-md p-3 relative zoom-in">
            <div
              class="flex-none relative block before:block before:w-full before:pt-[100%]"
            >
              <div class="absolute top-0 left-0 w-full h-full image-fit">
                <img
                  alt="Midone Tailwind HTML Admin Template"
                  class="rounded-md"
                  :src="faker.foods[0].image"
                />
              </div>
            </div>
            <div class="block font-medium text-center truncate mt-3">
              {{ faker.foods[0].name }}
            </div>
          </div>
        </a>
      </div>
    </div>
    <!-- END: Item List -->
    <!-- BEGIN: Ticket -->
    <TabGroup class="col-span-12 lg:col-span-4">
      <div class="intro-y pr-1">
        <div class="box p-2">
          <TabList class="nav-pills">
            <Tab class="w-full py-2" tag="button">Ticket</Tab>
            <Tab class="w-full py-2" tag="button">Details</Tab>
          </TabList>
        </div>
      </div>
      <TabPanels>
        <TabPanel>
          <div class="box p-2 mt-5">
            <a
              v-for="(faker, fakerKey) in $_.take($f(), 5)"
              :key="fakerKey"
              href="javascript:;"
              @click="addItemModal = true"
              class="flex items-center p-3 cursor-pointer transition duration-300 ease-in-out bg-white dark:bg-darkmode-600 hover:bg-slate-100 dark:hover:bg-darkmode-400 rounded-md"
            >
              <div class="max-w-[50%] truncate mr-1">
                {{ faker.foods[0].name }}
              </div>
              <div class="text-slate-500">x 1</div>
              <EditIcon class="w-4 h-4 text-slate-500 ml-2" />
              <div class="ml-auto font-medium">${{ faker.totals[0] }}</div>
            </a>
          </div>
          <div class="box flex p-5 mt-5">
            <input
              type="text"
              class="form-control py-3 px-4 w-full bg-slate-100 border-slate-200/60 pr-10"
              placeholder="Use coupon code..."
            />
            <button class="btn btn-primary ml-2">Apply</button>
          </div>
          <div class="box p-5 mt-5">
            <div class="flex">
              <div class="mr-auto">Subtotal</div>
              <div class="font-medium">$250</div>
            </div>
            <div class="flex mt-4">
              <div class="mr-auto">Discount</div>
              <div class="font-medium text-danger">-$20</div>
            </div>
            <div class="flex mt-4">
              <div class="mr-auto">Tax</div>
              <div class="font-medium">15%</div>
            </div>
            <div
              class="flex mt-4 pt-4 border-t border-slate-200/60 dark:border-darkmode-400"
            >
              <div class="mr-auto font-medium text-base">Total Charge</div>
              <div class="font-medium text-base">$220</div>
            </div>
          </div>
          <div class="flex mt-5">
            <button
              class="btn w-32 border-slate-300 dark:border-darkmode-400 text-slate-500"
            >
              Clear Items
            </button>
            <button class="btn btn-primary w-32 shadow-md ml-auto">
              Charge
            </button>
          </div>
        </TabPanel>
        <TabPanel>
          <div class="box p-5 mt-5">
            <div
              class="flex items-center border-b border-slate-200 dark:border-darkmode-400 pb-5"
            >
              <div>
                <div class="text-slate-500">Time</div>
                <div class="mt-1">02/06/20 02:10 PM</div>
              </div>
              <ClockIcon class="w-4 h-4 text-slate-500 ml-auto" />
            </div>
            <div
              class="flex items-center border-b border-slate-200 dark:border-darkmode-400 py-5"
            >
              <div>
                <div class="text-slate-500">Customer</div>
                <div class="mt-1">{{ $f()[0].users[0].name }}</div>
              </div>
              <UserIcon class="w-4 h-4 text-slate-500 ml-auto" />
            </div>
            <div
              class="flex items-center border-b border-slate-200 dark:border-darkmode-400 py-5"
            >
              <div>
                <div class="text-slate-500">People</div>
                <div class="mt-1">3</div>
              </div>
              <UsersIcon class="w-4 h-4 text-slate-500 ml-auto" />
            </div>
            <div class="flex items-center pt-5">
              <div>
                <div class="text-slate-500">Table</div>
                <div class="mt-1">21</div>
              </div>
              <MicIcon class="w-4 h-4 text-slate-500 ml-auto" />
            </div>
          </div>
        </TabPanel>
      </TabPanels>
    </TabGroup>
    <!-- END: Ticket -->
  </div>
  <!-- BEGIN: New Order Modal -->
  <Modal :show="newOrderModal" @hidden="newOrderModal = false">
    <ModalHeader>
      <h2 class="font-medium text-base mr-auto">New Order</h2>
    </ModalHeader>
    <ModalBody class="grid grid-cols-12 gap-4 gap-y-3">
      <div class="col-span-12">
        <label for="pos-form-1" class="form-label">Name</label>
        <input
          id="pos-form-1"
          type="text"
          class="form-control flex-1"
          placeholder="Customer name"
        />
      </div>
      <div class="col-span-12">
        <label for="pos-form-2" class="form-label">Table</label>
        <input
          id="pos-form-2"
          type="text"
          class="form-control flex-1"
          placeholder="Customer table"
        />
      </div>
      <div class="col-span-12">
        <label for="pos-form-3" class="form-label">Number of People</label>
        <input
          id="pos-form-3"
          type="text"
          class="form-control flex-1"
          placeholder="People"
        />
      </div>
    </ModalBody>
    <ModalFooter class="text-right">
      <button
        type="button"
        @click="newOrderModal = false"
        class="btn btn-outline-secondary w-32 mr-1"
      >
        Cancel
      </button>
      <button type="button" class="btn btn-primary w-32">Create Ticket</button>
    </ModalFooter>
  </Modal>
  <!-- END: New Order Modal -->
  <!-- BEGIN: Add Item Modal -->
  <Modal :show="addItemModal" @hidden="addItemModal = false">
    <ModalHeader>
      <h2 class="font-medium text-base mr-auto">
        {{ $f()[0].foods[0].name }}
      </h2>
    </ModalHeader>
    <ModalBody class="grid grid-cols-12 gap-4 gap-y-3">
      <div class="col-span-12">
        <label for="pos-form-4" class="form-label">Quantity</label>
        <div class="flex flex-1">
          <button
            type="button"
            class="btn w-12 border-slate-200 bg-slate-100 dark:bg-darkmode-700 dark:border-darkmode-500 text-slate-500 mr-1"
          >
            -
          </button>
          <input
            id="pos-form-4"
            type="text"
            class="form-control w-24 text-center"
            placeholder="Item quantity"
            value="2"
          />
          <button
            type="button"
            class="btn w-12 border-slate-200 bg-slate-100 dark:bg-darkmode-700 dark:border-darkmode-500 text-slate-500 ml-1"
          >
            +
          </button>
        </div>
      </div>
      <div class="col-span-12">
        <label for="pos-form-5" class="form-label">Notes</label>
        <textarea
          id="pos-form-5"
          class="form-control"
          placeholder="Item notes"
        ></textarea>
      </div>
    </ModalBody>
    <ModalFooter class="text-right">
      <button
        type="button"
        @click="addItemModal = false"
        class="btn btn-outline-secondary w-24 mr-1"
      >
        Cancel
      </button>
      <button type="button" class="btn btn-primary w-24">Add Item</button>
    </ModalFooter>
  </Modal>
  <!-- END: Add Item Modal -->
</template>

<script setup>
import { ref } from "vue";

const newOrderModal = ref(false);
const addItemModal = ref(false);
</script>
