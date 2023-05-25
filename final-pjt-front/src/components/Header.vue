<template>
  <div>
    <div class="navbar top">
      <router-link to="/">
        <img src="@/assets/logo.png" alt="Bootstrap" height="48">
      </router-link>
      <div class="mt-0 top nav-a">
        <router-link to="/" class="m-3">HOME</router-link> 
        <router-link to="/movie" class="m-3">MOVIE</router-link> 
        <router-link to="/community" class="m-3">COMMUNITY</router-link> 
        <router-link to="/my-page" class="m-3">MY PAGE</router-link>
      </div>
      <div class="d-flex">
        <router-link to="/search" id="white">
          <svg @click="searchBar" xmlns="http://www.w3.org/2000/svg" width="20" fill="currentColor" height="20" class="bi bi-search me-4" viewBox="0 0 16 16">
            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
          </svg>
        </router-link>
        <div v-if="isUserLogin" id="white">
          <svg type="button" @click="logOut" xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="24" height="24" class="bi bi-box-arrow-right" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z"/>
            <path fill-rule="evenodd" d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"/>
          </svg>
        </div>
        <div v-else>
          <router-link to="/login" id="white">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
              <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
              <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
            </svg>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'HeaderView',
  props: {
    msg: String
  },
  methods: {
    searchBar() {

    },
    logOut() {
      this.$store.dispatch('logOut')
    },
  },
  computed: {
    isUserLogin() {
      return this.$store.getters.isLogin
    }
  }
}
</script>

<style>
.top {
  padding: 10px 20px;
  margin-top: 10px;
  margin-right: 20px;
  font-size: x-large;
}

.top a {
  font-weight: bold;
  color: rgb(255, 206, 81);
  text-decoration-line: none;
}

.top a.router-link-exact-active {
  color: #6B71F2;
}

#white {
  color: white;
}
</style>
