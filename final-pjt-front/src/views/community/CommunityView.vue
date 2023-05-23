<template>
  <div>
    <CommunityChips class="mt-5"/>
    <router-link to="/community/create" class="btn btn-primary">CREATE</router-link>
    <CommunityList />
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

<style>

</style>