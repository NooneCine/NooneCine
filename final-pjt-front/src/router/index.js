import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/home/HomeView.vue'
import MovieView from '../views/movies/MovieView.vue'
import CommunityView from '../views/community/CommunityView.vue'
import MypageView from '../views/accounts/MypageView.vue'
import SignUpView from '../views/accounts/SignUpView.vue'
import LoginView from '../views/accounts/LoginView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/my-page',
    name: 'my-page',
    component: MypageView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
