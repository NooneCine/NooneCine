<template>
  <div class="profile">
    <div v-if="post.user" class="m-5 text-start">
      <img v-if="post.user.profile_img" :src="getImageUrl(post.user.profile_img)" alt="Profile Image">
      <img v-else src="@/assets/default.png" alt="Profile Image">
      <h5 class="mt-5 ms-3"><b>{{ post.user_nickname }}</b></h5>

      <div class="ms-3">
        <h4 class="mt-5 fw-bold">{{ post.user_nickname }}의 인생영화</h4>
        <p v-if="post.user?.favorite_movie" class="mt-5">{{ post.user?.favorite_movie }}</p>
        <p v-else class="mt-3">인생 영화가 아직 없습니다.</p>
        <!-- <p v-if="post.user?.favorite_movie === null">
          아직 인생 영화가 없어요ㅠ
        </p>
        <p v-else-if="post.user?.favorite_movie === ''">
          아직 인생 영화가 없어요ㅠ
        </p>
        <p v-else class="fs-4">{{ post.user?.favorite_movie }}</p> -->
      </div>

      <div class="mt-5 ms-3">
        <h4 class="fw-bold">{{ post.user_nickname }}의 게시물</h4>

        <div class="mt-4 row">
          <UserpagePostItem v-for="post in postList" :key="post.id" :post="post" class="col-sm-6 mb-3 mb-sm-0 ms-3"/>
        </div>
      </div>
<!-- 
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
        </span> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import UserpagePostItem from '@/components/UserpagePostItem.vue'

export default {
  name: 'UserPageView',
  components: {
    UserpagePostItem,
  },
  data() {
    return {
      movie: null,
      post: this.$store.state.post,
      user: null,
      postList: [],
    }
  },
  created() {
    this.fetchUser(),
    this.getPostUser()
  },
  methods: {
    fetchUser() {
      const API_URL = 'http://127.0.0.1:8000'
      const userPk = this.$store.state.post.user

      axios({
        method: 'get',
        url: `${API_URL}/api/v1/profile/${ userPk }/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        this.user = res.data
        this.postList = this.user.posts
        console.log(this.postList)
      })
      .catch((err) => {
        console.log(err)
      });
    },
    // getImageUrl(filename) {
    //   return 'http://127.0.0.1:8000' + filename
    // },
    // getPostUser() {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/api/v1/accounts/${ userPk }/`,
    //     headers: {
    //       Authorization: `Token ${this.$store.state.token}`
    //     }
    //   })
    //   .then((res) => {
    //     this.$store.commit('SET_POST', res.data)
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // }
  },
}
</script>

<style scoped>
.profile {
  margin-top: 100px;
  margin-left: 100px;
}
.overflow-text {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical; 
  overflow: hidden;
}
</style>