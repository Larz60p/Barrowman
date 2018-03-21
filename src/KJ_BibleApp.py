import BiblePaths
import json
import wx
from pygame import mixer


class KJ_BibleApp:
    def __init__(self, parent, id = wx.ID_ANY, title = "Bible for the Blind", xpos=20, ypos=20,
                 width=1200, height=600, style=wx.DEFAULT_FRAME_STYLE):
        self.bpath = BiblePaths.BiblePaths()
        self.app = wx.App()
        self.frame = wx.Frame(None, id=wx.ID_ANY, title=title, pos=(xpos, ypos),
                              size=(width, height), style=style)

        self.app.Bind(wx.EVT_CLOSE, self.OnClose)

        self.app.SetTopWindow(self.frame)

        with self.bpath.IndexedBible.open() as f:
            self.bible = json.load(f)

        self.ot = 'Old Testament'
        self.nt = 'New Testament'

        self.book_list = self.get_book_list()

        # dictionary to hold all notebook pages
        self.page = {}

        # Button position and dimensions
        self.button_width = 110
        self.button_height = 36
        self.button_hover_color = '#87ceeb'
        self.button_normal_color = wx.NullColour

        self.xpos = 0
        self.ypos = 0

        self.left_x = 5
        self.upper_left_y = 5

        self.x_increment = 150
        self.y_increment = 55

        self.x_max = width

        self.create_application()
        self.frame.Show()
        self.app.MainLoop()

    def create_application(self):
        self.create_notebook()
        self.create_pages()

    def create_notebook(self):
        self.nb = wx.Notebook(self.frame, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                              style=wx.NB_NOPAGETHEME, name=wx.NotebookNameStr)
        self.nb.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.nb.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)

    def set_page(self, event):
        self.nb.SetSelection(self.page['Index']['panel'])
        event.skip()

    def get_book_list(self):
        # Each entry is list[volume, book, chapters]
        # Chapters is the number of chapters
        book_list = []
        for volume, value in self.bible.items():
            for book, value1 in value.items():
                chapters = 0
                for chapter, unused in value1.items():
                    if chapter.isdigit():
                        chapters += 1
                book_list.append([volume, book, chapters])
        return book_list

    def new_button(self, button, panel, label_text):
        button = wx.Button(panel, id=wx.ID_ANY,
                            label=label_text,
                            pos=(self.xpos, self.ypos),
                            size=(self.button_width, self.button_height),
                           name=wx.ButtonNameStr)
        return button

    def new_xy(self):
        self.xpos += self.x_increment
        if self.xpos >= self.x_max:
            self.ypos += self.y_increment
            self.xpos = self.left_x

    def add_index_page(self):
        self.xpos = self.left_x
        self.ypos = self.upper_left_y
        self.page = {}
        # / =============== Index page is special ===============
        self.page['Index'] = {}
        self.page['Index']['panel'] = wx.Panel(self.nb, id=wx.ID_ANY, style=wx.CLIP_CHILDREN)
        self.home = self.page['Index']['page'] = self.nb.AddPage(self.page['Index']['panel'], text='Index')
        # Index buttons
        for TargetId, (volume, book, unused) in enumerate(self.book_list):
            chapter = None
            label_text = book
            pageidx = self.page['Index'][book] = {}
            btn = pageidx['button'] = self.new_button(pageidx, self.page['Index']['panel'], label_text)
            pinfo = pageidx['info'] = {}
            pinfo['volume'] = volume
            pinfo['book'] = book
            pinfo['chapter'] = None
            pinfo['target'] = TargetId + 1 # One more for Index Page
            btn.name = [TargetId + 1, pageidx, volume, book, chapter, self.page]
            btn.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow, btn)
            btn.Bind(wx.EVT_LEAVE_WINDOW, self.OnExitWindow, btn)
            btn.Bind(wx.EVT_BUTTON, self.OnClick, btn)
            self.new_xy()

    def add_exit_button(self, chapter, pageidx):
            # =============== Final button page points back to index page ===============
            # ===============  Name chapters (with 's') intentional here  ===============
            volume = pageidx['info']['volume']
            book = pageidx['info']['book']
            label_text = f'Index'
            btn = pageidx['button'] = self.new_button(pageidx, self.page[book]['panel'], label_text)
            pinfo = pageidx['info'] = {}
            pinfo['volume'] = 'Home'
            pinfo['Index'] = None
            pinfo['chapter'] = None
            TargetId = 0
            btn.name = [TargetId, pageidx, volume, book, chapter, self.page]
            btn.Bind(wx.EVT_BUTTON, self.OnIndex, btn)
            self.new_xy()

    def create_pages(self):
        self.add_index_page()
        # =============== chapter pages ===============
        for volume, book, chapters in self.book_list:
            self.page[book] = {}
            self.page[book]['panel'] = wx.Panel(self.nb, id=wx.ID_ANY, style=wx.CLIP_CHILDREN)
            self.page[book]['page'] = self.nb.AddPage(self.page[book]['panel'], text=book)
            self.xpos = self.left_x
            self.ypos = self.upper_left_y
            for chapter in range(chapters):
                chapter += 1
                label_text = f'{book}:{chapter}'
                pageidx = self.page[book][chapter] = {}
                btn = pageidx['button'] = self.new_button(pageidx, self.page[book]['panel'], label_text)
                pinfo = pageidx['info'] = {}
                pinfo['volume'] = volume
                pinfo['book'] = book
                pinfo['chapter'] = chapter
                TargetId = None
                btn.name = [TargetId, pageidx, volume, book, chapter, self.page]
                # Add additional user info as pinfo['userinfo'] = value
                # where userinfo replaced by meaningful name
                btn.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow, btn)
                btn.Bind(wx.EVT_LEAVE_WINDOW, self.OnExitWindow, btn)
                btn.Bind(wx.EVT_BUTTON, self.OnClick, btn)
                self.new_xy()
            self.add_exit_button(chapters, pageidx)

    def OnEnterWindow(self, event):
        TargetId, pageidx, volume, book, chapter, page = event.GetEventObject().name
        # print(f'volume: {volume}, book: {book}, chapter: {chapter}')
        pageidx['button'].SetBackgroundColour(self.button_hover_color)

    def OnExitWindow(self, event):
        TargetId, pageidx, volume, book, chapter, page = event.GetEventObject().name
        # print(f'volume: {volume}, book: {book}, chapter: {chapter}')
        pageidx['button'].SetBackgroundColour(self.button_normal_color)

    def OnClick(self, event):
        TargetId, pageidx, volume, book, chapter, page = event.GetEventObject().name
        if chapter is not None:
            mp3path = self.get_mp3_filepath(volume, book, str(chapter))
            mixer.init()
            mixer.music.load(mp3path)
            mixer.music.play()
        elif TargetId is not None:
            self.nb.SetSelection(TargetId)


    def OnIndex(self, event):
        sel = self.nb.SetSelection(0)
        event.Skip()

    def get_mp3_filepath(self, volume, book, chapter):
        mp3loc = self.bible[volume][book][chapter]['mp3path']
        # Hack until bug fixed
        mp3loc[1] = mp3loc[1].replace(' ', '_')
        mp3path = self.bpath.KingJamesAudiopath / mp3loc[0] / mp3loc[1]
        return (mp3path.resolve()).as_posix()

    def OnPageChanged(self, event):
        pass

    def OnPageChanging(self, event):
        pass

    def OnClose(self):
        self.app.Destroy()

if __name__ == '__main__':
    KJ_BibleApp(None, width=1200)
