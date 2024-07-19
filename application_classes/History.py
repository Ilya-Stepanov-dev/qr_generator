import flet as ft
import threading
from src import get_qr_files, get_dict_add_and_del, delete_file

class HistoryListQR(ft.ListTile):
    def __init__(self, title, subtitle, func_delete, change_main_view):
        super().__init__()
        self.title = ft.Text(value=title)
        self.subtitle = ft.Text(value=subtitle)
        self.leading = ft.Icon(ft.icons.QR_CODE_SHARP)
        self.trailing = ft.IconButton(ft.icons.DELETE, on_click=self.delete)
        self.on_click = self.view
        self.func_delete = func_delete
        self.change_main_view = change_main_view

    def view(self,e):
        self.change_main_view(self.title.value)

    def delete(self, e):
        self.func_delete({"file": self.title.value, "date": self.subtitle.value})


class HistoryViewQR(ft.ListView):
    def __init__(self, func_view):
        super().__init__()
        self.func_view = func_view
        self.controls = self.init_controls()
        self.list_files = self.init_list_files()
        self.height = 200
        self.auto_scroll=True
        self.expand=1 
        self.spacing=5
        self.padding=5

    def init_controls(self):
        list_qr = get_qr_files()
        list_controls = []
        # print(list_qr)
        for add in list_qr:
            # print(add)
            list_controls.append(HistoryListQR(title=add["file"], subtitle=add["date"], func_delete=self.delete_list, change_main_view=self.func_view))
        return list_controls


    def init_list_files(self):
        if self.controls == []:
            return []
        else:
            files = []
            for list_qr in self.controls:
                files.append({"file":list_qr.title.value, "date":list_qr.subtitle.value})
            return files
        
    def add_list(self, dict_list: dict):
        list_qr = HistoryListQR(title=dict_list["file"], subtitle=dict_list["date"], func_delete=self.delete_list, change_main_view=self.func_view)
        self.controls.append(list_qr)
        self.list_files.append(dict_list)
        self.update()

    def delete_list(self, dict_list):
        delete_file(dict_list["file"])
        for i in range(len(self.controls)):
            if self.controls[i].title.value == dict_list["file"]:
                self.controls.pop(i)
                break
        for i in range(len(self.list_files)):
            if dict_list == self.list_files[i]:
                self.list_files.pop(i)
                break
        self.update()
    
    def delete_all_files(self):
        for i in self.list_files:
            delete_file(i["file"])

    def update_content(self):
        list_qr = get_qr_files()
        dict_lists = get_dict_add_and_del(self.list_files, list_qr)
        for delete in dict_lists["delete"]:
            self.delete_list(delete)
        for add in dict_lists["add"]:
            self.add_list(add)
        self.update()

class History(ft.Column):
    def __init__(self, func_view):
        super().__init__()
        self.alignment=ft.MainAxisAlignment.START, 
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # self.on_scroll_interval=0,
        # self.sem = threading.Semaphore()
        # self.on_scroll=on_scroll,
        self.width = 400
        self.content = HistoryViewQR(func_view=func_view)

        self.panel = ft.ExpansionPanelList(
            elevation=0,
            controls=[
                ft.ExpansionPanel(
                    header = ft.ListTile(title=ft.Text(f"History",theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                                         subtitle=ft.Text("Recently generated QR codes"),
                                         leading=ft.Icon(ft.icons.HISTORY),
                                         trailing=ft.IconButton(ft.icons.DELETE, on_click=self.clear_history)
                    ),
                    content = self.content
                ) 
            ]
        )
        self.controls = [
            self.panel
        ]
    
    # def on_scroll(self, e: ft.OnScrollEvent):
    #     if e.pixels >= e.max_scroll_extent - 100:
    #         if sem.acquire(blocking=False):
    #             try:
    #                 for i in range(0, 10):
    #                     cl.controls.append(ft.Text(f"Text line {s.i}", key=str(s.i)))
    #                     s.i += 1
    #                 cl.update()
    #             finally:
    #                 sem.release()

    def clear_history(self, e):
        self.content.delete_all_files()
        self.content.controls = []
        self.content.list_files = []
        self.content.update()

    def update_content(self):
        self.content.update_content()
