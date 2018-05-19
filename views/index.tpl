<p><strong>Hello! I can record the BPM of a song or play a song at a given BPM.</strong></p>
<div id="chat">
    <p class="bot">{{response}}</p>
</div>
<form id="commandForm">
    <label>
        <input style="width: 200px" type="text" name="command" id="commandInput">
    </label>
    <input type="submit">
</form>

<script>
function addResponse(data) {
    // Add bot message to chat log
    let messageElement = document.createElement('p');
    messageElement.classList.add('bot');
    messageElement.innerHTML = data.message;
    chat.appendChild(messageElement);

    if (data.frontend == 'stop') {
        for (let audioElement of document.querySelectorAll('audio')) {
            audioElement.pause();
        }
    }
}

function sendCommand(command) {
    // Clear and disable input
    commandInput.value = '';
    //commandInput.disabled = true;

    // Add human message to chat log
    let messageElement = document.createElement('p');
    messageElement.classList.add('human');
    messageElement.textContent = command;
    chat.appendChild(messageElement);

    // Construct form data
    let formData = new FormData();
    formData.append('command', command)

    // Send message to server
    fetch('/command', { method: 'POST', body: formData }).then((response) => {
        return response.json();
    }).then((data) => {
        addResponse(data)

        // Re-enable input
        //commandInput.disabled = false;
    });
}

commandForm.addEventListener('submit', (event) => {
    event.preventDefault();
    sendCommand(commandInput.value);
    return false;
});
</script>
