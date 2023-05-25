<template>
  <div class="text-start container">
    <div class="ms-5">
      <h4 class="fw-bolder">게시글 목록</h4>
      <p>총 게시글: {{posts.length}}개</p>
    </div>
    <ul class="list-group">
      <CommunityListItem v-for="post in posts" :key="post.id" :post="post"/>
    </ul>
  </div>
</template>

<script>
import CommunityListItem from '@/components/CommunityListItem.vue'

export default {
  name: 'CommunityList',
  components: {
    CommunityListItem,
  },
  computed: {
    posts() {
      return this.$store.state.posts.slice().reverse()
    }
  }
}
</script>

<style scoped>
.container {
  width: 1600px;
}
</style>