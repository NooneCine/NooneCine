<template>
  <div class="container">
    <h1 class="m-5"><b>Login</b></h1>

    <form @submit.prevent="login">
      <div class="form-floating mb-4">
        <input type="email" id="email" v-model="email" class="form-control" placeholder="name@example.com">
        <label for="email" style="color: #606060; background-color: none;">이메일을 입력해주세요</label>
      </div>

      <div class="form-floating">
        <input type="password" id="password" v-model="password" class="form-control" placeholder="Password">
        <label for="password" style="color: #606060; background-color: none;">비밀번호를 입력해주세요</label>
        <br>
      </div>

      <input type="submit" value="Login" class="btn purple form-control mt-4 mb-4" style="height: 50px;">
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
.purple {
  color: white;
  background-color: #6B71F2;
}

a {
  color: #6B71F2;
  font-weight: 800;
  text-decoration-line: none;
}
</style>