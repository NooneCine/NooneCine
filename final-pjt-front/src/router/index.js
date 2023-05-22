import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/home/HomeView.vue'
import MovieView from '../views/movies/MovieView.vue'
import CommunityView from '../views/community/CommunityView.vue'
import CommunityCreateView from '../views/community/CommunityCreateView.vue'
import CommunityDetailView from '../views/community/CommunityDetailView.vue'
import MypageView from '../views/accounts/MypageView.vue'
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
    component: CommunityDetailView
  },
  {
    path: '/my-page',
    name: 'MypageView',
    component: MypageView
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
