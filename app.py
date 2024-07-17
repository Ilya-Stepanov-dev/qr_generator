import flet as ft
from src import create_qr as cr_qr
from src import create_mac_qr as cr_qr_mac
from src import save_counter

class EntryField(ft.Row):
    def __init__(self, text ,func_left_button, func_right_button):
        super().__init__()
        self.counter = text
        self.text_filed = ft.TextField(value=text, text_align=ft.TextAlign.CENTER, label="Number MAC to generate QR code", on_focus=self.clear_text)
        self.left_button = ft.IconButton(ft.icons.CLEAR, on_click=func_left_button)
        self.right_button = ft.IconButton(ft.icons.NAVIGATE_NEXT, on_click=func_right_button)
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.START
        self.controls = [self.left_button, self.text_filed, self.right_button]

    def incrementing_number(self):
        self.text_filed.value = str(int(self.text_filed.value) + 1)
        self.counter = self.text_filed.value
        save_counter(self.text_filed.value)
        self.update()

    def change_text_label(self, text):
        self.text_filed.label = text
        self.update()
    
    def change_to_mac(self):
        self.text_filed.value = self.counter
        self.change_text_label("Number MAC to generate QR code")
    
    def change_to_any(self):
        self.change_text_label("Text to generate QR code")

    def clear_text(self,e):
        self.text_filed.value = None
        self.update()

# class TabsName(enum.Enum):
#     MAC = 0
#     ETHER = 1
#     INTERNET = 2
#     ANY = 3

class Tabs(ft.Row):
    def __init__(self, func_on_change):
        super().__init__()
        self.tabs = ft.Tabs(selected_index=0,
                            on_change=func_on_change,
                            tabs=[ft.Tab(text="MAC"), 
                                  ft.Tab(text="ETHER"), 
                                  ft.Tab(text="INTERNET"),
                                  ft.Tab(text="ANY")],
        )
        self.num_tab = 0
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.START
        self.controls = [self.tabs]


class Image(ft.Image):
    def __init__(self, src):
        super().__init__()
        self.width = 300
        self.height = 300
        self.fit = ft.ImageFit.CONTAIN
        self.src = src


class Text(ft.Text):
    def __init__(self, text):
        super().__init__()
        self.value = text
        self.scale = 1.5
        self.alignment = ft.MainAxisAlignment.CENTER


class MainColumn(ft.Column):
    def __init__(self, img_path, text):
        super().__init__()
        # self.img_path = img_path
        # self.text_img = text
        self.alignment=ft.MainAxisAlignment.START, 
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls = [Image(img_path), Text(text)]
        self.mac_controls = [Image(img_path), Text(text)]
        self.ether_controls = [Image("qr_default\\ETHER.png"),Text("ETHER")]
        self.internet_controls = [Image("qr_default\\lihp08969fkhjgn.png"),Text("INTERNET")]
        self.any_controls = [Image(img_path), Text(text)]
        
    def change_controls(self, new_controls):
        self.controls = new_controls
        self.update()

    def change_controls_to_mac(self):
        self.change_controls(self.mac_controls)
    
    def change_controls_to_ether(self):
        self.change_controls(self.ether_controls)

    def change_controls_to_internet(self):
        self.change_controls(self.internet_controls)

    def change_controls_to_any(self):
        self.change_controls(self.any_controls)

    def update_mac_content(self, img_path, text):
        self.mac_controls = [Image(img_path), Text(text)]
        self.change_controls_to_mac()

    def update_any_content(self, img_path, text):
        self.any_controls = [Image(img_path), Text(text)]
        self.change_controls_to_any()


class History(ft.Column):
    def __init__(self):
        super().__init__()
        self.alignment=ft.MainAxisAlignment.START, 
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.title_row = ft.Row(
                controls = [ft.Text(value="HISTORY", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),],
                alignment = ft.MainAxisAlignment.CENTER,
                # horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                # height=50,
        )
        self.controls = [
            ft.Divider(),
            self.title_row,
        ]


class App(ft.Column):
    def __init__(self, text: str):
        super().__init__()
        self.alignment=ft.MainAxisAlignment.START, 
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.entry_field = EntryField(text=text, func_left_button=self.clear_text, func_right_button=self.create_qr)
        self.row_tabs = Tabs(func_on_change=self.func_on_change_tab)
        self.main_column = MainColumn("qr_default\\welcome.png", "Welcome to the QR Generator")
        self.history = History()

        self.controls = [
            ft.Row(
                controls = [ft.Text(value="QR Generator", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                alignment = ft.MainAxisAlignment.CENTER,
            ),
            self.entry_field,
            self.row_tabs,
            self.main_column,
            # ft.Row(
            #     controls = [ft.Text(value="HISTORY", theme_style=ft.TextThemeStyle.TITLE_MEDIUM)],
            #     alignment = ft.MainAxisAlignment.CENTER,
            #     height=50,
            # )
            self.history,
        ]

    def clear_text(self,e):
        self.entry_field.text_filed.value = None
        self.update()

    def create_qr(self,e):
        qr = None
        num_tab = self.row_tabs.num_tab
        if num_tab == 1 or num_tab == 2:
            return 0
        else:
            value = self.entry_field.text_filed.value
            if num_tab == 0:
                qr = cr_qr_mac(value=int(value))
                self.entry_field.incrementing_number()
                self.main_column.update_mac_content(img_path=qr['file_name'], text=qr['value'])
            elif num_tab == 3:
                qr = cr_qr(value=value)
                self.main_column.update_any_content(img_path=qr['file_name'], text=qr['value'])

    
    def func_on_change_tab(self, e):
        self.row_tabs.num_tab = self.row_tabs.tabs.selected_index
        num_tab = self.row_tabs.num_tab
        if num_tab == 0:
            self.entry_field.change_to_mac()
            self.main_column.change_controls_to_mac()
        elif num_tab == 1:
            self.main_column.change_controls_to_ether()
        elif num_tab == 2:
            self.main_column.change_controls_to_internet()            
        elif num_tab == 3:
            self.entry_field.change_to_any()
            self.main_column.change_controls_to_any()        
