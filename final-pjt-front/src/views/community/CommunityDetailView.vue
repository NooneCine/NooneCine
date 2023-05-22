<template>
  <div>
    <h1>CommunityDetailView</h1>
    <div v-if="post">
      <h5>{{ post.title }}</h5>
      <p>{{ post.user_nickname }}</p>
      <h5>{{ post.content }}</h5>
      <img :src="post.image" alt="Post Image" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'CommunityDetailView',
  data() {
    return {
      post: this.$store.state.post,
    }
  },
  created() {
    this.getPostDetail(this.$route.params.id)
  },
  methods: {
    getPostDetail(postId) {
      this.$store.dispatch('getPostDetail', postId)
    }
  }
}
</script>

<style>

</style>