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
        { id: 9, label: '와인과 치즈' }
      ]
    }
  ],
  recommendedGenre: null,
  selectedAnswerId: null
};

const mutations = {
  setCurrentQuestionIndex(state, index) {
    state.currentQuestionIndex = index
  },
  setRecommendedGenre(state, genre) {
    state.recommendedGenre = genre
  },
  setSelectedAnswerId(state, { questionIndex, answerId }) {
    state.questions[questionIndex].selectedAnswerId = answerId;
  }
};

const actions = {
  startRecommendation({ commit }) {
    // Start the genre recommendation process
    commit('setCurrentQuestionIndex', 0)
    commit('setRecommendedGenre', null)
  },
  selectAnswer({ commit, dispatch, state }, answer) {
    const genreConditions = {
      '1-4-7': '가족 영화',
      '1-4-8': '코미디',
      '1-4-9': '로맨스',
      '1-5-7': '미스터리',
      '1-5-8': '애니메이션',
      '1-5-9': '판타지',
      '1-6-7': '음악',
      '1-6-8': '모험',
      '1-6-9': '다큐멘터리',

      '2-4-7': '드라마',
      '2-4-8': '공상과학',
      '2-4-9': '음악',
      '2-5-7': '스릴러',
      '2-5-8': '범죄',
      '2-5-9': '액션',
      '2-6-7': '공포',
      '2-6-8': '전쟁',
      '2-6-9': '로맨스',

      '3-4-7': '스릴러',
      '3-4-8': '액션',
      '3-4-9': '공상과학',
      '3-5-7': '로맨스',
      '3-5-8': '미스터리',
      '3-5-9': '드라마',
      '3-6-7': '모험',
      '3-6-8': '애니메이션',
      '3-6-9': '다큐멘터리',
    }

    // Update the state with the selected answer
    console.log(dispatch, answer)
    commit('setSelectedAnswerId', { questionIndex: state.currentQuestionIndex, answerId: answer.id })

    const nextQuestionIndex = state.currentQuestionIndex + 1

    if (nextQuestionIndex <= state.questions.length) {
      // If there are more questions, proceed to the next question
      commit('setCurrentQuestionIndex', nextQuestionIndex)
    }
  
    if (nextQuestionIndex === state.questions.length) {

      const selectedAnswers = state.questions.map((q) => q.selectedAnswerId)
      const selectedAnswerIds = selectedAnswers.join('-')
      const recommendedGenre = genreConditions[selectedAnswerIds] || '기타 장르'

      commit('setRecommendedGenre', recommendedGenre)
    }
  }
}
   
export default {
  namespaced: true,
  state,
  mutations,
  actions
};