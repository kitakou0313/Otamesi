<template>
<div>
    <h4>Question title</h4>
    <b-card-group deck>
        <report></report>
        <front-terminal></front-terminal>
    </b-card-group>
</div>
</template>

<script>
import report from '../components/report.vue'
import frontTerminal from '../components/frontTerminal.vue'

export default {
    components: {
        frontTerminal,
        report
  },
  data() {
      return{
      }
    }
}
</script>

<style>

</style>