<template>
  <div>
    <h1 class="mt-5">CommunityCreateView</h1>
    <form @submit.prevent="createPost" enctype="multipart/form-data" class="container">
      <div class="form-floating mt-5">
        <input type="text" id="title" v-model.trim="title" class="form-control">
        <label for="title">제목</label>
      </div>
      <div class="form-floating mt-4">
        <textarea id="content" cols="30" rows="10" v-model="content" class="form-control custom-textarea"></textarea>
        <label for="content">내용</label>
      </div>
      <div>
        <input type="file" @change="handleFileUpload" ref="contentImage">
      </div>
      <!-- <div class="file-upload mt-5">
        <input type="file" @change="handleFileUpload" ref="contentImage" class="file-upload-input">
        <label for="contentImage" class="file-upload-button btn btn-warning">
          이미지 업로드
        </label>
        <span class="selected-file ms-3" v-if="selectedFileName">{{ selectedFileName }}</span>
      </div> -->
      <input type="submit" id="submit-button" class="btn btn-primary rounded-pill mt-5">
    </form>
  </div>
</template>

<script>

export default {
  name: 'CommunityCreateView',
  data() {
    return {
      title: null,
      content: null,
      image: null,
    }
  },
  methods: {
    createPost() {
      const title = this.title
      const content = this.content
      const user = this.$store.state.user
      let image = this.image

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content) {
        alert('내용 입력해주세요')
        return
      }

      if (!image) {
        image = null
      }

      const payload = {
        title, content, user, image
      }

      this.$store.dispatch('createPost', payload, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
      })
    },
    handleFileUpload(event) {
      this.image = event.target.files[0]
    },
  }
}
</script>

<style scoped>
.custom-textarea {
  height: 200px; /* 원하는 높이 값으로 설정 */
}
</style>
