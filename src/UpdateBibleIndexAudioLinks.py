import BiblePaths
import json
import re
import time
from shutil import copyfile


class UpdateBibleIndexAudioLinks:
    """
    Scans bpath.KingJamesAudiopath for all audio files, and either updates existing
    IndexedBible links or adds one if missing. (Larz60+)
    """
    def __init__(self):
        self.bpath = BiblePaths.BiblePaths()
        self.debug = False

        with self.bpath.IndexedBible.open() as f:
            self.bible_dict = json.load(f)

        self.audio_xref = {}
        self.audio_parent_paths = []
        self.bible_dict_chapters = []

        self.update_links()

    def get_parents(self):
        # Get parent paths
        parents = [dir.name for dir in self.bpath.KingJamesAudiopath.iterdir() if dir.is_dir()]
        parents.sort()
        return parents

    def get_books(self):
        # get list of IndexBible chapters
        books = list(self.bible_dict['Old Testament'].keys()) + list(self.bible_dict['New Testament'].keys())
        books.sort()
        return books

    def get_audio_xref(self, parents, books):
        audio_xref = dict(zip(parents, books))

        with self.bpath.AudioXref.open('w') as f:
            json.dump(audio_xref, f)
        return audio_xref

    def get_mp3_list(self, audio_path):
        mp3_list = [file.name for file in audio_path.iterdir() if file.is_file() and file.suffix == '.mp3']
        self.rename_mp3s(mp3_list, audio_path)
        return mp3_list

    def rename_mp3s(self, mp3_list, audio_path):
        # rename audio files eliminate spaces
        for filename in mp3_list:
            if ' ' in filename:
                new1 = filename.replace(' ', '_')
                new_filename = audio_path / new1
                file_path = audio_path / filename
                file_path.rename(new_filename)

    def get_book_key(self, audio_key, audio_xref):
        bible_key = audio_xref[audio_key]
        if bible_key in self.bible_dict['Old Testament']:
            book_key = self.bible_dict['Old Testament'][bible_key]
        else:
            book_key = self.bible_dict['New Testament'][bible_key]
        return book_key

    def remove_old_mp3_reference(self, book_key):
        try:
            del (book_key['mp3'])
        except KeyError:
            pass

    def get_verse(self, audio_file):
        filename = audio_file.split('-')[-1].split('.')[0]
        verse_idx = list(re.finditer(r'[a-z]', filename, re.I))[-1].start() + 1
        if len(filename) == verse_idx:
            verse = '1'
        else:
            verse = str(int(filename[verse_idx:]))
        return verse

    def update_links(self):
        """
        Get a list of all sub-directories and their contents fromm root of bpath.KingJamesAudiopath
        :return: updates self.audio_paths_dict
        """
        parent_paths = self.get_parents()
        books = self.get_books()
        audio_xref = self.get_audio_xref(parent_paths, books)

        # For loop gets book info
        for audio_key, bible_key in audio_xref.items():
            audio_path = self.bpath.KingJamesAudiopath / audio_key
            mp3_list = self.get_mp3_list(audio_path)

            book_key = self.get_book_key(audio_key, audio_xref)
            self.remove_old_mp3_reference(book_key)

            for audio_file in mp3_list:
                verse = self.get_verse(audio_file)
                verse_key = book_key[verse]
                verse_key['mp3path'] = [audio_key, audio_file]

        # Rename old BibleIndex
        fparts = self.bpath.IndexedBible.name.split('.')
        backup_filename = self.bpath.jsonpath / f'{fparts[0]}{int(time.time())}.{fparts[1]}'
        copyfile(self.bpath.IndexedBible, backup_filename)

        with self.bpath.IndexedBible.open('w') as f:
             json.dump(self.bible_dict, f)

if __name__ == '__main__':
    UpdateBibleIndexAudioLinks()
