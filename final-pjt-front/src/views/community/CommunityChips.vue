<template>
  <div>
    <CommunityChipsItem v-for="post in posts" :key="post.id" :post="post" class="chips"/>
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
      return this.$store.state.posts
    },
    // limitedPosts() {
    //   if (window.innerWidth > 576) {
    //     return this.posts.slice(-6).reverse()
    //   } else {
    //     return this.posts.slice(-2).reverse()
    //   }
    // }
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