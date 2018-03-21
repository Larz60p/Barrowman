from pathlib import Path
import shutil

class BiblePaths:
    def __init__(self):
        self.homepage = Path('.')
        self.doc = self.homepage / '..' / 'doc'
        self.doc.mkdir(exist_ok=True)
        self.scripts = self.homepage / '..' / 'scripts'
        self.scripts.mkdir(exist_ok=True)
        self.datapath = self.homepage / 'data'
        self.datapath.mkdir(exist_ok=True)
        self.htmlpath = self.datapath / 'html'
        self.htmlpath.mkdir(exist_ok=True)
        self.audio_html_path = self.htmlpath / 'audio'
        self.audio_html_path.mkdir(exist_ok=True)
        self.jsonpath = self.datapath / 'json'
        self.jsonpath.mkdir(exist_ok=True)
        self.KingJamespath = self.datapath / 'KingJames'
        self.KingJamespath.mkdir(exist_ok=True)
        self.KingJamesAudiopath = self.KingJamespath / 'audio'
        self.KingJamesAudiopath.mkdir(exist_ok=True)
        self.m3upath = self.KingJamesAudiopath / 'm3u'
        self.m3upath.mkdir(exist_ok=True)
        self.zippath = self.KingJamesAudiopath / 'zip'
        self.zippath.mkdir(exist_ok=True)
        self.tmpdir = self.datapath / 'tmp'
        self.tmpdir.mkdir(exist_ok=True)

        self.bible_url = 'http://ebible.org/kjv/kjvtxt.zip'

        self.complete_playlist_url = 'http://www.mp3bible.ca/playlistKJV/00000_CompletePLAYLIST-Total_KJV_Bible.m3u'
        self.complete_playlist_save = self.m3upath / 'CompletePLAYLIST-Total_KJV_Bible.m3u'
        self.audio_downloadold_url = 'http://www.mp3bible.ca/playlistKJV/'
        self.audio_zip_url = 'http://www.mp3bible.ca/zip/'
        self.audio_zip_savefile = self.zippath / 'zipindex.txt'
        self.audio_save_html = self.audio_html_path / 'mp3bible.html'

        self.bible_chapter_titles = 'https://austinbiblechurch.com/sites/default/files/documents/' \
                                    'oyttb/Bible_Chapter_Titles.pdf'
        self.bible_chapter_pdf = self.doc / 'bible-chapter-titles.pdf'
        self.bible_save = self.KingJamespath / 'kjvtxt.zip'
        self.IndexedBible = self.jsonpath / 'IndexedBible.json'
        self.BookXref = self.jsonpath / 'BookXref.json'
        self.AudioXref = self.jsonpath / 'AudioXref.json'
        self.emptyinit = self.homepage / '__init__.py'
        self.emptyinit.touch(exist_ok=True)

        self.static_json_script_bat = self.scripts / 'MakeTextIndexBible.bat'
        self.json_bat = self.jsonpath / 'MakeTextIndexBible.bat'

        shutil.copy(self.static_json_script_bat, self.json_bat)


def onetime():
    bp = BiblePaths()

if __name__ == '__main__':
    onetime()
