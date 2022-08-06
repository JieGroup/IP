<template>
  <div class="intro-y flex flex-col sm:flex-row items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Transaction Details</h2>
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
              <FileIcon class="w-4 h-4 mr-2" /> Export to PDF
            </DropdownItem>
          </DropdownContent>
        </DropdownMenu>
      </Dropdown>
    </div>
  </div>
  <!-- BEGIN: Transaction Details -->
  <div class="intro-y grid grid-cols-11 gap-5 mt-5">
    <div class="col-span-12 lg:col-span-4 2xl:col-span-3">
      <div class="box p-5 rounded-md">
        <div
          class="flex items-center border-b border-slate-200/60 dark:border-darkmode-400 pb-5 mb-5"
        >
          <div class="font-medium text-base truncate">Transaction Details</div>
          <a href="" class="flex items-center ml-auto text-primary">
            <EditIcon class="w-4 h-4 mr-2" /> Change Status
          </a>
        </div>
        <div class="flex items-center">
          <ClipboardIcon class="w-4 h-4 text-slate-500 mr-2" />
          Invoice:
          <a href="" class="underline decoration-dotted ml-1"
            >INV/20220217/MPL/2053411933</a
          >
        </div>
        <div class="flex items-center mt-3">
          <CalendarIcon class="w-4 h-4 text-slate-500 mr-2" />
          Purchase Date: 24 March 2022
        </div>
        <div class="flex items-center mt-3">
          <ClockIcon class="w-4 h-4 text-slate-500 mr-2" />
          Transaction Status:
          <span class="bg-success/20 text-success rounded px-2 ml-1"
            >Completed</span
          >
        </div>
      </div>
      <div class="box p-5 rounded-md mt-5">
        <div
          class="flex items-center border-b border-slate-200/60 dark:border-darkmode-400 pb-5 mb-5"
        >
          <div class="font-medium text-base truncate">Buyer Details</div>
          <a href="" class="flex items-center ml-auto text-primary">
            <EditIcon class="w-4 h-4 mr-2" /> View Details
          </a>
        </div>
        <div class="flex items-center">
          <ClipboardIcon class="w-4 h-4 text-slate-500 mr-2" />
          Name:
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
      </div>
      <div class="box p-5 rounded-md mt-5">
        <div
          class="flex items-center border-b border-slate-200/60 dark:border-darkmode-400 pb-5 mb-5"
        >
          <div class="font-medium text-base truncate">Payment Details</div>
        </div>
        <div class="flex items-center">
          <ClipboardIcon class="w-4 h-4 text-slate-500 mr-2" />
          Payment Method:
          <div class="ml-auto">Direct bank transfer</div>
        </div>
        <div class="flex items-center mt-3">
          <CreditCardIcon class="w-4 h-4 text-slate-500 mr-2" />
          Total Price (2 items):
          <div class="ml-auto">$12,500.00</div>
        </div>
        <div class="flex items-center mt-3">
          <CreditCardIcon class="w-4 h-4 text-slate-500 mr-2" />
          Total Shipping Cost (800 gr):
          <div class="ml-auto">$1,500.00</div>
        </div>
        <div class="flex items-center mt-3">
          <CreditCardIcon class="w-4 h-4 text-slate-500 mr-2" />
          Shipping Insurance:
          <div class="ml-auto">$600.00</div>
        </div>
        <div
          class="flex items-center border-t border-slate-200/60 dark:border-darkmode-400 pt-5 mt-5 font-medium"
        >
          <CreditCardIcon class="w-4 h-4 text-slate-500 mr-2" />
          Grand Total:
          <div class="ml-auto">$15,000.00</div>
        </div>
      </div>
      <div class="box p-5 rounded-md mt-5">
        <div
          class="flex items-center border-b border-slate-200/60 dark:border-darkmode-400 pb-5 mb-5"
        >
          <div class="font-medium text-base truncate">Shipping Information</div>
          <a href="" class="flex items-center ml-auto text-primary">
            <MapPinIcon class="w-4 h-4 mr-2" /> Tracking Info
          </a>
        </div>
        <div class="flex items-center">
          <ClipboardIcon class="w-4 h-4 text-slate-500 mr-2" />
          Courier: Left4code Express
        </div>
        <div class="flex items-center mt-3">
          <CalendarIcon class="w-4 h-4 text-slate-500 mr-2" />
          Tracking Number: 003005580322
          <CopyIcon class="w-4 h-4 text-slate-500 ml-2" />
        </div>
        <div class="flex items-center mt-3">
          <MapPinIcon class="w-4 h-4 text-slate-500 mr-2" />
          Address: 260 W. Storm Street New York, NY 10025.
        </div>
      </div>
    </div>
    <div class="col-span-12 lg:col-span-7 2xl:col-span-8">
      <div class="box p-5 rounded-md">
        <div
          class="flex items-center border-b border-slate-200/60 dark:border-darkmode-400 pb-5 mb-5"
        >
          <div class="font-medium text-base truncate">Order Details</div>
          <a href="" class="flex items-center ml-auto text-primary">
            <PlusIcon class="w-4 h-4 mr-2" /> Add Notes
          </a>
        </div>
        <div class="overflow-auto lg:overflow-visible -mt-3">
          <table class="table table-striped">
            <thead>
              <tr>
                <th class="whitespace-nowrap !py-5">Product</th>
                <th class="whitespace-nowrap text-right">Unit Price</th>
                <th class="whitespace-nowrap text-right">Qty</th>
                <th class="whitespace-nowrap text-right">Total</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(faker, fakerKey) in $_.take($f(), 8)" :key="fakerKey">
                <td class="!py-4">
                  <div class="flex items-center">
                    <div class="w-10 h-10 image-fit zoom-in">
                      <Tippy
                        tag="img"
                        alt="Midone - HTML Admin Template"
                        class="rounded-lg border-2 border-white shadow-md tooltip"
                        :src="faker.images[0]"
                        :content="`Uploaded at ${faker.dates[0]}`"
                      />
                    </div>
                    <a href="" class="font-medium whitespace-nowrap ml-4">{{
                      faker.products[0].name
                    }}</a>
                  </div>
                </td>
                <td class="text-right">${{ faker.totals[0] + ",000.00" }}</td>
                <td class="text-right">2</td>
                <td class="text-right">
                  ${{ faker.totals[0] * 2 + ",000.00" }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
  <!-- END: Transaction Details -->
</template>
