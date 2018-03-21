import wx


class ErrorMsg():
    def __init__(self):
        self.app = wx.App()

    def error_msg(self, message, title=''):
        """
        Display message in standard wx.MessageDialog
        :param message: (string) Value to be displayed
        :return: None
        """
        msg_dlg = wx.MessageDialog(None, message, title, wx.OK | wx.ICON_ERROR)
        val = msg_dlg.ShowModal()
        msg_dlg.Show()
        msg_dlg.Destroy()
        return val


def testit():
    '''
    Test message class
    :return: None
    '''
    em = ErrorMsg()
    val = em.error_msg(message='You are about to delete every file in the world!', title='The sky is falling')
    if val == wx.ID_OK:
        print('yahoo')


if __name__ == '__main__':
    testit()
