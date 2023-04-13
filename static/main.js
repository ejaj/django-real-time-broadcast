
var socket = new WebSocket(
    'ws://127.0.0.1:8000/ws/graph/'
)
socket.onmessage = function (event) {
    var data = JSON.parse(event.data);
    console.log(data);
    document.querySelector('#app').innerText = data.value;
}