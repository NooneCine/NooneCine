<template>
  <div class="container mt-4">
    <div class="d-flex flex-column justify-content-center">
      <h5 class="text-start"><b>나 빼고 다 본 영화, TOP 20</b></h5>
      <horizontal-scroll class="bar mt-3">
        <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie" :poster="movie.poster_path" class="posters"/>
      </horizontal-scroll>
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'
import axios from 'axios'
import HorizontalScroll from 'vue-horizontal-scroll'
import 'vue-horizontal-scroll/dist/vue-horizontal-scroll.css'

const API_KEY = '75e6eeb5f868a25d86953e24abf22120'
const API_URL = `https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}&language=ko-KR&page=1`


export default {
  name: 'MovieList',
  components: {
    MovieListItem,
    HorizontalScroll,
  },
  data() {
    return {
      movies: [],
    }
  },
  methods: {
    getMovieList() {
      axios({
        method: 'get',
        url: API_URL
      })
      .then((res) => {
        this.movies = res.data.results
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created() {
    this.getMovieList()
  }

}
</script>

<style>
.posters {
  display: inline-block;
}

.bar::-webkit-scrollbar {
  display: none;
}

.poster {
  height: 240px;
}
</style>