<template>
  <div class="container">
    <h1 class="m-5">Login</h1>

    <form @submit.prevent="login">
      <div class="form-floating mb-3">
        <input type="email" id="email" v-model="email" class="form-control" placeholder="name@example.com">
        <label for="email">이메일을 입력해주세요</label>
      </div>

      <div class="form-floating">
        <input type="password" id="password" v-model="password" class="form-control" placeholder="Password">
        <label for="password">비밀번호를 입력해주세요</label>
        <br>
      </div>

      <input type="submit" value="Login" class="btn btn-primary form-control mb-4">
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