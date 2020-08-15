<template>
 <b-card>
     <b-card-title>Report</b-card-title>
     <b-form >
     <b-card-body>
              <b-form-textarea
              id="textarea"
              v-model="text"
              placeholder="Enter something..."
              rows="10"
    ></b-form-textarea>
     </b-card-body>
     <b-card-footer ><div class="text-right"><b-button type="submit">Submit</b-button></div></b-card-footer>
     </b-form>
 </b-card>
</template>

<script>
export default {
    name:"report",
    data(){
        return{
            text:"Test hogehoge"
        }
    }
}
</script>

<style>

</style>