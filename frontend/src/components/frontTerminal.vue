<template>
  <div id="terminal"></div>
</template>

<script>

import { Terminal } from 'xterm';
/*
import { Terminal } from '../../node_modules/xterm/lib/xterm';
import { AttachAddon } from 'xterm-addon-attach';*/

export default {
  data(){
    return{
      term:null,
    }
  },
  mounted(){
        this.term = new Terminal();
        /*
        const socket = new WebSocket("ws://localhost:6000");
        const attachAddon = new AttachAddon(socket);
        terminal.loadAddon(attachAddon);
        */
        this.term.open(document.getElementById('terminal'));
        this.term.write('')
    }
}
</script>

<style>

</style>