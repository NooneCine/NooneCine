<template>
  <div class="home-view">
    <h1 class="head">NꙬNE CINE</h1>
    <button v-if="!start" @click="startButton()" class="btn purple btn-lg rounded-pill">START</button>
    <p v-if="!start" class="mt-3 light">버튼을 눌러서 영화를 추천받아 보세요</p>
    <div v-if="!start" class="movie-list-right mt-3">
      <MovieListItem v-for="movie in recommendMovieList" :key="movie.id" :movie="movie" :poster="movie?.poster_path" class="poster-item poster-item-right" />
    </div>
    <div v-if="!start" class="movie-list-left">
      <MovieListItem v-for="movie in recommendMovieList.reverse()" :key="movie.id" :movie="movie" :poster="movie?.poster_path" class="poster-item poster-item-left" />
    </div>

    <div v-else>
      <div v-if="currentQuestionIndex < questions.length" class="mt-5 pt-3">
        <h3>{{ questions[currentQuestionIndex].question }}</h3>
        <p class="mt-5 light">마음이 이끄는 그림을 선택해주세요</p>
        <div v-for="answer in questions[currentQuestionIndex].answers" :key="answer.id" class="div">
          <img @click="selectAnswer(answer)" :class="{ 'shake-animation': shouldShake }" :src="requireImage(answer.image)" style="width: 200px; height: 200px;"/>
        </div>
      </div>
      <div v-else class="mt-5">
        <h3>Ꙭ {{ recommendedGenre }} 장르가 누네띠네? Ꙭ</h3>
        
        <div v-if="recommendMovieList" class="mt-4">
          <MovieListItem v-for="movie in randomMovieList" :key="movie.id" :movie="movie" :poster="movie?.poster_path" class="posters"/>
        </div>

        <div class="d-flex flex-column align-items-center">
          <button @click="getRandomMovie()" class="btn purple rounded-pill mt-4">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-clockwise" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M8 3a5 5 0 1 0 4.546 2.914.5.5 0 0 1 .908-.417A6 6 0 1 1 8 2v1z"/>
              <path d="M8 4.466V.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384L8.41 4.658A.25.25 0 0 1 8 4.466z"/>
            </svg><span class="ms-2">다른 영화 보기</span> 
          </button>
          <button @click="restart" class="btn restart rounded-pill mt-2">다시 선택하기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name: 'HomeView',
  components: {
    MovieListItem,
  },
  data() {
    return {
      isInitialLoad: true,
      start: false,
      recommendMovieList: [],
      randomMovieList: [],
    }
  },
  mounted() {
    this.recommendGetMovie()
  },
  computed: {
    currentQuestionIndex() {
      return this.$store.state.recommends.currentQuestionIndex
    },
    questions() {
      return this.$store.state.recommends.questions
    },
    recommendedGenre() {
      return this.$store.state.recommends.recommendedGenre
    },
    shouldShake() {
      return this.isInitialLoad
    },
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    selectAnswer(answer) {
      this.$store.dispatch('recommends/selectAnswer', answer)
      if (this.currentQuestionIndex === this.questions.length - 1) {
        this.recommendGetMovie()
      }
    },
    restart() {
      this.$store.dispatch('recommends/restart')
      location.reload()
    },
    startButton() {
      if (!this.isLogin) {
        alert('로그인이 필요한 페이지입니다')
        this.$router.push({ name: 'LoginView' })
      }
      this.start = true
    },
    recommendGetMovie() {
      this.$store.dispatch('recommends/recommendMovieList')
        .then(() => {
          this.recommendMovieList = this.$store.state.recommends.recommendMovieList 
          this.isInitialLoad = false
          this.getRandomMovie()
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getRandomMovie() {
      const shuffledList = this.$store.state.recommends.recommendMovieList.sort(() => 0.5 - Math.random())
      this.randomMovieList = shuffledList.slice(0, 5)
    },
    requireImage(path) {
      const url = require(`@/assets/${path}`)
      return url
    }
  },
  created() {
    this.$store.dispatch('recommends/startRecommendation')
  },
};
</script>

<style scoped>
.home-view {
  text-align: center;
  margin-top: 50px;
}

h1 {
  font-size: 56px;
  font-weight: 800;
}

.head {
  padding-top: 30px;
}

@keyframes blink {
  0% { opacity: 0.6; }
  50% { opacity: 0.1; }
  100% { opacity: 0.6; }
}

.light {
  animation: blink 3s infinite;
}

.shake-animation {
  animation-name: shake;
  animation-duration: 1s;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
  display: inline-block;
}

@keyframes shake {
  0% {
    transform: translateY(-5px);
  }
  50% {
    transform: translateY(5px);
  }
  100% {
    transform: translateY(-5px);
  }
}

.div {
  display: inline-block;
  margin: 50px 30px;
  padding: 20px;
}

image {
  width: 200px;
}

.purple {
  background-color: #6B71F2;
  color: #eaedf0;
}

.restart {
  background-color: none;
  color: #eaedf0;
}

.movie-list-right,
.movie-list-left {
  display: flex;
  overflow: hidden;
}

.poster-item-left {
  animation: slideLeft 10s linear infinite;
}

.poster-item-right {
  animation: slideRight 10s linear infinite;
}

@keyframes slideLeft {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(-100%);
  }
}

@keyframes slideRight {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(100%);
  }
}
</style>