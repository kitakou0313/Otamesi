<template>
<div class="background">
  <topnav></topnav>
  <main class="main-content">
    <div class="main-content-container" >
      <div class="px-4">
        <article-page />
      </div>
      </div>
  </main>
</div>
</template>

<script>
import articlePage from './page/article.vue'
import  topnav  from "./navitems/topnav.vue"

export default {
  name: 'App',
  components: {
    articlePage,
    topnav
  }
}
</script>
<style>
.main-content {
  display: flex;
  flex-direction: column;
}
.main-content-container{
  margin: 1%;
}
</style>
