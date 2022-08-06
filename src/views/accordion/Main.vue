<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">Accordion</h2>
  </div>
  <div class="intro-y grid grid-cols-12 gap-6 mt-5">
    <!-- BEGIN: Basic Accordion -->
    <div class="col-span-12 lg:col-span-6">
      <PreviewComponent class="intro-y box" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Basic Accordion</h2>
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
            <AccordionGroup>
              <AccordionItem>
                <Accordion>
                  OpenSSL Essentials: Working with SSL Certificates, Private
                  Keys
                </Accordion>
                <AccordionPanel
                  class="text-slate-600 dark:text-slate-500 leading-relaxed"
                >
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s, when an unknown
                  printer took a galley of type and scrambled it to make a type
                  specimen book. It has survived not only five centuries, but
                  also the leap into electronic typesetting, remaining
                  essentially unchanged.
                </AccordionPanel>
              </AccordionItem>
              <AccordionItem>
                <Accordion>
                  Understanding IP Addresses, Subnets, and CIDR Notation
                </Accordion>
                <AccordionPanel
                  class="text-slate-600 dark:text-slate-500 leading-relaxed"
                >
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s, when an unknown
                  printer took a galley of type and scrambled it to make a type
                  specimen book. It has survived not only five centuries, but
                  also the leap into electronic typesetting, remaining
                  essentially unchanged.
                </AccordionPanel>
              </AccordionItem>
              <AccordionItem>
                <Accordion>
                  How To Troubleshoot Common HTTP Error Codes
                </Accordion>
                <AccordionPanel
                  class="text-slate-600 dark:text-slate-500 leading-relaxed"
                >
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s, when an unknown
                  printer took a galley of type and scrambled it to make a type
                  specimen book. It has survived not only five centuries, but
                  also the leap into electronic typesetting, remaining
                  essentially unchanged.
                </AccordionPanel>
              </AccordionItem>
              <AccordionItem>
                <Accordion>
                  An Introduction to Securing your Linux VPS
                </Accordion>
                <AccordionPanel
                  class="text-slate-600 dark:text-slate-500 leading-relaxed"
                >
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s, when an unknown
                  printer took a galley of type and scrambled it to make a type
                  specimen book. It has survived not only five centuries, but
                  also the leap into electronic typesetting, remaining
                  essentially unchanged.
                </AccordionPanel>
              </AccordionItem>
            </AccordionGroup>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <AccordionGroup>
                <AccordionItem>
                  <Accordion>
                    OpenSSL Essentials: Working with SSL Certificates, Private
                    Keys
                  </Accordion>
                  <AccordionPanel
                    class="text-slate-600 dark:text-slate-500 leading-relaxed"
                  >
                    Lorem Ipsum is simply dummy text of the printing and
                    typesetting industry. Lorem Ipsum has been the industry's
                    standard dummy text ever since the 1500s, when an unknown
                    printer took a galley of type and scrambled it to make a
                    type specimen book. It has survived not only five centuries,
                    but also the leap into electronic typesetting, remaining
                    essentially unchanged.
                  </AccordionPanel>
                </AccordionItem>
                <AccordionItem>
                  <Accordion>
                    Understanding IP Addresses, Subnets, and CIDR Notation
                  </Accordion>
                  <AccordionPanel
                    class="text-slate-600 dark:text-slate-500 leading-relaxed"
                  >
                    Lorem Ipsum is simply dummy text of the printing and
                    typesetting industry. Lorem Ipsum has been the industry's
                    standard dummy text ever since the 1500s, when an unknown
                    printer took a galley of type and scrambled it to make a
                    type specimen book. It has survived not only five centuries,
                    but also the leap into electronic typesetting, remaining
                    essentially unchanged.
                  </AccordionPanel>
                </AccordionItem>
                <AccordionItem>
                  <Accordion>
                    How To Troubleshoot Common HTTP Error Codes
                  </Accordion>
                  <AccordionPanel
                    class="text-slate-600 dark:text-slate-500 leading-relaxed"
                  >
                    Lorem Ipsum is simply dummy text of the printing and
                    typesetting industry. Lorem Ipsum has been the industry's
                    standard dummy text ever since the 1500s, when an unknown
                    printer took a galley of type and scrambled it to make a
                    type specimen book. It has survived not only five centuries,
                    but also the leap into electronic typesetting, remaining
                    essentially unchanged.
                  </AccordionPanel>
                </AccordionItem>
                <AccordionItem>
                  <Accordion>
                    An Introduction to Securing your Linux VPS
                  </Accordion>
                  <AccordionPanel
                    class="text-slate-600 dark:text-slate-500 leading-relaxed"
                  >
                    Lorem Ipsum is simply dummy text of the printing and
                    typesetting industry. Lorem Ipsum has been the industry's
                    standard dummy text ever since the 1500s, when an unknown
                    printer took a galley of type and scrambled it to make a
                    type specimen book. It has survived not only five centuries,
                    but also the leap into electronic typesetting, remaining
                    essentially unchanged.
                  </AccordionPanel>
                </AccordionItem>
              </AccordionGroup>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
      <PreviewComponent class="intro-y box mt-5" v-slot="{ toggle }">
        <div
          class="flex flex-col sm:flex-row items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Boxed Accordion</h2>
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
            <AccordionGroup class="accordion-boxed">
              <AccordionItem>
                <Accordion>
                  OpenSSL Essentials: Working with SSL Certificates, Private
                  Keys
                </Accordion>
                <AccordionPanel
                  class="text-slate-600 dark:text-slate-500 leading-relaxed"
                >
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s, when an unknown
                  printer took a galley of type and scrambled it to make a type
                  specimen book. It has survived not only five centuries, but
                  also the leap into electronic typesetting, remaining
                  essentially unchanged.
                </AccordionPanel>
              </AccordionItem>
              <AccordionItem>
                <Accordion>
                  Understanding IP Addresses, Subnets, and CIDR Notation
                </Accordion>
                <AccordionPanel
                  class="text-slate-600 dark:text-slate-500 leading-relaxed"
                >
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s, when an unknown
                  printer took a galley of type and scrambled it to make a type
                  specimen book. It has survived not only five centuries, but
                  also the leap into electronic typesetting, remaining
                  essentially unchanged.
                </AccordionPanel>
              </AccordionItem>
              <AccordionItem>
                <Accordion>
                  How To Troubleshoot Common HTTP Error Codes
                </Accordion>
                <AccordionPanel
                  class="text-slate-600 dark:text-slate-500 leading-relaxed"
                >
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s, when an unknown
                  printer took a galley of type and scrambled it to make a type
                  specimen book. It has survived not only five centuries, but
                  also the leap into electronic typesetting, remaining
                  essentially unchanged.
                </AccordionPanel>
              </AccordionItem>
              <AccordionItem>
                <Accordion>
                  An Introduction to Securing your Linux VPS
                </Accordion>
                <AccordionPanel
                  class="text-slate-600 dark:text-slate-500 leading-relaxed"
                >
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy text ever since the 1500s, when an unknown
                  printer took a galley of type and scrambled it to make a type
                  specimen book. It has survived not only five centuries, but
                  also the leap into electronic typesetting, remaining
                  essentially unchanged.
                </AccordionPanel>
              </AccordionItem>
            </AccordionGroup>
          </Preview>
          <Source>
            <Highlight>
              {{ `
              <AccordionGroup class="accordion-boxed">
                <AccordionItem>
                  <Accordion>
                    OpenSSL Essentials: Working with SSL Certificates, Private
                    Keys
                  </Accordion>
                  <AccordionPanel
                    class="text-slate-600 dark:text-slate-500 leading-relaxed"
                  >
                    Lorem Ipsum is simply dummy text of the printing and
                    typesetting industry. Lorem Ipsum has been the industry's
                    standard dummy text ever since the 1500s, when an unknown
                    printer took a galley of type and scrambled it to make a
                    type specimen book. It has survived not only five centuries,
                    but also the leap into electronic typesetting, remaining
                    essentially unchanged.
                  </AccordionPanel>
                </AccordionItem>
                <AccordionItem>
                  <Accordion>
                    Understanding IP Addresses, Subnets, and CIDR Notation
                  </Accordion>
                  <AccordionPanel
                    class="text-slate-600 dark:text-slate-500 leading-relaxed"
                  >
                    Lorem Ipsum is simply dummy text of the printing and
                    typesetting industry. Lorem Ipsum has been the industry's
                    standard dummy text ever since the 1500s, when an unknown
                    printer took a galley of type and scrambled it to make a
                    type specimen book. It has survived not only five centuries,
                    but also the leap into electronic typesetting, remaining
                    essentially unchanged.
                  </AccordionPanel>
                </AccordionItem>
                <AccordionItem>
                  <Accordion>
                    How To Troubleshoot Common HTTP Error Codes
                  </Accordion>
                  <AccordionPanel
                    class="text-slate-600 dark:text-slate-500 leading-relaxed"
                  >
                    Lorem Ipsum is simply dummy text of the printing and
                    typesetting industry. Lorem Ipsum has been the industry's
                    standard dummy text ever since the 1500s, when an unknown
                    printer took a galley of type and scrambled it to make a
                    type specimen book. It has survived not only five centuries,
                    but also the leap into electronic typesetting, remaining
                    essentially unchanged.
                  </AccordionPanel>
                </AccordionItem>
                <AccordionItem>
                  <Accordion>
                    An Introduction to Securing your Linux VPS
                  </Accordion>
                  <AccordionPanel
                    class="text-slate-600 dark:text-slate-500 leading-relaxed"
                  >
                    Lorem Ipsum is simply dummy text of the printing and
                    typesetting industry. Lorem Ipsum has been the industry's
                    standard dummy text ever since the 1500s, when an unknown
                    printer took a galley of type and scrambled it to make a
                    type specimen book. It has survived not only five centuries,
                    but also the leap into electronic typesetting, remaining
                    essentially unchanged.
                  </AccordionPanel>
                </AccordionItem>
              </AccordionGroup>
              ` }}
            </Highlight>
          </Source>
        </div>
      </PreviewComponent>
    </div>
    <!-- END: Basic Accordion -->
    <!-- BEGIN: Boxed Accordion -->
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
            Accordions are built using the
            <span class="text-red-500">`AccordionGroup`</span>,
            <span class="text-red-500">`AccordionItem`</span>,
            <span class="text-red-500">`Accordion`</span> and
            <span class="text-red-500">`AccordionPanel`</span> components.
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
          <div class="text-base font-medium">Accordion</div>
          <div class="mt-2">The main Accordion component.</div>
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
                <td class="align-top">`index`, `null`</td>
                <td class="align-top">`0`</td>
                <td class="align-top">
                  <div class="font-medium mb-1">`Number`, `Object`</div>
                  Specifies the index of the selected accordion.
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
                  This event fires immediately when there is a change in active
                  accordion.
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <!-- END: Component API -->
    </div>
    <!-- END: Boxed Accordion -->
  </div>
</template>
