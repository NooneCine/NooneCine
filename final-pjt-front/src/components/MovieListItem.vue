<template>
  <div class="col">
    <img :src="`https://image.tmdb.org/t/p/original${poster}`" class="poster m-2 rounded">
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
