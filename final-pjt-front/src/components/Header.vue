<template>
  <nav class="navbar">
    <div class="container">
      <router-link to="/" class="nav-item">
        <img src="@/assets/default.png" alt="Bootstrap" height="48">
      </router-link>
      <router-link to="/" class="nav-item">HOME</router-link> 
      <router-link to="/movie" class="nav-item">MOVIE</router-link> 
      <router-link to="/community" class="nav-item">COMMUNITY</router-link> 
      <router-link to="/my-page" class="nav-item">MY PAGE</router-link>
    </div>

    <router-link to="/signup">SIGN UP</router-link> |
    <router-link to="/login">LOGIN</router-link>
  </nav>
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
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration-line: none;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
