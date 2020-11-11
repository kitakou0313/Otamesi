<template>
<b-card no-body>
    <b-form @submit="submit">
   <b-card-title>問題制作フォーム</b-card-title>
   <b-card-body>
      <b-form-group
        id="input-group-1"
        label="Article Title"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="newArticle.title"
          type="text"
          required
          placeholder="Enter Title"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="DeployImage:" label-for="input-2" description="">
        <b-form-input
          id="input-2"
          v-model="newArticle.deployImage"
          required
          placeholder="Enter docker tub image"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-3"
        label="Article Detail"
        label-for="input-3"
      >
        <b-form-textarea
          id="input-3"
          v-model="newArticle.detail"
          type="text"
          required
          placeholder="Enter article's detail"
        ></b-form-textarea>
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
                title:"",
                deployImage:"",
                detail:""
            }
        }
    },
    methods:{
        async submit(){
            try {
                (await backendAPI.post('/articles/new', this.newArticle)).data

            } catch (error) {
                console.log(error)
            }
        }
    }
}
</script>

<style>

</style>