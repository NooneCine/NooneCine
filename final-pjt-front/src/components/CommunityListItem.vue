<template>
  <div class="d-flex">
    <router-link :to="{ name: 'CommunityDetailView', params: { id: post.id } }">
      <h5>{{ post.id }}</h5>
      <h5>{{ post.title }}</h5>
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