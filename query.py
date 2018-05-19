import bpm
import player

def playing(command):
	if 'bpm' in command.lower():
		before, after = command.split('bpm')
		tempo_string = before.split()[-1]
		try:
			tempo = int(tempo_string)
			song = bpm.get_song(tempo)
			player.play(song)
			return f'Playing {song} at {tempo} BPM.', None
		except ValueError:
			return f'{tempo_string} doesn\'t seem like a number.', 'playing'
	else:
		return 'Please phrase your answer in BPM', 'playing'

def recording(command):
    if 'bpm' in command.lower():
        before, after = command.split('bpm')
        tempo_string = before.split()[-1]
        try:
            tempo = int(tempo_string)
            recorded = bpm.set_song(song, tempo)
            return f'Recorded {song} as being {tempo} BPM!', None
        except ValueError:
            return f'{tempo_string} doesn\'t seem like a number.', 'recording'
    else:
        return 'Please phrase your answer in BPM', 'recording'


def query(command=None, context=None):
	if command is None:
		return 'Record a BPM? Or play a song?', None

	if context == 'recording':
		return recording(command)

	if context == 'playing':
		return playing(command)

	if 'record' in command.lower():
		return 'Tell me the song:', 'recording'
	elif 'play' in command.lower():
		return 'How fast would you like your song to be?', 'playing'
	elif 'stop' in command.lower():
		player.stop()
		return 'Stopped', None
	else:
		return 'Sorry I don\'t understand', None

if __name__ == '__main__':
	print('Hello! I can record the BPM of a song or play a song at a given BPM.')
	while True:
		choice = input('Record a BPM? Or play a song? ').lower()

		if 'record' in choice.lower():
			set_bpm()
		elif 'play' in choice.lower():
			query_bpm()
		elif 'stop' in choice.lower():
			player.stop()
		else:
			print('Sorry I don\'t understand')
