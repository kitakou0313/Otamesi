<template>
<div>
    <h4>Question title</h4>
    <Loading v-if="loading" :active="loading" :is-full-page="true" />
    <b-card-group deck v-else>
        <report :id="id"></report>
        <front-terminal></front-terminal>
    </b-card-group>
</div>
</template>

<script>
import report from '../components/report.vue'
import frontTerminal from '../components/frontTerminal.vue'
import Loading from 'vue-loading-overlay'

import backendAPI from '../api/index.js'

export default {
    props: {
        id: {
      type: Number,
      required: true
    }
    },
    components: {
        frontTerminal,
        report,
        Loading
  },
  data(){
      return{
          loading:true
      }
  },
  async created(){
      try {
          await backendAPI.get(`/servers/${this.id}`);
      } catch (error) {
          console.log(error)
      }
      this.loading = false
  },
  async beforeDestroy(){
      try {
         await backendAPI.delete(`/servers/${this.id}`);
      } catch (error) {
          console.log(error)
      }
  },
}
</script>

<style>

</style>