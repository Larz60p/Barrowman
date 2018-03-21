import BiblePaths
from pygame import mixer
import json


class PlayAudio:
    def __init__(self):
        self.bpath = BiblePaths.BiblePaths()

        with self.bpath.IndexedBible.open() as f:
            self.bible = json.load(f)

    def play_chapter(self, volume, book, chapter):
        mp3loc = self.bible[volume][book][chapter]['mp3path']
        # Hack until bug fixed
        mp3loc[1] = mp3loc[1].replace(' ', '_')
        mp3path = self.bpath.KingJamesAudiopath / mp3loc[0] / mp3loc[1]
        newpath = (mp3path.resolve()).as_posix()

        mixer.init()
        mixer.music.load(newpath)
        mixer.music.play()
        input('Press enter to quit')

def testit():
    pa = PlayAudio()
    pa.play_chapter('Old Testament', 'Jeremiah', '45')


if __name__ == '__main__':
    testit()
