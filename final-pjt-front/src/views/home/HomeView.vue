<template>
  <div class="home-view">
    <h1 class="head">널 위한 영화를 추천해줄게</h1>
    <button v-if="!start" @click="startButton()" class="btn btn-primary btn-lg rounded-pill mt-5">START</button>

    <div v-else>
      <div v-if="currentQuestionIndex < questions.length" class="mt-5 pt-3">
        <h3>{{ questions[currentQuestionIndex].question }}</h3>
        <div v-for="answer in questions[currentQuestionIndex].answers" :key="answer.id" class="div">
          <button @click="selectAnswer(answer)" :class="{ 'shake-animation': shouldShake }" class="btn">{{ answer.label }}</button>
        </div>
      </div>
      <div v-else>
        <h3>추천 장르 : {{ recommendedGenre }}</h3>
        <button @click="getRandomMovie()" class="btn btn-primary rounded-pill">다른 영화 보기</button>
        <div v-if="recommendMovieList">
          <MovieListItem v-for="movie in randomMovieList" :key="movie.id" :movie="movie" :poster="movie?.poster_path" class="posters"/>
        </div>

        <button @click="restart" class="btn btn-primary rounded-pill">Restart</button>
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
    this.recommendGetMovie();
  },
  computed: {
    currentQuestionIndex() {
      return this.$store.state.genre.currentQuestionIndex
    },
    questions() {
      return this.$store.state.genre.questions
    },
    recommendedGenre() {
      return this.$store.state.genre.recommendedGenre
    },
    shouldShake() {
      return this.isInitialLoad
    },
  },
  methods: {
    selectAnswer(answer) {
      this.$store.dispatch('genre/selectAnswer', answer)
      if (this.currentQuestionIndex === this.questions.length - 1) {
        this.recommendGetMovie()
      }
    },
    restart() {
      this.$store.dispatch('genre/restart')
      location.reload()
    },
    startButton() {
      this.start = true
    },
    recommendGetMovie() {
      this.$store.dispatch('genre/recommendMovieList')
        .then(() => {
          this.recommendMovieList = this.$store.state.genre.recommendMovieList 
          this.isInitialLoad = false
          this.getRandomMovie()
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getRandomMovie() {
      const shuffledList = this.$store.state.genre.recommendMovieList.sort(() => 0.5 - Math.random())
      this.randomMovieList = shuffledList.slice(0, 5)
    },
  },
  created() {
    // Initialize the genre recommendation process
    this.$store.dispatch('genre/startRecommendation')
  },
};
</script>

<style scoped>
.home-view {
  text-align: center;
  margin-top: 50px;
}

.head {
  padding-top: 50px;
}

.shake-animation {
  animation-name: shake;
  animation-duration: 1s;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
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
</style>
