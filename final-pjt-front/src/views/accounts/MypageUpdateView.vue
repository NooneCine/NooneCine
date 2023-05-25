<template>
  <div>
    <h2 class="mt-5">프로필 수정하기</h2>
    <form @submit.prevent="updateProfile" enctype="multipart/form-data" class="container">
      <div class="d-flex justify-content-around">
        <label for="profile-img">
          <div class="profile-image-container">
            <img v-if="user.profile_img" :src="user.profile_img" alt="Profile Image" class="profile-image">
            <img v-else src="@/assets/default.png" alt="Profile Image" class="profile-image">
            <input type="file" id="profile-img" @change="onProfileImageChange" accept="image/*" class="hidden-input">
          </div>
        </label>

        <div class="text-start">
          <div>이메일: {{ user.email }}</div>
          <div>이름: {{ user.name }}</div>
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
      <button type="submit" class="btn btn-primary rounded-pill mt-5">저장</button>
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
        
        this.$store.dispatch('updateProfile', updatedUser)
        this.$router.push({ name: 'MypageView' })
      })
      .catch(err => {
        console.log(err)
        alert('이미 사용 중인 닉네임입니다.')
        return
      })
    },
  }
}
</script>
<style scoped>
.custom-textarea {
  height: 200px; /* 원하는 높이 값으로 설정 */
}
.hidden-input {
  display: none;
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