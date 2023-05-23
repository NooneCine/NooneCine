<template>
  <div class="d-flex list-group list-group-flush">
    <router-link :to="{ name: 'CommunityDetailView', params: { id: post.id } }" class="list-group-item container d-flex justify-content-between align-items-center">
      <span>{{ post.id }}</span>
      <span>{{ post.title }}</span>
      <span>{{ post.user_nickname }}</span>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'CommunityListItem',
  props: {
    post: Object,
  },
}
</script>

<style>

</style>