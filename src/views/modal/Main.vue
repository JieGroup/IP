<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Modal</h2>
  </div>
  <div class="grid grid-cols-12 gap-6 mt-5">
    <div class="intro-y col-span-12 lg:col-span-6">
      <!-- BEGIN: Blank Modal -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Blank Modal</h2>
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
            <!-- BEGIN: Modal Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                @click="basicModalPreview = true"
                class="btn btn-primary"
                >Show Modal</a
              >
            </div>
            <!-- END: Modal Toggle -->
            <!-- BEGIN: Modal Content -->
            <Modal
              :show="basicModalPreview"
              @hidden="basicModalPreview = false"
            >
              <ModalBody class="p-10 text-center">
                This is totally awesome blank modal!
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
                  @click="basicModalPreview = true"
                  class="btn btn-primary"
                  >Show Modal</a
                >
              </div>
              <!-- END: Modal Toggle -->
              <!-- BEGIN: Modal Content -->
              <Modal
                :show="basicModalPreview"
                @hidden="basicModalPreview = false"
              >
                <ModalBody class="p-10 text-center">
                  This is totally awesome blank modal!
                </ModalBody>
              </Modal>
              <!-- END: Modal Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Blank Modal -->
      <!-- BEGIN: Modal Size -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Modal Size</h2>
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
            <div class="text-center">
              <!-- BEGIN: Small Modal Toggle -->
              <a
                href="javascript:;"
                @click="smallModalSizePreview = true"
                class="btn btn-primary mr-1 mb-2"
                >Show Small Modal</a
              >
              <!-- END: Small Modal Toggle -->
              <!-- BEGIN: Medium Modal Toggle -->
              <a
                href="javascript:;"
                @click="mediumModalSizePreview = true"
                class="btn btn-primary mr-1 mb-2"
                >Show Medium Modal</a
              >
              <!-- END: Medium Modal Toggle -->
              <!-- BEGIN: Large Modal Toggle -->
              <a
                href="javascript:;"
                @click="largeModalSizePreview = true"
                class="btn btn-primary mr-1 mb-2"
                >Show Large Modal</a
              >
              <!-- END: Large Modal Toggle -->
              <!-- BEGIN: Super Large Modal Toggle -->
              <a
                href="javascript:;"
                @click="superlargeModalSizePreview = true"
                class="btn btn-primary mr-1 mb-2"
                >Show Superlarge Modal</a
              >
              <!-- END: Super Large Modal Toggle -->
            </div>
            <!-- BEGIN: Small Modal Content -->
            <Modal
              size="modal-sm"
              :show="smallModalSizePreview"
              @hidden="smallModalSizePreview = false"
            >
              <ModalBody class="p-10 text-center">
                This is totally awesome small modal!
              </ModalBody>
            </Modal>
            <!-- END: Small Modal Content -->
            <!-- BEGIN: Medium Modal Content -->
            <Modal
              :show="mediumModalSizePreview"
              @hidden="mediumModalSizePreview = false"
            >
              <ModalBody class="p-10 text-center">
                This is totally awesome medium modal!
              </ModalBody>
            </Modal>
            <!-- END: Medium Modal Content -->
            <!-- BEGIN: Large Modal Content -->
            <Modal
              size="modal-lg"
              :show="largeModalSizePreview"
              @hidden="largeModalSizePreview = false"
            >
              <ModalBody class="p-10 text-center">
                This is totally awesome large modal!
              </ModalBody>
            </Modal>
            <!-- END: Large Modal Content -->
            <!-- BEGIN: Super Large Modal Content -->
            <Modal
              size="modal-xl"
              :show="superlargeModalSizePreview"
              @hidden="superlargeModalSizePreview = false"
            >
              <ModalBody class="p-10 text-center">
                This is totally awesome superlarge modal!
              </ModalBody>
            </Modal>
            <!-- END: Super Large Modal Content -->
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <div class="text-center">
                <!-- BEGIN: Small Modal Toggle -->
                <a
                  href="javascript:;"
                  @click="smallModalSizePreview = true"
                  class="btn btn-primary mr-1 mb-2"
                  >Show Small Modal</a
                >
                <!-- END: Small Modal Toggle -->
                <!-- BEGIN: Medium Modal Toggle -->
                <a
                  href="javascript:;"
                  @click="mediumModalSizePreview = true"
                  class="btn btn-primary mr-1 mb-2"
                  >Show Medium Modal</a
                >
                <!-- END: Medium Modal Toggle -->
                <!-- BEGIN: Large Modal Toggle -->
                <a
                  href="javascript:;"
                  @click="largeModalSizePreview = true"
                  class="btn btn-primary mr-1 mb-2"
                  >Show Large Modal</a
                >
                <!-- END: Large Modal Toggle -->
                <!-- BEGIN: Super Large Modal Toggle -->
                <a
                  href="javascript:;"
                  @click="superlargeModalSizePreview = true"
                  class="btn btn-primary mr-1 mb-2"
                  >Show Superlarge Modal</a
                >
                <!-- END: Super Large Modal Toggle -->
              </div>
              <!-- BEGIN: Small Modal Content -->
              <Modal
                size="modal-sm"
                :show="smallModalSizePreview"
                @hidden="smallModalSizePreview = false"
              >
                <ModalBody class="p-10 text-center">
                  This is totally awesome small modal!
                </ModalBody>
              </Modal>
              <!-- END: Small Modal Content -->
              <!-- BEGIN: Medium Modal Content -->
              <Modal
                :show="mediumModalSizePreview"
                @hidden="mediumModalSizePreview = false"
              >
                <ModalBody class="p-10 text-center">
                  This is totally awesome medium modal!
                </ModalBody>
              </Modal>
              <!-- END: Medium Modal Content -->
              <!-- BEGIN: Large Modal Content -->
              <Modal
                size="modal-lg"
                :show="largeModalSizePreview"
                @hidden="largeModalSizePreview = false"
              >
                <ModalBody class="p-10 text-center">
                  This is totally awesome large modal!
                </ModalBody>
              </Modal>
              <!-- END: Large Modal Content -->
              <!-- BEGIN: Super Large Modal Content -->
              <Modal
                size="modal-xl"
                :show="superlargeModalSizePreview"
                @hidden="superlargeModalSizePreview = false"
              >
                <ModalBody class="p-10 text-center">
                  This is totally awesome superlarge modal!
                </ModalBody>
              </Modal>
              <!-- END: Super Large Modal Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Modal Size -->
      <!-- BEGIN: Warning Modal -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Warning Modal</h2>
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
            <!-- BEGIN: Modal Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                class="btn btn-primary"
                @click="warningModalPreview = true"
                >Show Modal</a
              >
            </div>
            <!-- END: Modal Toggle -->
            <!-- BEGIN: Modal Content -->
            <Modal
              :show="warningModalPreview"
              @hidden="warningModalPreview = false"
            >
              <ModalBody class="p-0">
                <div class="p-5 text-center">
                  <XCircleIcon class="w-16 h-16 text-warning mx-auto mt-3" />
                  <div class="text-3xl mt-5">Oops...</div>
                  <div class="text-slate-500 mt-2">Something went wrong!</div>
                </div>
                <div class="px-5 pb-8 text-center">
                  <button
                    type="button"
                    @click="warningModalPreview = false"
                    class="btn w-24 btn-primary"
                  >
                    Ok
                  </button>
                </div>
                <div
                  class="p-5 text-center border-t border-slate-200/60 dark:border-darkmode-400"
                >
                  <a href="" class="text-primary">Why do I have this issue?</a>
                </div>
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
                  class="btn btn-primary"
                  @click="warningModalPreview = true"
                  >Show Modal</a
                >
              </div>
              <!-- END: Modal Toggle -->
              <!-- BEGIN: Modal Content -->
              <Modal
                :show="warningModalPreview"
                @hidden="warningModalPreview = false"
              >
                <ModalBody class="p-0">
                  <div class="p-5 text-center">
                    <XCircleIcon class="w-16 h-16 text-warning mx-auto mt-3" />
                    <div class="text-3xl mt-5">Oops...</div>
                    <div class="text-slate-500 mt-2">Something went wrong!</div>
                  </div>
                  <div class="px-5 pb-8 text-center">
                    <button
                      type="button"
                      @click="warningModalPreview = false"
                      class="btn w-24 btn-primary"
                    >
                      Ok
                    </button>
                  </div>
                  <div
                    class="p-5 text-center border-t border-slate-200/60 dark:border-darkmode-400"
                  >
                    <a href="" class="text-primary"
                      >Why do I have this issue?</a
                    >
                  </div>
                </ModalBody>
              </Modal>
              <!-- END: Modal Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Warning Modal -->
      <!-- BEGIN: Modal With Close Button -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Modal With Close Button</h2>
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
            <!-- BEGIN: Modal Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                @click="buttonModalPreview = true"
                class="btn btn-primary"
                >Show Modal</a
              >
            </div>
            <!-- END: Modal Toggle -->
            <!-- BEGIN: Modal Content -->
            <Modal
              :show="buttonModalPreview"
              @hidden="buttonModalPreview = false"
            >
              <a
                @click="buttonModalPreview = false"
                class="absolute right-0 top-0 mt-3 mr-3"
                href="javascript:;"
              >
                <XIcon class="w-8 h-8 text-slate-400" />
              </a>
              <ModalBody class="p-0">
                <div class="p-5 text-center">
                  <CheckCircleIcon
                    class="w-16 h-16 text-success mx-auto mt-3"
                  />
                  <div class="text-3xl mt-5">Modal Example</div>
                  <div class="text-slate-500 mt-2">Modal with close button</div>
                </div>
                <div class="px-5 pb-8 text-center">
                  <button
                    type="button"
                    @click="buttonModalPreview = false"
                    class="btn btn-primary w-24"
                  >
                    Ok
                  </button>
                </div>
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
                  @click="buttonModalPreview = true"
                  class="btn btn-primary"
                  >Show Modal</a
                >
              </div>
              <!-- END: Modal Toggle -->
              <!-- BEGIN: Modal Content -->
              <Modal
                :show="buttonModalPreview"
                @hidden="buttonModalPreview = false"
              >
                <a
                  @click="buttonModalPreview = false"
                  class="absolute right-0 top-0 mt-3 mr-3"
                  href="javascript:;"
                >
                  <XIcon class="w-8 h-8 text-slate-400" />
                </a>
                <ModalBody class="p-0">
                  <div class="p-5 text-center">
                    <CheckCircleIcon
                      class="w-16 h-16 text-success mx-auto mt-3"
                    />
                    <div class="text-3xl mt-5">Modal Example</div>
                    <div class="text-slate-500 mt-2">
                      Modal with close button
                    </div>
                  </div>
                  <div class="px-5 pb-8 text-center">
                    <button
                      type="button"
                      @click="buttonModalPreview = false"
                      class="btn btn-primary w-24"
                    >
                      Ok
                    </button>
                  </div>
                </ModalBody>
              </Modal>
              <!-- END: Modal Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Modal With Close Button -->
      <!-- BEGIN: Static Backdrop Modal -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Static Backdrop Modal</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-11"
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
            <!-- BEGIN: Modal Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                @click="staticBackdropModalPreview = true"
                class="btn btn-primary"
                >Show Modal</a
              >
            </div>
            <!-- END: Modal Toggle -->
            <!-- BEGIN: Modal Content -->
            <Modal
              backdrop="static"
              :show="staticBackdropModalPreview"
              @hidden="staticBackdropModalPreview = false"
            >
              <ModalBody class="px-5 py-10">
                <div class="text-center">
                  <div class="mb-5">
                    I will not close if you click outside me. Don't even try to
                    press escape key.
                  </div>
                  <button
                    type="button"
                    @click="staticBackdropModalPreview = false"
                    class="btn btn-primary w-24"
                  >
                    Ok
                  </button>
                </div>
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
                  @click="staticBackdropModalPreview = true"
                  class="btn btn-primary"
                  >Show Modal</a
                >
              </div>
              <!-- END: Modal Toggle -->
              <!-- BEGIN: Modal Content -->
              <Modal
                backdrop="static"
                :show="staticBackdropModalPreview"
                @hidden="staticBackdropModalPreview = false"
              >
                <ModalBody class="px-5 py-10">
                  <div class="text-center">
                    <div class="mb-5">
                      I will not close if you click outside me. Don't even try
                      to press escape key.
                    </div>
                    <button
                      type="button"
                      @click="staticBackdropModalPreview = false"
                      class="btn btn-primary w-24"
                    >
                      Ok
                    </button>
                  </div>
                </ModalBody>
              </Modal>
              <!-- END: Modal Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Static Backdrop Modal -->
      <!-- BEGIN: Overlapping Modal -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Overlapping Modal</h2>
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
            <!-- BEGIN: Modal Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                @click="overlappingModalPreview = true"
                class="btn btn-primary"
                >Show Modal</a
              >
            </div>
            <!-- END: Modal Toggle -->
            <!-- BEGIN: Modal Content -->
            <Modal
              :show="overlappingModalPreview"
              @hidden="overlappingModalPreview = false"
            >
              <ModalBody class="px-5 py-10">
                <div class="text-center">
                  <div class="mb-5">
                    Click button bellow to show overlapping modal!
                  </div>
                  <!-- BEGIN: Overlapping Modal Toggle -->
                  <a
                    href="javascript:;"
                    @click="nextOverlappingModalPreview = true"
                    class="btn btn-primary"
                    >Show Overlapping Modal</a
                  >
                  <!-- END: Overlapping Modal Toggle -->
                </div>
                <!-- BEGIN: Overlapping Modal Content -->
                <Modal
                  :show="nextOverlappingModalPreview"
                  @hidden="nextOverlappingModalPreview = false"
                >
                  <ModalBody class="text-center">
                    This is totally awesome overlapping modal!
                  </ModalBody>
                </Modal>
                <!-- END: Overlapping Modal Content -->
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
                  @click="overlappingModalPreview = true"
                  class="btn btn-primary"
                  >Show Modal</a
                >
              </div>
              <!-- END: Modal Toggle -->
              <!-- BEGIN: Modal Content -->
              <Modal
                :show="overlappingModalPreview"
                @hidden="overlappingModalPreview = false"
              >
                <ModalBody class="px-5 py-10">
                  <div class="text-center">
                    <div class="mb-5">
                      Click button bellow to show overlapping modal!
                    </div>
                    <!-- BEGIN: Overlapping Modal Toggle -->
                    <a
                      href="javascript:;"
                      @click="nextOverlappingModalPreview = true"
                      class="btn btn-primary"
                      >Show Overlapping Modal</a
                    >
                    <!-- END: Overlapping Modal Toggle -->
                  </div>
                  <!-- BEGIN: Overlapping Modal Content -->
                  <Modal
                    :show="nextOverlappingModalPreview"
                    @hidden="nextOverlappingModalPreview = false"
                  >
                    <ModalBody class="text-center">
                      This is totally awesome overlapping modal!
                    </ModalBody>
                  </Modal>
                  <!-- END: Overlapping Modal Content -->
                </ModalBody>
              </Modal>
              <!-- END: Modal Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Overlapping Modal -->
      <!-- BEGIN: Header & Footer Modal -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Header & Footer Modal</h2>
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
            <!-- BEGIN: Modal Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                @click="headerFooterModalPreview = true"
                class="btn btn-primary"
                >Show Modal</a
              >
            </div>
            <!-- END: Modal Toggle -->
            <!-- BEGIN: Modal Content -->
            <Modal
              :show="headerFooterModalPreview"
              @hidden="headerFooterModalPreview = false"
            >
              <ModalHeader>
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
              <ModalBody class="grid grid-cols-12 gap-4 gap-y-3">
                <div class="col-span-12 sm:col-span-6">
                  <label for="modal-form-1" class="form-label">From</label>
                  <input
                    id="modal-form-1"
                    type="text"
                    class="form-control"
                    placeholder="example@gmail.com"
                  />
                </div>
                <div class="col-span-12 sm:col-span-6">
                  <label for="modal-form-2" class="form-label">To</label>
                  <input
                    id="modal-form-2"
                    type="text"
                    class="form-control"
                    placeholder="example@gmail.com"
                  />
                </div>
                <div class="col-span-12 sm:col-span-6">
                  <label for="modal-form-3" class="form-label">Subject</label>
                  <input
                    id="modal-form-3"
                    type="text"
                    class="form-control"
                    placeholder="Important Meeting"
                  />
                </div>
                <div class="col-span-12 sm:col-span-6">
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
                <div class="col-span-12 sm:col-span-6">
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
                <div class="col-span-12 sm:col-span-6">
                  <label for="modal-form-6" class="form-label">Size</label>
                  <select id="modal-form-6" class="form-select">
                    <option>10</option>
                    <option>25</option>
                    <option>35</option>
                    <option>50</option>
                  </select>
                </div>
              </ModalBody>
              <ModalFooter>
                <button
                  type="button"
                  @click="headerFooterModalPreview = false"
                  class="btn btn-outline-secondary w-20 mr-1"
                >
                  Cancel
                </button>
                <button type="button" class="btn btn-primary w-20">Send</button>
              </ModalFooter>
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
                  @click="headerFooterModalPreview = true"
                  class="btn btn-primary"
                  >Show Modal</a
                >
              </div>
              <!-- END: Modal Toggle -->
              <!-- BEGIN: Modal Content -->
              <Modal
                :show="headerFooterModalPreview"
                @hidden="headerFooterModalPreview = false"
              >
                <ModalHeader>
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
                <ModalBody class="grid grid-cols-12 gap-4 gap-y-3">
                  <div class="col-span-12 sm:col-span-6">
                    <label for="modal-form-1" class="form-label">From</label>
                    <input
                      id="modal-form-1"
                      type="text"
                      class="form-control"
                      placeholder="example@gmail.com"
                    />
                  </div>
                  <div class="col-span-12 sm:col-span-6">
                    <label for="modal-form-2" class="form-label">To</label>
                    <input
                      id="modal-form-2"
                      type="text"
                      class="form-control"
                      placeholder="example@gmail.com"
                    />
                  </div>
                  <div class="col-span-12 sm:col-span-6">
                    <label for="modal-form-3" class="form-label">Subject</label>
                    <input
                      id="modal-form-3"
                      type="text"
                      class="form-control"
                      placeholder="Important Meeting"
                    />
                  </div>
                  <div class="col-span-12 sm:col-span-6">
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
                  <div class="col-span-12 sm:col-span-6">
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
                  <div class="col-span-12 sm:col-span-6">
                    <label for="modal-form-6" class="form-label">Size</label>
                    <select id="modal-form-6" class="form-select">
                      <option>10</option>
                      <option>25</option>
                      <option>35</option>
                      <option>50</option>
                    </select>
                  </div>
                </ModalBody>
                <ModalFooter>
                  <button
                    type="button"
                    @click="headerFooterModalPreview = false"
                    class="btn btn-outline-secondary w-20 mr-1"
                  >
                    Cancel
                  </button>
                  <button type="button" class="btn btn-primary w-20">
                    Send
                  </button>
                </ModalFooter>
              </Modal>
              <!-- END: Modal Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Header & Footer Modal -->
      <!-- BEGIN: Delete Modal -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Delete Modal</h2>
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
            <!-- BEGIN: Modal Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                @click="deleteModalPreview = true"
                class="btn btn-primary"
                >Show Modal</a
              >
            </div>
            <!-- END: Modal Toggle -->
            <!-- BEGIN: Modal Content -->
            <Modal
              :show="deleteModalPreview"
              @hidden="deleteModalPreview = false"
            >
              <ModalBody class="p-0">
                <div class="p-5 text-center">
                  <XCircleIcon class="w-16 h-16 text-danger mx-auto mt-3" />
                  <div class="text-3xl mt-5">Are you sure?</div>
                  <div class="text-slate-500 mt-2">
                    Do you really want to delete these records? <br />This
                    process cannot be undone.
                  </div>
                </div>
                <div class="px-5 pb-8 text-center">
                  <button
                    type="button"
                    @click="deleteModalPreview = false"
                    class="btn btn-outline-secondary w-24 mr-1"
                  >
                    Cancel
                  </button>
                  <button type="button" class="btn btn-danger w-24">
                    Delete
                  </button>
                </div>
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
                  @click="deleteModalPreview = true"
                  class="btn btn-primary"
                  >Show Modal</a
                >
              </div>
              <!-- END: Modal Toggle -->
              <!-- BEGIN: Modal Content -->
              <Modal
                :show="deleteModalPreview"
                @hidden="deleteModalPreview = false"
              >
                <ModalBody class="p-0">
                  <div class="p-5 text-center">
                    <XCircleIcon class="w-16 h-16 text-danger mx-auto mt-3" />
                    <div class="text-3xl mt-5">Are you sure?</div>
                    <div class="text-slate-500 mt-2">
                      Do you really want to delete these records? <br />This
                      process cannot be undone.
                    </div>
                  </div>
                  <div class="px-5 pb-8 text-center">
                    <button
                      type="button"
                      @click="deleteModalPreview = false"
                      class="btn btn-outline-secondary w-24 mr-1"
                    >
                      Cancel
                    </button>
                    <button type="button" class="btn btn-danger w-24">
                      Delete
                    </button>
                  </div>
                </ModalBody>
              </Modal>
              <!-- END: Modal Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Delete Modal -->
      <!-- BEGIN: Success Modal -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Success Modal</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-9"
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
            <!-- BEGIN: Modal Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                @click="successModalPreview = true"
                class="btn btn-primary"
                >Show Modal</a
              >
            </div>
            <!-- END: Modal Toggle -->
            <!-- BEGIN: Modal Content -->
            <Modal
              :show="successModalPreview"
              @hidden="successModalPreview = false"
            >
              <ModalBody class="p-0">
                <div class="p-5 text-center">
                  <CheckCircleIcon
                    class="w-16 h-16 text-success mx-auto mt-3"
                  />
                  <div class="text-3xl mt-5">Good job!</div>
                  <div class="text-slate-500 mt-2">You clicked the button!</div>
                </div>
                <div class="px-5 pb-8 text-center">
                  <button
                    type="button"
                    @click="successModalPreview = false"
                    class="btn btn-primary w-24"
                  >
                    Ok
                  </button>
                </div>
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
                  @click="successModalPreview = true"
                  class="btn btn-primary"
                  >Show Modal</a
                >
              </div>
              <!-- END: Modal Toggle -->
              <!-- BEGIN: Modal Content -->
              <Modal
                :show="successModalPreview"
                @hidden="successModalPreview = false"
              >
                <ModalBody class="p-0">
                  <div class="p-5 text-center">
                    <CheckCircleIcon
                      class="w-16 h-16 text-success mx-auto mt-3"
                    />
                    <div class="text-3xl mt-5">Good job!</div>
                    <div class="text-slate-500 mt-2">
                      You clicked the button!
                    </div>
                  </div>
                  <div class="px-5 pb-8 text-center">
                    <button
                      type="button"
                      @click="successModalPreview = false"
                      class="btn btn-primary w-24"
                    >
                      Ok
                    </button>
                  </div>
                </ModalBody>
              </Modal>
              <!-- END: Modal Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Success Modal -->
      <!-- BEGIN: Tiny Slider Modal -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Tiny Slider Modal</h2>
          <div
            class="form-check form-switch w-full sm:w-auto sm:ml-auto mt-3 sm:mt-0"
          >
            <label class="form-check-label ml-0" for="show-example-10"
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
            <!-- BEGIN: Modal Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                @click="tinySliderModalPreview = true"
                class="btn btn-primary"
                >Show Modal</a
              >
            </div>
            <!-- END: Modal Toggle -->
            <!-- BEGIN: Modal Content -->
            <Modal
              :show="tinySliderModalPreview"
              @hidden="tinySliderModalPreview = false"
            >
              <ModalBody>
                <div class="mx-6">
                  <TinySlider
                    :options="{
                      mouseDrag: true,
                      autoplay: false,
                      controls: true,
                      center: true,
                      items: 1,
                      nav: false,
                      speed: 500,
                      responsive: {
                        600: {
                          items: 2,
                        },
                      },
                    }"
                  >
                    <div class="h-56 px-2">
                      <div class="h-full image-fit rounded-md overflow-hidden">
                        <img
                          alt="Midone Tailwind HTML Admin Template"
                          :src="$f()[0].images[0]"
                        />
                      </div>
                    </div>
                    <div class="h-56 px-2">
                      <div class="h-full image-fit rounded-md overflow-hidden">
                        <img
                          alt="Midone Tailwind HTML Admin Template"
                          :src="$f()[0].images[1]"
                        />
                      </div>
                    </div>
                    <div class="h-56 px-2">
                      <div class="h-full image-fit rounded-md overflow-hidden">
                        <img
                          alt="Midone Tailwind HTML Admin Template"
                          :src="$f()[0].images[2]"
                        />
                      </div>
                    </div>
                    <div class="h-56 px-2">
                      <div class="h-full image-fit rounded-md overflow-hidden">
                        <img
                          alt="Midone Tailwind HTML Admin Template"
                          :src="$f()[0].images[3]"
                        />
                      </div>
                    </div>
                  </TinySlider>
                </div>
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
                  @click="tinySliderModalPreview = true"
                  class="btn btn-primary"
                  >Show Modal</a
                >
              </div>
              <!-- END: Modal Toggle -->
              <!-- BEGIN: Modal Content -->
              <Modal
                :show="tinySliderModalPreview"
                @hidden="tinySliderModalPreview = false"
              >
                <ModalBody>
                  <div class="mx-6">
                    <TinySlider
                      :options="{
                        mouseDrag: true,
                        autoplay: false,
                        controls: true,
                        center: true,
                        items: 1,
                        nav: false,
                        speed: 500,
                        responsive: {
                          600: {
                            items: 2,
                          },
                        },
                      }"
                    >
                      <div class="h-56 px-2">
                        <div
                          class="h-full image-fit rounded-md overflow-hidden"
                        >
                          <img
                            alt="Midone Tailwind HTML Admin Template"
                            :src="$f()[0].images[0]"
                          />
                        </div>
                      </div>
                      <div class="h-56 px-2">
                        <div
                          class="h-full image-fit rounded-md overflow-hidden"
                        >
                          <img
                            alt="Midone Tailwind HTML Admin Template"
                            :src="$f()[0].images[1]"
                          />
                        </div>
                      </div>
                      <div class="h-56 px-2">
                        <div
                          class="h-full image-fit rounded-md overflow-hidden"
                        >
                          <img
                            alt="Midone Tailwind HTML Admin Template"
                            :src="$f()[0].images[2]"
                          />
                        </div>
                      </div>
                      <div class="h-56 px-2">
                        <div
                          class="h-full image-fit rounded-md overflow-hidden"
                        >
                          <img
                            alt="Midone Tailwind HTML Admin Template"
                            :src="$f()[0].images[3]"
                          />
                        </div>
                      </div>
                    </TinySlider>
                  </div>
                </ModalBody>
              </Modal>
              <!-- END: Modal Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Tiny Slider Modal -->
      <!-- BEGIN: Programmatically Show/Hide Modal -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Programmatically Show/Hide Modal
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
        <div class="p-5">
          <Preview>
            <!-- BEGIN: Show Modal Toggle -->
            <div class="text-center">
              <a
                href="javascript:;"
                class="btn btn-primary mr-1 mb-2"
                @click="programmaticallyModal = true"
                >Show Modal</a
              >
            </div>
            <!-- END: Show Modal Toggle -->
            <!-- BEGIN: Modal Content -->
            <Modal
              :show="programmaticallyModal"
              @hidden="programmaticallyModal = false"
            >
              <ModalBody class="p-10 text-center">
                <!-- BEGIN: Hide Modal Toggle -->
                <a
                  href="javascript:;"
                  class="btn btn-primary mr-1"
                  @click="programmaticallyModal = false"
                  >Hide Modal</a
                >
                <!-- END: Hide Modal Toggle -->
                <!-- BEGIN: Toggle Modal Toggle -->
                <a
                  href="javascript:;"
                  class="btn btn-primary mr-1"
                  @click="programmaticallyModal = !programmaticallyModal"
                  >Toggle Modal</a
                >
                <!-- END: Toggle Modal Toggle -->
              </ModalBody>
            </Modal>
            <!-- END: Modal Content -->
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <!-- BEGIN: Show Modal Toggle -->
              <div class="text-center">
                <a
                  href="javascript:;"
                  class="btn btn-primary mr-1 mb-2"
                  @click="programmaticallyModal = true"
                  >Show Modal</a
                >
              </div>
              <!-- END: Show Modal Toggle -->
              <!-- BEGIN: Modal Content -->
              <Modal
                :show="programmaticallyModal"
                @hidden="programmaticallyModal = false"
              >
                <ModalBody class="p-10 text-center">
                  <!-- BEGIN: Hide Modal Toggle -->
                  <a
                    href="javascript:;"
                    class="btn btn-primary mr-1"
                    @click="programmaticallyModal = false"
                    >Hide Modal</a
                  >
                  <!-- END: Hide Modal Toggle -->
                  <!-- BEGIN: Toggle Modal Toggle -->
                  <a
                    href="javascript:;"
                    class="btn btn-primary mr-1"
                    @click="programmaticallyModal = !programmaticallyModal"
                    >Toggle Modal</a
                  >
                  <!-- END: Toggle Modal Toggle -->
                </ModalBody>
              </Modal>
              <!-- END: Modal Content -->
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Programmatically Show/Hide Modal -->
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
            Modals are built using the
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

const basicModalPreview = ref(false);
const smallModalSizePreview = ref(false);
const mediumModalSizePreview = ref(false);
const largeModalSizePreview = ref(false);
const superlargeModalSizePreview = ref(false);
const programmaticallyModal = ref(false);
const warningModalPreview = ref(false);
const buttonModalPreview = ref(false);
const staticBackdropModalPreview = ref(false);
const overlappingModalPreview = ref(false);
const nextOverlappingModalPreview = ref(false);
const headerFooterModalPreview = ref(false);
const deleteModalPreview = ref(false);
const successModalPreview = ref(false);
const tinySliderModalPreview = ref(false);
</script>
