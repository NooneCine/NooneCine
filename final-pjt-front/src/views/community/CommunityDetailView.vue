<template>
  <div>
    <!-- <h1>CommunityDetailView</h1> -->
    <router-link :to="{ name: 'CommunityView' }" class="mt-5 list">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-arrow-left-square-fill" viewBox="0 0 16 16">
        <path d="M16 14a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12zm-4.5-6.5H5.707l2.147-2.146a.5.5 0 1 0-.708-.708l-3 3a.5.5 0 0 0 0 .708l3 3a.5.5 0 0 0 .708-.708L5.707 8.5H11.5a.5.5 0 0 0 0-1z"/>
      </svg> <p class="ms-2">목록으로</p>
    </router-link>

    <div v-if="post" class="d-flex m-5">
      <img v-if="post?.image" :src="getImageUrl(post?.image)" alt="Post Image" width="50%"/>
      <div class="m-5 text-start">
        <button @click="likePost" class="like btn ps-0 mb-4">
          <svg v-if="liked" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="rgb(158, 95, 253)" class="bi bi-heart-fill" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
          </svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
            <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
          </svg>
        </button>
        <div class="d-flex">
          <h5 class="fw-bold">제목 : {{ post?.title }}</h5>
          <router-link v-if="post?.user === user.id" :to="{ name: 'CommunityUpdateView', params: { id: post.id } }">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-eraser-fill ms-5" viewBox="0 0 16 16">
              <path d="M8.086 2.207a2 2 0 0 1 2.828 0l3.879 3.879a2 2 0 0 1 0 2.828l-5.5 5.5A2 2 0 0 1 7.879 15H5.12a2 2 0 0 1-1.414-.586l-2.5-2.5a2 2 0 0 1 0-2.828l6.879-6.879zm.66 11.34L3.453 8.254 1.914 9.793a1 1 0 0 0 0 1.414l2.5 2.5a1 1 0 0 0 .707.293H7.88a1 1 0 0 0 .707-.293l.16-.16z"/>
            </svg>
          </router-link>
          <button v-if="post?.user === user.id" @click="deletePost" class="btn d-flex">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
              <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z"/>
            </svg>
          </button>
        </div>
        <p>작성자 : {{ post?.user_nickname }}</p>
        <h5 class="mt-5">{{ post?.content }}</h5>
      </div>
    </div>
    <div>
      <p>댓글 목록</p>
      <p>총 댓글: {{post.comment_count}}개</p>
      <div v-if="post?.comment_set">
        <p v-for="comment in post.comment_set" :key="comment.id">
          댓글 내용: {{ comment.content }}
          댓글 작성자: {{ comment.user_nickname }}
          <button v-if="comment.user === user.id" @click="deleteComment(comment.id)" class="btn">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
              <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z"/>
            </svg>
          </button>
        </p>
      </div>
      <form @submit="createComment">
          <textarea v-model="commentText" placeholder="댓글을 입력하세요"></textarea>
          <button type="submit">댓글 작성</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommunityDetailView',
  data() {
    return {
      liked: false,
      user: this.$store.state.user,
      commentText: ''
    }
  },
  computed: {
    post() {
      return this.$store.state.post
    }
  },
  created() {
    const postId = this.$route.params.id
    if (this.post) {
      this.liked = this.post.likes.includes(this.$store.state.user.id)
    } else {
      this.fetchPost(postId)
    }
  },
  methods: {
    fetchPost(postId) {
      const API_URL = 'http://127.0.0.1:8000';

      axios({
        method: 'get',
        url: `${API_URL}/community/${postId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.$store.commit('SET_POST', res.data)
        this.liked = res.data.likes.includes(this.$store.state.user.id)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getImageUrl(filename) {
      return 'http://127.0.0.1:8000' + filename;
    },
    deletePost() {
      this.$store.dispatch('deletePost', this.post.id)
    },
    likePost() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/community/${ this.post.id }/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
      .then(() => {
      if (this.liked) {
        this.liked = false;
        this.$store.commit('UNLIKE_POST');
      } else {
        this.liked = true;
        this.$store.commit('LIKE_POST');
        console.log(this.post)
      }
    })
      .catch ((err) => {
        console.log(err)
      })
    },
    createComment() {   
      const commentText = this.commentText

      if (!commentText) {
        alert('내용 입력해주세요.')
        return
      }

      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/community/posts/${ this.post.id }/comments/`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
        },
        data: {
            post: this.post.id,
            content: this.commentText
        }
        })
        .then((res) => {
          console.log(res)
          this.commentText = ''
        })
        .catch((err) => {
          console.log(err)
        });
    },
    deleteComment(commentId) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/comments/${commentId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        // console.log(this.post)
        window.location.reload()
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
}
</script>

<style scoped>
.list {
  color: rgb(158, 95, 253);
  text-align: left;
  display: flex;
  margin-left: 50px;
  margin-right: 30px;
  font-weight: bold;
}
</style>