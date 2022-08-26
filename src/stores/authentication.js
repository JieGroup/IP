import { defineStore } from "pinia";

console.log(localStorage.getItem("userToken"), localStorage.getItem("userToken") === null, localStorage.getItem("userToken") === '', localStorage.getItem("userToken") === undefined)
if (localStorage.getItem("userToken") !== null){

  console.log('sha', localStorage.getItem("userToken") !== null, localStorage.getItem('userToken'))
console.log('sha2', localStorage.getItem('userToken').split('.')[1])
console.log('shatokenstore', JSON.parse(atob(localStorage.getItem('userToken').split('.')[1])))
}

// console.log('sha', JSON.parse(atob(localStorage.getItem('userToken').split('.')[1])).authority_level )

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
        ? JSON.parse(atob(localStorage.getItem('userToken').split('.')[1])).authority_level 
        : 'user',
    // voterAuthorityValue: 
    //   localStorage.getItem('voterToken') !== null
    //     ? JSON.parse(atob(localStorage.getItem('voterToken').split('.')[1])).authority_level 
    //     : 'voter',
    userIdValue: 
      localStorage.getItem('userToken') !== null
        ? JSON.parse(atob(localStorage.getItem('userToken').split('.')[1])).user_id 
        : null,
    userNameValue: 
      localStorage.getItem('userToken') !== null
        ? JSON.parse(atob(localStorage.getItem('userToken').split('.')[1])).username 
        : null,
    displayNameValue: 
      localStorage.getItem('userToken') !== null
        ? JSON.parse(atob(localStorage.getItem('userToken').split('.')[1])).displayName 
        : null,
    userAvatarValue: 
      localStorage.getItem('userAvatar') !== null
        ? localStorage.getItem('userAvatar')
        : '',
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
    userName(state){
      return state.userNameValue;
    },
    displayName(state){
      return state.displayNameValue;
    },
    // voterAuthority(state) {
    //   return state.voterAuthorityValue;
    // },
    userId(state) {
      return state.userIdValue;
    },
    userAvatar(state) {
      return state.userAvatarValue;
    }
  },
  actions: {
    setUserToken(userToken) {
      localStorage.setItem("userToken", userToken);
      this.userTokenValue = userToken;
    },
    deleteUserToken() {
      localStorage.removeItem('userToken');
      this.userTokenValue = null;
    },
    setVoterToken(voterToken) {
      localStorage.setItem("voterToken", voterToken);
      this.voterTokenValue = voterToken;
    },
    deleteVoterToken() {
      localStorage.removeItem('voterToken');
      this.voterTokenValue = null;
    },
    setUserAuthority(authority_level) {
      this.userAuthorityValue = authority_level
    },
    setUserName(username) {
      this.userNameValue = username
    },
    setdisplayName(displayName) {
      this.displayNameValue = displayName
    },
    setUserID(user_id) {
      this.userIdValue = user_id
    },
    setIsUserAthenticated(isUserAthenticated) {
      this.isUserAuthenticatedValue = isUserAthenticated
    },
    setUserAvatar(userAvatar) {
      localStorage.setItem("userAvatar", userAvatar);
      this.userAvatarValue = userAvatar
    },
    deleteUserAvatar() {
      localStorage.removeItem("userAvatar");
      this.userAvatarValue = ''
    },
    loginAction (userToken) {
      console.log('loginAction triggered')
      const parsed_token = JSON.parse(atob(localStorage.getItem('userToken').split('.')[1]));
      console.log(`loginAction${parsed_token}`)
      let authority_level = parsed_token.authority_level;
      let username = parsed_token.username;
      let displayName = parsed_token.displayName;
      let user_id = parsed_token.user_id;
      
      this.setUserToken(userToken)
      this.setUserAuthority(authority_level)
      this.setUserName(username)
      this.setdisplayName(displayName)
      this.setUserID(user_id)
      this.setIsUserAthenticated(true)
    },
    logoutAction () {
      console.log('logoutAction triggered')
      this.deleteUserToken()
      this.setUserAuthority(null)
      this.setUserName(null)
      this.setdisplayName(null)
      this.setUserID(null)
      this.setIsUserAthenticated(false)
      this.deleteUserAvatar()
    },
  },
});