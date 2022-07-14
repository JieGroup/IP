import { defineStore } from "pinia";

export const useAuthenticationStore = defineStore("authentication", {
  state: () => ({
    userTokenValue: localStorage.getItem("userToken"),
    voterTokenValue: localStorage.getItem("voterToken"),
    isUserAuthenticated: 
      localStorage.getItem('userToken') !== null
        ? true 
        : false,
    isVoterAuthenticated: 
      localStorage.getItem('voterToken') !== null
        ? true 
        : false,
    userAuthority: 
      localStorage.getItem('userToken') !== null
        ? JSON.parse(atob(window.localStorage.getItem('userToken').split('.')[1])).authority 
        : 'user',
    voterAuthority: 
      localStorage.getItem('voterToken') !== null
        ? JSON.parse(atob(window.localStorage.getItem('voterToken').split('.')[1])).authority 
        : 'voter',
    userId: 
      localStorage.getItem('userToken') !== null
        ? JSON.parse(atob(window.localStorage.getItem('userToken').split('.')[1])).user_id 
        : null,
  }),
  getters: {
    userToken(state) {
      return state.userTokenValue;
    },
    voterToken(state) {
      return state.voterTokenValue;
    },
    isUserAthenticated(state) {
      return state.isUserAuthenticated;
    },
    isVoterAthenticated(state) {
      return state.isVoterAuthenticated;
    },
    userAuthority(state) {
      return state.userAuthority;
    },
    voterAuthority(state) {
      return state.voterAuthority;
    },
    userId(state) {
      return state.userId;
    },
  },
  actions: {
    setUserToken(userToken) {
      localStorage.setItem("userToken", userToken);
      this.userToken = userToken;
    },
    setVoterToken(voterToken) {
      localStorage.setItem("voterToken", voterToken);
      this.voterToken = voterToken;
    },
    loginAction (userToken) {
      console.log('loginAction triggered')
      this.setUserToken(userToken)
      this.isUserAuthenticated = true;
      const parsed_token = JSON.parse(atob(localStorage.getItem('userToken').split('.')[1]));
      this.userId = parsed_token.user_id;
    },
    logoutAction () {
      console.log('logoutAction triggered')
      localStorage.removeItem('userToken');
      this.isUserAuthenticated = false;
      this.userId = null;
    },
  },
});