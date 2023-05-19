<template>
  <div class="container mt-5">
    <div class="d-flex flex-column justify-content-center mt-4">
      <h5 class="text-start ms-2"><b>{{ msg[0].top_rated }}</b></h5>
      <horizontal-scroll class="bar mt-1">
        <MovieListItem v-for="movie in top_rated" :key="movie.id" :movie="movie" :poster="movie.poster_path" class="posters"/>
      </horizontal-scroll>
    </div>
    <div class="d-flex flex-column justify-content-center mt-4">
      <h5 class="text-start ms-2"><b>{{ msg[1].now_playing }}</b></h5>
      <horizontal-scroll class="bar mt-1">
        <MovieListItem v-for="movie in now_playing" :key="movie.id" :movie="movie" :poster="movie.poster_path" class="posters"/>
      </horizontal-scroll>
    </div>
    <div class="d-flex flex-column justify-content-center mt-4">
      <h5 class="text-start ms-2"><b>{{ msg[2].popular }}</b></h5>
      <horizontal-scroll class="bar mt-1">
        <MovieListItem v-for="movie in popular" :key="movie.id" :movie="movie" :poster="movie.poster_path" class="posters"/>
      </horizontal-scroll>
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'
import HorizontalScroll from 'vue-horizontal-scroll'
import 'vue-horizontal-scroll/dist/vue-horizontal-scroll.css'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
    HorizontalScroll,
  },
  data() {
    return {
      top_rated: this.$store.state.top_rated,
      now_playing: this.$store.state.now_playing,
      popular: this.$store.state.popular,
      msg: [{'top_rated':'명작만 모아모아! 탑 랭크된 영화 20'}, {'now_playing': '트렌디한 당신에게 선보이는, 현재 상영작'}, {'popular': '나 빼고 다 본 영화, TOP 20'}],
    }
  },
  methods: {
    async axiosRequest() {
      const arr = ['top_rated', 'now_playing', 'popular']
      for (let i=0; i < arr.length; i++) {
        console.log(i)
        try {
          this.$store.dispatch('getMovieList', arr[i])
        } catch (err) {
          console.log(err)
        }
      }
    },
  },
  created() {
      this.axiosRequest()
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