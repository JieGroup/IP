import { defineStore } from "pinia";

export const useSideMenuStore = defineStore("sideMenu", {
  state: () => ({
    menu: [
      // {
      //   icon: "HomeIcon",
      //   pageName: "side-menu-dashboard-overview-4",
      //   title: "Overview",
      // },
      {
        icon: "LogInIcon",
        pageName: "login",
        title: "Login",
      },
      {
        icon: "TrelloIcon",
        pageName: "side-menu-profile-overview-3",
        title: "Profile",
      },
      "devider",
      {
        icon: "SidebarIcon",
        pageName: "side-menu-create-new-survey",
        title: "Create New Survey",
      },
      {
        icon: "SidebarIcon",
        pageName: "side-menu-answer-form",
        title: "Answer Form",
      },
      // {
      //   icon: "SidebarIcon",
      //   pageName: "side-menu-get-voter-answers",
      //   title: "Get Voter Answers",
      // },
      "devider",
      
      {
        icon: "ShoppingBagIcon",
        pageName: "side-menu-histories",
        title: "Histories",
      },
      "devider",
      {
        icon: "LayoutIcon",
        pageName: "side-menu-faq-layout-3",
        title: "FAQ",
      }
      
      // {
      //   icon: "LayoutIcon",
      //   pageName: "side-menu-layout",
      //   title: "Pages",
      //   subMenu: [
      //     {
      //       icon: "",
      //       pageName: "side-menu-wizards",
      //       title: "Wizards",
      //       subMenu: [
      //         {
      //           icon: "",
      //           pageName: "side-menu-wizard-layout-1",
      //           title: "Layout 1",
      //         },
      //         {
      //           icon: "",
      //           pageName: "side-menu-wizard-layout-2",
      //           title: "Layout 2",
      //         },
      //         {
      //           icon: "",
      //           pageName: "side-menu-wizard-layout-3",
      //           title: "Layout 3",
      //         },
      //       ],
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-blog",
      //       title: "Blog",
      //       subMenu: [
      //         {
      //           icon: "",
      //           pageName: "side-menu-blog-layout-1",
      //           title: "Layout 1",
      //         },
      //         {
      //           icon: "",
      //           pageName: "side-menu-blog-layout-2",
      //           title: "Layout 2",
      //         },
      //         {
      //           icon: "",
      //           pageName: "side-menu-blog-layout-3",
      //           title: "Layout 3",
      //         },
      //       ],
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-pricing",
      //       title: "Pricing",
      //       subMenu: [
      //         {
      //           icon: "",
      //           pageName: "side-menu-pricing-layout-1",
      //           title: "Layout 1",
      //         },
      //         {
      //           icon: "",
      //           pageName: "side-menu-pricing-layout-2",
      //           title: "Layout 2",
      //         },
      //       ],
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-invoice",
      //       title: "Invoice",
      //       subMenu: [
      //         {
      //           icon: "",
      //           pageName: "side-menu-invoice-layout-1",
      //           title: "Layout 1",
      //         },
      //         {
      //           icon: "",
      //           pageName: "side-menu-invoice-layout-2",
      //           title: "Layout 2",
      //         },
      //       ],
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-faq",
      //       title: "FAQ",
      //       subMenu: [
      //         {
      //           icon: "",
      //           pageName: "side-menu-faq-layout-1",
      //           title: "Layout 1",
      //         },
      //         {
      //           icon: "",
      //           pageName: "side-menu-faq-layout-2",
      //           title: "Layout 2",
      //         },
      //         {
      //           icon: "",
      //           pageName: "side-menu-faq-layout-3",
      //           title: "Layout 3",
      //         },
      //       ],
      //     },
      //     {
      //       icon: "",
      //       pageName: "login",
      //       title: "Login",
      //     },
      //     {
      //       icon: "",
      //       pageName: "register",
      //       title: "Register",
      //     },
      //     {
      //       icon: "",
      //       pageName: "error-page",
      //       title: "Error Page",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-update-profile",
      //       title: "Update profile",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-change-password",
      //       title: "Change Password",
      //     },
      //   ],
      // },
      // {
      //   icon: "InboxIcon",
      //   pageName: "side-menu-components",
      //   title: "Components",
      //   subMenu: [
      //     {
      //       icon: "",
      //       pageName: "side-menu-table",
      //       title: "Table",
      //       subMenu: [
      //         {
      //           icon: "",
      //           pageName: "side-menu-regular-table",
      //           title: "Regular Table",
      //         },
      //         {
      //           icon: "",
      //           pageName: "side-menu-tabulator",
      //           title: "Tabulator",
      //         },
      //       ],
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-overlay",
      //       title: "Overlay",
      //       subMenu: [
      //         {
      //           icon: "",
      //           pageName: "side-menu-modal",
      //           title: "Modal",
      //         },
      //         {
      //           icon: "",
      //           pageName: "side-menu-slide-over",
      //           title: "Slide Over",
      //         },
      //         {
      //           icon: "",
      //           pageName: "side-menu-notification",
      //           title: "Notification",
      //         },
      //       ],
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-tab",
      //       title: "Tab",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-accordion",
      //       title: "Accordion",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-button",
      //       title: "Button",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-alert",
      //       title: "Alert",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-progress-bar",
      //       title: "Progress Bar",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-tooltip",
      //       title: "Tooltip",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-dropdown",
      //       title: "Dropdown",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-typography",
      //       title: "Typography",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-icon",
      //       title: "Icon",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-loading-icon",
      //       title: "Loading Icon",
      //     },
      //   ],
      // },
      // {
      //   icon: "SidebarIcon",
      //   pageName: "side-menu-forms",
      //   title: "Forms",
      //   subMenu: [
      //     {
      //       icon: "",
      //       pageName: "side-menu-regular-form",
      //       title: "Regular Form",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-datepicker",
      //       title: "Datepicker",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-tom-select",
      //       title: "Tom Select",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-file-upload",
      //       title: "File Upload",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-wysiwyg-editor",
      //       title: "Wysiwyg Editor",
      //     },
      //     // {
      //     //   icon: "",
      //     //   pageName: "side-menu-validation",
      //     //   title: "Validation",
      //     // },
      //   ],
      // },
      // {
      //   icon: "HardDriveIcon",
      //   pageName: "side-menu-widgets",
      //   title: "Widgets",
      //   subMenu: [
      //     {
      //       icon: "",
      //       pageName: "side-menu-chart",
      //       title: "Chart",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-slider",
      //       title: "Slider",
      //     },
      //     {
      //       icon: "",
      //       pageName: "side-menu-image-zoom",
      //       title: "Image Zoom",
      //     },
      //   ],
      // },
    ],
  }),
});
