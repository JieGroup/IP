<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Slide Over</h2>
  </div>
  <div class="grid grid-cols-12 gap-6 mt-5">
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- BEGIN: Blank Slide Over -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Blank Slide Over</h2>
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
        <div id="blank-slide-over" class="p-5">
          <Preview>
            <!-- BEGIN: Slide Over Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                @click="basicSlideOverPreview = true"
                class="btn btn-primary"
                >Show Slide Over</a
              >
            </div>
            <!-- END: Slide Over Toggle -->
            <!-- BEGIN: Slide Over Content -->
            <Modal
              :slideOver="true"
              :show="basicSlideOverPreview"
              @hidden="basicSlideOverPreview = false"
            >
              <ModalHeader class="p-5">
                <h2 class="font-medium text-base mr-auto">Blank Slide Over</h2>
              </ModalHeader>
              <ModalBody> This is totally awesome blank slide over! </ModalBody>
            </Modal>
            <!-- END: Slide Over Content -->
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Slide Over Toggle -->
              <div class="text-center">
                <a
                  href="javascript:;"
                  @click="basicSlideOverPreview = true"
                  class="btn btn-primary"
                  >Show Slide Over</a
                >
              </div>
              <!-- END: Slide Over Toggle -->
              <!-- BEGIN: Slide Over Content -->
              <Modal
                :slideOver="true"
                :show="basicSlideOverPreview"
                @hidden="basicSlideOverPreview = false"
              >
                <ModalHeader class="p-5">
                  <h2 class="font-medium text-base mr-auto">
                    Blank Slide Over
                  </h2>
                </ModalHeader>
                <ModalBody>
                  This is totally awesome blank slide over!
                </ModalBody>
              </Modal>
              <!-- END: Slide Over Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Blank Slide Over -->
      <!-- BEGIN: Slide Over Size -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Slide Over Size</h2>
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
        <div id="slide-over-size" class="p-5">
          <Preview>
            <div class="text-center">
              <!-- BEGIN: Small Slide Over Toggle -->
              <a
                href="javascript:;"
                @click="smallSlideOverSizePreview = true"
                class="btn btn-primary mr-1 mb-2"
                >Show Small Slide Over</a
              >
              <!-- END: Small Slide Over Toggle -->
              <!-- BEGIN: Medium Slide Over Toggle -->
              <a
                href="javascript:;"
                @click="mediumSlideOverSizePreview = true"
                class="btn btn-primary mr-1 mb-2"
                >Show Medium Slide Over</a
              >
              <!-- END: Medium Slide Over Toggle -->
              <!-- BEGIN: Large Slide Over Toggle -->
              <a
                href="javascript:;"
                @click="largeSlideOverSizePreview = true"
                class="btn btn-primary mr-1 mb-2"
                >Show Large Slide Over</a
              >
              <!-- END: Large Slide Over Toggle -->
              <!-- BEGIN: Super Large Slide Over Toggle -->
              <a
                href="javascript:;"
                @click="superlargeSlideOverSizePreview = true"
                class="btn btn-primary mr-1 mb-2"
                >Show Superlarge Slide Over</a
              >
              <!-- END: Super Large Slide Over Toggle -->
            </div>
            <!-- BEGIN: Small Slide Over Content -->
            <Modal
              size="modal-sm"
              :slideOver="true"
              :show="smallSlideOverSizePreview"
              @hidden="smallSlideOverSizePreview = false"
            >
              <ModalHeader class="p-5">
                <h2 class="font-medium text-base mr-auto">Small Slide Over</h2>
              </ModalHeader>
              <ModalBody>This is totally awesome small slide over!</ModalBody>
            </Modal>
            <!-- END: Small Slide Over Content -->
            <!-- BEGIN: Medium Slide Over Content -->
            <Modal
              :slideOver="true"
              :show="mediumSlideOverSizePreview"
              @hidden="mediumSlideOverSizePreview = false"
            >
              <ModalHeader class="p-5">
                <h2 class="font-medium text-base mr-auto">Medium Slide Over</h2>
              </ModalHeader>
              <ModalBody>This is totally awesome medium slide over!</ModalBody>
            </Modal>
            <!-- END: Medium Slide Over Content -->
            <!-- BEGIN: Large Slide Over Content -->
            <Modal
              size="modal-lg"
              :slideOver="true"
              :show="largeSlideOverSizePreview"
              @hidden="largeSlideOverSizePreview = false"
            >
              <ModalHeader class="p-5">
                <h2 class="font-medium text-base mr-auto">Large Slide Over</h2>
              </ModalHeader>
              <ModalBody>This is totally awesome large slide over!</ModalBody>
            </Modal>
            <!-- END: Large Slide Over Content -->
            <!-- BEGIN: Super Large Slide Over Content -->
            <Modal
              size="modal-xl"
              :slideOver="true"
              :show="superlargeSlideOverSizePreview"
              @hidden="superlargeSlideOverSizePreview = false"
            >
              <ModalHeader class="p-5">
                <h2 class="font-medium text-base mr-auto">
                  Superlarge Slide Over
                </h2>
              </ModalHeader>
              <ModalBody
                >This is totally awesome superlarge slide over!</ModalBody
              >
            </Modal>
            <!-- END: Super Large Slide Over Content -->
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div class="text-center">
                <!-- BEGIN: Small Slide Over Toggle -->
                <a
                  href="javascript:;"
                  @click="smallSlideOverSizePreview = true"
                  class="btn btn-primary mr-1 mb-2"
                  >Show Small Slide Over</a
                >
                <!-- END: Small Slide Over Toggle -->
                <!-- BEGIN: Medium Slide Over Toggle -->
                <a
                  href="javascript:;"
                  @click="mediumSlideOverSizePreview = true"
                  class="btn btn-primary mr-1 mb-2"
                  >Show Medium Slide Over</a
                >
                <!-- END: Medium Slide Over Toggle -->
                <!-- BEGIN: Large Slide Over Toggle -->
                <a
                  href="javascript:;"
                  @click="largeSlideOverSizePreview = true"
                  class="btn btn-primary mr-1 mb-2"
                  >Show Large Slide Over</a
                >
                <!-- END: Large Slide Over Toggle -->
                <!-- BEGIN: Super Large Slide Over Toggle -->
                <a
                  href="javascript:;"
                  @click="superlargeSlideOverSizePreview = true"
                  class="btn btn-primary mr-1 mb-2"
                  >Show Superlarge Slide Over</a
                >
                <!-- END: Super Large Slide Over Toggle -->
              </div>
              <!-- BEGIN: Small Slide Over Content -->
              <Modal
                size="modal-sm"
                :slideOver="true"
                :show="smallSlideOverSizePreview"
                @hidden="smallSlideOverSizePreview = false"
              >
                <ModalHeader class="p-5">
                  <h2 class="font-medium text-base mr-auto">
                    Small Slide Over
                  </h2>
                </ModalHeader>
                <ModalBody>This is totally awesome small slide over!</ModalBody>
              </Modal>
              <!-- END: Small Slide Over Content -->
              <!-- BEGIN: Medium Slide Over Content -->
              <Modal
                :slideOver="true"
                :show="mediumSlideOverSizePreview"
                @hidden="mediumSlideOverSizePreview = false"
              >
                <ModalHeader class="p-5">
                  <h2 class="font-medium text-base mr-auto">
                    Medium Slide Over
                  </h2>
                </ModalHeader>
                <ModalBody
                  >This is totally awesome medium slide over!</ModalBody
                >
              </Modal>
              <!-- END: Medium Slide Over Content -->
              <!-- BEGIN: Large Slide Over Content -->
              <Modal
                size="modal-lg"
                :slideOver="true"
                :show="largeSlideOverSizePreview"
                @hidden="largeSlideOverSizePreview = false"
              >
                <ModalHeader class="p-5">
                  <h2 class="font-medium text-base mr-auto">
                    Large Slide Over
                  </h2>
                </ModalHeader>
                <ModalBody>This is totally awesome large slide over!</ModalBody>
              </Modal>
              <!-- END: Large Slide Over Content -->
              <!-- BEGIN: Super Large Slide Over Content -->
              <Modal
                size="modal-xl"
                :slideOver="true"
                :show="superlargeSlideOverSizePreview"
                @hidden="superlargeSlideOverSizePreview = false"
              >
                <ModalHeader class="p-5">
                  <h2 class="font-medium text-base mr-auto">
                    Superlarge Slide Over
                  </h2>
                </ModalHeader>
                <ModalBody
                  >This is totally awesome superlarge slide over!</ModalBody
                >
              </Modal>
              <!-- END: Super Large Slide Over Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Slide Over Size -->
      <!-- BEGIN: Slide Over With Close Button -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Slide Over With Close Button
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
        <div id="button-slide-over" class="p-5">
          <Preview>
            <!-- BEGIN: Modal Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                @click="buttonSlideOverPreview = true"
                class="btn btn-primary"
                >Show Slide Over</a
              >
            </div>
            <!-- END: Modal Toggle -->
            <!-- BEGIN: Modal Content -->
            <Modal
              backdrop="static"
              :slideOver="true"
              :show="buttonSlideOverPreview"
              @hidden="buttonSlideOverPreview = false"
            >
              <a
                @click="buttonSlideOverPreview = false"
                class="absolute top-0 left-0 right-auto mt-4 -ml-12"
                href="javascript:;"
              >
                <XIcon class="w-8 h-8 text-slate-400" />
              </a>
              <ModalHeader class="p-5">
                <h2 class="font-medium text-base mr-auto">
                  Slide Over With Close Button
                </h2>
              </ModalHeader>
              <ModalBody>
                This is totally awesome slide over with close button!
              </ModalBody>
            </Modal>
            <!-- END: Modal Content -->
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Modal Toggle -->
              <div class="text-center">
                <a
                  href="javascript:;"
                  @click="buttonSlideOverPreview = true"
                  class="btn btn-primary"
                  >Show Slide Over</a
                >
              </div>
              <!-- END: Modal Toggle -->
              <!-- BEGIN: Modal Content -->
              <Modal
                backdrop="static"
                :slideOver="true"
                :show="buttonSlideOverPreview"
                @hidden="buttonSlideOverPreview = false"
              >
                <a
                  @click="buttonSlideOverPreview = false"
                  class="absolute top-0 left-0 right-auto mt-4 -ml-12"
                  href="javascript:;"
                >
                  <XIcon class="w-8 h-8 text-slate-400" />
                </a>
                <ModalHeader class="p-5">
                  <h2 class="font-medium text-base mr-auto">
                    Slide Over With Close Button
                  </h2>
                </ModalHeader>
                <ModalBody>
                  This is totally awesome slide over with close button!
                </ModalBody>
              </Modal>
              <!-- END: Modal Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Slide Over With Close Button -->
      <!-- BEGIN: Overlapping Slide Over -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Overlapping Slide Over</h2>
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
        <div id="overlapping-slide-over" class="p-5">
          <Preview>
            <!-- BEGIN: Slide Over Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                @click="overlappingSlideOverPreview = true"
                class="btn btn-primary"
                >Show Slide Over</a
              >
            </div>
            <!-- END: Slide Over Toggle -->
            <!-- BEGIN: Slide Over Content -->
            <Modal
              :slideOver="true"
              :show="overlappingSlideOverPreview"
              @hidden="overlappingSlideOverPreview = false"
            >
              <ModalHeader class="p-5">
                <h2 class="font-medium text-base mr-auto">
                  Overlapping Slide Over
                </h2>
              </ModalHeader>
              <ModalBody class="px-5 py-10">
                <div class="text-center">
                  <div class="mb-5">
                    Click button bellow to show overlapping slide over!
                  </div>
                  <!-- BEGIN: Overlapping Slide Over Toggle -->
                  <a
                    href="javascript:;"
                    @click="nextOverlappingSlideOverPreview = true"
                    class="btn btn-primary"
                    >Show Overlapping Slide Over</a
                  >
                  <!-- END: Overlapping Slide Over Toggle -->
                  <!-- BEGIN: Overlapping Slide Over Content -->
                  <Modal
                    :slideOver="true"
                    :show="nextOverlappingSlideOverPreview"
                    @hidden="nextOverlappingSlideOverPreview = false"
                  >
                    <ModalHeader class="p-5">
                      <h2 class="font-medium text-base mr-auto">
                        Overlapping Slide Over
                      </h2>
                    </ModalHeader>
                    <ModalBody class="text-center">
                      This is totally awesome overlapping slide over!
                    </ModalBody>
                  </Modal>
                  <!-- END: Overlapping Slide Over Content -->
                </div>
              </ModalBody>
            </Modal>
            <!-- END: Slide Over Content -->
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Slide Over Toggle -->
              <div class="text-center">
                <a
                  href="javascript:;"
                  @click="overlappingSlideOverPreview = true"
                  class="btn btn-primary"
                  >Show Slide Over</a
                >
              </div>
              <!-- END: Slide Over Toggle -->
              <!-- BEGIN: Slide Over Content -->
              <Modal
                :slideOver="true"
                :show="overlappingSlideOverPreview"
                @hidden="overlappingSlideOverPreview = false"
              >
                <ModalHeader class="p-5">
                  <h2 class="font-medium text-base mr-auto">
                    Overlapping Slide Over
                  </h2>
                </ModalHeader>
                <ModalBody class="px-5 py-10">
                  <div class="text-center">
                    <div class="mb-5">
                      Click button bellow to show overlapping slide over!
                    </div>
                    <!-- BEGIN: Overlapping Slide Over Toggle -->
                    <a
                      href="javascript:;"
                      @click="nextOverlappingSlideOverPreview = true"
                      class="btn btn-primary"
                      >Show Overlapping Slide Over</a
                    >
                    <!-- END: Overlapping Slide Over Toggle -->
                    <!-- BEGIN: Overlapping Slide Over Content -->
                    <Modal
                      :slideOver="true"
                      :show="nextOverlappingSlideOverPreview"
                      @hidden="nextOverlappingSlideOverPreview = false"
                    >
                      <ModalHeader class="p-5">
                        <h2 class="font-medium text-base mr-auto">
                          Overlapping Slide Over
                        </h2>
                      </ModalHeader>
                      <ModalBody class="text-center">
                        This is totally awesome overlapping slide over!
                      </ModalBody>
                    </Modal>
                    <!-- END: Overlapping Slide Over Content -->
                  </div>
                </ModalBody>
              </Modal>
              <!-- END: Slide Over Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Overlapping Slide Over -->
      <!-- BEGIN: Header & Footer Slide Over -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Header & Footer Slide Over
          </h2>
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
        <div id="header-footer-slide-over" class="p-5">
          <Preview>
            <!-- BEGIN: Slide Over Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                @click="headerFooterSlideOverPreview = true"
                class="btn btn-primary"
                >Show Slide Over</a
              >
            </div>
            <!-- END: Slide Over Toggle -->
            <!-- BEGIN: Slide Over Content -->
            <Modal
              backdrop="static"
              :slideOver="true"
              :show="headerFooterSlideOverPreview"
              @hidden="headerFooterSlideOverPreview = false"
            >
              <a
                @click="headerFooterSlideOverPreview = false"
                class="absolute top-0 left-0 right-auto mt-4 -ml-12"
                href="javascript:;"
              >
                <XIcon class="w-8 h-8 text-slate-400" />
              </a>
              <!-- BEGIN: Slide Over Header -->
              <ModalHeader class="p-5">
                <h2 class="font-medium text-base mr-auto">Broadcast Message</h2>
                <button class="btn btn-outline-secondary hidden sm:flex">
                  <FileIcon class="w-4 h-4 mr-2" /> Download Docs
                </button>
                <Dropdown class="sm:hidden">
                  <DropdownToggle class="w-5 h-5 block" href="javascript:;">
                    <MoreHorizontalIcon class="w-5 h-5 text-slate-500" />
                  </DropdownToggle>
                  <DropdownMenu class="w-40">
                    <DropdownContent>
                      <DropdownItem>
                        <FileIcon class="w-4 h-4 mr-2" />
                        Download Docs
                      </DropdownItem>
                    </DropdownContent>
                  </DropdownMenu>
                </Dropdown>
              </ModalHeader>
              <!-- END: Slide Over Header -->
              <!-- BEGIN: Slide Over Body -->
              <ModalBody>
                <div>
                  <label for="modal-form-1" class="form-label">From</label>
                  <input
                    id="modal-form-1"
                    type="text"
                    class="form-control"
                    placeholder="example@gmail.com"
                  />
                </div>
                <div class="mt-3">
                  <label for="modal-form-2" class="form-label">To</label>
                  <input
                    id="modal-form-2"
                    type="text"
                    class="form-control"
                    placeholder="example@gmail.com"
                  />
                </div>
                <div class="mt-3">
                  <label for="modal-form-3" class="form-label">Subject</label>
                  <input
                    id="modal-form-3"
                    type="text"
                    class="form-control"
                    placeholder="Important Meeting"
                  />
                </div>
                <div class="mt-3">
                  <label for="modal-form-4" class="form-label"
                    >Has the Words</label
                  >
                  <input
                    id="modal-form-4"
                    type="text"
                    class="form-control"
                    placeholder="Job, Work, Documentation"
                  />
                </div>
                <div class="mt-3">
                  <label for="modal-form-5" class="form-label"
                    >Doesn't Have</label
                  >
                  <input
                    id="modal-form-5"
                    type="text"
                    class="form-control"
                    placeholder="Job, Work, Documentation"
                  />
                </div>
                <div class="mt-3">
                  <label for="modal-form-6" class="form-label">Size</label>
                  <select id="modal-form-6" class="form-select">
                    <option>10</option>
                    <option>25</option>
                    <option>35</option>
                    <option>50</option>
                  </select>
                </div>
              </ModalBody>
              <!-- END: Slide Over Body -->
              <!-- BEGIN: Slide Over Footer -->
              <ModalFooter class="w-full absolute bottom-0">
                <button
                  type="button"
                  @click="headerFooterSlideOverPreview = false"
                  class="btn btn-outline-secondary w-20 mr-1"
                >
                  Cancel
                </button>
                <button type="button" class="btn btn-primary w-20">Send</button>
              </ModalFooter>
              <!-- END: Slide Over Footer -->
            </Modal>
            <!-- END: Slide Over Content -->
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Slide Over Toggle -->
              <div class="text-center">
                <a
                  href="javascript:;"
                  @click="headerFooterSlideOverPreview = true"
                  class="btn btn-primary"
                  >Show Slide Over</a
                >
              </div>
              <!-- END: Slide Over Toggle -->
              <!-- BEGIN: Slide Over Content -->
              <Modal
                backdrop="static"
                :slideOver="true"
                :show="headerFooterSlideOverPreview"
                @hidden="headerFooterSlideOverPreview = false"
              >
                <a
                  @click="headerFooterSlideOverPreview = false"
                  class="absolute top-0 left-0 right-auto mt-4 -ml-12"
                  href="javascript:;"
                >
                  <XIcon class="w-8 h-8 text-slate-400" />
                </a>
                <!-- BEGIN: Slide Over Header -->
                <ModalHeader class="p-5">
                  <h2 class="font-medium text-base mr-auto">
                    Broadcast Message
                  </h2>
                  <button class="btn btn-outline-secondary hidden sm:flex">
                    <FileIcon class="w-4 h-4 mr-2" /> Download Docs
                  </button>
                  <Dropdown class="sm:hidden">
                    <DropdownToggle class="w-5 h-5 block" href="javascript:;">
                      <MoreHorizontalIcon class="w-5 h-5 text-slate-500" />
                    </DropdownToggle>
                    <DropdownMenu class="w-40">
                      <DropdownContent>
                        <DropdownItem>
                          <FileIcon class="w-4 h-4 mr-2" />
                          Download Docs
                        </DropdownItem>
                      </DropdownContent>
                    </DropdownMenu>
                  </Dropdown>
                </ModalHeader>
                <!-- END: Slide Over Header -->
                <!-- BEGIN: Slide Over Body -->
                <ModalBody>
                  <div>
                    <label for="modal-form-1" class="form-label">From</label>
                    <input
                      id="modal-form-1"
                      type="text"
                      class="form-control"
                      placeholder="example@gmail.com"
                    />
                  </div>
                  <div class="mt-3">
                    <label for="modal-form-2" class="form-label">To</label>
                    <input
                      id="modal-form-2"
                      type="text"
                      class="form-control"
                      placeholder="example@gmail.com"
                    />
                  </div>
                  <div class="mt-3">
                    <label for="modal-form-3" class="form-label">Subject</label>
                    <input
                      id="modal-form-3"
                      type="text"
                      class="form-control"
                      placeholder="Important Meeting"
                    />
                  </div>
                  <div class="mt-3">
                    <label for="modal-form-4" class="form-label"
                      >Has the Words</label
                    >
                    <input
                      id="modal-form-4"
                      type="text"
                      class="form-control"
                      placeholder="Job, Work, Documentation"
                    />
                  </div>
                  <div class="mt-3">
                    <label for="modal-form-5" class="form-label"
                      >Doesn't Have</label
                    >
                    <input
                      id="modal-form-5"
                      type="text"
                      class="form-control"
                      placeholder="Job, Work, Documentation"
                    />
                  </div>
                  <div class="mt-3">
                    <label for="modal-form-6" class="form-label">Size</label>
                    <select id="modal-form-6" class="form-select">
                      <option>10</option>
                      <option>25</option>
                      <option>35</option>
                      <option>50</option>
                    </select>
                  </div>
                </ModalBody>
                <!-- END: Slide Over Body -->
                <!-- BEGIN: Slide Over Footer -->
                <ModalFooter class="w-full absolute bottom-0">
                  <button
                    type="button"
                    @click="headerFooterSlideOverPreview = false"
                    class="btn btn-outline-secondary w-20 mr-1"
                  >
                    Cancel
                  </button>
                  <button type="button" class="btn btn-primary w-20">
                    Send
                  </button>
                </ModalFooter>
                <!-- END: Slide Over Footer -->
              </Modal>
              <!-- END: Slide Over Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Header & Footer Slide Over -->
      <!-- BEGIN: Programmatically Show/Hide Slide Over -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Programmatically Show/Hide Slide Over
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
        <div id="programmatically-show-hide-slide-over" class="p-5">
          <Preview>
            <!-- BEGIN: Show Slide Over Toggle -->
            <div class="text-center">
              <a
                id="programmatically-show-slide-over"
                href="javascript:;"
                class="btn btn-primary mr-1 mb-2"
                @click="programmaticallySlideOver = true"
                >Show Slide Over</a
              >
            </div>
            <!-- END: Show Slide Over Toggle -->
            <!-- BEGIN: Slide Over Content -->
            <Modal
              :slideOver="true"
              :show="programmaticallySlideOver"
              @hidden="programmaticallySlideOver = false"
            >
              <ModalHeader class="p-5">
                <h2 class="font-medium text-base mr-auto">
                  Programmatically Show/Hide Slide Over
                </h2>
              </ModalHeader>
              <ModalBody class="p-10 text-center">
                <!-- BEGIN: Hide Slide Over Toggle -->
                <a
                  id="programmatically-hide-slide-over"
                  href="javascript:;"
                  class="btn btn-primary mr-1"
                  @click="programmaticallySlideOver = false"
                  >Hide Slide Over</a
                >
                <!-- END: Hide Slide Over Toggle -->
                <!-- BEGIN: Toggle Slide Over Toggle -->
                <a
                  id="programmatically-toggle-slide-over"
                  href="javascript:;"
                  class="btn btn-primary mr-1 mt-2 sm:mt-0"
                  @click="
                    programmaticallySlideOver = !programmaticallySlideOver
                  "
                  >Toggle Slide Over</a
                >
                <!-- END: Toggle Slide Over Toggle -->
              </ModalBody>
            </Modal>
            <!-- END: Slide Over Content -->
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Show Slide Over Toggle -->
              <div class="text-center">
                <a
                  id="programmatically-show-slide-over"
                  href="javascript:;"
                  class="btn btn-primary mr-1 mb-2"
                  @click="programmaticallySlideOver = true"
                  >Show Slide Over</a
                >
              </div>
              <!-- END: Show Slide Over Toggle -->
              <!-- BEGIN: Slide Over Content -->
              <Modal
                :slideOver="true"
                :show="programmaticallySlideOver"
                @hidden="programmaticallySlideOver = false"
              >
                <ModalHeader class="p-5">
                  <h2 class="font-medium text-base mr-auto">
                    Programmatically Show/Hide Slide Over
                  </h2>
                </ModalHeader>
                <ModalBody class="p-10 text-center">
                  <!-- BEGIN: Hide Slide Over Toggle -->
                  <a
                    id="programmatically-hide-slide-over"
                    href="javascript:;"
                    class="btn btn-primary mr-1"
                    @click="programmaticallySlideOver = false"
                    >Hide Slide Over</a
                  >
                  <!-- END: Hide Slide Over Toggle -->
                  <!-- BEGIN: Toggle Slide Over Toggle -->
                  <a
                    id="programmatically-toggle-slide-over"
                    href="javascript:;"
                    class="btn btn-primary mr-1 mt-2 sm:mt-0"
                    @click="
                      programmaticallySlideOver = !programmaticallySlideOver
                    "
                    >Toggle Slide Over</a
                  >
                  <!-- END: Toggle Slide Over Toggle -->
                </ModalBody>
              </Modal>
              <!-- END: Slide Over Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Programmatically Show/Hide Slide Over -->
    </div>
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- BEGIN: Component Reference -->
      <div class="intro-y box">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Component Reference</h2>
        </div>
        <div class="p-5">
          <div>
            Slide overs are built using the
            <span class="text-red-500">`Modal`</span>,
            <span class="text-red-500">`ModalHeader`</span>,
            <span class="text-red-500">`ModalBody`</span> and
            <span class="text-red-500">`ModalFooter`</span> components.
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
          <div class="text-base font-medium">Modal</div>
          <div class="mt-2">The main Modal component.</div>
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
                  Whether the Modal is open or not.
                </td>
              </tr>
              <tr>
                <td class="align-top text-red-500">`size`</td>
                <td class="align-top">`modal-sm`, `modal-lg`, `modal-xl`</td>
                <td class="align-top">-</td>
                <td class="align-top">
                  <div class="font-medium mb-1">`String`</div>
                  Size of Modal wrapper/content.
                </td>
              </tr>
              <tr>
                <td class="align-top text-red-500">`backdrop`</td>
                <td class="align-top">`static`</td>
                <td class="align-top">-</td>
                <td class="align-top">
                  <div class="font-medium mb-1">`String`</div>
                  Whether the Modal backdrop is static or not. When backdrop is
                  set to static, the Modal will not close when clicking outside
                  it.
                </td>
              </tr>
              <tr>
                <td class="align-top text-red-500">`slideOver`</td>
                <td class="align-top">`true`, `false`</td>
                <td class="align-top">`false`</td>
                <td class="align-top">
                  <div class="font-medium mb-1">`Boolean`</div>
                  Whether the Modal appears as a slideover or not.
                </td>
              </tr>
              <tr>
                <td class="align-top text-red-500">`refKey`</td>
                <td class="align-top">-</td>
                <td class="align-top">`null`</td>
                <td class="align-top">
                  <div class="font-medium mb-1">`String`</div>
                  A ref to the Modal element.
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
                  This event is fired when the modal has been made visible to
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
                  This event is fired when the modal has finished being hidden
                  from the user (will wait for CSS transitions to complete).
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
                <td class="align-top">Manually hides a modal.</td>
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

const basicSlideOverPreview = ref(false);
const smallSlideOverSizePreview = ref(false);
const mediumSlideOverSizePreview = ref(false);
const largeSlideOverSizePreview = ref(false);
const superlargeSlideOverSizePreview = ref(false);
const programmaticallySlideOver = ref(false);
const buttonSlideOverPreview = ref(false);
const overlappingSlideOverPreview = ref(false);
const nextOverlappingSlideOverPreview = ref(false);
const headerFooterSlideOverPreview = ref(false);
</script>
