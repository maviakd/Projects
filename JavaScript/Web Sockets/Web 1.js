// Create WebSocket connection.
const socket = new WebSocket('ws://localhost:8080');
socket.listen()

// Connection opened
socket.addEventListener('open', function (event) {
    socket.send('Hello Server!');
});

// Listen for messages
socket.addEventListener('message', function (event) {
    console.log('Message from server ', event.data);
});
