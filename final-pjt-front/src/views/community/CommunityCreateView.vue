<template>
  <div>
    <h2 class="mt-5">
      <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" fill="currentColor" class="bi bi-pen" viewBox="0 0 16 16">
      <path d="m13.498.795.149-.149a1.207 1.207 0 1 1 1.707 1.708l-.149.148a1.5 1.5 0 0 1-.059 2.059L4.854 14.854a.5.5 0 0 1-.233.131l-4 1a.5.5 0 0 1-.606-.606l1-4a.5.5 0 0 1 .131-.232l9.642-9.642a.5.5 0 0 0-.642.056L6.854 4.854a.5.5 0 1 1-.708-.708L9.44.854A1.5 1.5 0 0 1 11.5.796a1.5 1.5 0 0 1 1.998-.001zm-.644.766a.5.5 0 0 0-.707 0L1.95 11.756l-.764 3.057 3.057-.764L14.44 3.854a.5.5 0 0 0 0-.708l-1.585-1.585z"/>
    </svg>
    </h2>
    <form @submit.prevent="createPost" enctype="multipart/form-data" class="container">
      <div class="form-floating mt-5">
        <input type="text" id="title" v-model.trim="title" class="form-control">
        <label for="title">제목</label>
      </div>
      <div class="form-floating mt-4">
        <textarea id="content" cols="30" rows="10" v-model="content" class="form-control custom-textarea"></textarea>
        <label for="content">내용</label>
      </div>
      <div class="mt-4">
        <input type="file" @change="handleFileUpload" ref="contentImage">
      </div>
      <!-- <div class="file-upload mt-5">
        <input type="file" @change="handleFileUpload" ref="contentImage" class="file-upload-input">
        <label for="contentImage" class="file-upload-button btn btn-warning">
          이미지 업로드
        </label>
        <span class="selected-file ms-3" v-if="selectedFileName">{{ selectedFileName }}</span>
      </div> -->
      <input type="submit" id="submit-button" class="btn purple btn-lg rounded-pill mt-5" value="Create">
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
