const pty = require("node-pty");
const Io = require("socket.io");

const express = require("express");
const app = express();
const server = require("http").createServer(app);

var io = new Io(server);
io.on("connect", (socket) => {
  var term = pty.spawn("bash", [], {
    name: "xterm-color",
    cols: 80,
    rows: 24,
  });

  term.on("data", (data) => socket.emit("data", data));
  socket.on("data", (data) => term.write("data", data));
  socket.on("disconnect", () => term.destroy());
});

server.listen(6000);