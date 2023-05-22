<template>
  <div>
    <h1>CommunityView</h1>
    <CommunityList />
  </div>
</template>

<script>
import CommunityList from '@/components/CommunityList.vue'

export default {
  name: 'CommunityView',
  components: {
    CommunityList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getPosts()
  },
  methods: {
    getPosts() {
      if (this.isLogin) {
        this.$store.dispatch('getPosts')
      } else {
        alert('로그인이 필요한 페이지입니다')
        this.$router.push({ name: 'LoginView' })
      }
    }
  }
}
</script>

<style>

</style>