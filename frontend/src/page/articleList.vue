<template>
<b-card>
   <b-card-title>List of Trainings</b-card-title>
   <b-card-body>
       <b-table striped hover :items="items" :fields="fields">
        <template v-slot:cell(index)="data">
        {{ data.id }}
      </template>
        <template v-slot:cell(Title)="data">
            <router-link :to="{name:'articlePage', params:{ id: data.item.id }}">
                {{ data.item.Title }}
            </router-link>
      </template>
       </b-table>
   </b-card-body>
</b-card>
</template>

<script>
import backendAPI from '../api/index.js'
export default {

    async created(){
        try {
            const res = (await backendAPI.get('/articles')).data
            this.items = res
        } catch (error) {
            console.log(error)
        }
    },
    data(){
        return {
            items:null,
            fields: [
          { key: 'id', label: 'ID' },
          { key: 'title', label: 'Title of article' }
        ],
        }
    }
}
</script>

<style>

</style>