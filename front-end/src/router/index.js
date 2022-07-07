import { createRouter, createWebHistory } from "vue-router";
import SideMenu from "../layouts/side-menu/Main.vue";
import SimpleMenu from "../layouts/simple-menu/Main.vue";
import TopMenu from "../layouts/top-menu/Main.vue";
import DashboardOverview1 from "../views/dashboard-overview-1/Main.vue";
import DashboardOverview2 from "../views/dashboard-overview-2/Main.vue";
import DashboardOverview3 from "../views/dashboard-overview-3/Main.vue";
import DashboardOverview4 from "../views/dashboard-overview-4/Main.vue";
import Categories from "../views/categories/Main.vue";
import AddProduct from "../views/add-product/Main.vue";
import ProductList from "../views/product-list/Main.vue";
import ProductGrid from "../views/product-grid/Main.vue";
import TransactionList from "../views/transaction-list/Main.vue";
import TransactionDetail from "../views/transaction-detail/Main.vue";
import SellerList from "../views/seller-list/Main.vue";
import SellerDetail from "../views/seller-detail/Main.vue";
import Reviews from "../views/reviews/Main.vue";
import Inbox from "../views/inbox/Main.vue";
import FileManager from "../views/file-manager/Main.vue";
import PointOfSale from "../views/point-of-sale/Main.vue";
import Chat from "../views/chat/Main.vue";
import Post from "../views/post/Main.vue";
import Calendar from "../views/calendar/Main.vue";
import CrudDataList from "../views/crud-data-list/Main.vue";
import CrudForm from "../views/crud-form/Main.vue";
import UsersLayout1 from "../views/users-layout-1/Main.vue";
import UsersLayout2 from "../views/users-layout-2/Main.vue";
import UsersLayout3 from "../views/users-layout-3/Main.vue";
import ProfileOverview1 from "../views/profile-overview-1/Main.vue";
import ProfileOverview2 from "../views/profile-overview-2/Main.vue";
import ProfileOverview3 from "../views/profile-overview-3/Main.vue";
import WizardLayout1 from "../views/wizard-layout-1/Main.vue";
import WizardLayout2 from "../views/wizard-layout-2/Main.vue";
import WizardLayout3 from "../views/wizard-layout-3/Main.vue";
import BlogLayout1 from "../views/blog-layout-1/Main.vue";
import BlogLayout2 from "../views/blog-layout-2/Main.vue";
import BlogLayout3 from "../views/blog-layout-3/Main.vue";
import PricingLayout1 from "../views/pricing-layout-1/Main.vue";
import PricingLayout2 from "../views/pricing-layout-2/Main.vue";
import InvoiceLayout1 from "../views/invoice-layout-1/Main.vue";
import InvoiceLayout2 from "../views/invoice-layout-2/Main.vue";
import FaqLayout1 from "../views/faq-layout-1/Main.vue";
import FaqLayout2 from "../views/faq-layout-2/Main.vue";
import FaqLayout3 from "../views/faq-layout-3/Main.vue";
import Login from "../views/login/Main.vue";
import Register from "../views/register/Main.vue";
import ErrorPage from "../views/error-page/Main.vue";
import UpdateProfile from "../views/update-profile/Main.vue";
import ChangePassword from "../views/change-password/Main.vue";
import RegularTable from "../views/regular-table/Main.vue";
import Tabulator from "../views/tabulator/Main.vue";
import Modal from "../views/modal/Main.vue";
import SlideOver from "../views/slide-over/Main.vue";
import Notification from "../views/notification/Main.vue";
import Tab from "../views/tab/Main.vue";
import Accordion from "../views/accordion/Main.vue";
import Button from "../views/button/Main.vue";
import Alert from "../views/alert/Main.vue";
import ProgressBar from "../views/progress-bar/Main.vue";
import Tooltip from "../views/tooltip/Main.vue";
import Dropdown from "../views/dropdown/Main.vue";
import Typography from "../views/typography/Main.vue";
import Icon from "../views/icon/Main.vue";
import LoadingIcon from "../views/loading-icon/Main.vue";
import RegularForm from "../views/regular-form/Main.vue";
import Datepicker from "../views/datepicker/Main.vue";
import TomSelect from "../views/tom-select/Main.vue";
import FileUpload from "../views/file-upload/Main.vue";
import WysiwygEditor from "../views/wysiwg-editor/Main.vue";
import Validation from "../views/validation/Main.vue";
import Chart from "../views/chart/Main.vue";
import Slider from "../views/slider/Main.vue";
import ImageZoom from "../views/image-zoom/Main.vue";

const routes = [
  {
    path: "/",
    component: SideMenu,
    children: [
      {
        path: "/",
        name: "side-menu-dashboard-overview-1",
        component: DashboardOverview1,
      },
      {
        path: "dashboard-overview-2",
        name: "side-menu-dashboard-overview-2",
        component: DashboardOverview2,
      },
      {
        path: "dashboard-overview-3",
        name: "side-menu-dashboard-overview-3",
        component: DashboardOverview3,
      },
      {
        path: "dashboard-overview-4",
        name: "side-menu-dashboard-overview-4",
        component: DashboardOverview4,
      },
      {
        path: "categories",
        name: "side-menu-categories",
        component: Categories,
      },
      {
        path: "add-product",
        name: "side-menu-add-product",
        component: AddProduct,
      },
      {
        path: "product-list",
        name: "side-menu-product-list",
        component: ProductList,
      },
      {
        path: "product-grid",
        name: "side-menu-product-grid",
        component: ProductGrid,
      },
      {
        path: "transaction-list",
        name: "side-menu-transaction-list",
        component: TransactionList,
      },
      {
        path: "transaction-detail",
        name: "side-menu-transaction-detail",
        component: TransactionDetail,
      },
      {
        path: "seller-list",
        name: "side-menu-seller-list",
        component: SellerList,
      },
      {
        path: "seller-detail",
        name: "side-menu-seller-detail",
        component: SellerDetail,
      },
      {
        path: "reviews",
        name: "side-menu-reviews",
        component: Reviews,
      },
      {
        path: "inbox",
        name: "side-menu-inbox",
        component: Inbox,
      },
      {
        path: "file-manager",
        name: "side-menu-file-manager",
        component: FileManager,
      },
      {
        path: "point-of-sale",
        name: "side-menu-point-of-sale",
        component: PointOfSale,
      },
      {
        path: "chat",
        name: "side-menu-chat",
        component: Chat,
      },
      {
        path: "post",
        name: "side-menu-post",
        component: Post,
      },
      {
        path: "calendar",
        name: "side-menu-calendar",
        component: Calendar,
      },
      {
        path: "crud-data-list",
        name: "side-menu-crud-data-list",
        component: CrudDataList,
      },
      {
        path: "crud-form",
        name: "side-menu-crud-form",
        component: CrudForm,
      },
      {
        path: "users-layout-1",
        name: "side-menu-users-layout-1",
        component: UsersLayout1,
      },
      {
        path: "users-layout-2",
        name: "side-menu-users-layout-2",
        component: UsersLayout2,
      },
      {
        path: "users-layout-3",
        name: "side-menu-users-layout-3",
        component: UsersLayout3,
      },
      {
        path: "profile-overview-1",
        name: "side-menu-profile-overview-1",
        component: ProfileOverview1,
      },
      {
        path: "profile-overview-2",
        name: "side-menu-profile-overview-2",
        component: ProfileOverview2,
      },
      {
        path: "profile-overview-3",
        name: "side-menu-profile-overview-3",
        component: ProfileOverview3,
      },
      {
        path: "wizard-layout-1",
        name: "side-menu-wizard-layout-1",
        component: WizardLayout1,
      },
      {
        path: "wizard-layout-2",
        name: "side-menu-wizard-layout-2",
        component: WizardLayout2,
      },
      {
        path: "wizard-layout-3",
        name: "side-menu-wizard-layout-3",
        component: WizardLayout3,
      },
      {
        path: "blog-layout-1",
        name: "side-menu-blog-layout-1",
        component: BlogLayout1,
      },
      {
        path: "blog-layout-2",
        name: "side-menu-blog-layout-2",
        component: BlogLayout2,
      },
      {
        path: "blog-layout-3",
        name: "side-menu-blog-layout-3",
        component: BlogLayout3,
      },
      {
        path: "pricing-layout-1",
        name: "side-menu-pricing-layout-1",
        component: PricingLayout1,
      },
      {
        path: "pricing-layout-2",
        name: "side-menu-pricing-layout-2",
        component: PricingLayout2,
      },
      {
        path: "invoice-layout-1",
        name: "side-menu-invoice-layout-1",
        component: InvoiceLayout1,
      },
      {
        path: "invoice-layout-2",
        name: "side-menu-invoice-layout-2",
        component: InvoiceLayout2,
      },
      {
        path: "faq-layout-1",
        name: "side-menu-faq-layout-1",
        component: FaqLayout1,
      },
      {
        path: "faq-layout-2",
        name: "side-menu-faq-layout-2",
        component: FaqLayout2,
      },
      {
        path: "faq-layout-3",
        name: "side-menu-faq-layout-3",
        component: FaqLayout3,
      },
      {
        path: "update-profile",
        name: "side-menu-update-profile",
        component: UpdateProfile,
      },
      {
        path: "change-password",
        name: "side-menu-change-password",
        component: ChangePassword,
      },
      {
        path: "regular-table",
        name: "side-menu-regular-table",
        component: RegularTable,
      },
      {
        path: "tabulator",
        name: "side-menu-tabulator",
        component: Tabulator,
      },
      {
        path: "modal",
        name: "side-menu-modal",
        component: Modal,
      },
      {
        path: "slide-over",
        name: "side-menu-slide-over",
        component: SlideOver,
      },
      {
        path: "notification",
        name: "side-menu-notification",
        component: Notification,
      },
      {
        path: "tab",
        name: "side-menu-tab",
        component: Tab,
      },
      {
        path: "accordion",
        name: "side-menu-accordion",
        component: Accordion,
      },
      {
        path: "button",
        name: "side-menu-button",
        component: Button,
      },
      {
        path: "alert",
        name: "side-menu-alert",
        component: Alert,
      },
      {
        path: "progress-bar",
        name: "side-menu-progress-bar",
        component: ProgressBar,
      },
      {
        path: "tooltip",
        name: "side-menu-tooltip",
        component: Tooltip,
      },
      {
        path: "dropdown",
        name: "side-menu-dropdown",
        component: Dropdown,
      },
      {
        path: "typography",
        name: "side-menu-typography",
        component: Typography,
      },
      {
        path: "icon",
        name: "side-menu-icon",
        component: Icon,
      },
      {
        path: "loading-icon",
        name: "side-menu-loading-icon",
        component: LoadingIcon,
      },
      {
        path: "regular-form",
        name: "side-menu-regular-form",
        component: RegularForm,
      },
      {
        path: "datepicker",
        name: "side-menu-datepicker",
        component: Datepicker,
      },
      {
        path: "tom-select",
        name: "side-menu-tom-select",
        component: TomSelect,
      },
      {
        path: "file-upload",
        name: "side-menu-file-upload",
        component: FileUpload,
      },
      {
        path: "wysiwyg-editor",
        name: "side-menu-wysiwyg-editor",
        component: WysiwygEditor,
      },
      {
        path: "validation",
        name: "side-menu-validation",
        component: Validation,
      },
      {
        path: "chart",
        name: "side-menu-chart",
        component: Chart,
      },
      {
        path: "slider",
        name: "side-menu-slider",
        component: Slider,
      },
      {
        path: "image-zoom",
        name: "side-menu-image-zoom",
        component: ImageZoom,
      },
    ],
  },
  {
    path: "/simple-menu",
    component: SimpleMenu,
    children: [
      {
        path: "dashboard-overview-1",
        name: "simple-menu-dashboard-overview-1",
        component: DashboardOverview1,
      },
      {
        path: "dashboard-overview-2",
        name: "simple-menu-dashboard-overview-2",
        component: DashboardOverview2,
      },
      {
        path: "dashboard-overview-3",
        name: "simple-menu-dashboard-overview-3",
        component: DashboardOverview3,
      },
      {
        path: "dashboard-overview-4",
        name: "simple-menu-dashboard-overview-4",
        component: DashboardOverview4,
      },
      {
        path: "categories",
        name: "simple-menu-categories",
        component: Categories,
      },
      {
        path: "add-product",
        name: "simple-menu-add-product",
        component: AddProduct,
      },
      {
        path: "product-list",
        name: "simple-menu-product-list",
        component: ProductList,
      },
      {
        path: "product-grid",
        name: "simple-menu-product-grid",
        component: ProductGrid,
      },
      {
        path: "transaction-list",
        name: "simple-menu-transaction-list",
        component: TransactionList,
      },
      {
        path: "transaction-detail",
        name: "simple-menu-transaction-detail",
        component: TransactionDetail,
      },
      {
        path: "seller-list",
        name: "simple-menu-seller-list",
        component: SellerList,
      },
      {
        path: "seller-detail",
        name: "simple-menu-seller-detail",
        component: SellerDetail,
      },
      {
        path: "reviews",
        name: "simple-menu-reviews",
        component: Reviews,
      },
      {
        path: "inbox",
        name: "simple-menu-inbox",
        component: Inbox,
      },
      {
        path: "file-manager",
        name: "simple-menu-file-manager",
        component: FileManager,
      },
      {
        path: "point-of-sale",
        name: "simple-menu-point-of-sale",
        component: PointOfSale,
      },
      {
        path: "chat",
        name: "simple-menu-chat",
        component: Chat,
      },
      {
        path: "post",
        name: "simple-menu-post",
        component: Post,
      },
      {
        path: "calendar",
        name: "simple-menu-calendar",
        component: Calendar,
      },
      {
        path: "crud-data-list",
        name: "simple-menu-crud-data-list",
        component: CrudDataList,
      },
      {
        path: "crud-form",
        name: "simple-menu-crud-form",
        component: CrudForm,
      },
      {
        path: "users-layout-1",
        name: "simple-menu-users-layout-1",
        component: UsersLayout1,
      },
      {
        path: "users-layout-2",
        name: "simple-menu-users-layout-2",
        component: UsersLayout2,
      },
      {
        path: "users-layout-3",
        name: "simple-menu-users-layout-3",
        component: UsersLayout3,
      },
      {
        path: "profile-overview-1",
        name: "simple-menu-profile-overview-1",
        component: ProfileOverview1,
      },
      {
        path: "profile-overview-2",
        name: "simple-menu-profile-overview-2",
        component: ProfileOverview2,
      },
      {
        path: "profile-overview-3",
        name: "simple-menu-profile-overview-3",
        component: ProfileOverview3,
      },
      {
        path: "wizard-layout-1",
        name: "simple-menu-wizard-layout-1",
        component: WizardLayout1,
      },
      {
        path: "wizard-layout-2",
        name: "simple-menu-wizard-layout-2",
        component: WizardLayout2,
      },
      {
        path: "wizard-layout-3",
        name: "simple-menu-wizard-layout-3",
        component: WizardLayout3,
      },
      {
        path: "blog-layout-1",
        name: "simple-menu-blog-layout-1",
        component: BlogLayout1,
      },
      {
        path: "blog-layout-2",
        name: "simple-menu-blog-layout-2",
        component: BlogLayout2,
      },
      {
        path: "blog-layout-3",
        name: "simple-menu-blog-layout-3",
        component: BlogLayout3,
      },
      {
        path: "pricing-layout-1",
        name: "simple-menu-pricing-layout-1",
        component: PricingLayout1,
      },
      {
        path: "pricing-layout-2",
        name: "simple-menu-pricing-layout-2",
        component: PricingLayout2,
      },
      {
        path: "invoice-layout-1",
        name: "simple-menu-invoice-layout-1",
        component: InvoiceLayout1,
      },
      {
        path: "invoice-layout-2",
        name: "simple-menu-invoice-layout-2",
        component: InvoiceLayout2,
      },
      {
        path: "faq-layout-1",
        name: "simple-menu-faq-layout-1",
        component: FaqLayout1,
      },
      {
        path: "faq-layout-2",
        name: "simple-menu-faq-layout-2",
        component: FaqLayout2,
      },
      {
        path: "faq-layout-3",
        name: "simple-menu-faq-layout-3",
        component: FaqLayout3,
      },
      {
        path: "update-profile",
        name: "simple-menu-update-profile",
        component: UpdateProfile,
      },
      {
        path: "change-password",
        name: "simple-menu-change-password",
        component: ChangePassword,
      },
      {
        path: "regular-table",
        name: "simple-menu-regular-table",
        component: RegularTable,
      },
      {
        path: "tabulator",
        name: "simple-menu-tabulator",
        component: Tabulator,
      },
      {
        path: "modal",
        name: "simple-menu-modal",
        component: Modal,
      },
      {
        path: "slide-over",
        name: "simple-menu-slide-over",
        component: SlideOver,
      },
      {
        path: "notification",
        name: "simple-menu-notification",
        component: Notification,
      },
      {
        path: "tab",
        name: "simple-menu-tab",
        component: Tab,
      },
      {
        path: "accordion",
        name: "simple-menu-accordion",
        component: Accordion,
      },
      {
        path: "button",
        name: "simple-menu-button",
        component: Button,
      },
      {
        path: "alert",
        name: "simple-menu-alert",
        component: Alert,
      },
      {
        path: "progress-bar",
        name: "simple-menu-progress-bar",
        component: ProgressBar,
      },
      {
        path: "tooltip",
        name: "simple-menu-tooltip",
        component: Tooltip,
      },
      {
        path: "dropdown",
        name: "simple-menu-dropdown",
        component: Dropdown,
      },
      {
        path: "typography",
        name: "simple-menu-typography",
        component: Typography,
      },
      {
        path: "icon",
        name: "simple-menu-icon",
        component: Icon,
      },
      {
        path: "loading-icon",
        name: "simple-menu-loading-icon",
        component: LoadingIcon,
      },
      {
        path: "regular-form",
        name: "simple-menu-regular-form",
        component: RegularForm,
      },
      {
        path: "datepicker",
        name: "simple-menu-datepicker",
        component: Datepicker,
      },
      {
        path: "tom-select",
        name: "simple-menu-tom-select",
        component: TomSelect,
      },
      {
        path: "file-upload",
        name: "simple-menu-file-upload",
        component: FileUpload,
      },
      {
        path: "wysiwyg-editor",
        name: "simple-menu-wysiwyg-editor",
        component: WysiwygEditor,
      },
      {
        path: "validation",
        name: "simple-menu-validation",
        component: Validation,
      },
      {
        path: "chart",
        name: "simple-menu-chart",
        component: Chart,
      },
      {
        path: "slider",
        name: "simple-menu-slider",
        component: Slider,
      },
      {
        path: "image-zoom",
        name: "simple-menu-image-zoom",
        component: ImageZoom,
      },
    ],
  },
  {
    path: "/top-menu",
    component: TopMenu,
    children: [
      {
        path: "dashboard-overview-1",
        name: "top-menu-dashboard-overview-1",
        component: DashboardOverview1,
      },
      {
        path: "dashboard-overview-2",
        name: "top-menu-dashboard-overview-2",
        component: DashboardOverview2,
      },
      {
        path: "dashboard-overview-3",
        name: "top-menu-dashboard-overview-3",
        component: DashboardOverview3,
      },
      {
        path: "dashboard-overview-4",
        name: "top-menu-dashboard-overview-4",
        component: DashboardOverview4,
      },
      {
        path: "categories",
        name: "top-menu-categories",
        component: Categories,
      },
      {
        path: "add-product",
        name: "top-menu-add-product",
        component: AddProduct,
      },
      {
        path: "product-list",
        name: "top-menu-product-list",
        component: ProductList,
      },
      {
        path: "product-grid",
        name: "top-menu-product-grid",
        component: ProductGrid,
      },
      {
        path: "transaction-list",
        name: "top-menu-transaction-list",
        component: TransactionList,
      },
      {
        path: "transaction-detail",
        name: "top-menu-transaction-detail",
        component: TransactionDetail,
      },
      {
        path: "seller-list",
        name: "top-menu-seller-list",
        component: SellerList,
      },
      {
        path: "seller-detail",
        name: "top-menu-seller-detail",
        component: SellerDetail,
      },
      {
        path: "reviews",
        name: "top-menu-reviews",
        component: Reviews,
      },
      {
        path: "inbox",
        name: "top-menu-inbox",
        component: Inbox,
      },
      {
        path: "file-manager",
        name: "top-menu-file-manager",
        component: FileManager,
      },
      {
        path: "point-of-sale",
        name: "top-menu-point-of-sale",
        component: PointOfSale,
      },
      {
        path: "chat",
        name: "top-menu-chat",
        component: Chat,
      },
      {
        path: "post",
        name: "top-menu-post",
        component: Post,
      },
      {
        path: "calendar",
        name: "top-menu-calendar",
        component: Calendar,
      },
      {
        path: "crud-data-list",
        name: "top-menu-crud-data-list",
        component: CrudDataList,
      },
      {
        path: "crud-form",
        name: "top-menu-crud-form",
        component: CrudForm,
      },
      {
        path: "users-layout-1",
        name: "top-menu-users-layout-1",
        component: UsersLayout1,
      },
      {
        path: "users-layout-2",
        name: "top-menu-users-layout-2",
        component: UsersLayout2,
      },
      {
        path: "users-layout-3",
        name: "top-menu-users-layout-3",
        component: UsersLayout3,
      },
      {
        path: "profile-overview-1",
        name: "top-menu-profile-overview-1",
        component: ProfileOverview1,
      },
      {
        path: "profile-overview-2",
        name: "top-menu-profile-overview-2",
        component: ProfileOverview2,
      },
      {
        path: "profile-overview-3",
        name: "top-menu-profile-overview-3",
        component: ProfileOverview3,
      },
      {
        path: "wizard-layout-1",
        name: "top-menu-wizard-layout-1",
        component: WizardLayout1,
      },
      {
        path: "wizard-layout-2",
        name: "top-menu-wizard-layout-2",
        component: WizardLayout2,
      },
      {
        path: "wizard-layout-3",
        name: "top-menu-wizard-layout-3",
        component: WizardLayout3,
      },
      {
        path: "blog-layout-1",
        name: "top-menu-blog-layout-1",
        component: BlogLayout1,
      },
      {
        path: "blog-layout-2",
        name: "top-menu-blog-layout-2",
        component: BlogLayout2,
      },
      {
        path: "blog-layout-3",
        name: "top-menu-blog-layout-3",
        component: BlogLayout3,
      },
      {
        path: "pricing-layout-1",
        name: "top-menu-pricing-layout-1",
        component: PricingLayout1,
      },
      {
        path: "pricing-layout-2",
        name: "top-menu-pricing-layout-2",
        component: PricingLayout2,
      },
      {
        path: "invoice-layout-1",
        name: "top-menu-invoice-layout-1",
        component: InvoiceLayout1,
      },
      {
        path: "invoice-layout-2",
        name: "top-menu-invoice-layout-2",
        component: InvoiceLayout2,
      },
      {
        path: "faq-layout-1",
        name: "top-menu-faq-layout-1",
        component: FaqLayout1,
      },
      {
        path: "faq-layout-2",
        name: "top-menu-faq-layout-2",
        component: FaqLayout2,
      },
      {
        path: "faq-layout-3",
        name: "top-menu-faq-layout-3",
        component: FaqLayout3,
      },
      {
        path: "update-profile",
        name: "top-menu-update-profile",
        component: UpdateProfile,
      },
      {
        path: "change-password",
        name: "top-menu-change-password",
        component: ChangePassword,
      },
      {
        path: "regular-table",
        name: "top-menu-regular-table",
        component: RegularTable,
      },
      {
        path: "tabulator",
        name: "top-menu-tabulator",
        component: Tabulator,
      },
      {
        path: "modal",
        name: "top-menu-modal",
        component: Modal,
      },
      {
        path: "slide-over",
        name: "top-menu-slide-over",
        component: SlideOver,
      },
      {
        path: "notification",
        name: "top-menu-notification",
        component: Notification,
      },
      {
        path: "tab",
        name: "top-menu-tab",
        component: Tab,
      },
      {
        path: "accordion",
        name: "top-menu-accordion",
        component: Accordion,
      },
      {
        path: "button",
        name: "top-menu-button",
        component: Button,
      },
      {
        path: "alert",
        name: "top-menu-alert",
        component: Alert,
      },
      {
        path: "progress-bar",
        name: "top-menu-progress-bar",
        component: ProgressBar,
      },
      {
        path: "tooltip",
        name: "top-menu-tooltip",
        component: Tooltip,
      },
      {
        path: "dropdown",
        name: "top-menu-dropdown",
        component: Dropdown,
      },
      {
        path: "typography",
        name: "top-menu-typography",
        component: Typography,
      },
      {
        path: "icon",
        name: "top-menu-icon",
        component: Icon,
      },
      {
        path: "loading-icon",
        name: "top-menu-loading-icon",
        component: LoadingIcon,
      },
      {
        path: "regular-form",
        name: "top-menu-regular-form",
        component: RegularForm,
      },
      {
        path: "datepicker",
        name: "top-menu-datepicker",
        component: Datepicker,
      },
      {
        path: "tom-select",
        name: "top-menu-tom-select",
        component: TomSelect,
      },
      {
        path: "file-upload",
        name: "top-menu-file-upload",
        component: FileUpload,
      },
      {
        path: "wysiwyg-editor",
        name: "top-menu-wysiwyg-editor",
        component: WysiwygEditor,
      },
      {
        path: "validation",
        name: "top-menu-validation",
        component: Validation,
      },
      {
        path: "chart",
        name: "top-menu-chart",
        component: Chart,
      },
      {
        path: "slider",
        name: "top-menu-slider",
        component: Slider,
      },
      {
        path: "image-zoom",
        name: "top-menu-image-zoom",
        component: ImageZoom,
      },
    ],
  },
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/register",
    name: "register",
    component: Register,
  },
  {
    path: "/error-page",
    name: "error-page",
    component: ErrorPage,
  },
  {
    path: "/:pathMatch(.*)*",
    component: ErrorPage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { left: 0, top: 0 };
  },
});

export default router;
