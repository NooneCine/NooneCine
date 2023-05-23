<template>
  <div @click="getDetailPage(post.id)">
    <div class="card rounded-pill detail-pill d-flex flex-row justify-content-between">
      <img :src="getImageUrl(post.image)" class="rounded-circle img-thumb m-2"/>
      <div class="text-start text-pill mt-4 me-4">
        <h5 class="mt-2"><b>{{ post?.title }}</b></h5>
        <p class="nickname mt-3">{{ post.user_nickname }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CommunityChipsItem',
  data() {
    return {
      post: this.$store.state.post,
    }
  },
  created() {
    this.getPostDetail(this.$store.state.post.id)
  },
  methods: {
    getPostDetail(postId) {
      this.$store.dispatch('getPostDetail', postId)
      console.log(postId)
    },
    getImageUrl(filename) {
      return 'http://127.0.0.1:8000' + filename;
    },
    getDetailPage(id) {
      this.$router.push({ name: 'CommunityDetailView', params: { id: id } })
    },
  }
}
</script>

<style scoped>
.detail-pill {
  display: inline-block;
  clear: both;
  float: left;
}

.img-thumb {
  width: 100px;
  height: 100px;
}

.nickname {
  font-size: 0.75rem;
}
</style>