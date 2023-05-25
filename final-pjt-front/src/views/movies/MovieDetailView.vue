<template>
  <div>
    <!-- <h1>MovieDetailView</h1>
    <p>영화 제목: {{movie.title}}</p>
    <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" class="poster m-2"> -->
    <router-link :to="{ name: 'MovieView' }" class="mt-5 list yellow">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-arrow-left-square-fill" viewBox="0 0 16 16">
        <path d="M16 14a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12zm-4.5-6.5H5.707l2.147-2.146a.5.5 0 1 0-.708-.708l-3 3a.5.5 0 0 0 0 .708l3 3a.5.5 0 0 0 .708-.708L5.707 8.5H11.5a.5.5 0 0 0 0-1z"/>
      </svg> <p class="ms-2">목록으로</p>
    </router-link>

    <div v-if="selectedVideo" id="player">
      <div class="youtube-video-wrapper">
        <iframe :src="'https://www.youtube.com/embed/' + selectedVideo" frameborder="0" class="youtube-video"></iframe>
      </div>
    </div>

    <div class="container">
      <div class="d-flex align-items-center mt-3">
        <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" class="img-fluid img-thumbnail m-5" width="30%" height="auto"/>
        <div class="text-start">
          <!-- <div> 좋아요를 시도한 흔적
            <button @click="likeMovie" class="like btn ps-0 mb-4">
              <svg v-if="liked" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="rgb(158, 95, 253)" class="bi bi-heart-fill" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
              </svg>
              <svg v-else xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
              </svg>
            </button>
          </div> -->
          <h2 class="fw-bold my-3 mt-5">{{ movie.title }}</h2>
          <div>상영시간: {{movie.runtime}}분</div>
          <div>개봉일: {{movie.release_date}}</div>
          <div class="text-start mt-5">
            <p>줄거리</p>
            {{movie.overview}}
          </div>
          <div></div>
            
        </div>
      </div>
      
      <router-link :to="{ name: 'MovieView' }" class="mt-3 mb-5 list yellow">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-arrow-left-square-fill" viewBox="0 0 16 16">
          <path d="M16 14a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12zm-4.5-6.5H5.707l2.147-2.146a.5.5 0 1 0-.708-.708l-3 3a.5.5 0 0 0 0 .708l3 3a.5.5 0 0 0 .708-.708L5.707 8.5H11.5a.5.5 0 0 0 0-1z"/>
        </svg> <p class="ms-2">목록으로</p>
      </router-link>
      <!-- <form @submit.prevent="submitReview">
        <div class="form-group">
          <label for="reviewInput">리뷰 작성</label>
          <textarea class="form-control" id="reviewInput" rows="3" v-model="reviewInput"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">리뷰 등록</button>
      </form> -->
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
      movieId: null,
      // liked: false,
      // user: this.$store.state.user,
      searchWord: '',
      selectedVideo: null,
      // reviewInput: '',
    }
  },
  created() {
    const movieId = this.$route.params.id

    axios.get(`https://api.themoviedb.org/3/movie/${movieId}?api_key=${API_KEY}&language=ko-KR`)
      .then(res => {
        this.movieId = movieId
        this.movie = res.data
        this.searchWord = `${res.data.title} 예고편`
        this.getVideo()
      })
      .catch(err => {
        console.error(err)
      });
  },
  methods: {
    getVideo() {
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      const YOUTUBE_API_KEY = 'AIzaSyB3d1bUU36kACyaxWhRn8XNNgMpkXbPJ8I'

      axios({
        method: 'get',
        url: API_URL,
        params: {
          key: YOUTUBE_API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.searchWord
        }
      })
      .then(response => {
        const responseData = response.data.items[0]
        this.selectedVideo = responseData.id.videoId
      })
      .catch((error) => {
        console.log(error)
      })
    },
    // submitReview() {   
    //   axios({
    //     method: 'post',
    //     url: `/movies/${ this.movieId }/reviews/`,
    //     headers: {
    //         Authorization: `Token ${this.$store.state.token}`
    //     },
    //     data: {
    //       movieId: this.movieId,
    //       content: this.reviewInput,
    //     }
    //     })
    //     .then(response => {
    //       // 성공적으로 저장되었을 때의 처리
    //       console.log(response)
    //       this.reviewInput = '' // 폼 초기화
    //     })
    //     .catch(error => {
    //       // 저장 실패 시의 처리
    //       console.log(this.movie.id)
    //       console.error('댓글 저장 중 오류가 발생했습니다:', error)
    //     })
    // },
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
