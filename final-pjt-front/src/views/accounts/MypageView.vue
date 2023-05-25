<template>
  <div class="profile">
    <div v-if="user" class="m-5 text-start">
      <div class="d-flex">
        <img v-if="user.profile_img" :src="getImageUrl(user.profile_img)" alt="Profile Image" class="profile-image rounded-circle">
        <img v-else src="@/assets/default.png" alt="Profile Image" class="profile-image rounded-circle">
        <div class="mx-5">
          <h3 class="mt-5"><b>{{ user.nickname }}</b>
            <router-link :to="{ name: 'MypageUpdateView', params: { id: user.id } }" class="white">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-eraser-fill ms-3" viewBox="0 0 16 16">
                <path d="M8.086 2.207a2 2 0 0 1 2.828 0l3.879 3.879a2 2 0 0 1 0 2.828l-5.5 5.5A2 2 0 0 1 7.879 15H5.12a2 2 0 0 1-1.414-.586l-2.5-2.5a2 2 0 0 1 0-2.828l6.879-6.879zm.66 11.34L3.453 8.254 1.914 9.793a1 1 0 0 0 0 1.414l2.5 2.5a1 1 0 0 0 .707.293H7.88a1 1 0 0 0 .707-.293l.16-.16z"/>
              </svg>
            </router-link>
          </h3>
          <p>{{ user.email }}</p>
        </div>
      </div>
      
      <div class="ms-3">
        <h4 class="mt-5 fw-bold">{{ user.nickname }}의 인생영화</h4>
        <div v-if="user?.favorite_movie === null">
          인생 영화를 등록해주세요!
          <router-link :to="{ name: 'MypageUpdateView', params: { id: user.id } }">
            등록하러 가기
          </router-link>
        </div>
        <div v-else-if="user?.favorite_movie === ''">
          인생 영화를 등록해주세요!
          <router-link :to="{ name: 'MypageUpdateView', params: { id: user.id } }">
            등록하러 가기
          </router-link>
        </div>
        <div v-else class="fs-4">{{ user.favorite_movie }}</div>
      </div>

      <div class="mt-5 ms-3">
        <h4 class="fw-bold">내 게시물</h4>

        <div class="mt-4 row">
          <MypagePostItem v-for="post in postList" :key="post.id" :post="post" class="col-sm-6 mb-3 mb-sm-0 ms-3"/>
        </div>
      </div>
      <!-- <p class="mt-5 ms-3">좋아하는 영화 : {{ movie?.likes }}</p>
      <p class="mt-5 ms-3">좋아하는 배우 : {{ movie?.actor }}</p>
      <p class="mt-5 ms-3">본 영화 : {{ movie?.watched }}</p>
      <p class="mt-5 ms-3">보고싶은 영화 : {{ movie?.noonecine }}</p> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MypagePostItem from '@/components/MypagePostItem.vue'

export default {
  name: 'MypageView',
  components: {
    MypagePostItem,
  },
  data() {
    return {
      user: this.$store.state.user,
      movie: null,
      postList: [],
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.fetchUser()
  },
  methods: {
    fetchUser() {
      if (!this.isLogin) {
        alert('로그인이 필요한 페이지입니다')
        this.$router.push({ name: 'LoginView' })
      }

      const API_URL = 'http://127.0.0.1:8000'
      const userPk = this.$store.state.user.id

      axios({
        method: 'get',
        url: `${API_URL}/api/v1/profile/${userPk}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then(() => {
        this.postList = this.user.posts
      })
      .catch((err) => {
        console.log(err)
      });
    },
    getImageUrl(filename) {
      return filename
    },
  },
}
</script>

<style>
.profile {
  margin-top: 100px;
  margin-left: 100px;
}

.white {
  color: white;
}

.profile-image {
  width: 150px;
}
</style>