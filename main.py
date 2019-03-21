import wx
import glob
import eyed3


class EditDialog(wx.Dialog):
    def __init__(self, mp3):


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

        edit_button = wx.Button(self, label='Редактировать')
        edit_button.Bind(wx.EVT_BUTTON, self.on_edit)
        main_sizer.Add(edit_button, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(main_sizer)

    def on_edit(self, event):
        selection = self.list_ctrl.GetFocusedItem()
        if selection >= 0:
            mp3 = self.row_obj_dict[selection]
            dialog = EditDialog(mp3)
            dialog.ShowModal()
            self.update_mp3_listing(self.current_folder_path)
            dialog.Destroy()

    def update_mp3_listing(self, folder_path):
        self.current_folder_path = folder_path
        self.list_ctrl.ClearAll()

        self.list_ctrl.InsertColumn(0, 'Название', width=200)
        self.list_ctrl.InsertColumn(1, 'Артист', width=140)
        self.list_ctrl.InsertColumn(2, 'Альбом', width=140)

        mp3s = glob.glob(f'{folder_path}/*.mp3)')
        mp3_objects = []
        for index, mp3 in enumerate(mp3s):
            mp3_object = eyed3.load(mp3)
            self.list_ctrl.InsertItem(index, mp3_object.tag.title)
            self.list_ctrl.SetItem(index, 1, mp3_object.tag.artist)
            self.list_ctrl.SetItem(index, 2, mp3_object.tag.album)
            mp3_objects.append(mp3_object)
            self.row_obj_dict[index] = mp3_object


class Mp3Frame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Редактор тегов песен.')
        self.panel = Mp3Panel(self)
        self.create_menu()

        # Показать фрейм
        self.Show()

    def create_menu(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        open_folder_menu_item = file_menu.Append(
            wx.ID_ANY, 'Выбрать директорию',
            'Открыть папку с треками'
        )
        menu_bar.Append(file_menu, '&File')

        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_open_folder,
            source=open_folder_menu_item
        )
        self.SetMenuBar(menu_bar)

    def on_open_folder(self, event):
        title = 'Выберите директорию'
        dialog = wx.DirDialog(self, title, style=wx.DD_DEFAULT_STYLE)

        if dialog.ShowModal() == wx.ID_OK:
            self.panel.update_mp3_listing(dialog.GetPath())

        dialog.Destroy()


if __name__ == '__main__':
    # Инициализация приложения
    app = wx.App()
    # Собственный класс, унаследованный от библиотеки
    frame = Mp3Frame()
    # Цикл Событий - Event Loop
    app.MainLoop()
