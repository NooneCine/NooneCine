import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'
const API_KEY = '75e6eeb5f868a25d86953e24abf22120'


Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    top_rated: [],
    now_playing: [],
    popular: [],
  },
  getters: {
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'HomeView'}) // store/index.js $router 접근 불가 -> import를 해야함
    },
    MOVIE_LIST(state, payload) {
      if (payload.item == 'top_rated') {
        state.top_rated = payload.movie
        console.log(state.top_rated)
      } else if (payload.item === 'now_playing') {
        state.now_playing = payload.movie
      } else {
        state.popular = payload.movie
      }
    }
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    // components/MovieList
    getMovieList(context, num) {
      return new Promise(() => {
        axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${num}?api_key=${API_KEY}&language=ko-KR&page=1`,
        })
        .then((res) => {
          const payload = {
            'item': num,
            'movie': res.data.results
          }
          context.commit('MOVIE_LIST', payload)
          console.log(num)
        })
        .catch((err) => {
          console.log(err)
        })
      })
    }
  },
  modules: {
  }
})
