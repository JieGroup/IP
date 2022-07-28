import { defineStore } from "pinia";

export const voterAnswerStore = defineStore("voterAnswer", {
  state: () => ({
    surveyTopicsValue: 
      localStorage.getItem("surveyTopics") === null
        ? null
        : localStorage.getItem("surveyTopics"),
    surveyAnswerIDValue: 
      localStorage.getItem("surveyAnswerID") === null
        ? null
        : localStorage.getItem("surveyAnswerID"),
    surveyUpdateMethodValue: 
      localStorage.getItem("surveyUpdateMethod") === null
        ? null
        : localStorage.getItem("surveyUpdateMethod"),
  }),
  getters: {
    surveyTopics(state) {
      return state.surveyTopicsValue;
    },
    surveyAnswerID(state) {
      return state.surveyAnswerIDValue;
    },
    surveyUpdateMethod(state) {
      return state.surveyUpdateMethodValue;
    }
  },
  actions: {
    setsurveyTopics(surveyTopics) {
      console.log('?????!!surveyTopics', surveyTopics)
      localStorage.setItem("surveyTopics", surveyTopics);
      this.surveyTopicsValue = surveyTopics;
    },
    setsurveyAnswerID(surveyAnswerID) {
      localStorage.setItem("surveyAnswerID", surveyAnswerID);
      this.surveyAnswerIDValue = surveyAnswerID;
    },
    setsurveyUpdateMethod(surveyUpdateMethod) {
      localStorage.setItem("surveyUpdateMethod", surveyUpdateMethod);
      this.surveyUpdateMethodValue = surveyUpdateMethod;
    },
  },
});