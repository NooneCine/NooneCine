<template>
  <div>
    <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <router-link :to="{ name: 'MovieDetailView', params: { id: 502356 } }">
          <div class="carousel-item active">
            <img src="@/assets/1.png" class="d-block w-100" alt="...">
          </div>
        </router-link>
        <router-link :to="{ name: 'MovieDetailView', params: { id: 76600 } }">
          <div class="carousel-item">
            <img src="@/assets/2.png" class="d-block w-100" alt="...">
          </div>
        </router-link>
        <router-link :to="{ name: 'MovieDetailView', params: { id: 447365 } }">
          <div class="carousel-item">
            <img src="@/assets/3.png" class="d-block w-100" alt="...">
          </div>
        </router-link>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <MovieList class="mb-5"/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'


export default {
  name: 'MovieView',
  components: {
    MovieList,
  },
}
</script>

<style>
</style>