<template>
<b-card>
   <b-card-title>List of Trainings</b-card-title>
   <b-card-body>
       <b-table striped hover :items="items" :fields="fields">
        <template v-slot:cell(id)="data">
        {{ data.item.id }}
      </template>
        <template v-slot:cell(title)="data">
            <router-link :to="{name:'articlePage', params:{ id: data.item.id }}">
                {{ data.item.title }}
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