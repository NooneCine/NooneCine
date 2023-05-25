<template>
  <div>
    <CommunityChips class="mt-5 mx-5"/>
    <router-link to="/community/create" class="btn btn-lg purple m-4 rounded-pill">CREATE</router-link>
    <CommunityList class="mt-5"/>
  </div>
</template>

<script>
import CommunityList from '@/components/CommunityList.vue'
import CommunityChips from '@/views/community/CommunityChips.vue'

export default {
  name: 'CommunityView',
  components: {
    CommunityList,
    CommunityChips,
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

<style scoped>
.purple {
  background-color: #6B71F2;
  color: #eaedf0;
}
</style>