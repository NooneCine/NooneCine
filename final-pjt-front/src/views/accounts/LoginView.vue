<template>
  <div>
    <h1>LoginView</h1>
    <form @submit.prevent="login">
      <label for="email">email : </label>
      <input type="email" id="email" v-model="email"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="Login">
    </form>
    <p>아직 누네씨네의 회원이 아니신가요? <router-link to="/signup">회원가입 하기</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      email: null,
      password: null,
    }
  },
  methods: {
    login() {
      const email = this.email
      const password = this.password

      const payload = {
        email, password,
      }

      this.$store.dispatch('logIn', payload)

    }
  }
}
</script>

<style>
a {
  text-decoration-line: none;
}
</style>