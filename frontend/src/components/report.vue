<template>
 <b-card>
     <b-card-title>Report</b-card-title>
     <b-form >
     <b-card-body>
              <b-form-textarea
              id="textarea"
              v-model="articleData.report"
              placeholder="Enter something..."
              rows="10"
    ></b-form-textarea>
     </b-card-body>
     <b-card-footer ><div class="text-right"><b-button type="submit">Submit</b-button></div></b-card-footer>
     </b-form>
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