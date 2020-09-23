<template>
 <b-card header-tag="header" footer-tag="footer" no-body>
     <b-card-header>概要</b-card-header>
     <b-card-body>
         <b-card-text>
         {{articleData.detail}}
         </b-card-text>
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