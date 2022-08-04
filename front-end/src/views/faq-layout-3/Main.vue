<template>
  <div class="intro-y flex items-center mt-8">
    <h2 class="text-lg font-medium mr-auto">FAQ Layout</h2>
  </div>
  <div class="grid grid-cols-12 gap-6">
    <!-- BEGIN: FAQ Menu -->
    <div class="intro-y col-span-12 lg:col-span-4 xl:col-span-3">
      <div class="box mt-5">
        <div class="px-4 pb-3 pt-5">
          <a
            class="flex rounded-lg items-center px-4 py-2 bg-primary text-white font-medium"
            href=""
          >
            <ActivityIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">About Our Products</div>
          </a>
          <!-- <a class="flex items-center px-4 py-2 mt-1" href="">
            <BoxIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Related License</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <LockIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Single Application License</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <SettingsIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Multi Application License</div>
          </a> -->
        </div>
        <!-- <div
          class="px-4 py-3 border-t border-slate-200/60 dark:border-darkmode-400"
        >
          <a class="flex items-center px-4 py-2" href="">
            <ActivityIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Trem of Use</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <BoxIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Author Fees</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <LockIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Product Review</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <SettingsIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Privacy Policy</div>
          </a>
        </div> -->
        <!-- <div
          class="px-4 pt-3 pb-5 border-t border-slate-200/60 dark:border-darkmode-400"
        >
          <a class="flex items-center px-4 py-2" href="">
            <ActivityIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">About Our Products</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <BoxIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Related License</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <LockIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Single Application License</div>
          </a>
          <a class="flex items-center px-4 py-2 mt-1" href="">
            <SettingsIcon class="w-4 h-4 mr-2" />
            <div class="flex-1 truncate">Multi Application License</div>
          </a>
        </div> -->
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
        <AccordionGroup class="accordion-boxed p-5">
          <AccordionItem>
            <Accordion>
              Design your own survey to project voter's privacy
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              Interval Privacy is led by Professor Jie Ding. 
              He received his Ph.D. degree in Engineering Sciences from Harvard University, Cambridge, in 2017. 
              He obtained his B.S. degree from Tsinghua University, Beijing, in 2012. 
              He joined the faculty of the University of Minnesota, Twin Cities, in 2018, where he has been an Assistant Professor at the School of Statistics, with a graduate faculty appointment at the Department of Electrical and Computer Engineering. 
              His research is on the foundations of machine learning, statistics, and signal processing.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion>
              How to Create Survey?
            </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              1. Click 'Login' icon in the left bar
              <br/>
              2. Login to your account
              <br/>
              3. Click 'Create Form' icon in the left bar
              <br/>
              4. Design your own survey template
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion> How To Retrieve Survey Answers </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              1. Click 'Login' icon in the left bar
              <br/>
              2. Login to your account
              <br/>
              3. Click 'Histories' icon in the left bar
              <br/>
              4. All your designed survey template will be displayed in chronological order.
              By clicking 'Download', you can download all survey answers of the specific survey template.
              By clicking 'View Details', you can view your designed template.
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <Accordion> How to Answer Survey </Accordion>
            <AccordionPanel
              class="text-slate-600 dark:text-slate-500 leading-relaxed"
            >
              1. Click 'Answer Form' icon in the left bar
              <br/>
              2. Type in the Survey Template ID and your Mturk ID
              3. Keep answering the Survey until it shows 'Thank you for your participation'
              4. Record the Survey Answer ID to get your payment
            </AccordionPanel>
          </AccordionItem>
        </AccordionGroup>
      </div>
      <!-- <div class="intro-y box mt-5">
        <div
          class="flex items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Single Application License
          </h2>
        </div>
        <AccordionGroup class="accordion-boxed p-5">
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
      </div> -->
      <!-- <div class="intro-y box mt-5">
        <div
          class="flex items-center p-5 border-b border-slate-200/60 dark:border-darkmode-400"
        >
          <h2 class="font-medium text-base mr-auto">
            Multi Application License
          </h2>
        </div>
        <AccordionGroup class="accordion-boxed p-5">
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
      </div> -->
    </div>
    <!-- END: FAQ Content -->
  </div>
</template>
