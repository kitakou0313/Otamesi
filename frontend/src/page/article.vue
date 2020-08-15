<template>
<div>
<b-nav tabs fill>
    <b-nav-item @click="currentTab='report'">Report</b-nav-item>
    <b-nav-item @click="currentTab='front-terminal'">Terminal</b-nav-item>
</b-nav>
<keep-alive>
    <component :is="currentTab" />
</keep-alive>
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
    return {
      currentTab : "report"
    }
    }
}
</script>

<style>

</style>