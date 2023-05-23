<template>
  <div>
    <table class="container">
      <thead>
        <div class="d-flex justify-content-between border-bottom">
          <th scope="col">No.</th>
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
          <th scope="col">첨부파일</th>
        </div>
      </thead>
      <CommunityListItem v-for="post in posts" :key="post.id" :post="post"/>
    </table>
      <!-- <CommunityListItem v-for="post in posts" :key="post.id" :post="post"/> -->
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