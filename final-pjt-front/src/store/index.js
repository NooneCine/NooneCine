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
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      console.log(state.token)
      router.push({name : 'HomeView'}) // store/index.js $router 접근 불가 -> import를 해야함
    },
    LOGOUT(state) {
      state.token = null
      console.log(state.token)
      location.reload()
    },
    MOVIE_LIST(state, payload) {
      if (payload.item == 'top_rated') {
        state.top_rated = payload.movie
      } else if (payload.item === 'now_playing') {
        state.now_playing = payload.movie
        console.log(state.now_playing)
      } else {
        state.popular = payload.movie
        // console.log(state.popular)
      }
    }
  },
  actions: {
    signUp(context, payload) {
      const email = payload.email
      const password = payload.password
      const password2 = payload.password2
      const name = payload.name
      const nickname = payload.nickname

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/register/`,
        data: {
          email, password, password2, name, nickname,
        }
      })
        .then((res) => {
          console.log(res.data)
          context.commit('SAVE_TOKEN', res.data.token)
          router.push({name : 'LoginView'})
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logIn(context, payload) {
      const email = payload.email
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/login/`,
        data: {
          email, password
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.token)
      })
      .catch((err) => console.log(err))
    },
    logOut(context) {
      context.commit('LOGOUT')
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
