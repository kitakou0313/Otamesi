<template>
  <div id="terminal"></div>
</template>

<script>
import { Terminal } from 'xterm';
import { AttachAddon } from 'xterm-addon-attach';

export default {
    mounted:function(){
        const term = new Terminal()
        /*
        const socket = new WebSocket("ws://localhost:6000");
        const attachAddon = new AttachAddon(socket);
        terminal.loadAddon(attachAddon);
        */
        term.open(document.getElementById('terminal'));
        term.write('Hello from \x1B[1;3;31mxterm.js\x1B[0m $ ')
    }
}
</script>

<style>

</style>