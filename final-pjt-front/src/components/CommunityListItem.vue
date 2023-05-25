<template>
  <div class="mx-5">
    <router-link :to="{ name: 'CommunityDetailView', params: { id: post.id } }" class="list-group-item list-group-item-action">
      <div class="mx-3">
        <div class="d-flex w-100 justify-content-between my-2">
          <h4>{{ post.title }}</h4>
          <small>{{ formatTime(post.created_at) }}</small>
        </div>
        <div class="my-2 text-start overflow-text">{{ post.content }}</div>
        <small class="d-flex w-100 justify-content-left my-2">
          <span>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person" viewBox="0 0 16 16">
              <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4Zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10Z"/>
            </svg>
            {{ post.user_nickname }}
          </span>
          <span class="ms-3">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chat-square-dots" viewBox="0 0 16 16">
              <path d="M14 1a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1h-2.5a2 2 0 0 0-1.6.8L8 14.333 6.1 11.8a2 2 0 0 0-1.6-.8H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2.5a1 1 0 0 1 .8.4l1.9 2.533a1 1 0 0 0 1.6 0l1.9-2.533a1 1 0 0 1 .8-.4H14a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>
              <path d="M5 6a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"/>
            </svg>
            {{ post.comments_count }}
          </span>
          <span class="ms-3">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
              <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
            </svg>
            {{ post.likes_count }}
          </span>
        </small>
      </div>
    </router-link>
  </div>
</template>

<script>
import moment from 'moment'

export default {
  name: 'CommunityListItem',
  props: {
    post: Object,
  },
  methods: {
    formatTime(time) {
      const currentTime = moment();
      const postTime = moment(time);
      const hoursDiff = currentTime.diff(postTime, 'hours');
      const daysDiff = currentTime.diff(postTime, 'days');

      if (hoursDiff < 1) {
        return '방금 전';
      } else if (hoursDiff < 24) {
        return `${hoursDiff}시간 전`
      } else {
        return `${daysDiff}일 전`
      }
    }
  }
}
</script>

<style scoped>
a {
  margin: 0;
  color: black;
}
.overflow-text {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical; 
  overflow: hidden;
}

</style>