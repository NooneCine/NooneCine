<template>
  <div>
    <router-link :to="{ name: 'CommunityDetailView', params: { id: post.id } }" class="d-flex justify-content-between align-items-center m-3">
      <td class="row">{{ post.id }}</td>
      <th>{{ post.title }}</th>
      <td>{{ post.user_nickname }}</td>
      <td>{{ post.image? 0 : 'X' }}</td>
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

<style scoped>
a {
  margin: 0;
  color: black;
}
</style>