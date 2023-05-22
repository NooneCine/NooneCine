<template>
  <div>
    <h5>{{ post.id }}</h5>
    <h5>{{ post.title }}</h5>
  </div>
</template>

<script>
export default {
  name: 'CommunityListItem',
  props: {
    post: Object,
  }
}
</script>

<style>

</style>