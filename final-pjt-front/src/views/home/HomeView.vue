<template>
  <div class="home-view">
    <h1>널 위한 영화를 추천해줄게</h1>
    <div v-if="currentQuestionIndex < questions.length" class="mt-5">
      <h3>{{ questions[currentQuestionIndex].question }}</h3>
      <div v-for="answer in questions[currentQuestionIndex].answers" :key="answer.id">
        <button @click="selectAnswer(answer)">{{ answer.label }}</button>
      </div>
    </div>
    <div v-else>
      <h3>추천 장르 : {{ recommendedGenre }}</h3>
      <button @click="restart">Restart</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  computed: {
    currentQuestionIndex() {
      return this.$store.state.genre.currentQuestionIndex
    },
    questions() {
      return this.$store.state.genre.questions
    },
    recommendedGenre() {
      return this.$store.state.genre.recommendedGenre
    }
  },
  methods: {
    selectAnswer(answer) {
      this.$store.dispatch('genre/selectAnswer', answer)
    },
    restart() {
      this.$store.dispatch('genre/restart')
      location.reload()
    }
  },
  created() {
    // Initialize the genre recommendation process
    this.$store.dispatch('genre/startRecommendation')
  }
};
</script>

<style scoped>
.home-view {
  text-align: center;
  margin-top: 50px;
}
</style>
