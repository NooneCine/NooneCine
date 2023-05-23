<template>
  <div>
    <router-link :to="{ name: 'CommunityDetailView', params: { id: post.id } }">
    <div class="btn border rounded-pill detail-pill d-flex flex-row justify-content-between">
      <img :src="getImageUrl(post?.image)" class="rounded-circle img-thumb m-1"/>
      <div class="text-start text-pill mt-4 ms-3 me-4">
        <h5 class="mt-2"><b>{{ post?.title }}</b></h5>
        <p class="nickname mt-3">{{ post?.user_nickname }}</p>
      </div>
    </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'CommunityChipsItem',
  props: {
    post: Object,
  },
  methods: {
    getImageUrl(filename) {
      return 'http://127.0.0.1:8000' + filename;
    },
  }
}
</script>

<style scoped>
.detail-pill {
  display: inline-block;
  clear: both;
}

.img-thumb {
  width: 100px;
  height: 100px;
}

.nickname {
  font-size: 0.75rem;
}
</style>