<template>
  <div class="col">
    <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
      <img :src="`https://image.tmdb.org/t/p/original${poster}`" class="poster m-2 rounded">
    </router-link>
  </div>

</template>

<script>
export default {
  name: 'MovieListItem',
  data() {
    return {
      posterImage: null, 
    }
  },
  props: {
    movie: Object,
    poster: String,
  },
}
</script>

<style>
.poster {
  height: 240px;
}
</style>
