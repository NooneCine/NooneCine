<template>
  <div>
    <CommunityListItem v-for="post in posts" :key="post.id" :post="post"/>
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
      return this.$store.state.posts
    }
  }
}
</script>

<style>

</style>