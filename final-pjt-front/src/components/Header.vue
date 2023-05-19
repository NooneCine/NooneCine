<template>
  <div>
    <div class="navbar top">
      <router-link to="/">
        <img src="@/assets/default.png" alt="Bootstrap" height="48">
      </router-link>
      <div class="mt-0 top nav-a">
        <router-link to="/" class="m-3">HOME</router-link> 
        <router-link to="/movie" class="m-3">MOVIE</router-link> 
        <router-link to="/community" class="m-3">COMMUNITY</router-link> 
        <router-link to="/my-page" class="m-3">MY PAGE</router-link>
      </div>
      <div>
        <router-link to="/signup" class="me-3 text-primary">SIGN UP</router-link>
        <router-link to="/login" class="btn btn-primary text-white">LOGIN</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HeaderView',
  props: {
    msg: String
  }
}
</script>

<style>
.top {
  padding: 10px 20px;
  margin-right: 20px;
}

.top a {
  font-weight: bold;
  color: #FFC0B4;
  text-decoration-line: none;
}

.top a.router-link-exact-active {
  color: #FF2700;
}

.nav-a {
  font-size: 20px;
}
</style>
