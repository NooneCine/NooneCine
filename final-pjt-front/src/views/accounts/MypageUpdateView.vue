<template>
  <div>
    <h2 class="mt-5">
      <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" fill="currentColor" class="bi bi-eraser-fil" viewBox="0 0 16 16">
        <path d="M8.086 2.207a2 2 0 0 1 2.828 0l3.879 3.879a2 2 0 0 1 0 2.828l-5.5 5.5A2 2 0 0 1 7.879 15H5.12a2 2 0 0 1-1.414-.586l-2.5-2.5a2 2 0 0 1 0-2.828l6.879-6.879zm.66 11.34L3.453 8.254 1.914 9.793a1 1 0 0 0 0 1.414l2.5 2.5a1 1 0 0 0 .707.293H7.88a1 1 0 0 0 .707-.293l.16-.16z"/>
      </svg>
    </h2>
    <p class="mt-3">프로필 수정</p>
    <form @submit.prevent="updateProfile" enctype="multipart/form-data" class="container">
      <div class="d-flex justify-content-around">
        <label for="profile-img">
          <div>
            <img v-if="user.profile_img" :src="user.profile_img" alt="Profile Image" class="profile-image rounded-circle">
            <img v-else src="@/assets/default.png" alt="Profile Image" class="profile-image mb-3">
            <input type="file" id="profile-img" @change="onProfileImageChange" accept="image/*" class="hidden-input">
            <p>프로필 사진 수정</p>
          </div>
        </label>

        <div class="text-start white">
          <h4 class="fw-bold">{{ user.name }}</h4>
          <div>{{ user.email }}</div>
          <div>
            닉네임:
            <input type="text" id="nickname" v-model.trim="user.nickname" class="form-control" placeholder="">
            <label for="nickname"></label>
          </div>
          <div>
            인생영화:
            <input type="text" id="favorite_movie" v-model.trim="user.favorite_movie" class="form-control" placeholder="">
            <label for="favorite_movie"></label>
          </div>
        </div>

      </div>
      <button type="submit" class="btn purple btn-lg rounded-pill mt-5">저장</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityUpdateView',
  data() {
    return {
      user: {
        email: this.$store.state.user.email,
        name: this.$store.state.user.name,
        profile_img: this.$store.state.user.profile_img,
        nickname: this.$store.state.user.nickname,
        favorite_movie: this.$store.state.user.favorite_movie
      },
      imageFile: null
    }
  },
  methods: {
    onProfileImageChange(event) {
      this.imageFile = event.target.files[0];
      if (this.imageFile) {
        const reader = new FileReader()
        reader.onload = (e) => {
          this.user.profile_img = e.target.result
        };
        reader.readAsDataURL(this.imageFile)
      }
    },
    updateProfile() {
      const formData = new FormData()

      if(this.imageFile) {
        formData.append('profile_img', this.imageFile)
      }
      formData.append('nickname', this.user.nickname)
      formData.append('favorite_movie', this.user.favorite_movie)

      const userPk = this.$store.state.user.id

      axios({
        method: 'patch',
        url: `${API_URL}/api/v1/profile/${userPk}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: formData
      })
      .then(res => {
        const updatedUser = {
          ...res.data,
          nickname: this.user.nickname,
          favorite_movie: this.user.favorite_movie
        }

        // const isNicknameTaken = this.isNicknameTaken(updatedUser.nickname)
        // if (isNicknameTaken) {
        //   alert('이미 사용 중인 닉네임입니다.')
        //   return
        // }
        
        this.$store.dispatch('updateProfile', updatedUser)
        this.$router.push({ name: 'MypageView' })
      })
      .catch(err => {
        console.error('업데이트 실패:', err)
      })
    },
  }
}
</script>
<style scoped>
.container {
  margin-top: 100px;
}

p {
  opacity: 0.6;
}

.custom-textarea {
  height: 200px; /* 원하는 높이 값으로 설정 */
}
.hidden-input {
  display: none;
}
.profile-image {
  width: 200px;
  height: 200px;
  border-radius: 50%;
}

</style>