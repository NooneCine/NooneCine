<template>
  <div>
    <div class="d-flex list-group list-group-flush">
      <div class="list-group-item container d-flex justify-content-between align-items-center ps-1 pe-2">
        <p>번호</p>
        <p>제목</p>
        <p>닉네임</p>
      </div>
      <CommunityListItem v-for="post in posts" :key="post.id" :post="post"/>
    </div>
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

<style>

</style>