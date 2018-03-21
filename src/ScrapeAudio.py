# link http://www.mp3bible.ca/playlistKJV/
# Auto Download audio from above site to /data/audio/book/chapter
# Copyright URL: http://www.mp3bible.ca/copyright/Audio_Scriptures_International_Copyright_Info.mp3
import GetUrl
import BiblePaths
import CheckInternet
from bs4 import BeautifulSoup
import zipfile
import ErrorMsg
import time
import json
import GetRemoteDir


class ScrapeAudio:
    def __init__(self):
        self.bpath = BiblePaths.BiblePaths()
        self.ci = CheckInternet.CheckInternet()
        self.em = ErrorMsg.ErrorMsg()
        self.gu = GetUrl.GetUrl()
        self.get_url = self.gu.fetch_url
        self.rmd = GetRemoteDir.GetRemoteDir()

        self.max_file_age_hours = 168
        self.page = None
        self.ok_status = 200
        self.hrefs = []
        self.ziplist = []
        self.zipdirs = []
        self.entry = None
        self.chapter = None
        self.book = None

        self.audio_dict = {}

    def download_needed(self, filename):
        retval = True
        if filename.exists():
            stat = filename.stat()
            now = time.time()
            hours_old = int((now - stat.st_mtime) / 3600)
            if hours_old < self.max_file_age_hours:
                retval = False
        return retval

    def get_zip_files(self):
        if self.download_needed(self.bpath.audio_zip_savefile):
            if self.ci.check_availability():
                self.rmd.list_file_descriptor(self.bpath.audio_zip_url,
                                              savefile=self.bpath.audio_zip_savefile,
                                              suffix='.zip')

        with self.bpath.audio_zip_savefile.open() as f:
            zips = f.read()

        soup = BeautifulSoup(zips, 'lxml')
        links = soup.find_all('a')

        for link in links:
            href = link['href']
            if '.zip' not in href:
                continue
            if 'LARGE' in href:
                continue
            href = f'{self.bpath.audio_zip_url}{href}'
            self.ziplist.append(href)

        self.zipdirs = []
        for zfile in self.ziplist:
            zsp = zfile.split('/')
            z1 = zsp[-1].split('_')
            source_zip_name = z1[-2].split('-')[0]
            # print(f'zfile: {zfile}')
            # print(f'zsp: {zsp}')
            # print(f'z1: {z1}')
            print(f'Getting audio files for: {source_zip_name}')
            zip_save_path = self.bpath.KingJamesAudiopath / source_zip_name
            self.zipdirs.append(source_zip_name)
            zip_save_path.mkdir(exist_ok=True)
            # print(f'zip_save_path: {zip_save_path}')
            savefile = zip_save_path / f'{source_zip_name}.zip'
            # print(f'savefile: {savefile}')
            if self.download_needed(savefile):
                if self.ci.check_availability():
                    response = self.get_url(url=zfile, zip=True)
                    if response.status_code == self.ok_status:
                        with savefile.open('wb') as f:
                            f.write(response.content)
                        time.sleep(1)
                    else:
                        self.em.error_msg(message=f"Can't find {zfile}", title='get_files')
                        return None

        for dir in self.zipdirs:
            zdir = self.bpath.KingJamesAudiopath / dir
            files = []
            [files.append(file) for file in zdir.iterdir() if file.is_file()]
            if len(files) == 1:
                with zipfile.ZipFile(files[0], 'r') as zip_ref:
                    zip_ref.extractall(zdir)


if __name__ == '__main__':
    sa = ScrapeAudio()
    sa.get_zip_files()
