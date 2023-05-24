const state = {
  currentQuestionIndex: 0,
  questions: [
    {
      question: '오늘은 어떤 공간으로 떠나고 싶어?',
      answers: [
        { id: 1, label: '공원' },
        { id: 2, label: '바다' },
        { id: 3, label: '집' }
      ]
    },
    {
      question: '어떤 날씨가 좋을까?',
      answers: [
        { id: 4, label: '햇빛 쨍쨍한 날' },
        { id: 5, label: '비오는 날' },
        { id: 6, label: '눈오는 날' }
      ]
    },
    {
      question: '같이 먹고 싶은 음식은?',
      answers: [
        { id: 7, label: '팝콘' },
        { id: 8, label: '치맥' },
        { id: 9, label: '누네띠네' }
      ]
    }
  ],
  recommendedGenre: null
};

const mutations = {
  setCurrentQuestionIndex(state, index) {
    state.currentQuestionIndex = index;
  },
  setRecommendedGenre(state, genre) {
    state.recommendedGenre = genre;
  }
};

const actions = {
  startRecommendation({ commit }) {
    // Start the genre recommendation process
    commit('setCurrentQuestionIndex', 0);
    commit('setRecommendedGenre', null);
  },
  selectAnswer({ commit, dispatch, state }, answer) {
    // Update the state with the selected answer
    console.log(dispatch, answer)
    const nextQuestionIndex = state.currentQuestionIndex + 1;

    if (nextQuestionIndex <= state.questions.length) {
      // If there are more questions, proceed to the next question
      commit('setCurrentQuestionIndex', nextQuestionIndex);
    }
  
    if (nextQuestionIndex === state.questions.length + 1) {
      // If all questions are answered, recommend a genre
      const recommendedGenre = 'Action'; // Replace with your genre mapping logic
      commit('setRecommendedGenre', recommendedGenre);
    }
  }
}
   
export default {
  namespaced: true,
  state,
  mutations,
  actions
};