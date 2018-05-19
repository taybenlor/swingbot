import bpm
import player

def query_bpm():
	query = input('How fast would you like your song to be? ')

	if 'bpm' in query.lower():
		before, after = query.split('bpm')
		tempo_string = before.split()[-1]
		try:
			tempo = int(tempo_string)
			song = bpm.get_song(tempo)
			player.play(song)
			print(f'Playing {song} at {tempo} BPM.')
		except ValueError:
			print(f'{tempo_string} doesn\'t seem like a number.')
	else:
		print('Sorry, I\'m not sure I understand you. Please phrase your answer in BPM.')

def set_bpm():
	recorded = False
	song = input('Tell me the song: ')

	while not recorded:
		query = input('How fast is it in BPM? ')
		if 'bpm' in query.lower():
			before, after = query.split('bpm')
			tempo_string = before.split()[-1]
			try:
				tempo = int(tempo_string)
				recorded = bpm.set_song(song, tempo)
				print(f'Recorded {song} as being {tempo} BPM!')
			except ValueError:
				print(f'{tempo_string} doesn\'t seem like a number.')
		else:
			print('Sorry, I\'m not sure I understand you. Please phrase your answer in BPM.')

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
