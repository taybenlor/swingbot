import pickle

FILENAME = 'bpm.pickle'


def init():
    with open(FILENAME, 'wb') as f:
        data = ({}, {})
        pickle.dump(data, f)
        return True


def set_song(song, bpm):
    with open(FILENAME, 'rb') as f:
        song_to_bpm, bpm_to_song = pickle.load(f)
        song_to_bpm[song] = bpm
        bpm_to_song[bpm] = song
    with open(FILENAME, 'wb') as f:
        pickle.dump((song_to_bpm, bpm_to_song), f)
        return True


def get_bpm(song):
    with open(FILENAME, 'rb') as f:
        song_to_bpm, bpm_to_song = pickle.load(f)
        return song_to_bpm[song]


def get_song(bpm):
    with open(FILENAME, 'rb') as f:
        song_to_bpm, bpm_to_song = pickle.load(f)
        return bpm_to_song[bpm]

# init()
# init()
# set_song('hello world', 120)
# print(get_bpm('hello world'))
# print(get_song(120))
