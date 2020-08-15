<template>
<div>
    <h4>Question title</h4>
    <b-card-group deck>
        <report></report>
        <front-terminal></front-terminal>
    </b-card-group>
</div>
</template>

<script>
import report from '../components/report.vue'
import frontTerminal from '../components/frontTerminal.vue'

import backendAPI from '../api/index.js'

export default {
    props: ['id'],
    components: {
        frontTerminal,
        report
  },
  mounted(){
      try {
          backendAPI.get('/servers');
      } catch (error) {
          console.log(error)
      }
  },
  destoryed(){
      try {
          backendAPI.delete('/servers');
      } catch (error) {
          console.log(error)
      }
  },
  data() {
      return{
      }
    }
}
</script>

<style>

</style>