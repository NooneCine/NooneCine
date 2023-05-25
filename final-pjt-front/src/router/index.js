import Vue from 'vue'
import store from '../store'
import VueRouter from 'vue-router'
import axios from 'axios'
import HomeView from '../views/home/HomeView.vue'
import MovieView from '../views/movies/MovieView.vue'
import MovieDetailView from '../views/movies/MovieDetailView.vue'
import CommunityView from '../views/community/CommunityView.vue'
import CommunityCreateView from '../views/community/CommunityCreateView.vue'
import CommunityUpdateView from '../views/community/CommunityUpdateView.vue'
import CommunityDetailView from '../views/community/CommunityDetailView.vue'
import MypageView from '../views/accounts/MypageView.vue'
import MypageUpdateView from '../views/accounts/MypageUpdateView.vue'
import UserPageView from '../views/accounts/UserPageView.vue'
import SignUpView from '../views/accounts/SignUpView.vue'
import LoginView from '../views/accounts/LoginView.vue'
import SearchView from '../views/home/SearchView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/movie',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/movie/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/community/create',
    name: 'CommunityCreateView',
    component: CommunityCreateView
  },
  {
    path: '/community/:id',
    name: 'CommunityDetailView',
    component: CommunityDetailView,
    beforeEnter: (to, from, next) => {
      const API_URL = 'http://127.0.0.1:8000'

      axios({
        method: 'get',
        url: `${API_URL}/community/${ to.params.id }/`,
        headers: {
          Authorization: `Token ${ store.state.token }`
        }
      })
      .then((res) => {
        store.state.post = res.data
        next()
      })
      .catch((err) => {
        console.log(err)
        next(false)
      })
    }
  },
  {
    path: '/community/:id/update',
    name: 'CommunityUpdateView',
    component: CommunityUpdateView
  },
  {
    path: '/my-page',
    name: 'MypageView',
    component: MypageView
  },
  {
    path: '/update-mypage',
    name: 'MypageUpdateView',
    component: MypageUpdateView
  },
  {
    path: '/user-page/:id',
    name: 'UserPageView',
    component: UserPageView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
