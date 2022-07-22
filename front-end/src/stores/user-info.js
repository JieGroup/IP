import { defineStore } from "pinia";

export const useInfoStore = defineStore("info", {
  state: () => ({
    usernameValue: 
      localStorage.getItem("username") == null
        ? 'username'
        : localStorage.getItem("username"),
    passwordValue: 
      localStorage.getItem("password") == null
        ? 'password'
        : localStorage.getItem("password")
  }),
  getters: {
    username(state) {
      return state.usernameValue;
    },
    password(state) {
      return state.passwordValue;
    },
  },
  actions: {
    setUsername(username) {
      localStorage.setItem("username", username);
      this.username = username;
    },
    setPassword(password) {
      localStorage.setItem("password", password);
      this.password = password;
    },
  },
});