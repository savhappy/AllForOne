const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
const { instrument } = require("@socket.io/admin-ui");
const { first, middle, end } = require("./names");
const cors = require("cors");

// const { Controller } = require("./controllers");

const host = "localhost";
const port = 3000;

const corsOptions = {
  origin: "*",
  //   methods: ['GET']
};

app.use(cors(corsOptions));
app.use(express.json());

const ranNum = () => {
  return Math.floor(Math.random() * 14);
};
const generateUserName = (first, middle, end, cb) => {
  return `${first[cb()]}${middle[cb()]}${end[cb()]}`;
};
let userNames = [];

io.on("connection", (socket) => {
  console.log("a user connected", socket.id);

  //CAPTAIN CREATE ROOM AND JOIN
  socket.on("join room", async (roomCode) => {
    console.log(roomCode, "roomcade server side");
    socket.join(roomCode);
    // let ids = await io.in(roomCode).allSockets();
    userNames.push(generateUserName(first, middle, end, ranNum));
    io.to(roomCode).emit("users", [...userNames]);
  });
  //JOIN GAME
  socket.on("room check", async (roomCheck) => {
    const roomList = Array.from(io.sockets.adapter.rooms).filter((rm) => {
      return rm[0] == roomCheck;
    });

    socket.join(roomList[0][0]);
    // let ids = await io.in(roomCheck).allSockets();
    userNames.push(generateUserName(first, middle, end, ranNum));
    io.to(roomCheck).emit("users", [...userNames]);
  });

  // socket.to("some room").emit("some event");

  // socket.on("get users", async (roomCode) => {
  //   let ids = await io.in(roomCode).allSockets();
  //   console.log(ids, "IM AN ID");
  //   console.log(roomCode, "HI IM A ROOMCODE");
  //   socket.to(roomCode).emit("users", [...ids]);

  //   // socket.emit("users", [...ids]);
  // });

  // let users = [];
  // socket.on("update users", (username, amount) => {
  //   const user = {
  //     username,
  //     amount,
  //     id: socket.id,
  //   };
  //   users.push(user);
  //   console.log("Here is the users: ", users);
  //   io.emit("new user", users);
  // });

  // socket.on('join room', (roomName) => {
  //   socket.join(roomName);
  //   socket.emit('joined room', roomName);
  //   console.log('Here is the room code', roomName);
  // });

  // socket.on('disconnect', () => {
  //   users = users.filter((u) => u.id !== socket.id);
  //   io.emit('new user', users);
  // io.emit('user disconnected')
  // });
});

instrument(io, { auth: false });

server.listen(port, host, () => {
  console.log(`listening on ${host}:${port}...`);
});
