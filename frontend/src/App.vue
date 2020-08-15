<template>
<div>
  <topnav></topnav>
  <frontterminal></frontterminal>
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
