<template>
  <div>
    <MovieList />
    <MovieList />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'MovieView',
  components: {
    MovieList,
  },
}
</script>

<style>
</style>