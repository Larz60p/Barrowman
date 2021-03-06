import GetUrl
from bs4 import BeautifulSoup
import CheckInternet
import time
import sys


class GetRemoteDir:
    def __init__(self):
        self.soup = None
        self.gu = GetUrl.GetUrl()
        self.cki = CheckInternet.CheckInternet()
        self.internet_available = self.cki.check_availability()
        self.page = None
        self.refresh_hours_every = None

    def list_file_descriptor(self, url, savefile=None, refresh_hours_every=48, suffix=''):
        elapsed_hours = 0
        dirlist = []
        self.refresh_hours_every = refresh_hours_every
        self.url = url
        self.savefile = savefile
        self.suffix = suffix

        if self.savefile:
            if self.savefile.exists():
                lstats = self.savefile.lstat()
                elapsed_hours = (time.time() - lstats.st_mtime) / 3600
                if elapsed_hours > self.refresh_hours_every:
                    self.page = self.download_new_file()
                else:
                    with savefile.open('r') as f:
                        self.page = f.read()
            else:
                self.page = self.download_new_file()
        else:
            self.page = self.download_new_file()

        self.soup = BeautifulSoup(self.page, 'html.parser')
        links = self.soup.select('a')
        for link in links:
            try:
                if link['href'].endswith(suffix):
                    dirlist.append(link['href'])
            except:
                print("Unexpected error:", sys.exc_info()[0])
        return dirlist

    def download_new_file(self):
        page = None
        if self.internet_available:
            document = self.gu.fetch_url(self.url)
            page = document.content
            with self.savefile.open('wb') as f:
                f.write(page)
        else:
            print('Please enable internet and re-try')
        return page


    def list_dir(self, url, suffix):
        for item in self.list_file_descriptor(url, suffix):
            print(item)


if __name__ == '__main__':
    testit()
