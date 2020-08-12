<template>
  <div id="terminal"></div>
</template>

<script>
import { Terminal } from 'xterm';
import { AttachAddon } from 'xterm-addon-attach';
import { axios } from "../api";

export default {
    mounted:function(){
        const term = new Terminal()
        const socket = new WebSocket("ws://localhost:5000/websocket");

        term.open(document.getElementById('terminal'));

        term.on('data', data => socket.emit('data', data));
        socket.on('data', data => term.write(data));
    }
}
</script>

<style>

</style>