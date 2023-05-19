<template>
  <div class="container mt-4">
    <div class="d-flex flex-column justify-content-center">
      <h5 class="text-start"><b>{{ msg }}</b></h5>
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

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
    HorizontalScroll,
  },
  data() {
    return {
      movies: [],
      msg: [],
    }
  },
  methods: {
    async axiosRequest() {
      const arr = ['top_rated', 'now_playing', 'popular']
      const msgList = ['명작만 모아모아! 탑 랭크된 영화 20', '트렌디한 당신에게 선보이는 현재 상영작', '나 빼고 다 본 영화, TOP 20']
      for (let i=0; i < arr.length; i++) {
        console.log(i)
        try {
          this.getMovieList(arr[i])
          this.msg = msgList[i]
        } catch (err) {
          console.log(err)
        }
      }
    },
    getMovieList(num) {
      return new Promise(() => {
        axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${num}?api_key=${API_KEY}&language=ko-KR&page=1`,
        })
        .then((res) => {
          this.movies = res.data.results
          console.log(num)
        })
        .catch((err) => {
          console.log(err)
        })
      })
    }
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