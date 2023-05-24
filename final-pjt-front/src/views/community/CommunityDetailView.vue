<template>
  <div>
    <h1>CommunityDetailView</h1>
    <div v-if="post">
      <h5>{{ post?.title }}</h5>
      <p>{{ post?.user_nickname }}</p>
      <h5>{{ post?.content }}</h5>
      <img :src="getImageUrl(post?.image)" alt="Post Image" width="50%"/>
    </div>
    <router-link :to="{ name: 'CommunityUpdateView', params: { id: post.id } }">수정</router-link><br>
    <button @click="deletePost" class="btn btn-danger">삭제</button><br>

    <router-link :to="{ name: 'CommunityView' }"> 목록으로 </router-link>
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
  methods: {
    getImageUrl(filename) {
      return 'http://127.0.0.1:8000' + filename;
    },
    deletePost() {
      this.$store.dispatch('deletePost', this.post.id)
    }
  },
}
</script>

<style>

</style>