<template>
<b-card>
   <b-card-title>List of Trainings</b-card-title>
   <b-card-body>
       <b-table striped hover :items="items">
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
export default {
    data(){
        return {
            items:[
                 { id: 40, Title: 'Test' },
                 { id: 21, Title: 'Test2' },
            ]
        }
    }
}
</script>

<style>

</style>