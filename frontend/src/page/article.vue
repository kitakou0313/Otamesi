<template>
<div>
<Loading v-if="loading" :active="loading" :is-full-page="true" />
<div v-else>
    <h4>{{article.title}}</h4>
    <b-card-group deck>
        <report :id="id"></report>
        <front-terminal></front-terminal>
    </b-card-group>
</div>
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
          loading:true,
          article:{}
      }
  },
  async created(){
      try {
          const res = (await backendAPI.get(`/articles/${this.id}`)).data;
          await backendAPI.get(`/servers/${this.id}`);
          this.article = res;
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