<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">FAQ Layout</h2>
  </div>
  <div class="grid grid-cols-12 gap-6">
    <!-- BEGIN: FAQ Menu -->
    <div class="intro-y col-span-12 lg:col-span-4 xl:col-span-3">
      <div class="box mt-5">
        <div class="p-5">
          <a class="flex items-center text-primary font-medium" href="">
            <ActivityIcon class="w-4 h-4 mr-2" /> About Our Products
          </a>
          <a class="flex items-center mt-5" href="">
            <BoxIcon class="w-4 h-4 mr-2" /> Related License
          </a>
          <a class="flex items-center mt-5" href="">
            <LockIcon class="w-4 h-4 mr-2" /> Single Application License
          </a>
          <a class="flex items-center mt-5" href="">
            <SettingsIcon class="w-4 h-4 mr-2" /> Multi Application License
          </a>
        </div>
        <div class="p-5 border-t border-slate-200/60 dark:border-darkmode-400">
          <a class="flex items-center" href="">
            <ActivityIcon class="w-4 h-4 mr-2" /> Term of Use
          </a>
          <a class="flex items-center mt-5" href="">
            <BoxIcon class="w-4 h-4 mr-2" /> Author Fees
          </a>
          <a class="flex items-center mt-5" href="">
            <LockIcon class="w-4 h-4 mr-2" /> Product Review
          </a>
          <a class="flex items-center mt-5" href="">
            <SettingsIcon class="w-4 h-4 mr-2" /> Privacy Policy
          </a>
        </div>
        <div class="p-5 border-t border-slate-200/60 dark:border-darkmode-400">
          <a class="flex items-center" href="">
            <ActivityIcon class="w-4 h-4 mr-2" /> About Our Products
          </a>
          <a class="flex items-center mt-5" href="">
            <BoxIcon class="w-4 h-4 mr-2" /> Related License
          </a>
          <a class="flex items-center mt-5" href="">
            <LockIcon class="w-4 h-4 mr-2" /> Single Application License
          </a>
          <a class="flex items-center mt-5" href="">
            <SettingsIcon class="w-4 h-4 mr-2" /> Multi Application License
          </a>
        </div>
      </div>
    </div>
    <!-- END: FAQ Menu -->
    <!-- BEGIN: FAQ Content -->
    <div class="intro-y col-span-12 lg:col-span-8 xl:col-span-9">
      <div class="intro-y box lg:mt-5">
        <div
          class="flex items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">About Our Products</h2>
        </div>
        <AccordionGroup class="p-5">
          <AccordionItem>
            <Accordion>
              OpenSSL Essentials: Working with SSL Certificates, Private Keys
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion>
              Understanding IP Addresses, Subnets, and CIDR Notation
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion> How To Troubleshoot Common HTTP Error Codes </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion> An Introduction to Securing your Linux VPS </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
        </AccordionGroup>
      </div>
      <div class="intro-y box mt-5">
        <div
          class="flex items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">Related License</h2>
        </div>
        <AccordionGroup class="p-5">
          <AccordionItem>
            <Accordion>
              OpenSSL Essentials: Working with SSL Certificates, Private Keys
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion>
              Understanding IP Addresses, Subnets, and CIDR Notation
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion> How To Troubleshoot Common HTTP Error Codes </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion> An Introduction to Securing your Linux VPS </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
        </AccordionGroup>
      </div>
      <div class="intro-y box mt-5">
        <div
          class="flex items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Single Application License
          </h2>
        </div>
        <AccordionGroup class="p-5">
          <AccordionItem>
            <Accordion>
              OpenSSL Essentials: Working with SSL Certificates, Private Keys
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion>
              Understanding IP Addresses, Subnets, and CIDR Notation
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion> How To Troubleshoot Common HTTP Error Codes </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion> An Introduction to Securing your Linux VPS </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged.
            </AccordionPanel>
          </AccordionItem>
        </AccordionGroup>
      </div>
    </div>
    <!-- END: FAQ Content -->
  </div>
</template>
