<template>
  <div>
    <CommunityChipsItem v-for="post in limitedPosts" :key="post.id" :post="post" class="chips"/>
  </div>
</template>

<script>
import CommunityChipsItem from '@/components/CommunityChipsItem.vue'

export default {
  name: 'CommunityChips',
  components: {
    CommunityChipsItem,
  },
  computed: {
    posts() {
      return this.$store.state.posts.slice().reverse()
    },
    limitedPosts() {
      if (window.innerWidth > 576) {
        return this.posts.slice(-6)
      } else {
        return this.posts.slice(-2)
      }
    }
  },
  created() {
    console.log(this.limitedPosts)
  }
}
</script>

<style scoped>
.chips {
  display: inline-block;
  margin: 12px;
}
</style>