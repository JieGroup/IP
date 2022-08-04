import { defineStore } from "pinia";

export const useInfoStore = defineStore("info", {
  state: () => ({
    RememberValue:
      localStorage.getItem("remember") === null
        ? 'false'
        : localStorage.getItem("remember"),
    usernameValue: 
      localStorage.getItem("username") === null
        ? ''
        : localStorage.getItem("username"),
    passwordValue: 
      localStorage.getItem("password") === null
        ? ''
        : localStorage.getItem("password")
  }),
  getters: {
    remember(state) {
      return state.RememberValue;
    },
    username(state) {
      return state.usernameValue;
    },
    password(state) {
      return state.passwordValue;
    },
  },
  actions: {
    setRemember(remember) {
      localStorage.setItem("remember", remember);
      this.RememberValue = remember;
    },
    setUsername(username) {
      localStorage.setItem("username", username);
      this.usernameValue = username;
    },
    setPassword(password) {
      localStorage.setItem("password", password);
      this.passwordValue = password;
    },
  },
});