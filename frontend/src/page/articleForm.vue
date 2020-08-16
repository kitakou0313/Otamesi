<template>
<b-card>
    <b-form @submit="submit">
   <b-card-title>問題作りフォーム</b-card-title>
   <b-card-body>
      <b-form-group
        id="input-group-1"
        label="Article Title"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="newArticle.Title"
          type="text"
          required
          placeholder="Enter Title"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="DeployImage:" label-for="input-2" description="Please use tsl0922/ttyd image in FROM to access container from browsee.">
        <b-form-input
          id="input-2"
          v-model="newArticle.deployImage"
          required
          placeholder="Enter docker hub tub"
        ></b-form-input>
      </b-form-group>
       </b-card-body>
    <b-card-footer ><div class="text-right"><b-button type="submit">Submit</b-button></div></b-card-footer>
   </b-form>
</b-card>
</template>

<script>
import backendAPI from '../api/index.js'
export default {
    data(){
        return {
            newArticle:{
                Title:"",
                deployImage:""
            }
        }
    },
    methods:{
        async submit(){
            try {
                (await backendAPI.post('/article/new', this.newArticle)).data

            } catch (error) {
                console.log(error)
            }
        }
    }
}
</script>

<style>

</style>