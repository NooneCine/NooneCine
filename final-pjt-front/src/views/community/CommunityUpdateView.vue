<template>
  <div>
    <h2 class="mt-5">게시글 수정하기</h2>
    <form @submit.prevent="updatePost" enctype="multipart/form-data" class="container">
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
        <!-- 현재 이미지 표시 -->
        <span v-if="selectedFileName">{{ selectedFileName }}</span>
      </div>
      <input type="submit" id="submit-button" class="btn btn-primary rounded-pill mt-5">
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