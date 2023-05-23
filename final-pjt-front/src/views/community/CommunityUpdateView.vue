<template>
  <div>
    <h1>CommunityUpdateView</h1>
    <form @submit.prevent="updatePost()">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <div>
        <input type="file" @change="handleFileUpload" ref="contentImage">
      </div>
      <input type="submit" id="submit">
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
    }
  },
  methods: {
    updatePost() {
      const title = this.title
      const content = this.content
      const user = this.$store.state.user
      const id = this.$store.state.post.id
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
        title, content, user, image, id
      }

      this.$store.dispatch('updatePost', payload)
    },
    handleFileUpload(event) {
      this.image = event.target.files[0];
    },
  }
}
</script>

<style>

</style>