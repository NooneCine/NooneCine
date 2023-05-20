<template>
  <div>
    <h1>SignUpView</h1>
    <form @submit.prevent="signUp">
      <label for="email">email : </label>
      <input type="email" id="email" v-model="email"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <label for="name"> name : </label>
      <input type="text" id="name" v-model="name">

      <label for="nickname"> nickname : </label>
      <input type="text" id="nickname" v-model="nickname">
      
      <input type="submit" value="SignUp">
    </form>
    
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