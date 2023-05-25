<template>
  <div class="container">
    <h1 class="m-5"><b>SignUp</b></h1>
    <form @submit.prevent="signUp">
      <div class="form-floating mb-4">
        <input type="email" id="email" v-model="email" class="form-control" placeholder="name@example.com">
        <label for="email" style="color: #606060; background-color: none;">이메일을 입력해주세요</label>
      </div>

      <div class="form-floating mb-4">
        <input type="password" id="password" v-model="password" class="form-control" placeholder="Password">
        <label for="password" style="color: #606060; background-color: none;">비밀번호를 입력해주세요</label>
      </div>

      <div class="form-floating mb-4">
        <input type="password" id="password2" v-model="password2" class="form-control" placeholder="Password">
        <label for="password2" style="color: #606060; background-color: none;">비밀번호를 다시 입력해주세요</label>
      </div>
      
      <div class="row g-2">
        <div class="form-floating col-md">
          <input type="text" id="name" v-model="name" class="form-control" placeholder="text">
          <label for="name" style="color: #606060; background-color: none;">이름을 입력해주세요</label>
        </div>
        <br>
        <div class="form-floating col-md">
          <input type="text" id="nickname" v-model="nickname" class="form-control" placeholder="text">
          <label for="nickname" style="color: #606060; background-color: none;">닉네임을 입력해주세요</label>
        </div>
      </div>

      <input type="submit" value="SignUp" class="btn purple form-control mt-4 mb-4" style="height: 50px;">
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

<style scoped>
.purple {
  color: white;
  background-color: #6B71F2;
}

a {
  color: #6B71F2;
  font-weight: 800;
}
</style>