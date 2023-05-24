<template>
  <div>
    <router-link :to="{ name: 'MovieView' }" class="mt-5 list">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-arrow-left-square-fill" viewBox="0 0 16 16">
        <path d="M16 14a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12zm-4.5-6.5H5.707l2.147-2.146a.5.5 0 1 0-.708-.708l-3 3a.5.5 0 0 0 0 .708l3 3a.5.5 0 0 0 .708-.708L5.707 8.5H11.5a.5.5 0 0 0 0-1z"/>
      </svg> <p class="ms-2">목록으로</p>
    </router-link>

    <div v-if="selectedVideo" id="player">
      <iframe :src="'https://www.youtube.com/embed/' + selectedVideo" frameborder="0"></iframe>
    </div>

    <h2 class="fw-bold my-3">{{ movie.title }}</h2>
    <div class="container">
      <div class="d-flex align-items-center mt-5">
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
          <div>상영시간: {{movie.runtime}}분</div>
          <div>감독: {{movie.director}}</div>
          <div>출연: {{movie.actors}}</div>
          <div>개봉일: {{movie.release_date}}</div>
          <div></div>
            <!-- <div class="m-5">
              <span>이건 뭐야: {{movie.popularity}}</span>
              <span>관객수: {{movie.vote_count}}</span>
              <span>평점: {{movie.vote_average}}</span>
              <span>상영시간: {{movie.runtime}}</span>
              <span>감독: {{movie.director}}</span>
              <span>장르: {{movie.genres}}</span>
              <span>배우: {{movie.actors}}</span>
              <span>좋아요: {{movie.likes}}</span>
              <span>본 사람: {{movie.watched}}</span>
              <span>누네: {{movie.noonecine}}</span>
            </div> -->
        </div>
      </div>
      <div class="text-start">
        <p>줄거리</p>
        {{movie.overview}}
      </div>

      <div>
      <p>리뷰 목록</p>
      <p>총 리뷰: {{movie.review_count}}개</p>
      <div v-if="movie?.review_set">
        <p v-for="review in movie.review_set" :key="review.id">
          리뷰 내용: {{ review.content }}
          작성자: {{ review.user_nickname }}
          <button v-if="review.user === user.id" @click="deleteReview(review.id)" class="btn">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
              <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z"/>
            </svg>
          </button>
        </p>
      </div>
      <form @submit="createReview">
        <textarea v-model="reviewText" placeholder="리뷰를 입력하세요"></textarea>
        <button type="submit">리뷰 작성</button>
      </form>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_KEY = '75e6eeb5f868a25d86953e24abf22120'
const YOUTUBE_API_KEY = 'AIzaSyB3d1bUU36kACyaxWhRn8XNNgMpkXbPJ8I'
const movieId = this.$route.params.id


export default {
  name: 'MovieDetailView',
  data() {
    return {
      movie: {},
      // liked: false,
      // user: this.$store.state.user,
      searchWord: '',
      selectedVideo: null,
      reviewText: ''
    }
  },
  created() {
    axios.get(`https://api.themoviedb.org/3/movie/${movieId}?api_key=${API_KEY}&language=ko-KR`)
      .then(res => {
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
    createReview() {   
      const reviewText = this.reviewText

      if (!reviewText) {
        alert('내용 입력해주세요.')
        return
      }

      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${ movieId }/reviews/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          movie: movieId,
          content: this.reviewText,
          // 누네 스코어도 보내줘야 함
        }
      })
      .then((res) => {
        console.log(res)
        this.reviewText = ''
      })
      .catch((err) => {
        console.log(err)
      });
    },
    deleteReview(reviewId) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/reviews/${reviewId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        // console.log(this.post)
        window.location.reload()
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
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
</style>