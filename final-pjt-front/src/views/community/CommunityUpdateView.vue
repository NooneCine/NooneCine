<template>
  <div>
    <h2 class="mt-5">
      <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" fill="currentColor" class="bi bi-eraser-fill ms-4 mt-3" viewBox="0 0 16 16">
        <path d="M8.086 2.207a2 2 0 0 1 2.828 0l3.879 3.879a2 2 0 0 1 0 2.828l-5.5 5.5A2 2 0 0 1 7.879 15H5.12a2 2 0 0 1-1.414-.586l-2.5-2.5a2 2 0 0 1 0-2.828l6.879-6.879zm.66 11.34L3.453 8.254 1.914 9.793a1 1 0 0 0 0 1.414l2.5 2.5a1 1 0 0 0 .707.293H7.88a1 1 0 0 0 .707-.293l.16-.16z"/>
      </svg>
    </h2>
    <form @submit.prevent="updatePost" enctype="multipart/form-data" class="container">
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
      <input type="submit" id="submit-button" class="btn purple btn-lg rounded-pill mt-5" value="Update">
    </form>
  </div>
</template>

<script>

export default {
  name: 'CommunityUpdateView',
  data() {
    return {
      title: this.$store.state.post.title,
      content: this.$store.state.post.content,
      image: this.$store.state.post.image,
      selectedFileName: null
    }
  },
  mounted() {
    this.selectedFileName = this.$store.state.post.image ? this.$store.state.post.image.name : null;
  },
  methods: {
    updatePost() {
      const title = this.title
      const content = this.content
      const user = this.$store.state.user
      const id = this.$store.state.post.id
      let image = this.newImage || this.image

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
        title, content, user, image, id
      }

      this.$store.dispatch('updatePost', payload)
    },
    handleFileUpload(event) {
      this.image = event.target.files[0]
      this.selectedFileName = event.target.files[0] ? event.target.files[0].name : null
    },
  }
}
</script>

<style scoped>
.custom-textarea {
  height: 200px; /* 원하는 높이 값으로 설정 */
}
</style>