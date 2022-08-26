import { defineStore } from "pinia";

export const useWebStore = defineStore("web", {
  state: () => ({
    // websiteURLValue: "https://grand-liger-cad265.netlify.app"
    websiteURLValue: "http://localhost:3000"
  }),
  getters: {
    websiteURL(state) {
      return state.websiteURLValue;
    },
  },
//   actions: {
//     setRemember(remember) {
//       localStorage.setItem("remember", remember);
//       this.RememberValue = remember;
//     },
//     setUsername(username) {
//       localStorage.setItem("username", username);
//       this.usernameValue = username;
//     },
//     setPassword(password) {
//       localStorage.setItem("password", password);
//       this.passwordValue = password;
//     },
//   },
});