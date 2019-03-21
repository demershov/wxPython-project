import wx
import glob
# import eyed3


class Mp3Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.row_obj_dict = {}
        self.list_ctrl = wx.ListCtrl(
            self, size=(-1, 100),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.list_ctrl.InsertColumn(0, 'Название', width=200)
        self.list_ctrl.InsertColumn(1, 'Артист', width=140)
        self.list_ctrl.InsertColumn(2, 'Альбом', width=140)
        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        edit_button = wx.Button(self, label='Edit')
        edit_button.Bind(wx.EVT_BUTTON, self.on_edit)
        main_sizer.Add(edit_button, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(main_sizer)

    def on_edit(self, event):
        print('Редактируется')

    def update_mp3_listing(self, folder_path):
        print(folder_path)


class Mp3Frame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Mp3 тег редактор')
        self.panel = Mp3Panel(self)
        # Показать фрейм
        self.Show()


if __name__ == '__main__':
    # Инициализация приложения
    app = wx.App()
    # Собственный класс, унаследованный от библиотеки
    frame = Mp3Frame()
    # Цикл Событий - Event Loop
    app.MainLoop()
