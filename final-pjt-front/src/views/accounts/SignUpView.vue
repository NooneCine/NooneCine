<template>
  <div class="container">
    <h1 class="m-5">SignUp</h1>
    <form @submit.prevent="signUp">
      <div class="form-floating mb-3">
        <input type="email" id="email" v-model="email" class="form-control" placeholder="name@example.com">
        <label for="email">이메일을 입력해주세요</label>
      </div>

      <div class="form-floating mb-3">
        <input type="password" id="password" v-model="password" class="form-control" placeholder="Password">
        <label for="password">비밀번호를 입력해주세요</label>
      </div>

      <div class="form-floating mb-3">
        <input type="password" id="password2" v-model="password2" class="form-control" placeholder="Password">
        <label for="password2">비밀번호를 다시 입력해주세요</label>
      </div>
      
      <div class="row g-2">
        <div class="form-floating col-md">
          <input type="text" id="name" v-model="name" class="form-control" placeholder="text">
          <label for="name">이름을 입력해주세요</label>
        </div>
        <br>
        <div class="form-floating col-md">
          <input type="text" id="nickname" v-model="nickname" class="form-control" placeholder="text">
          <label for="nickname">닉네임을 입력해주세요</label>
        </div>
      </div>

      <input type="submit" value="SignUp" class="btn btn-primary form-control mt-3 mb-4">
    </form>
    <p>이미 누네씨네 계정이 있다면, <router-link to="/login">로그인 하기</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      email: null,
      password: null,
      password2: null,
      name: null,
      nickname: null,
    }
  },
  methods: {
    signUp() {
      // console.log('signup')
      const email = this.email
      const password = this.password
      const password2 = this.password2
      const name = this.name
      const nickname = this.nickname

      const payload = {
        email, password, password2, name, nickname
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>

<style>

</style>