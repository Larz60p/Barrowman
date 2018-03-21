import BiblePaths
import requests
import CheckInternet
import ErrorMsg

class GetUrl:
    def __init__(self):
        self.em = ErrorMsg.ErrorMsg()
        self.bpath = BiblePaths.BiblePaths()

        self.ci = CheckInternet.CheckInternet()
        self.ok_status = 200
        self.response = None

    def fetch_url(self, url, zip=False):
        self.response = None
        if self.ci.check_availability():
            if zip:
                self.response = requests.get(url, stream=True, allow_redirects=False)
            else:
                self.response = requests.get(url, allow_redirects=False)
        else:
            self.em.error_msg(message='No network found', title='GetUrl:fetch_url')
        return self.response

def testit():
    gu = GetUrl()
    page = gu.fetch_url('https://www.google.com/')
    count = 0
    maxcount = 20
    try:
        if page.status_code == 200:
            ptext = page.text.split('/n')
            for line in ptext:
                print(f'{line}\n')
                count += 1
                if count > maxcount:
                    break
        else:
            print(f'Error retreving file status code: {page.status_code}')
    except AttributeError:
        print('Please enable internet and try again')

if __name__ == '__main__':
    testit()
