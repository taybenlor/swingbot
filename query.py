import bpm

def playing(command, context):
	if 'bpm' in command.lower():
		before, after = command.lower().split('bpm')
		tempo_string = before.split()[-1]
		try:
			tempo = int(tempo_string)
			song = bpm.get_song(tempo)
			return f'''
				<audio src="/music/{song}.wav" autoplay controls></audio><br>
				Playing {song} at {tempo} BPM. Record a BPM? Or play a song?
			''', None
		except ValueError:
			return f'{tempo_string} doesn\'t seem like a number.', context
	else:
		return 'Please phrase your answer in BPM', context

def telling(command, context):
	return 'What is the BPM of the song?', { 'intent': 'recording', 'song_name': command }

def recording(command, context):
	song = context['song_name']
	if 'bpm' in command.lower():
		before, after = command.lower().split('bpm')
		tempo_string = before.split()[-1]
		try:
			tempo = int(tempo_string)
			recorded = bpm.set_song(song, tempo)
			return f'Recorded {song} as being {tempo} BPM! Record a BPM? Or play a song?', None
		except ValueError:
			return f'{tempo_string} doesn\'t seem like a number.', context
	else:
		return 'Please phrase your answer in BPM', context

def query(command=None, context=None):
	if command is None:
		return 'Record a BPM? Or play a song?', None

	if context is not None:
		intent = context.get('intent')

		if intent == 'recording':
			return recording(command, context)

		if intent == 'playing':
			return playing(command, context)

		if intent == 'telling':
			return telling(command, context)

	if 'record' in command.lower():
		return 'Tell me the song:', { 'intent': 'telling' }
	elif 'play' in command.lower():
		return 'How fast would you like your song to be?', { 'intent': 'playing' }
	elif 'stop' in command.lower():
		return 'Stopped. Record a BPM? Or play a song?', { 'frontend': 'stop' }
	else:
		return 'Sorry I don\'t understand. Record a BPM? Or play a song?', None
