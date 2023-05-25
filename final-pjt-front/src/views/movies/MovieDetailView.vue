<template>
  <div>
    <router-link :to="{ name: 'MovieView' }" class="mt-5 list yellow">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-arrow-left-square-fill" viewBox="0 0 16 16">
        <path d="M16 14a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12zm-4.5-6.5H5.707l2.147-2.146a.5.5 0 1 0-.708-.708l-3 3a.5.5 0 0 0 0 .708l3 3a.5.5 0 0 0 .708-.708L5.707 8.5H11.5a.5.5 0 0 0 0-1z"/>
      </svg> <p class="ms-2">목록으로</p>
    </router-link>

    <div v-if="trailers" id="player">
      <div class="youtube-video-wrapper">
        <iframe :src="`https://www.youtube.com/embed/${trailer.key}`" frameborder="0" class="youtube-video"></iframe>
      </div>
    </div>

    <div class="container">
      <div class="d-flex align-items-center mt-3">
        <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" class="img-fluid img-thumbnail m-5" width="30%" height="auto"/>
        <div class="text-start">
          <h2 v-if="movie.title" class="fw-bold my-3 mt-5">{{ movie.title }}</h2>
          <h2 v-else class="fw-bold my-3 mt-5">{{ movie.original_title
 }}</h2>
          <div class="mt-1">개봉일: {{ movie.release_date ? movie.release_date : '정보없음' }}</div>
          <div class="mt-1">상영시간: {{ movie.runtime ? movie.runtime + ' 분' : '정보없음' }}</div>
          <div class="mt-1">평점: {{ movie.vote_average ? movie.vote_average + '점' : '정보없음' }}</div>

          <div class="text-start mt-5">
            <p>줄거리</p>
            {{ movie.overview ? movie.overview : '정보없음' }}
          </div>
          <div></div>
            
        </div>
      </div>
      
      <router-link :to="{ name: 'MovieView' }" class="mt-3 mb-5 list yellow">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-arrow-left-square-fill" viewBox="0 0 16 16">
          <path d="M16 14a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12zm-4.5-6.5H5.707l2.147-2.146a.5.5 0 1 0-.708-.708l-3 3a.5.5 0 0 0 0 .708l3 3a.5.5 0 0 0 .708-.708L5.707 8.5H11.5a.5.5 0 0 0 0-1z"/>
        </svg> <p class="ms-2">목록으로</p>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_KEY = '75e6eeb5f868a25d86953e24abf22120'
// const movieId = this.$route.params.id


export default {
  name: 'MovieDetailView',
  data() {
    return {
      movie: {},
      trailers: [],
      trailer: {}
    }
  },
  created() {
    const movieId = this.$route.params.id

    axios.get(`https://api.themoviedb.org/3/movie/${movieId}?api_key=${API_KEY}&language=ko-KR`)
      .then(res => {
        this.movie = res.data
        console.log(this.movie)
        this.getTrailers(movieId)
      })
      .catch(err => {
        console.error(err)
      });
  },
  methods: {
    getTrailers(movieId) {
      axios.get(`https://api.themoviedb.org/3/movie/${movieId}/videos?api_key=${API_KEY}`)
        .then(res => {
          this.trailers = res.data.results.filter(trailer => trailer.type === 'Trailer')
          this.trailer = this.trailers[-1]
        })
        .catch(err => {
          console.error(err)
        })
    },
  },
}
</script>

<style scoped>
.list {
  color: rgb(158, 95, 253);
  text-align: left;
  display: flex;
  margin-left: 50px;
  margin-right: 30px;
  font-weight: bold;
}

.container {
  width: 80%;
}

#player {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.youtube-video-wrapper {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 비율의 경우 */
  height: 0;
  overflow: hidden;
}

.youtube-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.yellow {
  color: #F2D06B;
}
</style>
