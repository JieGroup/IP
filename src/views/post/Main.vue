<template>
  <div class="intro-y flex flex-col sm:flex-row items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Add New Post</h2>
    <div class="w-full sm:w-auto flex mt-4 sm:mt-0">
      <Dropdown class="mr-2">
        <DropdownToggle class="btn box flex items-center">
          English <ChevronDownIcon class="w-4 h-4 ml-2" />
        </DropdownToggle>
        <DropdownMenu class="w-40">
          <DropdownContent>
            <DropdownItem>
              <ActivityIcon class="w-4 h-4 mr-2" />
              <span class="truncate">English</span>
            </DropdownItem>
            <DropdownItem>
              <ActivityIcon class="w-4 h-4 mr-2" />
              <span class="truncate">Indonesian</span>
            </DropdownItem>
          </DropdownContent>
        </DropdownMenu>
      </Dropdown>
      <button
        type="button"
        class="btn box mr-2 flex items-center ml-auto sm:ml-0"
      >
        <EyeIcon class="w-4 h-4 mr-2" /> Preview
      </button>
      <Dropdown>
        <DropdownToggle class="btn btn-primary shadow-md flex items-center">
          Save <ChevronDownIcon class="w-4 h-4 ml-2" />
        </DropdownToggle>
        <DropdownMenu class="w-40">
          <DropdownContent>
            <DropdownItem>
              <FileTextIcon class="w-4 h-4 mr-2" /> As New Post
            </DropdownItem>
            <DropdownItem>
              <FileTextIcon class="w-4 h-4 mr-2" /> As Draft
            </DropdownItem>
            <DropdownItem>
              <FileTextIcon class="w-4 h-4 mr-2" /> Export to PDF
            </DropdownItem>
            <DropdownItem>
              <FileTextIcon class="w-4 h-4 mr-2" /> Export to Word
            </DropdownItem>
          </DropdownContent>
        </DropdownMenu>
      </Dropdown>
    </div>
  </div>
  <div class="pos intro-y grid grid-cols-12 gap-5 mt-5">
    <!-- BEGIN: Post Content -->
    <div class="intro-y col-span-12 lg:col-span-8">
      <input
        type="text"
        class="intro-y form-control py-3 px-4 box pr-10"
        placeholder="Title"
      />
      <TabGroup class="post intro-y overflow-hidden box mt-5">
        <TabList
          class="post__tabs nav-tabs flex-col sm:flex-row bg-slate-200 dark:bg-darkmode-800"
        >
          <Tab :fullWidth="false" class="w-full sm:w-40 py-0 px-0" tag="button">
            <Tippy
              content="Fill in the article content"
              class="tooltip w-full flex items-center justify-center py-4"
              aria-controls="content"
              aria-selected="true"
            >
              <FileTextIcon class="w-4 h-4 mr-2" /> Content
            </Tippy>
          </Tab>
          <Tab :fullWidth="false" class="w-full sm:w-40 py-0 px-0" tag="button">
            <Tippy
              content="Adjust the meta title"
              class="tooltip w-full flex items-center justify-center py-4"
              aria-selected="false"
            >
              <CodeIcon class="w-4 h-4 mr-2" /> Meta Title
            </Tippy>
          </Tab>
          <Tab :fullWidth="false" class="w-full sm:w-40 py-0 px-0" tag="button">
            <Tippy
              content="Use search keywords"
              class="tooltip w-full flex items-center justify-center py-4"
              aria-selected="false"
            >
              <AlignLeftIcon class="w-4 h-4 mr-2" /> Keywords
            </Tippy>
          </Tab>
        </TabList>
        <TabPanels class="post__content">
          <TabPanel class="p-5">
            <div
              class="border border-slate-200/60 dark:border-darkmode-400 rounded-md p-5"
            >
              <div
                class="font-medium flex items-center border-b border-slate-200/60 dark:border-darkmode-400 pb-5"
              >
                <ChevronDownIcon class="w-4 h-4 mr-2" /> Text Content
              </div>
              <div class="mt-5">
                <ClassicEditor v-model="editorData" />
              </div>
            </div>
            <div
              class="border border-slate-200/60 dark:border-darkmode-400 rounded-md p-5 mt-5"
            >
              <div
                class="font-medium flex items-center border-b border-slate-200/60 dark:border-darkmode-400 pb-5"
              >
                <ChevronDownIcon class="w-4 h-4 mr-2" /> Caption & Images
              </div>
              <div class="mt-5">
                <div>
                  <label for="post-form-7" class="form-label">Caption</label>
                  <input
                    id="post-form-7"
                    type="text"
                    class="form-control"
                    placeholder="Write caption"
                  />
                </div>
                <div class="mt-3">
                  <label class="form-label">Upload Image</label>
                  <div
                    class="border-2 border-dashed dark:border-darkmode-400 rounded-md pt-4"
                  >
                    <div class="flex flex-wrap px-4">
                      <div
                        v-for="(faker, fakerKey) in $_.take($f(), 4)"
                        :key="fakerKey"
                        class="w-24 h-24 relative image-fit mb-5 mr-5 cursor-pointer zoom-in"
                      >
                        <img
                          class="rounded-md"
                          alt="Midone Tailwind HTML Admin Template"
                          :src="faker.images[0]"
                        />
                        <Tippy
                          tag="div"
                          content="Remove this image?"
                          class="w-5 h-5 flex items-center justify-center absolute rounded-full text-white bg-danger right-0 top-0 -mr-2 -mt-2"
                        >
                          <xIcon class="w-4 h-4" />
                        </Tippy>
                      </div>
                    </div>
                    <div
                      class="px-4 pb-4 flex items-center cursor-pointer relative"
                    >
                      <ImageIcon class="w-4 h-4 mr-2" />
                      <span class="text-primary mr-1">Upload a file</span> or
                      drag and drop
                      <input
                        type="file"
                        class="w-full h-full top-0 left-0 absolute opacity-0"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </TabPanel>
        </TabPanels>
      </TabGroup>
    </div>
    <!-- END: Post Content -->
    <!-- BEGIN: Post Info -->
    <div class="col-span-12 lg:col-span-4">
      <div class="intro-y box p-5">
        <div>
          <label class="form-label">Written By</label>
          <Dropdown>
            <DropdownToggle
              tag="div"
              class="btn w-full btn-outline-secondary dark:bg-darkmode-800 dark:border-darkmode-800 flex items-center justify-start"
              role="button"
            >
              <div class="w-6 h-6 image-fit mr-3">
                <img
                  class="rounded"
                  alt="Midone Tailwind HTML Admin Template"
                  :src="$f()[0].photos[0]"
                />
              </div>
              <div class="truncate">{{ $f()[0].users[0].name }}</div>
              <ChevronDownIcon class="w-4 h-4 ml-auto" />
            </DropdownToggle>
            <DropdownMenu class="w-full">
              <DropdownContent>
                <DropdownItem
                  v-for="(faker, fakerKey) in $_.take($f(), 5)"
                  :key="fakerKey"
                >
                  <div class="w-6 h-6 absolute image-fit mr-3">
                    <img
                      class="rounded"
                      alt="Midone Tailwind HTML Admin Template"
                      :src="faker.photos[0]"
                    />
                  </div>
                  <div class="ml-8 pl-1">{{ faker.users[0].name }}</div>
                </DropdownItem>
              </DropdownContent>
            </DropdownMenu>
          </Dropdown>
        </div>
        <div class="mt-3">
          <label for="post-form-2" class="form-label">Post Date</label>
          <Litepicker
            id="post-form-2"
            v-model="salesReportFilter"
            :options="{
              autoApply: false,
              showWeekNumbers: true,
              dropdowns: {
                minYear: 1990,
                maxYear: null,
                months: true,
                years: true,
              },
            }"
            class="form-control"
          />
        </div>
        <div class="mt-3">
          <label for="post-form-3" class="form-label">Categories</label>
          <TomSelect
            id="post-form-3"
            v-model="categories"
            class="w-full"
            multiple
          >
            <option value="1">Horror</option>
            <option value="2">Sci-fi</option>
            <option value="3">Action</option>
            <option value="4">Drama</option>
            <option value="5">Comedy</option>
          </TomSelect>
        </div>
        <div class="mt-3">
          <label for="post-form-4" class="form-label">Tags</label>
          <TomSelect id="post-form-4" v-model="tags" class="w-full" multiple>
            <option value="1">Leonardo DiCaprio</option>
            <option value="2">Johnny Deep</option>
            <option value="3">Robert Downey, Jr</option>
            <option value="4">Samuel L. Jackson</option>
            <option value="5">Morgan Freeman</option>
          </TomSelect>
        </div>
        <div class="form-check form-switch flex flex-col items-start mt-3">
          <label for="post-form-5" class="form-check-label ml-0 mb-2"
            >Published</label
          >
          <input id="post-form-5" class="form-check-input" type="checkbox" />
        </div>
        <div class="form-check form-switch flex flex-col items-start mt-3">
          <label for="post-form-6" class="form-check-label ml-0 mb-2"
            >Show Author Name</label
          >
          <input id="post-form-6" class="form-check-input" type="checkbox" />
        </div>
      </div>
    </div>
    <!-- END: Post Info -->
  </div>
</template>

<script setup>
import { ref } from "vue";

const categories = ref(["1", "2"]);
const tags = ref(["1", "2"]);
const salesReportFilter = ref("");
const editorData = ref("<p>Content of the editor.</p>");
</script>
