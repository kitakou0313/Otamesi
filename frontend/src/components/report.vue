<template>
 <b-card>
     <b-card-title>概要</b-card-title>
     <b-card-body>
         {{articleData.detail}}
     </b-card-body>
 </b-card>
</template>

<script>
import backendAPI from '../api/index.js'
export default {
    name:"report",
    props: ['id'],
    async created(){
      try {
          const res = (await backendAPI.get(`/articles/${this.id}`)).data;
          this.articleData = res
      } catch (error) {
          console.log(error)
      }
  },
    data(){
        return{
            articleData:{}
        }
    }
}
</script>

<style>

</style>