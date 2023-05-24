<template>
  <div>
    <h1>MovieDetailView</h1>
    <p>영화 제목: {{movie.title}}</p>
    <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" class="poster m-2">
  </div>
</template>

<script>
import axios from 'axios'
const API_KEY = '75e6eeb5f868a25d86953e24abf22120'

export default {
  name: 'MovieDetailView',
  data() {
    return {
      movie: {}
    }
  },
  created() {
    const movieId = this.$route.params.id

    axios.get(`https://api.themoviedb.org/3/movie/${movieId}?api_key=${API_KEY}`)
      .then(res => {
        this.movie = res.data
      })
      .catch(err => {
        console.error(err)
      });
  }
}
</script>

<style>

</style>