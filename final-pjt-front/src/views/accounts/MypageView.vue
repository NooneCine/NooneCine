<template>
  <div class="profile">
    <div v-if="user" class="m-5 text-start">
      <img v-if="user.profile_img" :src="getImageUrl(user.profile_img)" alt="Profile Image">
      <img v-else src="@/assets/default.png" alt="Profile Image">
      <h5 class="mt-5 ms-3"><b>{{ user.nickname }}</b></h5>

      <p class="ms-3">{{ user.email }}</p>
      <p class="mt-5 ms-3">인생 영화 : {{ user?.favorite_movie }}</p>
      <p class="mt-5 ms-3">내 게시물 : {{ user?.favorite_movie }}</p>
      <p class="mt-5 ms-3">좋아하는 영화 : {{ movie?.likes }}</p>
      <p class="mt-5 ms-3">좋아하는 배우 : {{ movie?.actor }}</p>
      <p class="mt-5 ms-3">본 영화 : {{ movie?.watched }}</p>
      <p class="mt-5 ms-3">보고싶은 영화 : {{ movie?.noonecine }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MypageView',
  data() {
    return {
      user: null,
      movie: null,
    }
  },
  created() {
    this.fetchUser()
  },
  methods: {
    fetchUser() {
      const API_URL = 'http://127.0.0.1:8000'

      axios({
        method: 'get',
        url: `${API_URL}/api/v1/profile/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        this.user = res.data
      })
      .catch((err) => {
        console.log(err)
      });
    },
    getImageUrl(filename) {
      return 'http://127.0.0.1:8000' + filename
    },
  },
}
</script>

<style>
.profile {
  margin-top: 100px;
  margin-left: 100px;
}
</style>