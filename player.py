import pygame

pygame.init()
pygame.mixer.init()


paused = False


def play(song=None):
    if song is None and paused:
        pygame.mixer.music.unpause()
        return
    if song is None:
        song = 'shake_that_thing'
    pygame.mixer.music.load(f'music/{song}.wav')
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    global paused
    paused = True
    pygame.mixer.music.pause()


if __name__ == '__main__':
    while True:
        s = input('Whats up? ')
        if 'play' in s:
            play(s[5:])
        if 'stop' in s:
            pygame.mixer.music.stop()
        if 'pause' in s:
            pygame.mixer.music.pause()
            paused = True
