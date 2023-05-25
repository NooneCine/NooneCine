<template>
  <div id="app" style="background-color: #0D0D0D;">
    <HeaderView class="fixed-top header"/>
    <div class="box"></div>
    <router-view />
    <FooterView class="fixed-bottom footer" />
  </div>
</template>

<script>
import HeaderView from '@/components/Header.vue'
import FooterView from '@/components/Footer.vue'

export default {
  name: 'AppView',
  components: {
    HeaderView,
    FooterView,
  }
}
</script>

<style>
:root {
  background-color: #0D0D0D;
  color: white;
}

#app {
  font-family: 'Gothic A1', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
}

.header {
  background-color: #0D0D0D;
}

.box {
  height: 68px;
}

.footer {
  position: fixed;
  bottom: 0;
  width: 100%;
  background-color: #0D0D0D;
}
</style>
