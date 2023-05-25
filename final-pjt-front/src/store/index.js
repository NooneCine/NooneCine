import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'
import genre from './modules/genre'


const API_URL = 'http://127.0.0.1:8000'
const API_KEY = '75e6eeb5f868a25d86953e24abf22120'


Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    user: [],
    top_rated: [],
    now_playing: [],
    popular: [],
    posts: [],
    post: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    SAVE_TOKEN(state, payload) {
      state.token = payload.token
      state.user = payload.user
      console.log(state.token)
      router.push({name : 'HomeView'}) // store/index.js $router 접근 불가 -> import를 해야함
    },
    LOGOUT(state) {
      state.token = null
      state.user = []
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
      }
    },
    GET_POSTS(state, posts) {
      state.posts = posts
    },
    DELETE_POST(state, id) {
      state.posts = state.posts.filter((post)=>{
        return !(post.id===id)
      })
    },
    LIKE_POST(state) {
      const likedPost = state.posts.find(post => post.id === state.post.id);
      if (likedPost) {
        likedPost.likes.push(state.user.id);
      }
    },
    UNLIKE_POST(state) {
      const likedPost = state.posts.find(post => post.id === state.post.id);
      if (likedPost) {
        const index = likedPost.likes.indexOf(state.user.id);
        if (index !== -1) {
          likedPost.likes.splice(index, 1);
        }
      }
    },
    UPDATE_PROFILE(state, user) {
      state.user = {
        ...state.user,
        ...user
      }
    },
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
          context.commit('SAVE_TOKEN', res.data)
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
        context.commit('SAVE_TOKEN', res.data)
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
    },

    // components/Community
    getPosts(context) {
      axios({
        method: 'get',
        url: `${API_URL}/community/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((res) => {
        context.commit('GET_POSTS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    createPost(context, payload) {
      const title = payload.title
      const content = payload.content
      const image = payload.image
      const user = payload.user.id

      let formData = new FormData()
      formData.append('title', title)
      formData.append('content', content)
      formData.append('user', user)
      if (image) {
        formData.append('image', image);
      }

      axios({
        method: 'post',
        url: `${API_URL}/community/`,
        data: formData,
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((res) => {
        this.posts = res.data
        router.push({ name: 'CommunityView' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    deletePost(context, id) {
      axios({
        method: 'delete',
        url: `${API_URL}/community/${ id }/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then(() => {
        context.commit('DELETE_POST', id)
        router.push({ name: 'CommunityView' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    updatePost(context, payload) {
      const id = payload.id
      const title = payload.title
      const content = payload.content
      const image = payload.image
      const user = payload.user.id

      let formData = new FormData()
      formData.append('title', title)
      formData.append('content', content)
      formData.append('user', user)
      formData.append('image', image)

      axios({
        method: 'put',
        url: `${API_URL}/community/${ id }/`,
        data: formData,
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((res) => {
        this.post = res.data
        router.push({ name: 'CommunityDetailView', params: { id: id } })
      })
      .catch((err) => {
        console.log(err)
      })
    },

    // mypage
    updateProfile({ commit }, user) {
      commit('UPDATE_PROFILE', user)
    },
  },
  modules: {
    genre
  }
})
