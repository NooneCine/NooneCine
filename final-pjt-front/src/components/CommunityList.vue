<template>
  <div>
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

<style>

</style>