<template>
<div>
  <topnav></topnav>
  <main class="main-content">
    <div class="main-content-container" >
      <div class="px-4">
         <frontterminal></frontterminal>
      </div>
      </div>
  </main>

</div>
</template>

<script>
import frontterminal from './components/frontTerminal.vue'
import  topnav  from "./navitems/topnav.vue"

export default {
  name: 'App',
  components: {
    frontterminal,
    topnav
  }
}
</script>
<style>
.main-content {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: rgb(235, 235, 235);
}
</style>
