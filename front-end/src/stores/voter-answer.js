import { defineStore } from "pinia";

export const voterAnswerStore = defineStore("voterAnswer", {
  state: () => ({
    surveyTopicsValue: 
      localStorage.getItem("surveyTopics") == null
        ? null
        : localStorage.getItem("surveyTopics")
  }),
  getters: {
    surveyTopics(state) {
      return state.surveyTopicsValue;
    },
  },
  actions: {
    setsurveyTopics(surveyTopics) {
      localStorage.setItem("surveyTopics", surveyTopics);
      this.surveyTopics = surveyTopics;
    },
  },
});