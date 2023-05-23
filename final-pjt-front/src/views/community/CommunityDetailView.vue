<template>
  <div>
    <h1>CommunityDetailView</h1>
    <div v-if="post">
      <h5>{{ post?.title }}</h5>
      <p>{{ post?.user_nickname }}</p>
      <h5>{{ post?.content }}</h5>
      <img :src="getImageUrl(post?.image)" alt="Post Image" width="50%"/>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'CommunityDetailView',
  data() {
    return {
      post: this.$store.state.post,
    }
  },
  methods: {
    getImageUrl(filename) {
      return 'http://127.0.0.1:8000' + filename;
    },
  },
}
</script>

<style>

</style>