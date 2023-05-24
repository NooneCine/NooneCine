import axios from "axios";

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
  recommendMovieList: [],
};

const mutations = {
  setCurrentQuestionIndex(state, index) {
    state.currentQuestionIndex = index
  },
  setRecommendedGenre(state, genre) {
    state.recommendedGenre = genre
  },
  setSelectedAnswerId(state, { questionIndex, answerId }) {
    state.questions[questionIndex].selectedAnswerId = answerId
  },
  RECOMMEND_LIST(state, payload) {
    state.recommendMovieList = payload
  },
};

const actions = {
  startRecommendation({ commit }) {
    // Start the genre recommendation process
    commit('setCurrentQuestionIndex', 0)
    commit('setRecommendedGenre', null)
  },
  selectAnswer({ commit, dispatch, state }, answer) {
    const genreConditions = {
      '1-4-7': 'Family',
      '1-4-8': 'Comedy',
      '1-4-9': 'Romance',
      '1-5-7': 'Mystery',
      '1-5-8': 'Animation',
      '1-5-9': 'Fantasy',
      '1-6-7': 'Music',
      '1-6-8': 'Adventure',
      '1-6-9': 'Documentary',

      '2-4-7': 'Drama',
      '2-4-8': 'Science Fiction',
      '2-4-9': 'Music',
      '2-5-7': 'Thriller',
      '2-5-8': 'Crime',
      '2-5-9': 'Action',
      '2-6-7': 'Horror',
      '2-6-8': 'War',
      '2-6-9': 'Romance',

      '3-4-7': 'Thriller',
      '3-4-8': 'Action',
      '3-4-9': 'Science Fiction',
      '3-5-7': 'Romance',
      '3-5-8': 'Mystery',
      '3-5-9': 'Drama',
      '3-6-7': 'Adventure',
      '3-6-8': 'Animation',
      '3-6-9': 'Documentary',
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
      const recommendedGenre = genreConditions[selectedAnswerIds] || 'Western'

      commit('setRecommendedGenre', recommendedGenre)
    }
  },
  recommendMovieList({ commit }) {
    const sortOptions = ['revenue', 'popularity', 'primary_release_date', 'vote_average']
    const randomSort = sortOptions[Math.floor(Math.random() * sortOptions.length)]

    axios({
      method: 'get',
      headers: {
        accept: 'application/json',
        Authorization: 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NWU2ZWViNWY4NjhhMjVkODY5NTNlMjRhYmYyMjEyMCIsInN1YiI6IjYzZDMzNGRiY2I3MWI4MDA4OTZjZmIzZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.nGBlA4h6pmnikj7UL406_zeDsmdDj_eevOjGU1MI84I'
      },
      url: `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=${ randomSort }.desc&with_genres=${ state.recommendedGenre }`
    })
    .then((res) => {
      commit('RECOMMEND_LIST', res.data.results)
      console.log(randomSort)
      console.log(res.data.results)
    })
    .catch((err) => {
      console.log(err)
    })
  }
}
   
export default {
  namespaced: true,
  state,
  mutations,
  actions
};