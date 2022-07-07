<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Tab</h2>
  </div>
  <div class="intro-y grid grid-cols-12 gap-6 mt-5">
    <div class="col-span-12 lg:col-span-6">
      <!-- BEGIN: Basic Tab -->
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Basic Tab</h2>
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
            <TabGroup>
              <TabList class="nav-tabs">
                <Tab class="w-full py-2" tag="button">Example Tab 1</Tab>
                <Tab class="w-full py-2" tag="button">Example Tab 2</Tab>
              </TabList>
              <TabPanels class="border-l border-r border-b">
                <TabPanel class="leading-relaxed p-5">
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s, when an unknown
                  printer took a galley of type and scrambled it to make a type
                  specimen book. It has survived not only five centuries, but
                  also the leap into electronic typesetting, remaining
                  essentially unchanged. It was popularised in the 1960s with
                  the release of Letraset sheets containing Lorem Ipsum
                  passages, and more recently with desktop publishing software
                  like Aldus PageMaker including versions of Lorem Ipsum.
                </TabPanel>
                <TabPanel class="leading-relaxed p-5">
                  It is a long established fact that a reader will be distracted
                  by the readable content of a page when looking at its layout.
                  The point of using Lorem Ipsum is that it has a more-or-less
                  normal distribution of letters, as opposed to using 'Content
                  here, content here', making it look like readable English.
                  Many desktop publishing packages and web page editors now use
                  Lorem Ipsum as their default model text, and a search for
                  'lorem ipsum' will uncover many web sites still in their
                  infancy. Various versions have evolved over the years,
                  sometimes by accident, sometimes on purpose (injected humour
                  and the like).
                </TabPanel>
              </TabPanels>
            </TabGroup>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <TabGroup>
                <TabList class="nav-tabs">
                  <Tab class="w-full py-2" tag="button">Example Tab 1</Tab>
                  <Tab class="w-full py-2" tag="button">Example Tab 2</Tab>
                </TabList>
                <TabPanels class="border-l border-r border-b">
                  <TabPanel class="leading-relaxed p-5">
                    Lorem Ipsum is simply dummy text of the printing and
                    typesetting industry. Lorem Ipsum has been the industry's
                    standard dummy text ever since the 1500s, when an unknown
                    printer took a galley of type and scrambled it to make a
                    type specimen book. It has survived not only five centuries,
                    but also the leap into electronic typesetting, remaining
                    essentially unchanged. It was popularised in the 1960s with
                    the release of Letraset sheets containing Lorem Ipsum
                    passages, and more recently with desktop publishing software
                    like Aldus PageMaker including versions of Lorem Ipsum.
                  </TabPanel>
                  <TabPanel class="leading-relaxed p-5">
                    It is a long established fact that a reader will be
                    distracted by the readable content of a page when looking at
                    its layout. The point of using Lorem Ipsum is that it has a
                    more-or-less normal distribution of letters, as opposed to
                    using 'Content here, content here', making it look like
                    readable English. Many desktop publishing packages and web
                    page editors now use Lorem Ipsum as their default model
                    text, and a search for 'lorem ipsum' will uncover many web
                    sites still in their infancy. Various versions have evolved
                    over the years, sometimes by accident, sometimes on purpose
                    (injected humour and the like).
                  </TabPanel>
                </TabPanels>
              </TabGroup>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Basic Tab -->
      <!-- BEGIN: Boxed Tab -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Boxed Tab</h2>
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
            <TabGroup>
              <TabList class="nav-boxed-tabs">
                <Tab class="w-full py-2" tag="button">Example Tab 1</Tab>
                <Tab class="w-full py-2" tag="button">Example Tab 2</Tab>
              </TabList>
              <TabPanels class="mt-5">
                <TabPanel class="leading-relaxed">
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s, when an unknown
                  printer took a galley of type and scrambled it to make a type
                  specimen book. It has survived not only five centuries, but
                  also the leap into electronic typesetting, remaining
                  essentially unchanged. It was popularised in the 1960s with
                  the release of Letraset sheets containing Lorem Ipsum
                  passages, and more recently with desktop publishing software
                  like Aldus PageMaker including versions of Lorem Ipsum.
                </TabPanel>
                <TabPanel class="leading-relaxed">
                  It is a long established fact that a reader will be distracted
                  by the readable content of a page when looking at its layout.
                  The point of using Lorem Ipsum is that it has a more-or-less
                  normal distribution of letters, as opposed to using 'Content
                  here, content here', making it look like readable English.
                  Many desktop publishing packages and web page editors now use
                  Lorem Ipsum as their default model text, and a search for
                  'lorem ipsum' will uncover many web sites still in their
                  infancy. Various versions have evolved over the years,
                  sometimes by accident, sometimes on purpose (injected humour
                  and the like).
                </TabPanel>
              </TabPanels>
            </TabGroup>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <TabGroup>
                <TabList class="nav-boxed-tabs">
                  <Tab class="w-full py-2" tag="button">Example Tab 1</Tab>
                  <Tab class="w-full py-2" tag="button">Example Tab 2</Tab>
                </TabList>
                <TabPanels class="mt-5">
                  <TabPanel class="leading-relaxed">
                    Lorem Ipsum is simply dummy text of the printing and
                    typesetting industry. Lorem Ipsum has been the industry's
                    standard dummy text ever since the 1500s, when an unknown
                    printer took a galley of type and scrambled it to make a
                    type specimen book. It has survived not only five centuries,
                    but also the leap into electronic typesetting, remaining
                    essentially unchanged. It was popularised in the 1960s with
                    the release of Letraset sheets containing Lorem Ipsum
                    passages, and more recently with desktop publishing software
                    like Aldus PageMaker including versions of Lorem Ipsum.
                  </TabPanel>
                  <TabPanel class="leading-relaxed">
                    It is a long established fact that a reader will be
                    distracted by the readable content of a page when looking at
                    its layout. The point of using Lorem Ipsum is that it has a
                    more-or-less normal distribution of letters, as opposed to
                    using 'Content here, content here', making it look like
                    readable English. Many desktop publishing packages and web
                    page editors now use Lorem Ipsum as their default model
                    text, and a search for 'lorem ipsum' will uncover many web
                    sites still in their infancy. Various versions have evolved
                    over the years, sometimes by accident, sometimes on purpose
                    (injected humour and the like).
                  </TabPanel>
                </TabPanels>
              </TabGroup>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Boxed Tab -->
      <!-- BEGIN: Link Tab -->
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Link Tab</h2>
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
            <TabGroup>
              <TabList class="nav-link-tabs">
                <Tab class="w-full py-2" tag="button">Example Tab 1</Tab>
                <Tab class="w-full py-2" tag="button">Example Tab 2</Tab>
              </TabList>
              <TabPanels class="mt-5">
                <TabPanel class="leading-relaxed">
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s, when an unknown
                  printer took a galley of type and scrambled it to make a type
                  specimen book. It has survived not only five centuries, but
                  also the leap into electronic typesetting, remaining
                  essentially unchanged. It was popularised in the 1960s with
                  the release of Letraset sheets containing Lorem Ipsum
                  passages, and more recently with desktop publishing software
                  like Aldus PageMaker including versions of Lorem Ipsum.
                </TabPanel>
                <TabPanel class="leading-relaxed">
                  It is a long established fact that a reader will be distracted
                  by the readable content of a page when looking at its layout.
                  The point of using Lorem Ipsum is that it has a more-or-less
                  normal distribution of letters, as opposed to using 'Content
                  here, content here', making it look like readable English.
                  Many desktop publishing packages and web page editors now use
                  Lorem Ipsum as their default model text, and a search for
                  'lorem ipsum' will uncover many web sites still in their
                  infancy. Various versions have evolved over the years,
                  sometimes by accident, sometimes on purpose (injected humour
                  and the like).
                </TabPanel>
              </TabPanels>
            </TabGroup>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <TabGroup>
                <TabList class="nav-link-tabs">
                  <Tab class="w-full py-2" tag="button">Example Tab 1</Tab>
                  <Tab class="w-full py-2" tag="button">Example Tab 2</Tab>
                </TabList>
                <TabPanels class="mt-5">
                  <TabPanel class="leading-relaxed">
                    Lorem Ipsum is simply dummy text of the printing and
                    typesetting industry. Lorem Ipsum has been the industry's
                    standard dummy text ever since the 1500s, when an unknown
                    printer took a galley of type and scrambled it to make a
                    type specimen book. It has survived not only five centuries,
                    but also the leap into electronic typesetting, remaining
                    essentially unchanged. It was popularised in the 1960s with
                    the release of Letraset sheets containing Lorem Ipsum
                    passages, and more recently with desktop publishing software
                    like Aldus PageMaker including versions of Lorem Ipsum.
                  </TabPanel>
                  <TabPanel class="leading-relaxed">
                    It is a long established fact that a reader will be
                    distracted by the readable content of a page when looking at
                    its layout. The point of using Lorem Ipsum is that it has a
                    more-or-less normal distribution of letters, as opposed to
                    using 'Content here, content here', making it look like
                    readable English. Many desktop publishing packages and web
                    page editors now use Lorem Ipsum as their default model
                    text, and a search for 'lorem ipsum' will uncover many web
                    sites still in their infancy. Various versions have evolved
                    over the years, sometimes by accident, sometimes on purpose
                    (injected humour and the like).
                  </TabPanel>
                </TabPanels>
              </TabGroup>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <!-- END: Basic Tab -->
    </div>
    <div class="col-span-12 lg:col-span-6">
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
              Tabs are built using the
              <span class="text-red-500">`TabGroup`</span>,
              <span class="text-red-500">`TabList`</span>,
              <span class="text-red-500">`Tab`</span>,
              <span class="text-red-500">`TabPanels`</span> and
              <span class="text-red-500">`TabPanel`</span> components.
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
            <div class="text-base font-medium">TabGroup</div>
            <div class="mt-2">The main TabGroup component.</div>
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
                  <td class="align-top text-red-500">`selectedIndex`</td>
                  <td class="align-top">`index`</td>
                  <td class="align-top">`0`</td>
                  <td class="align-top">
                    <div class="font-medium mb-1">`Number`</div>
                    Specifies the index of the selected tab.
                  </td>
                </tr>
                <tr>
                  <td class="align-top text-red-500">`tag`</td>
                  <td class="align-top">`div`</td>
                  <td class="align-top">`div`</td>
                  <td class="align-top">
                    <div class="font-medium mb-1">`String`</div>
                    Specifies HTML tag to use.
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
                  <td class="align-top text-red-500">`change`</td>
                  <td class="align-top">
                    This event fires immediately when there is a change in
                    active tab.
                  </td>
                </tr>
              </tbody>
            </table>
            <div class="text-base font-medium mt-5">Tab</div>
            <div class="mt-2">The main Tab component.</div>
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
                  <td class="align-top text-red-500">`fullWidth`</td>
                  <td class="align-top">`true`, `false`</td>
                  <td class="align-top">`true`</td>
                  <td class="align-top">
                    <div class="font-medium mb-1">`Boolean`</div>
                    Whether the Tab appears as full width or not.
                  </td>
                </tr>
                <tr>
                  <td class="align-top text-red-500">`tag`</td>
                  <td class="align-top">`a`</td>
                  <td class="align-top">`a`</td>
                  <td class="align-top">
                    <div class="font-medium mb-1">`String`</div>
                    Specifies HTML tag to use.
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <!-- END: Component API -->
      </div>
    </div>
  </div>
</template>
