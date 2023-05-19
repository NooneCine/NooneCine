<template>
  <div class="mt-5">
    <h2>검색</h2>
    <SearchBar class="container mt-5"/>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'

export default {
  name: 'SearchView',
  components: {
    SearchBar,
  },
}
</script>

<style>
.container {
  width: 60%;
  margin-top: 30px;
}
</style>