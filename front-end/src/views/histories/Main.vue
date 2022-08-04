<template>
  <h2 class="intro-y text-lg font-medium mt-10">Histories</h2>
  <div class="grid grid-cols-12 gap-6 mt-5">
    <div
      class="intro-y col-span-12 flex flex-wrap xl:flex-nowrap items-center mt-2"
    >
      <div class="flex w-full sm:w-auto">
        <!-- <div class="w-48 relative text-slate-500">
          <input
            type="text"
            class="form-control w-48 box pr-10"
            placeholder="Search by name..."
          />
          <SearchIcon class="w-4 h-4 absolute my-auto inset-y-0 mr-3 right-0" />
        </div>
        <select class="w-48 xl:w-auto form-select box ml-2">
          <option>Status</option>
          <option>Active</option>
          <option>Removed</option>
        </select> -->
      </div>
      <div class="hidden xl:block mx-auto text-slate-500">
        <!-- Showing 1 to 10 of 150 entries -->
        Showing {{ startIndex+1 }} to {{ endIndex }} of {{ historiesData.length }} entries
      </div>
      <div
        class="w-full xl:w-auto flex flex-wrap xl:flex-nowrap items-center gap-y-3 mt-3 xl:mt-0"
      >
        <!-- <button class="btn btn-primary shadow-md mr-2">
          <FileTextIcon class="w-4 h-4 mr-2" /> Export to Excel
        </button>
        <button class="btn btn-primary shadow-md mr-2">
          <FileTextIcon class="w-4 h-4 mr-2" /> Export to PDF
        </button> -->
        <!-- <Dropdown>
          <DropdownToggle class="btn px-2 box">
            <span class="w-5 h-5 flex items-center justify-center">
              <PlusIcon class="w-4 h-4" />
            </span>
          </DropdownToggle>
          <DropdownMenu class="w-40">
            <DropdownContent>
              <DropdownItem>
                <ArrowLeftRightIcon class="w-4 h-4 mr-2" /> Change Status
              </DropdownItem>
              <DropdownItem>
                <BookmarkIcon class="w-4 h-4 mr-2" /> Bookmark
              </DropdownItem>
            </DropdownContent>
          </DropdownMenu>
        </Dropdown> -->
      </div>
    </div>
    <!-- BEGIN: Data List -->
    <div class="intro-y col-span-12 overflow-auto 2xl:overflow-visible">
      <table class="table table-report -mt-2">
        <thead>
          <tr>
            <!-- <th class="whitespace-nowrap">
              <input class="form-check-input" type="checkbox" />
            </th> -->
            <th class="whitespace-nowrap">Template Name</th>
            <th class="whitespace-nowrap">Template ID</th>
            <!-- <th class="whitespace-nowrap">POSTED TIME</th> -->
            <!-- <th class="whitespace-nowrap">RATING</th> -->
            <th class="text-center whitespace-nowrap">POSTED TIME</th>
            <th class="text-center whitespace-nowrap">STATUS</th>
            <th class="text-center whitespace-nowrap">DOWNLOAD ANSWERS</th>
            <th class="text-center whitespace-nowrap">ACTIONS</th>
          </tr>
        </thead>
        <!-- historiesData: {{ historiesData }} -->
        <!-- startIndex {{ startIndex}} {{ endIndex }} -->
        <tbody>
          <tr
            v-for="(item, index) in $_.slice(historiesData, startIndex, endIndex)"
            :key="index"
            class="intro-x"
          >
            <!-- history item {{ item }} -->
            <!-- <td class="w-10">
              <input class="form-check-input" type="checkbox" />
            </td> -->
            <td class="!py-4">
              <div class="flex items-center">
                <!-- <div class="w-10 h-10 image-fit zoom-in">
                  <Tippy
                    tag="img"
                    alt="Midone - HTML Admin Template"
                    class="rounded-lg border-1 border-white shadow-md"
                    :src="faker.images[0]"
                    :content="`Uploaded at ${faker.dates[0]}`"
                  />
                </div> -->
                <a href="" class="font-medium whitespace-nowrap ml-4">{{
                  item.survey_template_name
                }}</a>
              </div>
            </td>
            <td class="!py-4">
              <div class="flex items-center">
                <!-- <div class="w-10 h-10 image-fit zoom-in">
                  <Tippy
                    tag="img"
                    alt="Midone - HTML Admin Template"
                    class="rounded-lg border-1 border-white shadow-md"
                    :src="faker.images[0]"
                    :content="`Uploaded at ${faker.dates[0]}`"
                  />
                </div> -->
                <!-- <a href="" class="font-medium whitespace-nowrap ml-4">{{
                  item.survey_template_id
                }}</a> -->
                <!-- <a href="" class="font-medium whitespace-nowrap ml-4">{{ -->
                  {{ item.survey_template_id }}
                <!-- }}</a> -->
              </div>
            </td>
            <!-- <td class="whitespace-nowrap">
              <a
                class="flex items-center underline decoration-dotted"
                href="javascript:;"
                >{{ faker.users[0].name }}</a
              >
            </td> -->
            <!-- <td class="text-center">
              <div class="flex items-center">
                <div class="flex items-center">
                  <StarIcon class="text-pending fill-pending/30 w-4 h-4 mr-1" />
                  <StarIcon class="text-pending fill-pending/30 w-4 h-4 mr-1" />
                  <StarIcon class="text-pending fill-pending/30 w-4 h-4 mr-1" />
                  <StarIcon class="text-pending fill-pending/30 w-4 h-4 mr-1" />
                  <StarIcon class="text-slate-400 fill-slate/30 w-4 h-4 mr-1" />
                </div>
                <div class="text-xs text-slate-500 ml-1">(2.5+)</div>
              </div>
            </td> -->
            <td class="text-center whitespace-nowrap">
              {{ item.creation_time }}
            </td>
            <td class="w-40">
              <div
                class="flex items-center justify-center"
                :class="{
                  'text-success': item.status,
                  'text-danger': !item.status,
                }"
              >
                <CheckSquareIcon class="w-4 h-4 mr-2" />
                {{ item.status ? "Active" : "Removed" }}
              </div>
            </td>
            <td class="w-40">
              <div
                class="flex items-center justify-center" @click='download_file(item.survey_template_name, item.survey_template_id)'
              >
                <!-- Download -->
                <CheckSquareIcon class="w-4 h-4 mr-1" /> Download
              </div>
            </td>
            <td class="table-report__action w-56">
              <div class="flex justify-center items-center" @click="go_to_template_page(item.survey_template_id)">
                <a
                  class="flex items-center text-primary whitespace-nowrap"
                  href="javascript:;"
                >
                  <CheckSquareIcon class="w-4 h-4 mr-1" /> View Details
                </a>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- END: Data List -->
    <!-- BEGIN: Pagination -->
    <div
      class="intro-y col-span-12 flex flex-wrap sm:flex-row sm:flex-nowrap items-center"
    >
      <nav class="w-full sm:w-auto sm:mr-auto">
        <ul class="pagination">

          <li class="page-item" @click="first_page">
            <a class="page-link" href="#">
              <ChevronsLeftIcon class="w-4 h-4" />
            </a>
          </li>

          <li class="page-item" @click="prev_page">
            <a class="page-link" href="#">
              <ChevronLeftIcon class="w-4 h-4" />
            </a>
          </li>

          <li :class="index+1 === pageNumber ? 'page-item active' : 'page-item'"
              v-for="(item, index) in pageNumberArray.pageNumberArray"
              :key="index"
              @click="to_click_page(index+1)"
              >
            <a class="page-link" href="#">{{ index+1 }}</a>
          </li>

          <li class="page-item" @click="next_page">
            <a class="page-link" href="#">
              <ChevronRightIcon class="w-4 h-4" />
            </a>
          </li>

          <li class="page-item" @click="last_page">
            <a class="page-link" href="#">
              <ChevronsRightIcon class="w-4 h-4" />
            </a>
          </li>

        </ul>
      </nav>
      <select class="w-20 form-select box mt-3 sm:mt-0" @change="change_itemPerPage()" v-model="itemPerPage">
        <!-- <option value=10>10</option>
        <option value=25>25</option>
        <option value=35>35</option>
        <option value=50>50</option> -->

        <option value=5>5</option>
        <option value=10>10</option>
        <option value=20>20</option>
        <!-- <option value=5>5</option> -->
      </select>
      <!-- itemPerPage {{ itemPerPage }} -->
    </div>
    <!-- END: Pagination -->
  </div>
  <!-- BEGIN: Request Success Content -->
  <div
    id="success-notification-content"
    class="toastify-content hidden flex"
  >
    <CheckCircleIcon class="text-success" />
    <div class="ml-4 mr-4">
      <div class="font-medium">Send request successfully!</div>
      <div class="text-slate-500 mt-1">
        Please wait for the response
      </div>
    </div>
  </div>
  <!-- END: Request Success Content -->
  <!-- BEGIN: Request Error Content -->
  <div
    id="request-error-content"
    class="toastify-content hidden flex"
  >
    <CheckCircleIcon class="text-danger" />
    <div class="ml-4 mr-4">
      <div class="font-medium">Request error!</div>
      <div class="text-slate-500 mt-1">
        <!-- {{ request_error }}
        error_name: {{ request_error['error_name'] }}
        error_msg: {{ request_error.error_msg }}
        error_status: {{ request_error.error_status }} -->
        <!-- <div> -->
        The error may caused by the following reasons:
        <br/>
          1. Still no voter answer this survey template
          <br />
          2. The survey template has beed deleted
        <!-- </div> -->
      </div>
    </div>
  </div>
  <!-- END: Request Error Content -->
  <!-- BEGIN: Delete Confirmation Modal -->
  <Modal
    :show="deleteConfirmationModal"
    @hidden="deleteConfirmationModal = false"
  >
    <ModalBody class="p-0">
      <div class="p-5 text-center">
        <XCircleIcon class="w-16 h-16 text-danger mx-auto mt-3" />
        <div class="text-3xl mt-5">Are you sure?</div>
        <div class="text-slate-500 mt-2">
          Do you really want to delete these records? <br />This process cannot
          be undone.
        </div>
      </div>
      <div class="px-5 pb-8 text-center">
        <button
          type="button"
          @click="deleteConfirmationModal = false"
          class="btn btn-outline-secondary w-24 mr-1"
        >
          Cancel
        </button>
        <button type="button" class="btn btn-danger w-24">Delete</button>
      </div>
    </ModalBody>
  </Modal>
  <!-- END: Delete Confirmation Modal -->
</template>

<script setup>
import { ref, reactive, onBeforeMount, onMounted } from "vue";
import { axios } from "@/utils/axios";
import Toastify from "toastify-js";
import { process_axios_response, process_axios_error, get_api_url } from "@/utils/axios_utils"
import { linkTo } from "./index"
import { useRoute, useRouter } from "vue-router";

const router = useRouter();
const deleteConfirmationModal = ref(false);

const historiesData = reactive([]);
const startIndex = ref(0);
const endIndex = ref(0);
const pageNumber = ref(1);
const pageNumberArray = reactive({
  'pageNumberArray': []
});
const itemPerPage = ref(5)

const go_to_template_page = (surveyTemplateID) => {
  // let surveyTemplateID
  let params = {
    'surveyTemplateID': surveyTemplateID
  }
  linkTo('side-menu-template-form', router, params)

}


const download_file = async (survey_template_name, survey_template_id) => {
  try {

    // static categorical: 62e220016648301fab9ab211
  // static categorical_multiple: 62e2e89b6be732eba69f0b6a
  // static continuous: 62e220226648301fab9ab213
  // static categorical + continuous: 62e2204c6648301fab9ab215
  // uniform categorical: 62e220af6648301fab9ab217
  // uniform continuous: 62e220d76648301fab9ab219
  // uniform categorical + continuous: 62e2210d6648301fab9ab21b
    // survey_template_id = '62e220016648301fab9ab211';
    let response = await axios({
      method: 'post',
      url: get_api_url('get_voter_answers_of_template'), 
      data: {
        'survey_template_id': survey_template_id
      },
      // responseType: 'blob'
    });

    // let data = [
    //   {
    //     'survey_template_id': '1',
    //     'creation_time': '1 days ago',
    //     'status': true,
    //     'shishi': { 
    //       'ceshi': 5
    //     },
    //   },
    //   {
    //     'survey_template_id': '2',
    //     'creation_time': '1 days ago',
    //     'status': true,
    //   },
    // ];
    // let a = JSON.stringify({
    //     'survey_template_id': '1',
    //     'creation_time': '1 days ago',
    //     'status': true,
    //   })
    // let b = JSON.stringify({
    //     'survey_template_id': '1',
    //     'creation_time': '1 days ago',
    //     'status': true,
    //   })
    // let c = [a, b]

    // let c = ['survey_template_id', 'creation_time', 'status',
    //     '\n',
    //     '1',
    //     '1 day ago',
    //     {2: 3},
    //     '\n',
    //     '1',
    //     '1 day ago',
    //     {2: 3},
        
    //     ]
    // data = data.join('\n');
    // let data = ['adasdasdfsadfsadfsa', 'asdas\n']
    // console.log(c)
    // [JSON.stringify(data)]
    // [JSON.stringify(data)]
    console.log('voter_answersresponse', response)
    let data = process_axios_response(response);
    console.log('voter_answersdatae', data)
    let voter_answers = data.voter_answers
    console.log('voter_answers+data', voter_answers)
    const blob = new Blob([JSON.stringify(voter_answers)], { type: "text/csv", endings: "native"} );//处理文档流
    
    console.log('blob', blob, typeof blob)
    const fileName = `${survey_template_name}.csv`;
    const down = document.createElement('a');
    down.download = fileName;
    down.style.display = 'none';//隐藏,没必要展示出来
    down.href = URL.createObjectURL(blob);
    document.body.appendChild(down);
    down.click();
    URL.revokeObjectURL(down.href); // 释放URL 对象
    document.body.removeChild(down)
    
    // console.log(`send_form response: ${processed_response}`)
    /*
    History data form:
    {
      survey_template_name: str
      survey_template_id: str
        unique template id
      creation_time: str
      status: true or false
        true: still not expire
        false: expire
    }
    */
    Toastify({
      node: dom("#success-notification-content")
        .clone()
        .removeClass("hidden")[0],
      duration: 10000,
      newWindow: true,
      close: true,
      gravity: "top",
      position: "right",
      stopOnFocus: true,
    }).showToast();
  } catch (err) {
    console.log(`send_form err 0.5: ${err}`)
    let processed_err = process_axios_error(err)
    console.log(`send_form err: ${processed_err}`)

    Toastify({
      node: dom("#request-error-content")
        .clone()
        .removeClass("hidden")[0],
      duration: 10000,
      newWindow: true,
      close: true,
      gravity: "top",
      position: "right",
      stopOnFocus: true,
    }).showToast();
  }
}
const change_itemPerPage = () => {
  console.log('change_itemPerPage', itemPerPage.value)
  let temp = []
  for (let i = 0; i < page_count(); i++) {
    temp.push([])
  }
  pageNumberArray.pageNumberArray = temp
  pageNumber.value = 1
  let res = update_index(pageNumber.value, itemPerPage.value, historiesData.length)
  startIndex.value = res.newStartIndex;
  endIndex.value = res.newEndIndex
}


const update_index = (pageNumber, itemPerPage, historiesDataLength) => {
  let newStartIndex = (pageNumber - 1) * itemPerPage
  let newEndIndex = Math.min(itemPerPage * pageNumber, historiesDataLength)

  return {
    newStartIndex,
    newEndIndex
  }
}

const prev_page = () => {
  // do nothing if currently locate at first page
  console.log('prev_page', pageNumber.value)
  if (pageNumber.value === 1) {
    return
  }
  // decrease pageNumber
  pageNumber.value--;
  let res = update_index(pageNumber.value, itemPerPage.value, historiesData.length)
  startIndex.value = res.newStartIndex;
  endIndex.value = res.newEndIndex
}

const next_page = () => {
  // do nothing if currently locate at last page
  if (pageNumber.value === page_count()) {
    return
  }
  // increase pageNumber
  pageNumber.value++;
  let res = update_index(pageNumber.value, itemPerPage.value, historiesData.length)
  startIndex.value = res.newStartIndex;
  endIndex.value = res.newEndIndex
}

const first_page = () => {
  pageNumber.value = 1;
  let res = update_index(pageNumber.value, itemPerPage.value, historiesData.length)
  startIndex.value = res.newStartIndex;
  endIndex.value = res.newEndIndex
}

const last_page = () => {
  pageNumber.value = page_count();
  let res = update_index(pageNumber.value, itemPerPage.value, historiesData.length)
  startIndex.value = res.newStartIndex;
  endIndex.value = res.newEndIndex
}

const to_click_page = (clickedPageNumber) => {
  pageNumber.value = clickedPageNumber
  let res = update_index(pageNumber.value, itemPerPage.value, historiesData.length)
  console.log('to_click_page', res, pageNumber.value)
  startIndex.value = res.newStartIndex;
  endIndex.value = res.newEndIndex
}

const page_count = () => {
  /*
    Total page Count decided by the length of historiesData and the
    itemPerPage
  */
  let total_histories_num = historiesData.length;
  console.log('total_histories_num', total_histories_num, historiesData.length)
  let pageCount = Math.ceil(total_histories_num / itemPerPage.value)
  console.log('page_count', pageCount)
  return pageCount;
}

// const get_histories = async () => {
  
// }

onMounted(() => {
  console.log('history-mounted')

})

onBeforeMount(async () => {
  console.log('history-before-mounted')
  /*
    1. get history items from back-end
    2. update the startIndex and endIndex
  */
  try {
    let response = await axios.post(get_api_url('get_user_histories'));
    console.log('response', response)
    console.log('asda', response.data)
    let processed_response = process_axios_response(response);
    console.log(`processed_response response:`, processed_response)
    let histories = processed_response.histories
    console.log('send_form response:', histories)
    /*
    History data form:
    {
      survey_template_name: str
      survey_template_id: str
        unique template id
      creation_time: str
      status: true or false
        true: still not expire
        false: expire
    }
    */
    historiesData.push(...histories)
    console.log('fuzhi', historiesData, historiesData.length, historiesData.value)
    let pageCount = page_count()
    // item num is less than the itemPerPage
    if (pageCount === 1) {
      startIndex.value = 0
      endIndex.value = historiesData.length
    } else if (pageCount > 1) {
      // item num is greater than the itemPerPage
      startIndex.value = 0
      endIndex.value = itemPerPage.value
    }
    let temp = []
    for (let i = 0; i < pageCount; i++) {
      temp.push([])
    }
    pageNumberArray.pageNumberArray = temp
    // Toastify({
    //   node: dom("#success-notification-content")
    //     .clone()
    //     .removeClass("hidden")[0],
    //   duration: 10000,
    //   newWindow: true,
    //   close: true,
    //   gravity: "top",
    //   position: "right",
    //   stopOnFocus: true,
    // }).showToast();
  } catch (err) {
    console.log(`send_form err 0.5: ${err}`)
    let processed_err = process_axios_error(err)
    console.log(`send_form err: ${processed_err}`)

    Toastify({
      node: dom("#request-error-content")
        .clone()
        .removeClass("hidden")[0],
      duration: 10000,
      newWindow: true,
      close: true,
      gravity: "top",
      position: "right",
      stopOnFocus: true,
    }).showToast();
  }
  console.log('after_history')
  // let Data = [
  //   {
  //     'survey_template_name': 'as',
  //     'survey_template_id': '1',
  //     'creation_time': '1 days ago',
  //     'status': true,
  //   },
  //   {
  //     'survey_template_name': 'as',
  //     'survey_template_id': '2',
  //     'creation_time': '2 days ago',
  //     'status': false,
  //   },
  //   {
  //     'survey_template_name': 'as',
  //     'survey_template_id': '3',
  //     'creation_time': '2 days ago',
  //     'status': false,
  //   },
  //   {
  //     'survey_template_name': 'as',
  //     'survey_template_id': '4',
  //     'creation_time': '2 days ago',
  //     'status': false,
  //   },
  //   {
  //     'survey_template_name': 'as',
  //     'survey_template_id': '5',
  //     'creation_time': '2 days ago',
  //     'status': false,
  //   },
  //   {
  //     'survey_template_name': 'as',
  //     'survey_template_id': '6',
  //     'creation_time': '2 days ago',
  //     'status': false,
  //   },
  //   {
  //     'survey_template_name': 'as',
  //     'survey_template_id': '7',
  //     'creation_time': '2 days ago',
  //     'status': false,
  //   },
  //   {
  //     'survey_template_name': 'as',
  //     'survey_template_id': '8',
  //     'creation_time': '2 days ago',
  //     'status': false,
  //   },
  //   {
  //     'survey_template_name': 'as',
  //     'survey_template_id': '9',
  //     'creation_time': '2 days ago',
  //     'status': false,
  //   },
  //   {
  //     'survey_template_name': 'as',
  //     'survey_template_id': '10',
  //     'creation_time': '2 days ago',
  //     'status': false,
  //   },
  //   {
  //     'survey_template_name': 'as',
  //     'survey_template_id': '11',
  //     'creation_time': '2 days ago',
  //     'status': false,
  //   },
  //   {
  //     'survey_template_name': 'as',
  //     'survey_template_id': '12',
  //     'creation_time': '2 days ago',
  //     'status': false,
  //   }

  // ]
  // historiesData.push(...Data)
  
})
// let Data = [
//   {
//     'survey_template_id': '123',
//     'creation_time': '1 days ago',
//     'status': true,
//   },
//   {
//     'survey_template_id': '456',
//     'creation_time': '2 days ago',
//     'status': false,
//   }
// ]

// testData.push(...Data)
</script>
