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

<script src="https://sdk.scdn.co/spotify-player.js"></script>
<script>
window.onSpotifyWebPlaybackSDKReady = () => {
    var token = 'BQCtwVWbsrdW2bmv8p8Eb6PyVZbYiYDwW0RyL3JDAJ6WFDQZKGeUpt1ypDoqHMMUyYxKn_qqyx6Ol9xXC8BDqxIJPtj-dTmC6ladq4APF-pM7c5dRva2Fy7xsoC2Tk-TfFRIoZDxvJzc92AaeRGkjBS61isWMhVqI9qeEEa8wDgKyCcBlWGwseQiZw';
    var player = new Spotify.Player({
        name: 'Swingbot',
        getOAuthToken: cb => { cb(token); }
    });

    // Error handling
    player.addListener('initialization_error', ({ message }) => { console.error(message); });
    player.addListener('authentication_error', ({ message }) => { console.error(message); });
    player.addListener('account_error', ({ message }) => { console.error(message); });
    player.addListener('playback_error', ({ message }) => { console.error(message); });

    // Playback status updates
    player.addListener('player_state_changed', state => { console.log(state); });

    // Ready
    player.addListener('ready', ({ device_id }) => {
        console.log('Ready with Device ID', device_id);

        window.play = function(song) {
            play({
                playerInstance: player,
                song: song
            });
        };
    });

    // Not Ready
    player.addListener('not_ready', ({ device_id }) => {
        console.log('Device ID has gone offline', device_id);
    });

    // Connect to the player!
    player.connect();

    function play(_ref) {
        var song = _ref.song,
            _ref$playerInstance$_ = _ref.playerInstance._options,
            getOAuthToken = _ref$playerInstance$_.getOAuthToken,
            id = _ref$playerInstance$_.id;

        getOAuthToken(function (access_token) {
            fetch('https://api.spotify.com/v1/search/?type=track&q=' + song, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + access_token
                }
            })
            .then(function(response){ return response.json(); })
            .then(function(result) {
                var track = result['tracks']['items'][0];
                fetch('https://api.spotify.com/v1/me/player/play?device_id=' + id, {
                    method: 'PUT',
                    body: JSON.stringify({ uris: ['spotify:track:'+track['id']] }),
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + access_token
                    }
                });
            });
        });
    };
};
</script>
