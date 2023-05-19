<template>
  <div class="footer">
    <footer class="container">
      <div>
        <router-link to="/">Home</router-link>
        <router-link to="/movie">Movie</router-link>
        <router-link to="/community">Community</router-link>
      </div>
      <br>
      <p>Copyright © UngNi All Rights Reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'FooterView',
}
</script>

<style scoped>
.footer {
  background-color: rgb(172, 170, 164);
  color: white;
  height: 140px;
}

p {
  margin-bottom: 0;
  font-size: 0.8em;
  text-align: left;
}

a {
  text-decoration-line: none;
  color: white;
  display: flex;
}
</style>
