<template>
  <div id="terminal"></div>
</template>

<script>

import { Terminal } from 'xterm';
import { AttachAddon } from 'xterm-addon-attach';

export default {
  data(){
    return{
      term:null,
    }
  },
  mounted(){
        this.term = new Terminal();

        const socket = new WebSocket("ws://localhost:8000");
        const attachAddon = new AttachAddon(socket);
        this.term.loadAddon(attachAddon);

        this.term.open(document.getElementById('terminal'));
    }
}
</script>

<style>

</style>