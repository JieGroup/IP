<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Dropdown</h2>
  </div>
  <div class="grid grid-cols-12 gap-6 mt-5">
    <div class="col-span-12 lg:col-span-6">
      <!-- BEGIN: Basic Dropdown -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Basic Dropdown</h2>
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
            <div class="flex justify-center">
              <Dropdown>
                <DropdownToggle class="btn btn-primary">
                  Show Dropdown
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Dropdown>
                <DropdownToggle class="btn btn-primary">
                  Show Dropdown
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Basic Dropdown -->
      <!-- BEGIN: Header & Footer Dropdown -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Header & Footer Dropdown
          </h2>
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
            <div class="flex justify-center">
              <Dropdown>
                <DropdownToggle class="btn btn-primary">
                  Show Dropdown
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
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Dropdown>
                <DropdownToggle class="btn btn-primary">
                  Show Dropdown
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
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Header & Footer Dropdown -->
      <!-- BEGIN: Icon Dropdown -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Icon Dropdown</h2>
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
            <div class="flex justify-center">
              <Dropdown>
                <DropdownToggle class="btn btn-primary">
                  Show Dropdown
                </DropdownToggle>
                <DropdownMenu class="w-48">
                  <DropdownContent>
                    <DropdownItem>
                      <Edit2Icon class="w-4 h-4 mr-2" /> New Dropdown
                    </DropdownItem>
                    <DropdownItem>
                      <TrashIcon class="w-4 h-4 mr-2" /> Delete Dropdown
                    </DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Dropdown>
                <DropdownToggle class="btn btn-primary">
                  Show Dropdown
                </DropdownToggle>
                <DropdownMenu class="w-48">
                  <DropdownContent>
                    <DropdownItem>
                      <Edit2Icon class="w-4 h-4 mr-2" /> New Dropdown
                    </DropdownItem>
                    <DropdownItem>
                      <TrashIcon class="w-4 h-4 mr-2" /> Delete Dropdown
                    </DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Icon Dropdown -->
      <!-- BEGIN: Dropdown with close button -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Dropdown with close button
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
              <Dropdown
                class="inline-block"
                placement="bottom-start"
                v-slot="{ dismiss }"
              >
                <DropdownToggle class="btn btn-primary">
                  Filter Dropdown
                  <ChevronDownIcon class="w-4 h-4 ml-2" />
                </DropdownToggle>
                <DropdownMenu>
                  <DropdownContent tag="div">
                    <div class="p-2">
                      <div>
                        <div class="text-xs">From</div>
                        <input
                          type="text"
                          class="form-control mt-2 flex-1"
                          placeholder="example@gmail.com"
                        />
                      </div>
                      <div class="mt-3">
                        <div class="text-xs">To</div>
                        <input
                          type="text"
                          class="form-control mt-2 flex-1"
                          placeholder="example@gmail.com"
                        />
                      </div>
                      <div class="flex items-center mt-3">
                        <button
                          @click="dismiss"
                          class="btn btn-secondary w-32 ml-auto"
                        >
                          Close
                        </button>
                        <button class="btn btn-primary w-32 ml-2">
                          Search
                        </button>
                      </div>
                    </div>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div class="text-center">
                <Dropdown
                  class="inline-block"
                  placement="bottom-start"
                  v-slot="{ dismiss }"
                >
                  <DropdownToggle class="btn btn-primary">
                    Filter Dropdown
                    <ChevronDownIcon class="w-4 h-4 ml-2" />
                  </DropdownToggle>
                  <DropdownMenu>
                    <DropdownContent tag="div">
                      <div class="p-2">
                        <div>
                          <div class="text-xs">From</div>
                          <input
                            type="text"
                            class="form-control mt-2 flex-1"
                            placeholder="example@gmail.com"
                          />
                        </div>
                        <div class="mt-3">
                          <div class="text-xs">To</div>
                          <input
                            type="text"
                            class="form-control mt-2 flex-1"
                            placeholder="example@gmail.com"
                          />
                        </div>
                        <div class="flex items-center mt-3">
                          <button
                            @click="dismiss"
                            class="btn btn-secondary w-32 ml-auto"
                          >
                            Close
                          </button>
                          <button class="btn btn-primary w-32 ml-2">
                            Search
                          </button>
                        </div>
                      </div>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
              </div>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Dropdown with close button -->
      <!-- BEGIN: Scrolled Dropdown -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Scrolled Dropdown</h2>
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
            <div class="flex justify-center">
              <Dropdown>
                <DropdownToggle class="btn btn-primary">
                  Show Dropdown
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
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Dropdown>
                <DropdownToggle class="btn btn-primary">
                  Show Dropdown
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
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Scrolled Dropdown -->
      <!-- BEGIN: Header & Icon Dropdown -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Header & Icon Dropdown</h2>
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
            <div class="flex justify-center">
              <Dropdown>
                <DropdownToggle class="btn btn-primary">
                  Show Dropdown
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
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <Dropdown>
                <DropdownToggle class="btn btn-primary">
                  Show Dropdown
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
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Header & Icon Dropdown -->
      <!-- BEGIN: Dropdown Placement -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Dropdown Placement</h2>
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
            <div class="text-center">
              <Dropdown class="inline-block" placement="top-start">
                <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                  Top Start
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <Dropdown class="inline-block" placement="top">
                <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                  Top
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <Dropdown class="inline-block" placement="top-end">
                <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                  Top End
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <Dropdown class="inline-block" placement="right-start">
                <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                  Right Start
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <Dropdown class="inline-block" placement="right">
                <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                  Right
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <Dropdown class="inline-block" placement="right-end">
                <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                  Right End
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <Dropdown class="inline-block" placement="bottom-end">
                <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                  Bottom End
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <Dropdown class="inline-block" placement="bottom">
                <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                  Bottom
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <Dropdown class="inline-block" placement="bottom-start">
                <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                  Bottom Start
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <Dropdown class="inline-block" placement="left-start">
                <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                  Left Start
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <Dropdown class="inline-block" placement="left">
                <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                  Left
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <Dropdown class="inline-block" placement="left-end">
                <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                  Left End
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div class="text-center">
                <Dropdown class="inline-block" placement="top-start">
                  <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                    Top Start
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>New Dropdown</DropdownItem>
                      <DropdownItem>Delete Dropdown</DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
                <Dropdown class="inline-block" placement="top">
                  <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                    Top
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>New Dropdown</DropdownItem>
                      <DropdownItem>Delete Dropdown</DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
                <Dropdown class="inline-block" placement="top-end">
                  <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                    Top End
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>New Dropdown</DropdownItem>
                      <DropdownItem>Delete Dropdown</DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
                <Dropdown class="inline-block" placement="right-start">
                  <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                    Right Start
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>New Dropdown</DropdownItem>
                      <DropdownItem>Delete Dropdown</DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
                <Dropdown class="inline-block" placement="right">
                  <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                    Right
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>New Dropdown</DropdownItem>
                      <DropdownItem>Delete Dropdown</DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
                <Dropdown class="inline-block" placement="right-end">
                  <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                    Right End
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>New Dropdown</DropdownItem>
                      <DropdownItem>Delete Dropdown</DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
                <Dropdown class="inline-block" placement="bottom-end">
                  <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                    Bottom End
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>New Dropdown</DropdownItem>
                      <DropdownItem>Delete Dropdown</DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
                <Dropdown class="inline-block" placement="bottom">
                  <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                    Bottom
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>New Dropdown</DropdownItem>
                      <DropdownItem>Delete Dropdown</DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
                <Dropdown class="inline-block" placement="bottom-start">
                  <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                    Bottom Start
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>New Dropdown</DropdownItem>
                      <DropdownItem>Delete Dropdown</DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
                <Dropdown class="inline-block" placement="left-start">
                  <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                    Left Start
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>New Dropdown</DropdownItem>
                      <DropdownItem>Delete Dropdown</DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
                <Dropdown class="inline-block" placement="left">
                  <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                    Left
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>New Dropdown</DropdownItem>
                      <DropdownItem>Delete Dropdown</DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
                <Dropdown class="inline-block" placement="left-end">
                  <DropdownToggle class="btn btn-primary w-32 mr-1 mb-2">
                    Left End
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>New Dropdown</DropdownItem>
                      <DropdownItem>Delete Dropdown</DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
              </div>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Dropdown Placement -->
      <!-- BEGIN: Programmatically Show/Hide Dropdown -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Programmatically Show/Hide Dropdown
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
              <!-- BEGIN: Show Dropdown Toggle -->
              <button
                class="btn btn-primary w-40 mr-1 mb-2"
                @click="programmaticDropdown = true"
              >
                Show
              </button>
              <!-- END: Show Dropdown Toggle -->
              <!-- BEGIN: Hide Dropdown Toggle -->
              <button
                class="btn btn-primary w-40 mr-1 mb-2"
                @click="programmaticDropdown = false"
              >
                Hide
              </button>
              <!-- END: Hide Dropdown Toggle -->
              <!-- BEGIN: Toggle Dropdown Toggle -->
              <button
                class="btn btn-primary w-40 mr-1 mb-2"
                @click="programmaticDropdown = !programmaticDropdown"
              >
                Toggle
              </button>
              <!-- END: Toggle Dropdown Toggle -->
              <!-- BEGIN: Dropdown Content -->
              <Dropdown
                :show="programmaticDropdown"
                @hidden="programmaticDropdown = false"
                class="inline-block"
              >
                <DropdownToggle class="btn btn-primary w-40 mr-1 mb-2">
                  Example Dropdown
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <!-- END: Dropdown Content -->
            </div>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Show Dropdown Toggle -->
              <button
                class="btn btn-primary w-40 mr-1 mb-2"
                @click="programmaticDropdown = true"
              >
                Show
              </button>
              <!-- END: Show Dropdown Toggle -->
              <!-- BEGIN: Hide Dropdown Toggle -->
              <button
                class="btn btn-primary w-40 mr-1 mb-2"
                @click="programmaticDropdown = false"
              >
                Hide
              </button>
              <!-- END: Hide Dropdown Toggle -->
              <!-- BEGIN: Toggle Dropdown Toggle -->
              <button
                class="btn btn-primary w-40 mr-1 mb-2"
                @click="programmaticDropdown = !programmaticDropdown"
              >
                Toggle
              </button>
              <!-- END: Toggle Dropdown Toggle -->
              <!-- BEGIN: Dropdown Content -->
              <Dropdown
                :show="programmaticDropdown"
                @hidden="programmaticDropdown = false"
                class="inline-block"
              >
                <DropdownToggle class="btn btn-primary w-40 mr-1 mb-2">
                  Example Dropdown
                </DropdownToggle>
                <DropdownMenu class="w-40">
                  <DropdownContent>
                    <DropdownItem>New Dropdown</DropdownItem>
                    <DropdownItem>Delete Dropdown</DropdownItem>
                  </DropdownContent>
                </DropdownMenu>
              </Dropdown>
              <!-- END: Dropdown Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Programmatically Show/Hide Dropdown -->
    </div>
    <div class="col-span-12 lg:col-span-6">
      <!-- BEGIN: Component Reference -->
      <div class="intro-y box">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Component Reference</h2>
        </div>
        <div class="p-5">
          <div>
            Dropdowns are built using the
            <span class="text-red-500">`Dropdown`</span>,
            <span class="text-red-500">`DropdownToggle`</span>,
            <span class="text-red-500">`DropdownMenu`</span>,
            <span class="text-red-500">`DropdownContent`</span>,
            <span class="text-red-500">`DropdownItem`</span>,
            <span class="text-red-500">`DropdownHeader`</span>,
            <span class="text-red-500">`DropdownFooter`</span> and
            <span class="text-red-500">`DropdownDivider`</span> components.
          </div>
        </div>
      </div>
      <!-- END: Component Reference -->
      <!-- BEGIN: Component API -->
      <div class="intro-y box mt-5">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Component API</h2>
        </div>
        <div class="p-5">
          <div class="text-base font-medium">Dropdown</div>
          <div class="mt-2">The main Dropdown component.</div>
          <table class="table mt-5">
            <thead>
              <tr>
                <th class="whitespace-nowrap w-24">Prop</th>
                <th class="whitespace-nowrap">Values</th>
                <th class="whitespace-nowrap">Default</th>
                <th class="whitespace-nowrap">Description</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="align-top text-red-500">`show`</td>
                <td class="align-top">`true`, `false`</td>
                <td class="align-top">`false`</td>
                <td class="align-top">
                  <div class="font-medium mb-1">`Boolean`</div>
                  Whether the Dropdown is open or not.
                </td>
              </tr>
              <tr>
                <td class="align-top text-red-500">`placement`</td>
                <td class="align-top">
                  `top-start`, `top`, `top-end`, `right-start`, `right`,
                  `right-end`, `bottom-end`, `bottom`, `bottom-start`,
                  `left-start`, `left`, `left-end`,
                </td>
                <td class="align-top">-</td>
                <td class="align-top">
                  <div class="font-medium mb-1">`String`</div>
                  Dropdown position when displayed.
                </td>
              </tr>
              <tr>
                <td class="align-top text-red-500">`refKey`</td>
                <td class="align-top">-</td>
                <td class="align-top">`null`</td>
                <td class="align-top">
                  <div class="font-medium mb-1">`String`</div>
                  A ref to the Dropdown element.
                </td>
              </tr>
            </tbody>
          </table>
          <table class="table mt-5">
            <thead>
              <tr>
                <th class="whitespace-nowrap w-24">Event</th>
                <th class="whitespace-nowrap">Description</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="align-top text-red-500">`show`</td>
                <td class="align-top">
                  This event fires immediately when the
                  <span class="text-red-500">show</span> instance method is
                  called.
                </td>
              </tr>
              <tr>
                <td class="align-top text-red-500">`shown`</td>
                <td class="align-top">
                  This event is fired when the dropdown has been made visible to
                  the user (will wait for CSS transitions to complete)
                </td>
              </tr>
              <tr>
                <td class="align-top text-red-500">`hide`</td>
                <td class="align-top">
                  This event is fired immediately when the
                  <span class="text-red-500">hide</span> instance method has
                  been called.
                </td>
              </tr>
              <tr>
                <td class="align-top text-red-500">`hidden`</td>
                <td class="align-top">
                  This event is fired when the dropdown has finished being
                  hidden from the user (will wait for CSS transitions to
                  complete).
                </td>
              </tr>
            </tbody>
          </table>
          <table class="table mt-5">
            <thead>
              <tr>
                <th class="whitespace-nowrap w-24">Slot Prop</th>
                <th class="whitespace-nowrap">Description</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="align-top text-red-500">`dismiss`</td>
                <td class="align-top">Manually hides a dropdown.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <!-- END: Component API -->
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const programmaticDropdown = ref(false);
</script>
