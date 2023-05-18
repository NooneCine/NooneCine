<template>
  <div>
    <nav>
      <router-link to="/">HOME</router-link> |
      <router-link to="/movie">MOVIE</router-link> |
      <router-link to="/community">COMMUNITY</router-link> |
      <router-link to="/my-page">MY PAGE</router-link> |
      <router-link to="/signup">SIGN UP</router-link> |
      <router-link to="/login">LOGIN</router-link>
    </nav>
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

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
