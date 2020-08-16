<template>
<b-card>
   <b-card-title>Terminal of hogehoge</b-card-title>
   <b-card-body>
 <b-embed
    type="iframe"
    src="http://localhost:7681"
  ></b-embed>
   </b-card-body>
</b-card>
</template>

<script>
export default {
    name:"front-terminal",
    async created(){
       const _sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
       await _sleep(15000);
    }
}
</script>

<style>

</style>