<template>
  <div class="profile">
    <div v-if="user" class="m-5 text-start">
      <div class="d-flex">
        <div class="profile-image-container">
          <img v-if="user.profile_img" :src="getImageUrl(user.profile_img)" alt="Profile Image" class="profile-image">
          <img v-else src="@/assets/default.png" alt="Profile Image">
        </div>
        <div class="mx-5">
          <h5 class="mt-5"><b>{{ user.nickname }}</b></h5>
          <p>{{ user.email }}</p>
        </div>
        <router-link :to="{ name: 'MypageUpdateView', params: { id: user.id } }">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-eraser-fill ms-5" viewBox="0 0 16 16">
            <path d="M8.086 2.207a2 2 0 0 1 2.828 0l3.879 3.879a2 2 0 0 1 0 2.828l-5.5 5.5A2 2 0 0 1 7.879 15H5.12a2 2 0 0 1-1.414-.586l-2.5-2.5a2 2 0 0 1 0-2.828l6.879-6.879zm.66 11.34L3.453 8.254 1.914 9.793a1 1 0 0 0 0 1.414l2.5 2.5a1 1 0 0 0 .707.293H7.88a1 1 0 0 0 .707-.293l.16-.16z"/>
          </svg>
        </router-link>
      </div>
      

      <p class="mt-5 ms-3">인생 영화 : {{ user?.favorite_movie }}</p>
      <p class="mt-5 ms-3">내 게시물
        <span v-for="post in postList" :key="post.id">
          <div class="card" style="width: 18rem;">
            <router-link :to="{ name: 'CommunityDetailView', params: { id: post.id } }" class="mt-3">
              <div class="card-body">
                <h5 class="card-title">{{ post.title }}</h5>
                <p class="card-text overflow-text">{{post.comtent}}</p>
                <span>
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                    <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
                  </svg>
                  {{ post.likes_count }}
                </span>
                <span class="ms-2">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chat-square-dots" viewBox="0 0 16 16">
                    <path d="M14 1a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1h-2.5a2 2 0 0 0-1.6.8L8 14.333 6.1 11.8a2 2 0 0 0-1.6-.8H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2.5a1 1 0 0 1 .8.4l1.9 2.533a1 1 0 0 0 1.6 0l1.9-2.533a1 1 0 0 1 .8-.4H14a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
                    <path d="M5 6a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"/>
                  </svg>
                  {{ post.comment_count }}
                </span>
              </div>
            </router-link>
          </div>
        </span>
      </p>
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
      user: this.$store.state.user,
      movie: null,
      postList: [],
    }
  },
  created() {
    this.fetchUser()
  },
  methods: {
    fetchUser() {
      const API_URL = 'http://127.0.0.1:8000'
      const userPk = this.$store.state.user.id

      axios({
        method: 'get',
        url: `${API_URL}/api/v1/profile/${userPk}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        this.user = res.data
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
.profile-image-container {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  overflow: hidden;
}

.profile-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>