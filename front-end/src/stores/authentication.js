import { defineStore } from "pinia";

export const useAuthenticationStore = defineStore("authentication", {
  state: () => ({
    userTokenValue: localStorage.getItem("userToken"),
    voterTokenValue: localStorage.getItem("voterToken"),
    isUserAuthenticatedValue: 
      localStorage.getItem('userToken') !== null
        ? true 
        : false,
    isVoterAuthenticatedValue: 
      localStorage.getItem('voterToken') !== null
        ? true 
        : false,
    userAuthorityValue: 
      localStorage.getItem('userToken') !== null
        ? JSON.parse(atob(window.localStorage.getItem('userToken').split('.')[1])).authority 
        : 'user',
    voterAuthorityValue: 
      localStorage.getItem('voterToken') !== null
        ? JSON.parse(atob(window.localStorage.getItem('voterToken').split('.')[1])).authority 
        : 'voter',
    userIdValue: 
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
      return state.isUserAuthenticatedValue;
    },
    isVoterAthenticated(state) {
      return state.isVoterAuthenticatedValue;
    },
    userAuthority(state) {
      return state.userAuthorityValue;
    },
    voterAuthority(state) {
      return state.voterAuthorityValue;
    },
    userId(state) {
      return state.userIdValue;
    },
  },
  actions: {
    setUserToken(userToken) {
      localStorage.setItem("userToken", userToken);
      this.userTokenValue = userToken;
    },
    setVoterToken(voterToken) {
      localStorage.setItem("voterToken", voterToken);
      this.voterTokenValue = voterToken;
    },
    loginAction (userToken) {
      console.log('loginAction triggered')
      const parsed_token = JSON.parse(atob(localStorage.getItem('userToken').split('.')[1]));
      this.userIdValue = parsed_token.user_id;
      this.setUserToken(userToken)
      this.isUserAuthenticatedValue = true;
    },
    logoutAction () {
      console.log('logoutAction triggered')
      this.userIdValue = null;
      localStorage.removeItem('userToken');
      this.isUserAuthenticatedValue = false;
    },
  },
});